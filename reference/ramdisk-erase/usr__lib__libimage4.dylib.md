# `/usr/lib/libimage4.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 635,680 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 22 (Size: 2496)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (5)

- `/usr/lib/libimage4.dylib (compatibility version 1.0.0, current version 374.0.0)`
- `/usr/lib/libImage4_V2.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (869)

```
failed to parse payload: %d
heap
DERDecodeSeqContentInit: %d
panic: sysctlnametomib: %s%d
AP [software ff01]
odometer[%s]: restore info nonce too large: actual = %lu, expected <= %lu
panic: nonce too large: actual = %lu, expected <= %ld
stock runtime; not querying for mix-n-match policy
MUST EXIST
cryptex1
failed to entangle nonce: %d
kext cannot parse argument vector: v = %hx, how = %s, trap = %s: %d
odometer[%s:%s]: internal unit; not enforcing policy
manifest boot failed: %s: %d
certificate-security-mode
_darwin_runtime_get_identifier_cstr
odometer allocated on %s
panic: Img4DecodeCopyPayloadDigest: %d
srd nonce hash
.
unprivileged limit
PDI-DIGEST
odometer[%s:%s]: allowing cross-group policy: production status
DEREncoderAddUInt64: %d
_darwin_runtime_copy_nonce
forcing sideload anti-replay policy due to subsequent stage firmware evaluation
non-executable privilege level
%s: enforcing length[%s %s %s]: %lu %s %lu: %d
panic: incomplete coprocessor map: handle = %lld, expected < %lld
user client method failed: v = %hx, trap = %s, kr = %#x, sys = %#x, sub = %#x, code = %#x
panic: illegal chip configuration: %s
Cryptex1 mobile asset code load [AP host]
applied transform: p = %s, type = %s, xf kind = %s, value = [%s => 0x%llx], error = [%d => %d]
panic: non-sensical crypto hash method: %s
DERImg4DecodeProperty: %d
panic: digest length overflow: actual = %u, expected >= %lu
_restore_runtime_get_identifier_cstr
resolving environment: coproc = %s, handle = %llx, secure boot = %llx
trust evaluation failed: %d
found object: %s
invalid unique tag list: actual length = %u, expected %% %lu == 0
DEREncoderCreate: %d
Cryptex1 prospective boot [AP host]
odometer[%s:%s]: manifest self-entitled for mix-n-match; relaxing all odometer policy
img4_nonce_domain_roll_nonce: %d
CHIP_CRYPTEX1_BOOT_VMA2_CLONE_VERIFICATION
boot uuid
id4->id_p->p_type->pt_switchable
effective-production-status-ap
unrecognized object property: %s
computing nonce digest: chip = %s, digest length = %lu
%s: read: %d
rd
secureboot key scheme
panic: bogus nonce length: actual = %lu, expected <= %lu
info
exception level
forcing sideload anti-replay policy
kImg4DecodeSecureBootG7Rsa4kSha384IM4C
pmap data
failed to allocate node
property not present: %s: %d
crypto-hash-method
CHIP_CRYPTEX1_BOOT_AP_REDUCED_PROSPECTIVE
panic: unsupported digest type: oid len = %lu
rsa4096
kImg4DecodeSecureBootRsa4kSha384DDI
unexpected section tag: %s
failed to add MANP node: %d
CHIP_CRYPTEX1_MOBILE_ASSET_DFU_VMA2
decode context allocated on %s
odometer[%s:%s]: failed to query restore info nonce: %d
_restore_runtime_get_identifier_uint32
SEP_
panic: iteration underflow: idx = 0x%lx, %ld
%s: finding digest algorithm for oid: %s
local policy
failed to allocate item node
odometer[%s:%s]: mix-n-match god mode not set; enforcing strict mix-n-match behavior
panic: attempt to deallocate static buffer
cryptex1 chip identifier
panic: failed to get defaults node
payload
panic: closure node deallocated while still in list
CHAIN
panic: buffer not large enough for digest: actual = %lu, expected >= %lu
odometer[%s]: versions directly comparable; allowing enforcement decision to stand
DEREncoderCreateImage4Dictionary: %d
DEREncoderAddImage4Tag: IM4M: %d
_restore_runtime_set_nonce
RELEASE
panic: illegal chip definition: anti-reply and sideload policies defined: %s
darwin-user
Cryptex1 boot verification [AP host]
no boolean property callback
property failed to impose on environment: %s: %d
%s: enforcing[%s %s %s]: 0x%x %s 0x%x: success
odometer[%s]: enforcing anti-replay
odometer[%s:%s]: failed to query boot nonce hash: %d
security.mac.image4.kmod.evaluate_trust_vn
security.mac.image4.nonce.roll
security.mac.image4.image.dfu
panic: bogus exit from enforcement loop: pdr = %d
constraint->type
security.mac.image4.image.copy_active
CRYPTEX0
MOBILE_ASSET_CODE_INSTALL
set resolver
cryptex1 chip subtype
booted manifest
panic: unexpected trust evaluation entry: i = %lu
panic: invalid log file descriptor: actual = %ld, expected <= %d
panic: object overflows buffer: object = firmware, length = %lu, required = %lu
security domain
%s: enforcing length[%s %s %s]: %lu %s %lu: success
odometer[%s]: failed to query chip boot: %s: %d
user client method success
Repair UCRT
certificate epoch
IOServiceOpen: %d
%s: Img4DecodeGetPayloadType: %d
allow mix-n-match
panic: attempt to deallocate loaned buffer without returning
_restore_runtime_log_handle
cryptex1 manifest hash
normalize
odometer[%s:%s]: no manifest constraint for policy selection
error
_t_preference
no manifest with which to select chip
volume group uuid
[DEBUG] 
forcing failure after audit completion: %d
prepared custom nonce hash
certificate
security.mac.image4.kmod.test_firebloom
GENERIC
%s: inserting node: %s
md0
%6s  %-36s : %s
kImg4DecodeLocalPolicyEc384Sha384QA
manx section constraints not implemented
CHIP_CRYPTEX1_GENERIC_AP
%s: inserting item node
[error decoding data %d]
boot manifest
odometer[%s]: expert does not boot chip
board-id
CHIP_AP_SOFTWARE_FF01
lvl
panic: unsupported container for posting: %u
panic: Img4DecodeGetPayload: %d
AP
%s: removing node
odometer[%s]: manifest is live and boot chain is intact
%s: chip has no associated dfu policy: %d
%s %-36s : 0x%x
cryptex1 auxilliary boot nonce hash
x509
AP_LOCAL_
Img4DecodePerformManifestTrustEvaluation: %d
unconstrained absence
payload->i4b_len
kImg4DecodeSecureBootRsa4kSha384X86
%s: tag not in unique list
CRYPTEX1-BOOT-SECURE-BOOT
len
,
odometer[%s:%s]: internal use-only unit entitlement found
odometer[%s:%s]: boot object has restore info
cryptex1 boot nonce hash
%#x
odometer[%s:%s]: enforcing nonce hash directly
performing boot trust evaluation: coprocessor = %s, type = %s
panic: object overflows buffer: object = chip, length = %lu, required = %lu
property does not exist: container = %s, type = %x, p = %s
object property failed to impose on environment: %d
known-constant allocation
querying custom runtime for boot manifest hash
supported chip
QA
kImg4DecodeSecureBootRsa4kSha384AVP
CHIP_CRYPTEX1_BOOT_AP
digest
panic: illegal property definition: %s
odometer[%s:%s]: switch constraint not satisfied
internal use-only unit
rsa3072
panic: illegal chip definition: sideload and pivot policies defined: %s
%s: failed to encode property node: %d
failed to allocate item sequence encoder: %d
panic: integer cast underflow: v = %s, actual = %lld, expected >= 0
odometer[%s]: expert boots chip
ERROR
unconstrain
performing normalization trust evaluation: coprocessor = %s, handle = %llx, evaluation type = %s
id4->id_p->p_constraint->pc_code
failed to decode property: container = %s, type = %x, p = %s: %d
im4c
img4_nonce_domain_peek_nonce: %d
odometer[%s]: nonce hash supplied; simulating first-stage boot
Cryptex1 mobile asset [VMA2 host]
certificate chain verification failed: %d
odometer[%s:%s]: constraint violation: %s: %d
panic: no anti-replay policy selected
%s: cur offset = %lld
incoming parameter error
cryptex1 auxilliary boot nonce
%d
^~
/dev/console
AppleImage4
trying chip: %s
%s: retrieved pinned root from trust store: type = 0x%llx, length = %lu, oid = %s, oid length = %lu
diagnostic level
%s: simulating chip boot for reduced-security virtual chip policy
generic error
panic: length not expressible as ssize_t: %lu
unexpected type: actual = %s, expected = %s
CHIP_VMA2_CLONE
EL0
Cryptex1 boot [reduced-security AP host]
panic: no more property record slots
failed to copy kcinstall nonce hash: %d
failed to check for %s: %d
stock runtime; not querying for boot manifest hash
security.mac.image4.nonce.verify
unique tag entry[%zu] = %s
odometer[%s:%s]: chip has no property for policy
CHIP_VMA2_DDI
firmware
AP-SECURE-BOOT
DEREncoderAddSetFromEncoder: %d
engineering use-only unit
panic: invalid min/max: min = %u, max = %u
sign
kcinstall nonce hash
panic: operation not supported on this structure version: actual = %hu, expected >= %hu
cryptex1-certificate-format
panic: integer cast overflow: v = %s, actual = %llu, expected <= %llu
Img4DecodeGetPropertyInteger64: %d
panic: illegal chip definition: no static decode implementation: %s
pdi nonce hash
failed to parse boot session uuid: %s: %d
panic: function should never be called: %s
%s constraint satisfied: property = %s, type = %s
function not implemented in this configuration
CHIP_AP_REDUCED
uniq
panic: could not resolve chip for environment
boot manifest hash
panic: failed to resolve expert for runtime
PDI
panic: property is not constrainable: %s
failed to impose manifest for boot: %d
get kmod connection
boot-manifest-hash
chip has custom constraint for property: %s
KCINSTALL
queried cylinder: p = %s, v = 0x%x
panic: invalid coprocessor handle: actual = %llu, expected < %u
kern.osreleasetype
panic: invalid log file descriptor
sha1
panic: illegal chip definition: no dynamic decode implementation: %s | %d
BOOTPC_
recording property for closure computation: %s%s%s
MOBILE_ASSET_CODE_LOAD
preflight
EL1
BOOT_SIDELOAD
Img4DecodeGetPropertyInteger: %d
_restore_runtime_log
cryptex1 boot nonce
none
panic: illegal coprocessor map: canonical handle has no static or dynamic decode implementation
secure boot
cannot select chip with first-stage boots
kImg4DecodeSecureBootGlobalG1Rsa4kSha384IM4C
CHAIN_MANIFEST
panic: specialist not set after runtime entry
Cryptex1 boot verification [VMA2 host]
Cryptex1 boot [vma2 host clone]
Darwin Image4 Library Version 7.0.0: Sat Oct  3 16:24:37 PDT 2026; root:AppleImage4_libraries-374~9642/libimage4/RELEASE_ARM64E
panic: trust chain length exceeded: %lu
engineering-use-only-unit
object
preparing mix-n-match policy: 0x%x
:
generic
user client not supported on this target
panic: illegal %s property: %s
trust evaluation: dr = %d, ct = 0x%x, error = %d
validation
PDI-VMA2
>
manifest properties
falling back to base expert for property: %s
%y%m%d%H%M%SZ
%s property not imposable on chip: %s
GENERIC_CRYPTEX0
panic: attempt to deallocate loaned buffer
CHIP_CRYPTEX1_BOOT_VMA2_VERIFICATION
odometer[%s]: failed to query odometer cylinder: %s: %d
Yonkers - Factory
odometer[%s:%s]: policy is enforceable
manifest boot succeeded: %s
sysctlbyname[kern.bootsessionuuid]: %d
lp-stng
manifest
failed to query manifest hash identifier: %d
mfr
Cryptex1 boot [AP host]
  🔥🌸 
