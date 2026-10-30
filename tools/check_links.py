"""Check every relative Markdown link in the repo and report the ones whose target file does not exist.

usage: check_links.py [repo root]   (exit status 1 if any link is broken)
"""
import collections
import os
import re
import sys
from urllib.parse import unquote

root = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINK = re.compile(r'\]\(([^)\s]+)\)')
broken = collections.Counter()
examples = {}
checked = 0
for dp, dn, fn in os.walk(root):
    dn[:] = [d for d in dn if d != '.git']
    for f in fn:
        if not f.endswith('.md'):
            continue
        src = os.path.join(dp, f)
        text = open(src, encoding='utf-8', errors='replace').read()
        text = re.sub(r'```.*?```', '', text, flags=re.S)  # code blocks hold raw strings, not links
        text = re.sub(r'`[^`\n]*`', '', text)
        for target in LINK.findall(text):
            if re.match(r'^[a-z]+:', target) or target.startswith('#'):
                continue
            path = unquote(target.split('#')[0])
            if not path:
                continue
            checked += 1
            if not os.path.exists(os.path.normpath(os.path.join(dp, path))):
                key = os.path.relpath(os.path.normpath(os.path.join(dp, path)), root)
                broken[key] += 1
                examples.setdefault(key, os.path.relpath(src, root))
print(f'{checked:,} relative links checked, {sum(broken.values()):,} broken, {len(broken):,} distinct missing targets')
for k, n in broken.most_common(60):
    print(f'{n:6}  {k}   (e.g. from {examples[k]})')
sys.exit(1 if broken else 0)
