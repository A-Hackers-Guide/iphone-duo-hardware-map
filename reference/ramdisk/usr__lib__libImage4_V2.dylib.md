# `/usr/lib/libImage4_V2.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 481,280 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 21 (Size: 2032)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (5)

- `/usr/lib/libImage4_V2.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/system/libcorecrypto.dylib (compatibility version 1.0.0, current version 2109.40.22)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`

## Entitlements

```xml
  - no entitlements
```

## Strings (283)

```
payload evaluation: property ignored\n
allow data-only: %u\n
chip-id: 0x%04X\n
AP|AntiReplayNone|Global
manifest evaluation: previous stage digest mismatch\n
manifest evaluation: environment enables mix-and-match\n
Cryptex1|Splat
Cryptex1|Splat|SubsequentStage
manifest evaluation: failed to compute manifest digest: %d\n
cryptex1-certificate-format
>=
Cryptex1|Splat|AntiReplayNone
Cryptex1|Generic|AntiReplayNone
IOKit error when querying supplemental Root CA: %d\n
manifest evaluation: unable to resolve a valid decode implementation\n
chip-id
manifest evaluation: using caller-provided previous stage digest\n
IOKit error for activating object: %u | %d\n
Cryptex1|SecureMobileAssetBrain
IOKit error when querying nonce proposal: %d\n
local-policy-epoch: %llu\n
secure-boot: n/a\n
local-policy: n/a\n
lp-stng
manifest evaluation: no policy for subsequent stage anti-replay\n
manifest evaluation: unable to obtain previous stage digest: %u\n
payload evaluation: failed security mode check: %u\n
unable to acquire Diavlo Root CA from expert: %u\n
board-id: n/a\n
diavlo: n/a\n
vmm-present
Image4
current-production-status: n/a\n
cryptex1: n/a\n
payload evaluation: trust evaluation successful\n
==
IOKit error when querying nonce digest: %d\n
manifest evaluation: 'lobo' ignored for satellite evaluation\n
match integer32: value [0x%X] %s property [0x%X]\n
<empty>
unable to build decode implementation for Diavlo: %u\n
manifest evaluation: attempting first stage anti-replay policy: %u\n
board-id: 0x%02X\n
Cryptex1|Generic
userspace
security-domain: %u\n
payload evaluation: '%c%c%c%c'\n
lp-spih
unable to connect with %s kernel service: %d\n
booted-with-local-policy: %u\n
esdm-fuses
chip-epoch
rsa3072
manifest evaluation: unable to get seed from restore-info: %u\n
manifest evaluation: unable to compute nonce with expert: %u\n
%y%m%d%H%M%SZ
allow internal-use-only-builds: %u\n
cryptex1-chip-id: 0x%04X\n
payload evaluation: failed to compute payload digest: %d\n
LocalPolicy
unable to query nonce proposal: %u | %u\n
IOKit error when rolling nonce: %d\n
%02x
darwin pseudo-expert: starting boot\n
cryptex1-product-class: 0x%02X\n
manifest evaluation: starting auxiliary evaluation\n
manifest evaluation: manifest does not have anti-replay nonce\n
Cryptex1|SecureMobileAssetWithCodeLoad
platform: %u\n
factory-prerelease-global-trust
cryptex1-chip-id
AP|SRDP
unable to find /product\n
certificate-production-status: n/a\n
manifest evaluation: signature and identity evaluation successful\n
internal-use-only-unit
manifest evaluation: nonce type: %u\n
manifest evaluation: nonce tag:  '%c%c%c%c'\n
manifest evaluation: enforcing subsequent stage policy: %u\n
IMAGE4_LOG_FILE
love
com.apple.Image4
manifest evaluation: environment specific policy successful\n
<=
certificate-security-mode: %u\n
payload evaluation: unable to resolve a valid decode implementation\n
manifest evaluation: property matched\n
secureboot-key-scheme
AP|DDI
Cryptex1|SplatGlobal
avp: %u\n
payload evaluation: starting trust evaluation\n
manifest evaluation: enforcing restore-info nonce\n
environment
Ap|EphemeralDiavlo
unable to find /defaults\n
chip-epoch: %u\n
manifest evaluation: 'stng' ignored for satellite evaluation\n
manifest evaluation: property mismatch: %u\n
IOKit error when querying proposed nonce seed: %d\n
manifest evaluation: failed: %d, %u\n
darwin pseudo-expert: boot complete\n
AP|PDI
v8@?0
current-security-mode: n/a\n
darwin pseudo-expert: unable to provide UniqueDeviceID [ChipID]\n
rsa2048
manifest evaluation: nonce tag: '%c%c%c%c'\n
AP|FirstStage
Cryptex1|SecureMobileAssetBrainX86Global
current-production-status: %u\n
x509
unique-chip-id
chip-epoch: n/a\n
chip-id: n/a\n
os-version: %.*s\n
payload evaluation: insufficient space for payload hash\n
Software|FF01
Cryptex1|UpdateBrain
00000000-0000-0000-0000-000000000000
manifest evaluation: no policy for first stage anti-replay\n
unique-chip-id: 0x%016llX\n
volume-uuid: %s\n
payload evaluation: starting auxiliary evaluation\n
manifest evaluation: unexpected property\n
payload evaluation: failed: %d, %u\n
lp-smb0
cryptex1-product-class
[na]
manifest evaluation: starting signature and identity evaluation: %s\n
manifest evaluation: starting anti-replay evaluation\n
manifest evaluation: '%c%c%c%c'\n
LocalPolicyTatsu|LiveBoot
unable to find /chosen\n
payload evaluation: property matched\n
Cryptex1|Splat|FirstStage
manifest evaluation: failed first stage anti-replay: %u\n
payload evaluation: failed fusing policy: %u\n
manifest evaluation: enforcing boot nonce\n
manifest evaluation: using nonce type:  %u\n
supplementary Root CA already exists: %u\n
%u.%u.%u.%u.%u,%u
extended-security-domain: n/a\n
payload evaluation: attempting fusing policy: '%c%c%c%c'\n
AP
Cryptex1|Splat|AntiReplayNone|Global
booted-locally: %u\n
extended-security-domain: %u\n
manifest evaluation: auxiliary evaluation successful\n
manifest evaluation: signing-authority: %u\n
manifest evaluation: restore-info tag: '%c%c%c%c'\n
manifest evaluation: attempting 'vnum' policy\n
Cryptex1|GenericDiavlo
apfs-preboot-uuid
rsa1024
manifest evaluation: unable to get nonce from manifest: %u\n
manifest evaluation: 'vnum' ignored for satellite evaluation\n
%F
certificate-security-mode: n/a\n
certificate-production-status: %u\n
cryptex1: %.*s | %.*s\n
payload evaluation: starting signature evaluation: %s\n
manifest evaluation: 'vuid' ignored for satellite evaluation\n
manifest evaluation: attempting subsequent stage anti-replay policy: %u\n
manifest evaluation: unable to obtain environment OS version: %u\n
Cryptex1|SafariDownlevel
unable to find %s kernel service\n
secure-boot: %.*s | %.*s\n
local-policy: %.*s | %.*s\n
uses-avp-root-ca
manifest evaluation: unable to get type from domain: %u\n
manifest evaluation: 'vnum' mismatch: build tuple %u\n
manifest evaluation: 'EPRO' and 'ESEC' ignored for satellite evaluation\n
payload evaluation: failed to get payload type: %d\n
manifest evaluation: exempted 'vnum' policy due to sideloading\n
match boolean: value [%u] %s property [%u]\n
volume-uuid: n/a\n
payload evaluation: property mismatch: %u\n
Cryptex1|SecureMobileAssetX86Global
local-policy-epoch: n/a\n
LocalPolicy|Linked
secureboot-certificate-format
boot-manifest-hash
expert: %s\n
diavlo: %.*s | %.*s\n
manifest evaluation: coreTrustVerifySignature failure: 0x%0X\n
lp-smb1
cryptex1-key-scheme
pqc-validation-flags
manifest evaluation: '%c%c%c%c' mismatch\n
Cryptex1|GenericX86Global
disable-pqc: %u\n
name
darwin pseudo-expert: invalid VolumeUuid [Encoding]\n
im4c
IOKit error when querying nonce seed: %d\n
stdout
IOKit error when querying supplemental Root CA length: %d\n
runtime: %u\n
mix-n-match-prevention-status
darwin pseudo-expert: invalid VolumeUuid [Length]\n
hybridscheme3
manifest evaluation: unable to get nonce from expert: %u\n
unable to query proposed nonce seed: %u | %u\n
manifest evaluation: no environment specific auxiliary policy\n
manifest evaluation: insufficient space for manifest hash\n
manifest
Cryptex1|SecureMobileAssetLoad
Ap|PersistentDiavlo
stderr
manifest evaluation: %s: version: %s\n
Cryptex1|SemiSplatGlobal
manifest evaluation: starting trust evaluation\n
manifest evaluation: restore-info seed too large: %lu\n
manifest evaluation: property ignored\n
rsa4096
manifest evaluation: unable to obtain manifest version: %u\n
%02x%02x...%02x%02x
AP|AntiReplayNone
LocalPolicyTatsu|RecoveryBoot
Cryptex1|SecureMobileAssetInstall
Software|FF06
payload evaluation: payload type: '%c%c%c%c'\n
Cryptex1|SemiSplat
security-domain: n/a\n
effective-production-status-ap
manifest evaluation: domain tag: '%c%c%c%c'\n
unable to query nonce seed: %u | %u\n
unable to find /chosen/manifest-properties\n
%Y%m%d%H%M%SZ
match integer64: value [0x%llX] %s property [0x%llX]\n
current-security-mode: %u\n
manifest evaluation: coreTrustVerifyChain failure: 0x%0X\n
AP|OSManifest
unique-chip-id: n/a\n
manifest evaluation: 'iuob' ignored for satellite evaluation\n
engineering-use-only-unit
security-domain
satellite trust evaluation disallowed with type: 0x%08X\n
manifest evaluation: enforcing cryptex1 nonce\n
AP|SubsequentStage
mix-and-match: %u\n
certificate-production-status
manifest evaluation: exempted 'vnum' policy due to build group\n
LocalPolicy|AntiReplayNone
match data: value [%lub,%s] %s property [%lub,%s]\n
payload evaluation: '%c%c%c%c' mismtch\n
Userspace
Cryptex1|SecureMobileAssetWithCodeInstall
manifest evaluation: subsequent stage anti-replay successful\n
boot-command
manifest evaluation: trust evaluation successful\n
manifest evaluation: attempting 'rpnh' policy\n
manifest evaluation: using caller-provided nonce\n
manifest evaluation: unable to get domain from manifest: %u\n
payload evaluation: failed production status check: %u\n
manifest evaluation: first stage anti-replay successful\n
manifest evaluation: 'data' ignored for satellite evaluation\n
unable to roll nonce: %u | %llu\n
unable to query supplemental Root CA: %llu\n
manifest evaluation: failed subsequent stage anti-replay: %u\n
payload evaluation: fusing policy successful\n
payload evaluation: auxiliary evaluation successful\n
certificate-security-mode
darwin pseudo-expert: unable to provide UniqueDeviceID [UniqueChipID]\n
manifest evaluation: manifest does not have an attached restore-info\n
unable to set supplemental Root CA: %u | %u\n
board-id
darwin pseudo-expert: invalid VolumeUuid [Termination]\n
os-version: n/a\n
manifest evaluation: manifest enables mix-and-match\n
Software|FF00
effective-security-mode-ap
[un]
unable to find /chosen/asmb\n
manifest evaluation: failed environment specific policy: %u\n
manifest evaluation: anti-replay evaluation successful\n
manifest evaluation: manifest tag: '%c%c%c%c'\n
avp3: %u\n
payload evaluation: signature evaluation successful\n
manifest evaluation: 'vnum' policy successful\n
AP|Global
2006-05-31
```
