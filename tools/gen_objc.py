"""One page per Objective-C class and protocol in the hardware-facing dyld-cache images (those with a full
page in reference/userland): superclass, adopted protocols, instance variables, properties, and every
instance and class method. Also fixes each image page's method count and links it to its class pages.

usage: gen_objc.py <dyld_shared_cache> reference/userland reference/objc [workers]
"""
import multiprocessing as mp
import os
import re
import subprocess
import sys

dsc, upages, out = sys.argv[1:4]
workers = int(sys.argv[4]) if len(sys.argv) > 4 else 3
os.makedirs(out, exist_ok=True)
BLOCK = re.compile(r'^@(interface|protocol) (\S+?)(?:\s*:\s*(\S+))?(?:\s*<([^>]*)>)?\s*\{?\s*$(.*?)^@end', re.M | re.S)


def run(*a, timeout=900):
    try:
        return subprocess.run(a, capture_output=True, timeout=timeout).stdout.decode('utf-8', 'replace')
    except subprocess.TimeoutExpired:
        return ''


def slug(p):
    return re.sub(r'[^A-Za-z0-9_.,+-]', '_', p.strip('/').replace('/', '__'))


def cname(kind, name, image):
    # class names are unique per process but may repeat across images; qualify by image basename
    return re.sub(r'[^A-Za-z0-9_.,+-]', '_', f'{name}@{os.path.basename(image)}') + ('.protocol' if kind == 'protocol' else '') + '.md'


def work(image):
    objc = run('ipsw', 'dyld', 'macho', '--no-color', dsc, image, '--objc')
    made = []
    for m in BLOCK.finditer(objc):
        kind, name, sup, prots, body = m.groups()
        lines = [l.rstrip() for l in body.splitlines()]
        ivars = [l.strip() for l in lines if l.startswith('    ') and not l.strip().startswith('/*')]
        props = [l.strip() for l in lines if l.startswith('@property')]
        imeth = [l.strip() for l in lines if l.startswith('-[')]
        cmeth = [l.strip() for l in lines if l.startswith('+[')]
        f = cname(kind, name, image)
        L = [f'# `{name}`' + (' (protocol)' if kind == 'protocol' else ''), '',
             f'- Image: [`{image}`](../userland/{slug(image)}.md) (iOS 27.2 dyld shared cache) **[DSC]**']
        if sup:
            L.append(f'- Superclass: `{sup}`')
        if prots:
            L.append('- Protocols: ' + ', '.join(f'`{p.strip()}`' for p in prots.split(',') if p.strip()))
        L.append(f'- {len(ivars)} instance variables, {len(props)} properties, {len(imeth)} instance methods, {len(cmeth)} class methods')
        if ivars:
            L += ['', '## Instance variables', '', '```'] + ivars + ['```']
        if props:
            L += ['', '## Properties', '', '```'] + props + ['```']
        if cmeth:
            L += ['', '## Class methods', '', '```'] + cmeth + ['```']
        if imeth:
            L += ['', '## Instance methods', '', '```'] + imeth + ['```']
        open(os.path.join(out, f), 'w').write('\n'.join(L) + '\n')
        made.append((kind, name, f, len(imeth) + len(cmeth)))
    # patch the image page: true method count and links to the class pages
    page = os.path.join(upages, slug(image) + '.md')
    if os.path.exists(page) and made:
        txt = open(page).read()
        total = sum(x[3] for x in made)
        txt = re.sub(r'(## Objective-C: \d+ classes, \d+ protocols, )\d+( methods)', rf'\g<1>{total}\g<2>', txt, count=1)
        if '### Class pages' not in txt:
            links = ', '.join(f'[`{n}`](../objc/{f})' for k, n, f, _ in sorted(made, key=lambda x: x[1]))
            txt = re.sub(r'(## Objective-C:[^\n]*\n)', lambda m: m.group(1) + f'\n### Class pages\n\nEvery class and protocol, with its methods: {links}\n', txt, count=1)
        open(page, 'w').write(txt)
    return image, made


if __name__ == '__main__':
    images = []
    for f in sorted(os.listdir(upages)):
        if f.endswith('.md') and f != 'README.md':
            head = open(os.path.join(upages, f)).read(4000)
            if '## Strings' in open(os.path.join(upages, f)).read() and head.startswith('# `'):
                images.append(head.split('`')[1])
    print(len(images), 'full images', flush=True)
    index = []
    with mp.Pool(workers) as pool:
        for n, (image, made) in enumerate(pool.imap_unordered(work, images), 1):
            index += [(name, kind, f, image, nm) for kind, name, f, nm in made]
            if n % 25 == 0:
                print(n, len(index), flush=True)
    I = ['# Objective-C classes and protocols', '', f'{len(index):,} classes and protocols from {len(images)} hardware-facing images, '
         'one page each with every method. **[DSC]**', '', '| Name | Kind | Image | Methods |', '|---|---|---|---|']
    for name, kind, f, image, nm in sorted(index):
        I.append(f'| [`{name}`]({f}) | {kind} | `{os.path.basename(image)}` | {nm} |')
    open(os.path.join(out, 'README.md'), 'w').write('\n'.join(I) + '\n')
    print('done', len(index))
