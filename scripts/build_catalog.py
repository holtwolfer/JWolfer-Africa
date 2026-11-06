import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
items = []
seen = set()
for p in sorted((root / 'content' / 'artifacts').glob('*.json')):
    a = json.loads(p.read_text(encoding='utf-8'))
    if a['id'] in seen: raise ValueError(f"Duplicate artifact ID: {a['id']}")
    seen.add(a['id'])
    if p.stem != a['id']: raise ValueError(f"Filename/ID mismatch: {p}")
    for k in ('notes','images'):
        a[k] = a.get(k) or []
    for k in ('number','group','country','original'):
        a[k] = a.get(k) or (None if k == 'number' else '')
    a['slide'] = a.get('slide') or None
    items.append(a)
items.sort(key=lambda a: (a['slide'] is None, a['slide'] or 999999, a['id']))
(root / 'catalog.json').write_text(json.dumps(items, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(f"Built catalog with {len(items)} artifacts")
