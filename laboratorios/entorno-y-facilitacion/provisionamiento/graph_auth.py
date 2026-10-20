import sys, os, json, msal

TENANT = 'eeee485f-b8f7-4983-b3dc-d5d97a0ad2bc'
CLIENT_ID = '14d82eec-204b-4c2f-b7e8-296a70dab67e'  # Microsoft Graph Command Line Tools
SCOPES = [f'https://graph.microsoft.com/{s}' for s in (
    'Policy.ReadWrite.AuthenticationMethod', 'Policy.Read.All', 'UserAuthenticationMethod.ReadWrite.All',
    'User.ReadWrite.All', 'Group.ReadWrite.All', 'Directory.ReadWrite.All')]
CACHE = os.path.join(os.environ['USERPROFILE'], '.bci-lab', 'msal_cache.json')

cache = msal.SerializableTokenCache()
if os.path.exists(CACHE):
    cache.deserialize(open(CACHE).read())
app = msal.PublicClientApplication(CLIENT_ID, authority=f'https://login.microsoftonline.com/{TENANT}', token_cache=cache)

def save():
    if cache.has_state_changed:
        open(CACHE, 'w').write(cache.serialize())

mode = sys.argv[1] if len(sys.argv) > 1 else 'token'
if mode == 'login':
    flow = app.initiate_device_flow(scopes=SCOPES)
    print(flow['message'], flush=True)
    res = app.acquire_token_by_device_flow(flow)  # espera hasta ~15 min
    save()
    if 'access_token' in res:
        print('LOGIN OK:', res.get('id_token_claims', {}).get('preferred_username'), flush=True)
    else:
        print('LOGIN FAILED:', res.get('error'), res.get('error_description'), flush=True)
        sys.exit(1)
else:
    accts = app.get_accounts()
    if not accts:
        print('NO_ACCOUNT', file=sys.stderr); sys.exit(2)
    res = app.acquire_token_silent(SCOPES, account=accts[0])
    save()
    if not res or 'access_token' not in res:
        print('NO_TOKEN', file=sys.stderr); sys.exit(3)
    print(res['access_token'])
