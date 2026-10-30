"""Build explorer/index.html: a single self-contained page to browse and search the device tree,
with drivers, decoded properties, function wiring and interrupts. Open it straight from disk.

usage: gen_explorer.py data/adt-nodes.json explorer/index.html
"""
import json
import os
import struct
import sys

nodes = json.load(open(sys.argv[1]))
ph = {n['phandle']: n['path'] for n in nodes if n['phandle'] is not None}


def val(p):
    if 'str' in p and not (p['len'] == 4 and isinstance(p['str'], str) and len(p['str']) < 3):
        s = p['str']
        return ', '.join(s) if isinstance(s, list) else s
    if 'u32' in p:
        v = p['u32']
        return f'{v} (0x{v:x})'
    if 'u64' in p:
        return f'0x{p["u64"]:x}'
    if p['len'] == 0:
        return '(empty)'
    if 'u32s' in p and p['len'] <= 256:
        return ' '.join(f'0x{x:x}' for x in p['u32s'])
    return f'{p["len"]} bytes: {p["hex"][:128]}' + ('…' if p['len'] > 64 else '')


def fns(n):
    out = []
    for k, p in n['props'].items():
        if k.startswith('function-') and p['len'] >= 8:
            b = bytes.fromhex(p['hex'])
            w = struct.unpack(f'<{len(b) // 4}I', b[:len(b) // 4 * 4])
            out.append([k[9:], ph.get(w[0], f'phandle {w[0]}'), struct.pack('<I', w[1])[::-1].decode('latin-1'), ' '.join(f'0x{x:x}' for x in w[2:])])
    return out


data = []
for n in nodes:
    ip = n['props'].get('interrupt-parent', {}).get('u32')
    data.append({
        'p': n['path'].replace('device-tree', '') or '/',
        'c': n['compatible'],
        'd': sorted({f'{d["class"]} ({d["kext"]})' for d in n['drivers']}),
        'f': [[a, (b or '').replace('device-tree', ''), c, d] for a, b, c, d in fns(n)],
        'ip': (ph.get(ip) or '').replace('device-tree', ''),
        'pr': [[k, val(n['props'][k])] for k in sorted(n['props'])],
    })

HTML = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Duo Device Tree</title>
<style>
:root{--bg:#fbfbfa;--fg:#1d1d1b;--mut:#6b6b66;--line:#e3e2dc;--acc:#2f5bd3;--chip:#eef0f7}
@media (prefers-color-scheme:dark){:root{--bg:#161615;--fg:#ecebe6;--mut:#9a9992;--line:#2c2c29;--acc:#86a6ff;--chip:#23263a}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:14px/1.45 -apple-system,system-ui,sans-serif}
header{padding:14px 16px;border-bottom:1px solid var(--line);display:flex;gap:12px;align-items:center;flex-wrap:wrap}
h1{font-size:16px;margin:0}input{flex:1;min-width:200px;padding:8px 10px;border:1px solid var(--line);border-radius:8px;background:transparent;color:var(--fg);font:inherit}
main{display:grid;grid-template-columns:minmax(260px,38%) 1fr;height:calc(100vh - 62px)}
@media (max-width:760px){main{grid-template-columns:1fr;height:auto}#list{max-height:40vh}}
#list{overflow:auto;border-right:1px solid var(--line)}#list div{padding:3px 12px;cursor:pointer;white-space:nowrap;font:12px ui-monospace,Menlo,monospace}
#list div:hover,#list div.sel{background:var(--chip)}#list .drv{color:var(--acc)}
#det{overflow:auto;padding:16px}code,td{font:12px ui-monospace,Menlo,monospace}table{border-collapse:collapse;width:100%}
td{border-top:1px solid var(--line);padding:4px 8px;vertical-align:top;word-break:break-all}td:first-child{white-space:nowrap;color:var(--mut);word-break:normal}
h2{font-size:15px;margin:0 0 6px}h3{font-size:13px;margin:16px 0 6px;color:var(--mut);text-transform:uppercase;letter-spacing:.04em}
a{color:var(--acc);cursor:pointer}.muted{color:var(--mut)}
</style></head><body>
<header><h1>iPhone Duo device tree</h1><span class="muted" id="count"></span><input id="q" placeholder="Search path, compatible, driver or property (regex)" autofocus></header>
<main><div id="list"></div><div id="det"><p class="muted">Pick a node. Data: DeviceTree.v68ap.im4p, iOS 27.2 24B91020, parsed byte-exact.</p></div></main>
<script>
const D = __DATA__;
const byPath = Object.fromEntries(D.map(n => [n.p, n]));
const L = document.getElementById('list'), Q = document.getElementById('q'), det = document.getElementById('det');
const esc = s => String(s).replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
function render(rx) {
  L.innerHTML = ''; let n = 0;
  for (const x of D) {
    const hay = x.p + ' ' + x.c.join(' ') + ' ' + x.d.join(' ') + ' ' + x.pr.map(p => p[0]).join(' ');
    if (rx && !rx.test(hay)) continue;
    const el = document.createElement('div'); n++;
    const depth = (x.p.match(/\\//g) || []).length;
    el.innerHTML = '&nbsp;'.repeat(Math.max(0, depth - 1) * 2) + esc(x.p.split('/').pop() || '/') + (x.d.length ? ' <span class="drv">● ' + esc(x.d[0].split(' ')[0]) + '</span>' : '');
    el.onclick = () => { show(x.p); document.querySelectorAll('#list .sel').forEach(e => e.classList.remove('sel')); el.classList.add('sel'); };
    L.appendChild(el);
  }
  document.getElementById('count').textContent = n + ' of ' + D.length + ' nodes';
}
function link(p) { return p && byPath[p] ? `<a onclick="show('${p}')">${esc(p)}</a>` : esc(p || '?'); }
function show(p) {
  const x = byPath[p]; if (!x) return;
  const refs = D.filter(y => y.f.some(f => f[1] === p) || y.ip === p).map(y => y.p);
  const kids = D.filter(y => y.p.startsWith(p === '/' ? '/' : p + '/') && y.p.split('/').length === (p === '/' ? 2 : p.split('/').length + 1)).map(y => y.p);
  det.innerHTML = `<h2>${esc(p)}</h2><div class="muted">${esc(x.c.join(', '))}</div>
  <h3>Driver</h3>${x.d.length ? x.d.map(esc).join('<br>') : '<span class="muted">none by name match</span>'}
  ${x.ip ? `<h3>Interrupt controller</h3>${link(x.ip)}` : ''}
  ${x.f.length ? '<h3>Functions it calls</h3><table>' + x.f.map(f => `<tr><td>${esc(f[0])}</td><td>${link(f[1])} <code>${esc(f[2])}</code> ${esc(f[3])}</td></tr>`).join('') + '</table>' : ''}
  ${refs.length ? '<h3>Referenced by</h3>' + refs.map(link).join('<br>') : ''}
  ${kids.length ? '<h3>Children</h3>' + kids.map(link).join('<br>') : ''}
  <h3>Properties (${x.pr.length})</h3><table>${x.pr.map(r => `<tr><td>${esc(r[0])}</td><td>${esc(r[1])}</td></tr>`).join('')}</table>`;
  det.scrollTop = 0;
}
Q.oninput = () => { let rx = null; try { rx = Q.value ? new RegExp(Q.value, 'i') : null; } catch (e) { return; } render(rx); };
render(null);
</script></body></html>
"""
os.makedirs(os.path.dirname(sys.argv[2]), exist_ok=True)
open(sys.argv[2], 'w').write(HTML.replace('__DATA__', json.dumps(data, separators=(',', ':'))))
print('wrote', sys.argv[2], os.path.getsize(sys.argv[2]), 'bytes')