%6s  %-36s : 0x%llx
environment not supported: coprocessor = %s, handle = %llx: %d
CHIP_CRYPTEX1_MOBILE_ASSET_DFU_AP
%s: decode selection: dynamic
AP [software ff00]
%s: found unique tag
[error decoding uint %d]
trust evaluation failed: coprocessor = %s, sequence number = %lu, chain length = %lu: %d
hybridscheme3
panic: closure measurement requires a parsed manifest
_restore_runtime_get_identifier_uint64
object properties
host application processor
pi->p_type->pt_switchable
property callback: tag = %s, type = %d, asn1 type = %s, v length = %lu
kImg4DecodeSecureBootRsa3kSha384
SHA2_256
prospective cryptex1 manifest hash
[error decoding bool %d]
<data: %u bytes>
_restore_runtime_get_identifier_digest
board identifier
queried property: %s => 0x%x
chip has no static or dynamic decode implementation: %s
panic: iteration overflow: idx = 0x%lx, %lu
factory pre-release global trust
%s: failed to encode item node: %d
uint32
%s: enforcing[%s %s %s]: 0x%llx %s 0x%llx: %d
boot nonce hash
absence
booter environment not supported: %s: %d
BOOT_FLASH_SECONDARY
software update freshness nonce
374
odometer[%s]: manifest is current
failed to boot expert for chip selection: %d
kImg4DecodeLocalPolicyEc384Sha384Hacktivate
security.mac.image4.kmod.copy_version
<null>
%s: enforcing[%s %s %s]: %s %s %s: success
0.0.0.0.0,0
cps->cps_type
INIT
syscall: %s
odometer[%s:%s]: manifest inconsistent with restore info: %d
panic: length not expressible as unsigned 32-bit integer: %lu
set supervisor
CHIP_BOOTPC_SHA2_256
panic: nonce length overflow: actual = %lu, expected >= %lu
odometer[%s:%s]: no caller-supplied nonce hash
no data property callback
Img4DecodePerformTrustEvaluationWithCallbacks: %d
found %s; skipping
%s: decode selection: dynamic | %s
panic: digest length overflow: actual = %lu, expected >= %lu
odometer[%s]: failed to query restore info for boot nonce: %d
panic: digest buffer overflow: actual = %lu, expected >= %lu
DEBUG
panic: failed to get manifest properties
lp-smb1
panic: illegal chip definition: invalid manifest type for dynamic selection: %s
SHA2_384
virtual machine monitor present
odometer[%s:%s]: enforcing strict mix-n-match behavior
cryptex1-key-scheme
trust evaluation succeeded for payload: %s
DEREncoderAddSequenceFromEncoder: %d
%s: encoding closure property: p = %s, item = %s, type = %llx, val = %s
restore
cryptex1 certificate format
panic: bogus digest length: %lu
execute
performing trust evaluation: type = %s %s, chip = %s, chip type = 0x%llx, chip expert = %s, payload = %s
DERImg4DecodeProperty: %s: %d
panic: invalid trap number: actual = %#llx, expected < %#llx
panic: kernel nonce overflows bounds: actual = %u, expected <= %u
Img4DecodeIterateObjectItems: %d
CHIP_AP_LOCAL_PROSPECTIVE
cryptex1-product-class
odometer[%s:%s]: failed to entangle nonce: %d
failed to get boot nonce from callback: %d
panic: Img4DecodeCopyManifestDigest: %d
__image4_chp
AP_LOCAL
Cryptex1 boot [vma2 host]
Cryptex1 mobile asset code install [AP host]
CHAIN_FUTURE
%s %-36s
performing audit trust evaluation: coprocessor = %s, handle = %llx, secure boot level = %llx, evaluation type = %s
IOServiceOpen: success
panic: no cryptex1 guests for %s
trust evaluation succeeded; manifest is live
%s constraint violated: property = %s, type = %s: %d
pc
panic: failed to get secure boot level: %d
CHIP_VMA2_PDI
security.mac.image4.kmod.evaluate_trust_dlxk
security.mac.image4.nonce.generate_proposal
bootpc
_restore_runtime_roll_nonce
odometer[%s]: querying restore info for boot nonce: %s
DEREncoderAddBoolean: %d
null
expert
queried property: %s => %s
Img4DecodeGetPropertyData: %s: %d
manifest trust evaluation succeeded
misc. decoding error (badly formatted DER)
odometer[%s:%s]: sideload chip has no notary
ACDC
certificate-production-status
esdm-fuses
panic: bogus property container input: actual = %u, expected < %u
wrap
%s: read: bad read: actual = %ld, requested = %lu, chunk length = %lu: %d
trap failed: v = %hx, how = %s, trap = %s: %d
odometer[%s:%s]: manifest is consistent with boot chain
entangled boot nonce
vmm-present
preparing custom boot manifest hash: %s
FF00
odometer[%s:%s]: boot manifest hash is caller-supplied
get chip instance
v
odometer[%s:%s]: using caller-provided nonce hash
IOServiceGetMatchingService failed
%s: %s\n
panic: invalid secure boot state: %#x
panic: unreachable case: %s = 0x%llx
>=
|>
%s: enforcing[%s %s %s]: 0x%llx %s 0x%llx: success
secure_boot
debug level
BOOT_PRECOMP
CHIP_CRYPTEX1_ASSET_BRAIN_AP
HACKTIVATE_ECDSA
AP [software ff06]
cryptex1 key scheme
debug
panic: illegal chip definition: trust store cannot override static decode implementation: %s
Cryptex1 generic content [AP host]
treating payload as non-Image4 wrapped
posted property: container = %s, type = %x, p = %s
initialized trap: %s
failed to allocate DER encoder
odometer[%s:%s]: allowing cross-group policy: full security
panic: illegal chip/expert configuration
HOST_
com.apple.security.libimage4
*=
Cryptex1 boot verification [VMA2 clone host]
%s: stall while reading file
2006-05-31
bounds safety
pqc-validation-flags
panic: Img4DecodeRestoreInfoExists: %d
unrecognized manifest property: %s
kImg4DecodeSecureBootRsa1kSha1
unexpected certificate property type: tag = %s, type = 0x%llx
security.mac.image4.kmod.evaluate_trust
panic: memset_s: %d
panic: insufficient memory for expert: actual = %lu, expected >= %lu
no callbacks present
property callback: tag = %s, type = %d, asn1 type = %s, v = 0x%llx
%s: enforcing[%s %s %s]: %s %s %s: %d
panic: close%d
 [INFO] 
