import json, re, sys

MAP = {
 'aplicá':'aplica','auditá':'audita','combiná':'combina','conectá':'conecta','confirmá':'confirma','controlás':'controlas',
 'correlacioná':'correlaciona','corré':'corre','corrés':'corres','definí':'define','describí':'describe','devolvé':'devuelve',
 'elegí':'elige','empezá':'empieza','guardá':'guarda','migrá':'migra','podés':'puedes','preferí':'prefiere','publicá':'publica',
 'redactá':'redacta','registrá':'registra','revisá':'revisa','seguí':'sigue','separá':'separa','sondeá':'sondea','tratá':'trata',
 'usá':'usa','validá':'valida','iterá':'itera','tenés':'tienes','querés':'quieres','sabés':'sabes','necesitás':'necesitas',
 'hacés':'haces','usás':'usas','elegís':'eliges','vos':'tú','mirá':'mira','probá':'prueba','pasá':'pasa','agregá':'agrega',
 'evaluá':'evalúa','diseñá':'diseña','ejecutá':'ejecuta','abrí':'abre','dividí':'divide','mostrá':'muestra','pensá':'piensa',
 'armá':'arma','creá':'crea','cargá':'carga','instalá':'instala','configurá':'configura','limitá':'limita','protegé':'protege',
 'exponé':'expón','almacená':'almacena','generá':'genera','medí':'mide','pedí':'pide','dejá':'deja','tené':'ten','poné':'pon',
 'sumá':'suma','chequeá':'revisa','verificá':'verifica','habilitá':'habilita','asigná':'asigna','activá':'activa',
}

def conv(t):
    def rep(m):
        w = m.group(0)
        lw = w.lower()
        if lw in MAP:
            r = MAP[lw]
            if w[0].isupper():
                r = r[0].upper() + r[1:]
            return r
        return w
    pat = re.compile(r"\b[A-Za-zÁÉÍÓÚáéíóúñÑ]+\b")
    return pat.sub(rep, t)

SKIP = {'url', 'repoUrl', 'filename', 'layout', 'language', 'code'}
changes = 0

def walk(o):
    global changes
    if isinstance(o, dict):
        return {k: (v if k in SKIP else walk(v)) for k, v in o.items()}
    if isinstance(o, list):
        return [walk(v) for v in o]
    if isinstance(o, str):
        n = conv(o)
        if n != o:
            changes += 1
        return n
    return o

for p in sys.argv[1:]:
    d = json.load(open(p, encoding='utf-8'))
    changes = 0
    d2 = walk(d)
    json.dump(d2, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(p.split('\\')[-1], 'strings modified:', changes)
