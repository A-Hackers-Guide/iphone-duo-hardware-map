"""Write STATS.md: pages and lines per section of the repo, plus tool code size.

usage: stats.py [repo root]
"""
import os
import sys

root = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows, tp, tl = [], 0, 0
for sect in ['docs'] + sorted(os.path.join('reference', d) for d in os.listdir(os.path.join(root, 'reference'))
                              if os.path.isdir(os.path.join(root, 'reference', d))):
    pages = lines = 0
    for dp, dn, fn in os.walk(os.path.join(root, sect)):
        for f in fn:
            if f.endswith('.md'):
                pages += 1
                with open(os.path.join(dp, f), encoding='utf-8', errors='replace') as fh:
                    lines += sum(1 for _ in fh)
    rows.append((sect, pages, lines))
    tp += pages
    tl += lines
code = sum(sum(1 for _ in open(os.path.join(root, 'tools', f))) for f in os.listdir(os.path.join(root, 'tools')) if f.endswith('.py'))
L = ['# Repository statistics', '', f'{tp:,} Markdown pages, {tl:,} lines. Tooling: {code:,} lines of Python in `tools/`.', '',
     '| Section | Pages | Lines |', '|---|---|---|']
L += [f'| [`{s}`]({s}/) | {p:,} | {l:,} |' for s, p, l in rows]
open(os.path.join(root, 'STATS.md'), 'w').write('\n'.join(L) + '\n')
print('\n'.join(L))
