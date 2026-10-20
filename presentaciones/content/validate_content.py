import json, sys, re

LIM = {
    'title': 72,
}

def err(errors, i, msg):
    errors.append(f'slide {i}: {msg}')

def chk_str(errors, i, name, v, maxlen, required=True):
    if v is None or v == '':
        if required:
            err(errors, i, f'falta "{name}"')
        return
    if not isinstance(v, str):
        err(errors, i, f'"{name}" debe ser string')
        return
    if len(v) > maxlen:
        err(errors, i, f'"{name}" excede {maxlen} chars ({len(v)}): {v[:50]}...')

def chk_list(errors, i, name, v, lo, hi):
    if not isinstance(v, list):
        err(errors, i, f'"{name}" debe ser lista')
        return False
    if not (lo <= len(v) <= hi):
        err(errors, i, f'"{name}" debe tener entre {lo} y {hi} elementos (tiene {len(v)})')
    return True

def validate(path):
    errors = []
    warns = []
    d = json.load(open(path, encoding='utf-8'))
    meta = d.get('meta', {})
    for k in ('deck_title', 'day', 'filename'):
        if k not in meta:
            errors.append(f'meta.{k} faltante')
    slides = d.get('slides')
    if not isinstance(slides, list) or not slides:
        errors.append('slides vacío')
        return errors, warns
    prev_layout = []
    for i, s in enumerate(slides, 1):
        lay = s.get('layout')
        if lay not in ('title','agenda','section','bullets','cards','grid','compare','process','layers','table','code','stats','demo','lab','takeaway','resources','closing'):
            err(errors, i, f'layout inválido: {lay}')
            continue
        chk_str(errors, i, 'title', s.get('title'), 72)
        notes = s.get('notes', '')
        if lay != 'title' and len(notes) < 80:
            warns.append(f'slide {i} ({lay}): notas muy cortas ({len(notes)} chars)')
        if lay == 'title':
            chk_str(errors, i, 'subtitle', s.get('subtitle'), 120)
            chk_str(errors, i, 'meta', s.get('meta'), 120, False)
        elif lay == 'agenda':
            if chk_list(errors, i, 'items', s.get('items'), 3, 9):
                for it in s['items']:
                    chk_str(errors, i, 'item.time', it.get('time'), 16)
                    chk_str(errors, i, 'item.title', it.get('title'), 60)
                    chk_str(errors, i, 'item.detail', it.get('detail'), 90, False)
        elif lay == 'section':
            chk_str(errors, i, 'subtitle', s.get('subtitle'), 130, False)
            chk_str(errors, i, 'number', str(s.get('number', '')), 4)
            chk_str(errors, i, 'duration', s.get('duration'), 20, False)
        elif lay == 'bullets':
            if chk_list(errors, i, 'bullets', s.get('bullets'), 2, 6):
                for b in s['bullets']:
                    chk_str(errors, i, 'bullet', b, 120)
            chk_str(errors, i, 'callout', s.get('callout'), 150, False)
        elif lay == 'cards':
            if chk_list(errors, i, 'cards', s.get('cards'), 3, 4):
                for c in s['cards']:
                    chk_str(errors, i, 'card.title', c.get('title'), 40)
                    chk_str(errors, i, 'card.body', c.get('body'), 150)
            chk_str(errors, i, 'footer', s.get('footer'), 130, False)
        elif lay == 'grid':
            if chk_list(errors, i, 'cells', s.get('cells'), 4, 6):
                for c in s['cells']:
                    chk_str(errors, i, 'cell.title', c.get('title'), 36)
                    chk_str(errors, i, 'cell.body', c.get('body'), 110)
        elif lay == 'compare':
            for side in ('left', 'right'):
                sd = s.get(side) or {}
                chk_str(errors, i, f'{side}.title', sd.get('title'), 40)
                if chk_list(errors, i, f'{side}.items', sd.get('items'), 2, 5):
                    for b in sd['items']:
                        chk_str(errors, i, f'{side}.item', b, 100)
            chk_str(errors, i, 'verdict', s.get('verdict'), 140, False)
        elif lay == 'process':
            if chk_list(errors, i, 'steps', s.get('steps'), 3, 6):
                for st in s['steps']:
                    chk_str(errors, i, 'step.title', st.get('title'), 28)
                    chk_str(errors, i, 'step.body', st.get('body'), 95)
        elif lay == 'layers':
            if chk_list(errors, i, 'layers', s.get('layers'), 3, 5):
                for st in s['layers']:
                    chk_str(errors, i, 'layer.title', st.get('title'), 40)
                    chk_str(errors, i, 'layer.body', st.get('body'), 120)
        elif lay == 'table':
            cols = s.get('columns')
            rows = s.get('rows')
            if chk_list(errors, i, 'columns', cols, 2, 4) and chk_list(errors, i, 'rows', rows, 2, 7):
                for r in rows:
                    if len(r) != len(cols):
                        err(errors, i, 'fila con distinta cantidad de columnas')
                    for c in r:
                        chk_str(errors, i, 'cell', str(c), 70)
            chk_str(errors, i, 'note', s.get('note'), 140, False)
        elif lay == 'code':
            code = s.get('code', '')
            lines = code.split('\n')
            if len(lines) > 15:
                err(errors, i, f'code tiene {len(lines)} líneas (máx 15)')
            for ln in lines:
                if len(ln) > 78:
                    err(errors, i, f'línea de código > 78 chars: {ln[:40]}...')
                    break
            chk_str(errors, i, 'caption', s.get('caption'), 130, False)
        elif lay == 'stats':
            if chk_list(errors, i, 'stats', s.get('stats'), 3, 4):
                for st in s['stats']:
                    chk_str(errors, i, 'stat.value', st.get('value'), 12)
                    chk_str(errors, i, 'stat.label', st.get('label'), 70)
            chk_str(errors, i, 'note', s.get('note'), 140, False)
        elif lay == 'demo':
            chk_str(errors, i, 'scenario', s.get('scenario'), 160)
            if chk_list(errors, i, 'steps', s.get('steps'), 3, 6):
                for b in s['steps']:
                    chk_str(errors, i, 'step', b, 100)
            chk_str(errors, i, 'expected', s.get('expected'), 140, False)
        elif lay == 'lab':
            chk_str(errors, i, 'objective', s.get('objective'), 160)
            chk_str(errors, i, 'time', s.get('time'), 20, False)
            if chk_list(errors, i, 'steps', s.get('steps'), 3, 7):
                for b in s['steps']:
                    chk_str(errors, i, 'step', b, 100)
            if s.get('deliverables') is not None:
                chk_list(errors, i, 'deliverables', s.get('deliverables'), 1, 4)
                for b in s.get('deliverables', []):
                    chk_str(errors, i, 'deliverable', b, 90)
            chk_str(errors, i, 'repoUrl', s.get('repoUrl'), 120, False)
        elif lay == 'takeaway':
            if chk_list(errors, i, 'points', s.get('points'), 3, 4):
                for b in s['points']:
                    chk_str(errors, i, 'point', b, 130)
        elif lay == 'resources':
            if chk_list(errors, i, 'links', s.get('links'), 3, 8):
                for l in s['links']:
                    chk_str(errors, i, 'link.label', l.get('label'), 70)
                    chk_str(errors, i, 'link.url', l.get('url'), 120)
                    if not l.get('url', '').startswith('https://'):
                        err(errors, i, 'link.url debe empezar con https://')
        elif lay == 'closing':
            chk_str(errors, i, 'message', s.get('message'), 160, False)
        # tracking: no más de 2 bullets seguidos
        prev_layout.append(lay)
        if len(prev_layout) >= 3 and prev_layout[-3:] == ['bullets'] * 3:
            warns.append(f'slide {i}: 3 slides "bullets" seguidos; variar layout')
        # contenido interno prohibido en slides visibles
        vis = json.dumps({k: v for k, v in s.items() if k != 'notes'}, ensure_ascii=False)
        if re.search(r'customer-success-microsoft|eng\.ms|ASDIPRelease|sharepoint\.com|asd-management|Confidential', vis, re.I):
            err(errors, i, 'contenido interno de Microsoft en slide visible (solo permitido en notas)')
    return errors, warns

if __name__ == '__main__':
    e, w = validate(sys.argv[1])
    print(f'{len(e)} errores, {len(w)} avisos')
    for x in e:
        print('ERROR', x)
    for x in w[:40]:
        print('AVISO', x)
    sys.exit(1 if e else 0)
