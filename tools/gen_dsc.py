"""Userland reference from the iOS 27.2 dyld shared cache: an index of every image, and for each
hardware-facing image its linked libraries, Objective-C classes and methods, Swift types and strings.

usage: gen_dsc.py <dyld_shared_cache_arm64e_x1> reference/userland [--all-pattern REGEX]
"""
import os
import re
import subprocess
import sys

dsc, out = sys.argv[1:3]
os.makedirs(out, exist_ok=True)
MAX_STR = 3000
MAX_METH = 6000

# Images whose names say they drive, abstract or consume hardware.
HW = re.compile(r'(IOKit|IOSurface|IOAccel|IOMobileFramebuffer|IOGPU|IOUSB|IOHID|HID|BackBoard|FrontBoard|SpringBoardFoundation|'
                r'SpringBoard$|CoreMotion|locationd|CoreLocation|CoreBrightness|QuartzCore|CoreDisplay|AGX|Metal|MTL|'
                r'CoreAudio|AudioToolbox|AudioSession|MediaToolbox|VideoToolbox|AVF|CMCapture|CameraKit|Camera|ISP|'
                r'AppleNeuralEngine|ANE|Espresso|CoreML|BiometricKit|LocalAuthentication|SEP|Keychain|Security$|'
                r'CoreTelephony|CommCenter|Telephony|Baseband|WiFi|Wifi|Centauri|Bluetooth|CoreBT|NearbyInteraction|'
                r'Nearby|Rose|NFC|Stockholm|SecureElement|PowerLog|IOPM|BatteryCenter|Battery|Thermal|CLPC|Haptic|'
                r'Taptic|Thread|Network\.framework|libnetwork|Skywalk|libnetcore|MobileGestalt|DeviceIdentity|'
                r'AOP|SPU|Sensor|Accessory|Charging|MagSafe|Lightning|USB|DisplayServices|UIKitCore|UIKitServices|'
                r'Posture|Hinge|Fold|Pose|GPS|GNSS|Satellite|Stewie|Exclave|Tightbeam|RTBuddy|DriverKit|CoreUI$|'
                r'AppleDisplay|Brightness|Backlight|TrueTone|Flash|Torch|Pencil|Speaker|Microphone|VoiceTrigger)', re.I)


def run(*a, timeout=900):
    try:
        return subprocess.run(a, capture_output=True, timeout=timeout).stdout.decode('utf-8', 'replace')
    except subprocess.TimeoutExpired:
        return ''


def slug(p):
    return re.sub(r'[^A-Za-z0-9_.,+-]', '_', p.strip('/').replace('/', '__'))


listing = run('ipsw', 'dyld', 'info', '-l', '--no-color', dsc)
images = []
for line in listing.splitlines():
    m = re.search(r'(/(?:System|usr|Library|private|AppleInternal)\S+)', line)
    if m:
        ver = re.search(r'\b(\d+(?:\.\d+){1,4})\b', line)
        images.append((m.group(1), ver.group(1) if ver else ''))
seen = set()
images = [x for x in images if not (x[0] in seen or seen.add(x[0]))]

pages = {}
for path, ver in images:
    base = os.path.basename(path)
    if 'AccessibilityBundles' in path or (not HW.search(base) and not HW.search(path.split('/')[-2] if '/' in path else '')):
        continue
    existing = os.path.join(out, slug(path) + '.md')
    if os.path.exists(existing):
        # resume: keep a page written by an earlier run, recover its counts for the index
        txt = open(existing).read()
        oc = re.search(r'## Objective-C: (\d+) classes, \d+ protocols, (\d+) methods', txt)
        st = re.search(r'## Strings \(([\d,]+)\)', txt)
        pages[path] = (slug(path) + '.md', int(oc.group(1)) if oc else 0, int(oc.group(2)) if oc else 0,
                       int(st.group(1).replace(',', '')) if st else 0)
        continue
    L = [f'# `{path}`', '', f'iOS 27.2 dyld shared cache image. Version `{ver}`. **[DSC]**', '']
    loads = run('ipsw', 'dyld', 'macho', '--no-color', dsc, path, '-l')
    deps = re.findall(r'LC_(?:REEXPORT_|LOAD_WEAK_|LOAD_UPWARD_|LAZY_LOAD_)?(?:LOAD_)?DYLIB\s+(\S+)', loads)
    if deps:
        L += [f'## Linked libraries ({len(deps)})', ''] + [f'- `{d}`' for d in deps] + ['']
    objc = run('ipsw', 'dyld', 'macho', '--no-color', dsc, path, '--objc')
    cls = sorted(set(re.findall(r'@interface (\S+)', objc)))
    prot = sorted(set(re.findall(r'@protocol (\S+)', objc)))
    meth = [l.strip() for l in objc.splitlines() if re.match(r'\s*[-+]\[', l)]
    props = [l.strip() for l in objc.splitlines() if l.strip().startswith('@property')]
    if cls or prot:
        L += [f'## Objective-C: {len(cls)} classes, {len(prot)} protocols, {len(meth)} methods, {len(props)} properties', '']
        if cls:
            L += ['### Classes', '', ', '.join(f'`{c}`' for c in cls), '']
        if prot:
            L += ['### Protocols', '', ', '.join(f'`{c}`' for c in prot), '']
        if props:
            L += ['### Properties', '', '```'] + props[:MAX_METH] + ['```', '']
        if meth:
            L += ['### Methods', '', '```'] + meth[:MAX_METH] + ['```', '']
            if len(meth) > MAX_METH:
                L.append(f'First {MAX_METH:,} of {len(meth):,} methods.')
    swift = run('ipsw', 'dyld', 'macho', '--no-color', dsc, path, '--swift')
    stypes = sorted(set(re.findall(r'^(?:struct|class|enum|protocol|actor) (\S+)', swift, re.M)))
    if stypes:
        L += [f'## Swift types ({len(stypes)})', '', ', '.join(f'`{t}`' for t in stypes[:2000]), '']
    strs = run('ipsw', 'dyld', 'macho', '--no-color', dsc, path, '--strings')
    sl = [m.group(1) for m in (re.match(r'\s*0x[0-9a-f]+: "(.*)"$', l) for l in strs.splitlines()) if m]
    L += [f'## Strings ({len(sl):,})', '']
    if len(sl) > MAX_STR:
        L.append(f'First {MAX_STR:,} of {len(sl):,}.')
    L += ['```'] + [s[:240] for s in sl[:MAX_STR]] + ['```']
    page = slug(path) + '.md'
    open(os.path.join(out, page), 'w').write('\n'.join(L) + '\n')
    pages[path] = (page, len(cls), len(meth), len(sl))
    print(len(pages), path, flush=True)

I = ['# Userland: iOS 27.2 dyld shared cache', '', f'{len(images):,} images in the cache. {len(pages)} hardware-facing images have their own page '
     '(linked libraries, Objective-C classes/methods/properties, Swift types, strings). **[DSC]**', '',
     '| Image | Version | Classes | Methods | Strings |', '|---|---|---|---|---|']
for path, ver in images:
    if path in pages:
        page, c, m, s = pages[path]
        I.append(f'| [`{path}`]({page}) | {ver} | {c} | {m} | {s:,} |')
    else:
        I.append(f'| `{path}` | {ver} | | | |')
open(os.path.join(out, 'README.md'), 'w').write('\n'.join(I) + '\n')
print('done', len(images), 'images', len(pages), 'pages')