Savage - Factory
CHIP_AP_SRDP
0x%llx
data
boot
buffer overflow
DEREncoderAddImage4TagUInt32: %d
panic: non-%s property set: property = %s, type = %s
/Library/Caches/com.apple.xbs/DA468FD9-0FD8-4F31-A85C-FDEDC90B7D37/TemporaryDirectory.AVOBqm/Binaries/AppleImage4_libraries/install/Symbols/image4
prospective local policy generation
boot chip
p_where
%s: %#x
secureboot-key-scheme
Img4DecodePerformManifestTrustEvaluationWithCallbacks: %d
%Y%m%d%H%M%SZ
panic: null coprocessor handle
odometer[%s:%s]: manifest has no pivot constraint
kImg4DecodeSecureBootRsa4kSha384DDIGlobal
trap failed: %s: %d
BOOT_LIVE
panic: attempt to destroy already destroyed buffer
==
BOOT_STATIC
panic: nonce cannot fit into 64-bit integer: actual = %lu, expected <= %lu
panic: trust chaining not supported for evaluation: %s
no integer record for tag: %s
CHIP_AP_DDI_SHA2_384
manifest-only evaluation; permitting replay
%s: left to read = %lu
CHIP_AP_SOFTWARE_FF06
\n
manifest replay denied: %d
Img4DecodeGetPropertyInteger64: %s: %d
%s: failed to query anchor: 0x%llx: %d
CHIP_VMA3
SHA2_224
odometer[%s:%s]: boot object has no restore info
static
CHIP_AP_LOCAL
panic: unexpected expert: op = %s, actual = %s, expected = %s
GL1
querying property with chip expert resolution: p = %s, chip = %s, chip type = 0x%llx, chip expert authority >= 0x%llx
allow-ecid-mismatch
CHIP_CRYPTEX1_MOBILE_ASSET_VMA2
restore info
d->d_len
X86_
secure enclave processor
IMAGE4_LOG_FD
kImg4DecodeLocalPolicyEc384Sha384
%s: decode selection: static
AP_
%s: enforcing[%s %s %s]: 0x%x %s 0x%x: %d
CHIP_AP_SHA2_384
cryptex1 chip type
mix-n-match-prevention-status
calling out to manifest prepare function
research mode
application processor
chip environment not booted: %s: %d
X86
%s: encoding closure item: %s
level
sha2-384
Img4DecodeGetPropertyBoolean: %s: %d
querying custom runtime for mix-n-match policy
VMA2_DDI
SHA2_512
panic: invalid mode trying to open console
manifest property: %s
signature verification failed: %d
FF01
odometer[%s:%s]: environment allows mix-n-match; relaxing chain integrity policy
odometer[%s:%s]: allowing cross-group version comparison
extended security domain
property callback: tag = %s, type = %d, asn1 type = %s, v length = 0x%x
pseudo
unique chip identifier
bad argument vector provided to kext: v = %hx, how = %s, trap = %s: %d
w
odometer[%s:%s]: anti-replay violation: %d
expert magic
image
%s: AppleImage4 %s
%F
CHIP_VMA2
release type
failed to boot expert for syscall: %d
_darwin_runtime_set_nonce
odometer[%s]: Img4DecodeGetPropertyData: %d
expert state
secure boot state: smb0 = %#x, smb1 = %#x, secure boot = %#x
uses-avp-root-ca
chip-epoch
no integer property callback
asn1type
object property: %s
auditing manifest; ignoring validation result: %d
Darwin Userspace [arm64]
factory-prerelease-global-trust
CHIP_AP_SOFTWARE_FF00
success
object digest
odometer[%s:%s]: manifest has mix-n-match entitlement and environment allows mix-n-match; relaxing chain integrity policy
 [INIT] 
