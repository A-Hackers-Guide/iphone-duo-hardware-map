"""Kext dependency map from OSBundleLibraries: per kext, its dependencies and its dependents (direct and total),
sorted by how much of the kernel rests on it. Writes reference/maps/kext-dependencies.md.

usage: gen_kextdeps.py data/kexts-full.json reference/maps/kext-dependencies.md
"""
import json
import sys

kexts = json.load(open(sys.argv[1]))
ids = {k.get('CFBundleIdentifier') for k in kexts}
deps = {k.get('CFBundleIdentifier'): sorted((k.get('OSBundleLibraries') or {}).keys()) for k in kexts}
rdeps = {}
for k, ds in deps.items():
    for d in ds:
        rdeps.setdefault(d, set()).add(k)


def closure(k):
    seen, stack = set(), list(rdeps.get(k, []))
    while stack:
        x = stack.pop()
        if x not in seen:
            seen.add(x)
            stack += rdeps.get(x, [])
    return seen


def link(x):
    return f'[`{x}`](../kexts/{x}.md)' if x in ids else f'`{x}`'


allk = sorted(set(deps) | set(rdeps), key=lambda x: (-len(closure(x)), x))
L = ['# Kext dependency map', '', f'{len(ids)} kexts. Dependencies come from each kext\'s `OSBundleLibraries`; `com.apple.kpi.*` entries are the '
     'kernel\'s exported programming interfaces. Sorted by how many kexts depend on each one, directly or indirectly. **[KC]**', '',
     '| Kext | Depended on by (total) | Direct dependents | Depends on |', '|---|---|---|---|']
for k in allk:
    d = sorted(rdeps.get(k, []))
    L.append(f'| {link(k)} | {len(closure(k))} | {", ".join(link(x) for x in d[:12])}{f" … +{len(d) - 12}" if len(d) > 12 else ""} | '
             f'{", ".join(link(x) for x in deps.get(k, []))} |')
open(sys.argv[2], 'w').write('\n'.join(L) + '\n')
print(len(allk))
