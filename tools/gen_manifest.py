"""Document BuildManifest.plist: every build identity and every component's path, digest, trust flags and info keys.

usage: gen_manifest.py BuildManifest.plist reference/manifest.md
"""
import plistlib
import sys

m = plistlib.load(open(sys.argv[1], 'rb'))
L = ['# BuildManifest', '', 'Every component Apple signs for the iPhone19,4 iOS 27.2 restore, per build identity. '
     'Personalization (the IM4M ticket from Apple\'s signing server) covers each component\'s digest; flags such as '
     '`Trusted`, `ESEC` and `EPRO` say how it is checked. **[FW]**', '',
     f'- ProductVersion: `{m.get("ProductVersion")}`, ProductBuildVersion: `{m.get("ProductBuildVersion")}`',
     f'- SupportedProductTypes: {", ".join(f"`{x}`" for x in m.get("SupportedProductTypes", []))}', '']
for bi in m['BuildIdentities']:
    info = bi.get('Info', {})
    L += [f'## {info.get("Variant", "?")}', '']
    for k in ('ApChipID', 'ApBoardID', 'ApSecurityDomain', 'Ap,ProductType', 'Ap,Target', 'Ap,TargetType', 'Ap,ProductMarketingVersion', 'Ap,OSLongVersion'):
        if k in bi:
            L.append(f'- `{k}`: `{bi[k]}`')
    for k in sorted(info):
        if isinstance(info[k], (str, int, bool)):
            L.append(f'- Info `{k}`: `{info[k]}`')
    comps = bi.get('Manifest', {})
    L += ['', f'{len(comps)} components.', '', '| Component | Path | Digest (SHA-384, first 16 hex) | Flags |', '|---|---|---|---|']
    for name in sorted(comps):
        c = comps[name]
        ci = c.get('Info', {})
        dg = c.get('Digest')
        flags = [k for k in ('Trusted', 'ESEC', 'EPRO', 'IsFirmwarePayload', 'IsLoadedByiBoot', 'IsLoadedByiBootStage1', 'IsiBootEANFirmware',
                             'IsiBootNonEssentialFirmware', 'IsSecondaryFirmware', 'IsFUDFirmware', 'IsEarlyAccessFirmware',
                             'IsLoadedByiBootStage1', 'RestoreRequestRules') if c.get(k) or ci.get(k)]
        L.append(f'| `{name}` | `{ci.get("Path", "")}` | `{dg.hex()[:16] if isinstance(dg, bytes) else ""}` | {", ".join(flags)} |')
    L += ['', '### Component details', '']
    for name in sorted(comps):
        c = comps[name]
        L.append(f'#### `{name}`')
        for k in sorted(c):
            if k == 'Info':
                for ik in sorted(c['Info']):
                    v = c['Info'][ik]
                    L.append(f'- Info `{ik}`: `{v.hex() if isinstance(v, bytes) else str(v)[:300]}`')
            else:
                v = c[k]
                L.append(f'- `{k}`: `{v.hex() if isinstance(v, bytes) else str(v)[:300]}`')
        L.append('')
open(sys.argv[2], 'w').write('\n'.join(L) + '\n')
print(len(L), 'lines')
