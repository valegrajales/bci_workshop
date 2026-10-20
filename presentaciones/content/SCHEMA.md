# Esquema de contenido de las presentaciones (JSON)

Cada día es un archivo `dayN.json` con esta forma:

```json
{
  "meta": {
    "deck_title": "Microsoft Foundry – Fundamentos (L100)",
    "day": 1,
    "date_label": "Miércoles 21 de octubre de 2026",
    "filename": "BCI_Foundry_Dia1_L100_Fundamentos"
  },
  "slides": [ { "layout": "...", "title": "...", "notes": "..." } ]
}
```

Todos los slides llevan `layout`, `title` y `notes` (notas del orador en español, 80–200 palabras: guion hablado + dato/demo a mostrar + `Fuente:` con la ruta relativa del material usado).
Texto visible en español (rioplatense/chileno neutro), nombres de producto y términos técnicos en inglés (Foundry, Agent Service, RAG, MCP…).

| layout | campos (además de title y notes) | límites |
|---|---|---|
| `title` | `subtitle`, `meta` (fecha·hora·lugar) | subtitle ≤120 |
| `agenda` | `items`: `[{time, title, detail?}]` | 3–9 items; title ≤60 |
| `section` | `number`, `subtitle?`, `duration?` | |
| `bullets` | `bullets[]` (2–6), `callout?` | bullet ≤120, callout ≤150 |
| `cards` | `cards: [{title, body}]` (3–4), `footer?` | title ≤40, body ≤150 |
| `grid` | `cells: [{title, body}]` (4 o 6) | title ≤36, body ≤110 |
| `compare` | `left {title, items[]}`, `right {title, items[]}`, `verdict?` | 2–5 items por lado, ≤100 |
| `process` | `steps: [{title, body}]` (3–6) | title ≤28, body ≤95 |
| `layers` | `layers: [{title, body}]` (3–5, de arriba hacia abajo) | title ≤40, body ≤120 |
| `table` | `columns[]` (2–4), `rows[][]` (2–7), `note?` | celda ≤70 |
| `code` | `language`, `code` (≤15 líneas, ≤78 chars), `caption?` | |
| `stats` | `stats: [{value, label}]` (3–4), `note?` | value ≤12, label ≤70 |
| `demo` | `scenario`, `steps[]` (3–6), `expected?` | |
| `lab` | `objective`, `time?`, `steps[]` (3–7), `deliverables[]?`, `repoUrl?` | repoUrl solo público |
| `takeaway` | `points[]` (3–4) | ≤130 |
| `resources` | `links: [{label, url}]` (3–8, https) | solo enlaces públicos |
| `closing` | `message?` | |

Reglas de contenido:
- Nada de contenido interno de Microsoft en el texto visible (repos internos, eng.ms, SharePoint, "Confidential"). Las rutas a material interno van **solo en `notes`**.
- Sin datos reales de BCI ni de clientes: escenarios bancarios ficticios.
- Sin precios ni cuotas numéricas salvo que la doc oficial local los indique explícitamente (citar en notas).
- Funciones en preview: marcarlas "(preview)" solo si la documentación local lo dice.
- Variar layouts: nunca más de 2 `bullets` seguidos.

Validar con: `python validate_content.py dayN.json`