&
set specialist
HOST
Cryptex1 prospective boot [reduced-security AP host]
CHIP_CRYPTEX1_BOOT_AP_VERIFICATION
CHIP_CRYPTEX1_BOOT_VMA2
%s: stalled out: %d
posting properties for container: 0x%x
CHAIN_SIDELOAD
CHIP_CRYPTEX1_BOOT_AP_REDUCED_VERIFICATION
long os version
init
failed to compute closure: %d
use-ddi-secure-boot
unique-chip-id
panic: unreachable
security.mac.image4.image.activate
failed to parse manifest for boot: %d
odometer[%s:%s]: failed to query nonce: %d
INFO
no boolean record for tag: %s
posting property callback: container = %x, type = %x, tag = %s
research-enabled
audit
CHIP_CRYPTEX1_MOBILE_ASSET_AP
certificate properties invalid length: actual = %lu, expected > 0
chip identifier
integer
manifest matches chip: %s
effective security mode
panic: illegal chip definition: provided static decode implementation: %s
CHIP_AP_PDI_SHA2_384
CHIP_AP_UNSUPPORTED
pti->pt_switchable
secureboot-certificate-format
Cryptex1 Safari downlevel [AP host]
BOOTPC
VMA2_PDI
DEREncoderAddOctetString: %d
CHIP_CRYPTEX1_BOOT_VMA2_CLONE
failed to resolve chip environment: %d
%s: fstat: %d
0
payload properties
certificate production status
panic: exited enforcement loop with bogus value: dr = %d
security.mac.image4.nonce.unroll
incomplete sequence
odometer[%s:%s]: chip is not secondary-stage dfu policy
SAFARI_DOWNLEVEL
kern.bootsessionuuid
sysctl
Cryptex1 asset brain [AP host]
stack
chip
panic: failed to query expert: expert = %s, p = %s, fourcc = %s, code = %llu: %d
not an expert property
odometer[%s]: Img4DecodeGetPropertyInteger64: %d
panic: failed to get chosen node
_darwin_runtime_get_identifier_uint32
panic: Img4DecodeGetManifest: %d
failed to allocate closure node
restoreOS
@(#)VERSION:Darwin Image4 Library Version 7.0.0: Sat Oct  3 16:24:37 PDT 2026; root:AppleImage4_libraries-374~9642/libimage4/RELEASE_ARM64E
BOOT_EPHEMERAL
odometer[%s:%s]: manifest has no constraint for policy
panic: failed to read property: %s: %d
HACKTIVATE_RSA
VMA2_
_restore_runtime_get_identifier_bool
panic: illegal odometer consumption configuration
secureboot certificate format
selected property expert: property = %s, selected = %s, base = %s
crypto method: %s
chip-id
%s: failed to parse root: %d
img4_nonce_domain_preroll_nonce: %d
odometer[%s]: Img4DecodeGetPropertyInteger: %d
ucrt
NULL
CHIP_CRYPTEX1_MOBILE_ASSET_CODE_LOAD_AP
transform not applied: p = %s, kind = %s: %d
SEP
asmb
lp-spih
%s: decode selection: trust store [0x%llx]
nonce domain
panic: critical trust evaluation failure: chip = %s, p = %s, payload = %s
apfs-preboot-uuid
pqc validation flags
panic: digest length overflow: actual = %lu, expected <= %lu
DDI
vma2
panic: boot object has no restore info
use AVP secure boot
applied transform: p = %s, type = %s, xf kind = %s, value = [%s => 0x%x], error = [%d => %d]
manifest trust evaluation succeeded: %s
found unique tag list: cnt = %u
VMA3_
VMA3
resolved: %s
iokit
_darwin_runtime_log_handle
bool
SRDP
ASSET_BRAIN
panic
cryptex1 product class
CHIP_CRYPTEX1_MOBILE_ASSET_CODE_INSTALL_AP
not a manifest property
0x%x
panic: failed to get product node
kImg4DecodeSecureBootRsa4kSha384
CHIP_CRYPTEX1_BOOT_AP_PROSPECTIVE
panic: illegal chip definition: anti-replay and static lifetime policies defined: %s
1
trap not present trap: %s: %d
entitlement present for chip
DEREncoderAddNull: %d
certificate trust evaluation failed
chp->chp_type
security.mac.image4.kmod.copy_abi_version
VMA2_ACDC
MANB
panic: invalid offset: %lld
odometer[%s]: nonce supplied; simulating first-stage boot
panic: property not present in chip instance: %s
sb
queried property: %s => 0x%llx
_darwin_runtime_roll_nonce
panic: should never be called
panic: buffer not sufficient for digest: actual = %lu, expected >= %lu
odometer[%s:%s]: development silicon; not enforcing policy
performing leaf trust evaluation: coprocessor = %s, handle = %llx, evaluation type = %s
_darwin_runtime_get_identifier_uint64
anti-replay property consumed by odometer: %s
imposing object digest
security.mac.image4.nonce.peek_hash
unexpected tag found while decoding
FF06
EL2
post-process
applied transform: p = %s, type = %s, xf kind = %s, value = [%s => %s], error = [%d => %d]
decode failure
_restore_runtime_init
_restore_runtime_dealloc_type
odometer[%s:%s]: failed to query expert: p = %s: %d
panic: four-character codes must be four characters long
lp-smb0
property callback: tag = %s, type = %d, asn1 type = %s, v = 0x%x
octet string
%s: DERDecodeItem: %d
bad certificate tag: actual = 0x%llx, expected = 0x%llx
unexpected certificate dictionary type: actual = 0x%llx, expected = 0x%llx
img4_nonce_domain_copy_nonce: %d
odometer[%s]: restore info has no boot nonce
internal use-only build
returning secure boot state: %#llx
effective-security-mode-ap
_darwin_runtime_alloc_type
security.mac.image4.kmod.pin_root
odp->odp_type
_restore_runtime_alloc_type
panic: non-sensical property digest specification: %s
panic: unsupported struct version: actual = %hu, expected <= %u
no data record for tag: %s
certificate security mode
odometer[%s:%s]: chip has no properties for policy
n/a
failed to query property: %s: %d
no asmb
security-domain
__DATA_CONST
%s: Img4DecodeInitAsPayload: %d
ACDC-VMA2
finding entitlement for chip: entitlement = %s, chip = %s
panic: error not set to valid posix code: %d
panic: invalid secure boot level: actual = %llu, expected <= %llu
p->p_container
cryptex1 live nonce hash
odometer[%s]: Img4DecodeGetPropertyBoolean: %d
[ERROR] 
boot closure hash
i4p->type
%s does not exist
rsa1024
AP-DIGEST
MOBILE_ASSET
VMA2
odometer[%s:%s]: chip has no associated dfu policy
DEREncoderAddPrivateFromEncoder: %d
odometer[%s:%s]: boot chain integrity violation: %d
_darwin_runtime_init
%s
panic: version property iterated during identification: p = %s, fourcc = %s
_darwin_runtime_log
loanee
uint64
<
manifest matches coproc: %s
odometer[%s]: fetched boot nonce from restore info
panic: invalid Image4 tag: %s
love
Img4DecodeInitAsManifest: %d
%s: unexpected payload type: actual = %s, expected = %s
chained manifest hash
BOOT
vma3
entitlement not present in chip
failed to boot expert for user client call: %d
CHIP_AP_KCINSTALL
unable to load object via Image4: %u
DERDecodeSeqInit: %d
odometer[%s:%s]: manifest has no chained hash constraint
odometer[%s:%s]: manifest self-entitled for mix-n-match; relaxing chain integrity policy
x86
odometer[%s:%s]: environment allows mix-n-match; relaxing all odometer policy
version
failed to get nonce digest from callback: %d
panic: no decode implementation available for chip: %s
Cryptex1 mobile asset [AP host]
x86 certificate production status
panic: digest computation failed: %d
end of sequence or set
<=
kext and dylib are out of sync: v = %hx, how = %s, trap = %s: %d
failed to copy active cryptex0 root: %d
internal-use-only-unit
Img4DecodeGetPropertyBoolean: %d
loan
_restore_runtime_copy_nonce
odometer[%s:%s]: allowing cross-group policy: engineering use
CHIP_BOOTPC_SHA2_512
GL0
boot nonce
kmod connection
IM4M
DEREncoderAddUInt: manifest version: %d
odometer[%s:%s]: expert does not boot chip; relaxing chain integrity policy
CHIP_BOOTPC_SHA2_224
CHIP_BOOTPC_SHA2_384
panic: type not available
_darwin_runtime_dealloc_type
effective production status
panic: cstring is not a fourcc: length = %lu
odometer[%s:%s]: environment is a first-stage booter
failed to query expert: expert = %s, p = %s, fourcc = %s, code = %llu: %d
odometer[%s:%s]: nonce is bootstrapping; using boot nonce hash
panic: optional not set
odometer[%s:%s]: manifest is current
CHIP_CRYPTEX1_BOOT_AP_REDUCED
sysctlbyname[kern.osreleasetype]: %d
security.mac.image4.nonce.copy_hash
panic: insufficient nonce buffer length: actual = %lu, expected >= %lu
p->p_constraint->pc_code
custom chip
p->p_type->pt_switchable
failed to initialize compute context: %d
CRYPTEX1_
**
%#llx
GL2
failed to parse manifest: %d
darwin userspace
failed to query mix-n-match identifier: %d
MUST NOT EXIST
CHIP_CRYPTEX1_SAFARI_DOWNLEVEL_AP
panic: failed to get secure boot: %d
odometer[%s:%s]: no caller-supplied boot manifest hash
CHAIN_PIVOT
universal device identifier
DEREncoderCreateEncodedBuffer: %d
!=
odometer[%s:%s]: allowing cross-group policy: mix-n-match
panic: version property iterated during instantiation: p = %s, fourcc = %s
failed to prepare anti-replay: %d
Img4DecodeGetPropertyData: %d
error printing buffer: %s
allocation failed: obj = %s, size = %lu, error = %s
assertion failure: \"fclose(f_old)\" -> %{errno}d
```
