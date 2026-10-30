# `/usr/lib/libImage4_V2.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 481,280 bytes.

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
local-policy: %.*s | %.*s\n
manifest evaluation: insufficient space for manifest hash\n
payload evaluation: auxiliary evaluation successful\n
cryptex1-key-scheme
payload evaluation: trust evaluation successful\n
payload evaluation: attempting fusing policy: '%c%c%c%c'\n
AP|SRDP
Image4
manifest evaluation: failed: %d, %u\n
satellite trust evaluation disallowed with type: 0x%08X\n
manifest evaluation: unable to get seed from restore-info: %u\n
unable to query nonce seed: %u | %u\n
chip-epoch: %u\n
chip-id: n/a\n
payload evaluation: starting auxiliary evaluation\n
internal-use-only-unit
vmm-present
effective-security-mode-ap
lp-smb0
Cryptex1|SecureMobileAssetWithCodeLoad
darwin pseudo-expert: unable to provide UniqueDeviceID [ChipID]\n
darwin pseudo-expert: invalid VolumeUuid [Encoding]\n
manifest evaluation: enforcing boot nonce\n
manifest evaluation: restore-info tag: '%c%c%c%c'\n
LocalPolicy|Linked
IMAGE4_LOG_FILE
manifest evaluation: no environment specific auxiliary policy\n
payload evaluation: payload type: '%c%c%c%c'\n
rsa4096
volume-uuid: %s\n
manifest evaluation: using caller-provided nonce\n
manifest evaluation: attempting subsequent stage anti-replay policy: %u\n
IOKit error when querying nonce seed: %d\n
certificate-production-status: %u\n
os-version: n/a\n
payload evaluation: failed fusing policy: %u\n
supplementary Root CA already exists: %u\n
manifest evaluation: manifest does not have anti-replay nonce\n
Cryptex1|SemiSplatGlobal
current-production-status: n/a\n
manifest evaluation: failed to compute manifest digest: %d\n
apfs-preboot-uuid
rsa3072
LocalPolicy
unable to find %s kernel service\n
payload evaluation: property mismatch: %u\n
chip-epoch
manifest evaluation: using caller-provided previous stage digest\n
unable to acquire Diavlo Root CA from expert: %u\n
manifest evaluation: %s: version: %s\n
manifest evaluation: unable to resolve a valid decode implementation\n
love
00000000-0000-0000-0000-000000000000
[un]
secure-boot: %.*s | %.*s\n
manifest evaluation: property mismatch: %u\n
payload evaluation: signature evaluation successful\n
manifest evaluation: unable to obtain manifest version: %u\n
==
unable to find /product\n
extended-security-domain: %u\n
manifest evaluation: manifest enables mix-and-match\n
manifest evaluation: attempting 'vnum' policy\n
security-domain: n/a\n
os-version: %.*s\n
manifest evaluation: failed subsequent stage anti-replay: %u\n
payload evaluation: fusing policy successful\n
manifest evaluation: '%c%c%c%c' mismatch\n
match integer32: value [0x%X] %s property [0x%X]\n
Cryptex1|SecureMobileAssetBrainX86Global
environment
Cryptex1|UpdateBrain
allow data-only: %u\n
payload evaluation: '%c%c%c%c'\n
manifest evaluation: attempting 'rpnh' policy\n
manifest evaluation: signing-authority: %u\n
manifest evaluation: 'vnum' policy successful\n
manifest evaluation: signature and identity evaluation successful\n
manifest evaluation: 'vuid' ignored for satellite evaluation\n
certificate-security-mode
manifest evaluation: attempting first stage anti-replay policy: %u\n
Cryptex1|Splat
Cryptex1|SecureMobileAssetInstall
Software|FF00
unable to query supplemental Root CA: %llu\n
manifest evaluation: 'lobo' ignored for satellite evaluation\n
manifest evaluation: unable to get nonce from expert: %u\n
manifest evaluation: manifest tag: '%c%c%c%c'\n
manifest evaluation: exempted 'vnum' policy due to sideloading\n
avp: %u\n
volume-uuid: n/a\n
manifest evaluation: trust evaluation successful\n
payload evaluation: starting trust evaluation\n
manifest evaluation: unable to obtain environment OS version: %u\n
v8@?0
disable-pqc: %u\n
darwin pseudo-expert: unable to provide UniqueDeviceID [UniqueChipID]\n
AP|PDI
Ap|EphemeralDiavlo
unable to find /defaults\n
unable to set supplemental Root CA: %u | %u\n
certificate-security-mode: %u\n
name
manifest evaluation: no policy for first stage anti-replay\n
payload evaluation: failed security mode check: %u\n
Cryptex1|Generic
IOKit error when querying proposed nonce seed: %d\n
manifest evaluation: auxiliary evaluation successful\n
payload evaluation: starting signature evaluation: %s\n
manifest evaluation: 'iuob' ignored for satellite evaluation\n
AP|Global
IOKit error when querying nonce digest: %d\n
board-id: n/a\n
manifest evaluation: unable to get domain from manifest: %u\n
payload evaluation: '%c%c%c%c' mismtch\n
Cryptex1|Splat|AntiReplayNone|Global
payload evaluation: property matched\n
Cryptex1|GenericDiavlo
x509
cryptex1-product-class
Userspace
certificate-production-status: n/a\n
manifest evaluation: 'stng' ignored for satellite evaluation\n
manifest evaluation: coreTrustVerifySignature failure: 0x%0X\n
uses-avp-root-ca
darwin pseudo-expert: invalid VolumeUuid [Termination]\n
manifest evaluation: enforcing restore-info nonce\n
%y%m%d%H%M%SZ
LocalPolicy|AntiReplayNone
factory-prerelease-global-trust
lp-spih
manifest evaluation: 'vnum' mismatch: build tuple %u\n
<=
AP|FirstStage
Cryptex1|GenericX86Global
Cryptex1|Splat|SubsequentStage
current-security-mode: n/a\n
manifest evaluation: subsequent stage anti-replay successful\n
cryptex1-certificate-format
[na]
manifest evaluation: unable to get nonce from manifest: %u\n
manifest evaluation: unable to compute nonce with expert: %u\n
Cryptex1|SemiSplat
manifest evaluation: starting signature and identity evaluation: %s\n
manifest evaluation: starting auxiliary evaluation\n
payload evaluation: failed: %d, %u\n
AP|DDI
payload evaluation: unable to resolve a valid decode implementation\n
manifest evaluation: unexpected property\n
Cryptex1|SecureMobileAssetX86Global
unable to query proposed nonce seed: %u | %u\n
%F
local-policy-epoch: %llu\n
manifest evaluation: failed first stage anti-replay: %u\n
Cryptex1|Generic|AntiReplayNone
secureboot-certificate-format
cryptex1-chip-id
match boolean: value [%u] %s property [%u]\n
>=
Software|FF01
cryptex1-chip-id: 0x%04X\n
local-policy-epoch: n/a\n
manifest evaluation: nonce tag: '%c%c%c%c'\n
manifest evaluation: no policy for subsequent stage anti-replay\n
manifest evaluation: previous stage digest mismatch\n
current-production-status: %u\n
diavlo: n/a\n
unable to find /chosen/manifest-properties\n
payload evaluation: failed to compute payload digest: %d\n
manifest evaluation: nonce tag:  '%c%c%c%c'\n
%02x%02x...%02x%02x
AP
unable to find /chosen\n
secureboot-key-scheme
match integer64: value [0x%llX] %s property [0x%llX]\n
Cryptex1|SecureMobileAssetBrain
Cryptex1|Splat|FirstStage
cryptex1-product-class: 0x%02X\n
manifest evaluation: environment specific policy successful\n
IOKit error when querying nonce proposal: %d\n
runtime: %u\n
security-domain: %u\n
local-policy: n/a\n
lp-stng
stdout
certificate-security-mode: n/a\n
unique-chip-id
hybridscheme3
manifest evaluation: unable to obtain previous stage digest: %u\n
allow internal-use-only-builds: %u\n
effective-production-status-ap
darwin pseudo-expert: starting boot\n
chip-id
boot-manifest-hash
manifest evaluation: exempted 'vnum' policy due to build group\n
unable to connect with %s kernel service: %d\n
manifest evaluation: '%c%c%c%c'\n
LocalPolicyTatsu|RecoveryBoot
Cryptex1|SafariDownlevel
Ap|PersistentDiavlo
manifest evaluation: failed environment specific policy: %u\n
manifest evaluation: property ignored\n
engineering-use-only-unit
im4c
manifest evaluation: unable to get type from domain: %u\n
match data: value [%lub,%s] %s property [%lub,%s]\n
com.apple.Image4
Cryptex1|Splat|AntiReplayNone
booted-locally: %u\n
manifest evaluation: property matched\n
Cryptex1|SplatGlobal
unable to build decode implementation for Diavlo: %u\n
pqc-validation-flags
manifest
Software|FF06
unique-chip-id: n/a\n
cryptex1: %.*s | %.*s\n
cryptex1: n/a\n
lp-smb1
<empty>
IOKit error when querying supplemental Root CA: %d\n
unable to find /chosen/asmb\n
secure-boot: n/a\n
manifest evaluation: using nonce type:  %u\n
AP|AntiReplayNone|Global
unable to query nonce proposal: %u | %u\n
%u.%u.%u.%u.%u,%u
platform: %u\n
manifest evaluation: starting anti-replay evaluation\n
payload evaluation: property ignored\n
boot-command
board-id
avp3: %u\n
chip-id: 0x%04X\n
manifest evaluation: anti-replay evaluation successful\n
rsa1024
IOKit error for activating object: %u | %d\n
certificate-production-status
esdm-fuses
%Y%m%d%H%M%SZ
expert: %s\n
unique-chip-id: 0x%016llX\n
rsa2048
%02x
darwin pseudo-expert: boot complete\n
manifest evaluation: starting trust evaluation\n
IOKit error when rolling nonce: %d\n
unable to roll nonce: %u | %llu\n
IOKit error when querying supplemental Root CA length: %d\n
current-security-mode: %u\n
manifest evaluation: restore-info seed too large: %lu\n
manifest evaluation: 'EPRO' and 'ESEC' ignored for satellite evaluation\n
AP|SubsequentStage
Cryptex1|SecureMobileAssetWithCodeInstall
booted-with-local-policy: %u\n
security-domain
manifest evaluation: enforcing subsequent stage policy: %u\n
2006-05-31
board-id: 0x%02X\n
payload evaluation: insufficient space for payload hash\n
manifest evaluation: enforcing cryptex1 nonce\n
manifest evaluation: manifest does not have an attached restore-info\n
chip-epoch: n/a\n
diavlo: %.*s | %.*s\n
manifest evaluation: coreTrustVerifyChain failure: 0x%0X\n
Cryptex1|SecureMobileAssetLoad
mix-and-match: %u\n
extended-security-domain: n/a\n
manifest evaluation: first stage anti-replay successful\n
manifest evaluation: 'data' ignored for satellite evaluation\n
manifest evaluation: domain tag: '%c%c%c%c'\n
stderr
darwin pseudo-expert: invalid VolumeUuid [Length]\n
manifest evaluation: nonce type: %u\n
manifest evaluation: 'vnum' ignored for satellite evaluation\n
payload evaluation: failed production status check: %u\n
AP|OSManifest
LocalPolicyTatsu|LiveBoot
userspace
payload evaluation: failed to get payload type: %d\n
mix-n-match-prevention-status
manifest evaluation: environment enables mix-and-match\n
AP|AntiReplayNone
```
