# `/usr/lib/libimage4.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 635,680 bytes.

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
universal device identifier
_restore_runtime_set_nonce
Cryptex1 boot verification [VMA2 host]
odometer[%s:%s]: allowing cross-group policy: full security
odometer[%s:%s]: allowing cross-group version comparison
%s: left to read = %lu
panic: illegal chip configuration: %s
long os version
querying property with chip expert resolution: p = %s, chip = %s, chip type = 0x%llx, chip expert authority >= 0x%llx
applied transform: p = %s, type = %s, xf kind = %s, value = [%s => %s], error = [%d => %d]
%s: %#x
cryptex1-key-scheme
panic: integer cast overflow: v = %s, actual = %llu, expected <= %llu
_darwin_runtime_copy_nonce
panic: trust chaining not supported for evaluation: %s
chip-epoch
panic: object overflows buffer: object = chip, length = %lu, required = %lu
CHIP_CRYPTEX1_MOBILE_ASSET_DFU_VMA2
calling out to manifest prepare function
%s
kImg4DecodeSecureBootRsa4kSha384X86
kImg4DecodeSecureBootG7Rsa4kSha384IM4C
failed to get nonce digest from callback: %d
panic: invalid log file descriptor: actual = %ld, expected <= %d
manifest-only evaluation; permitting replay
buffer overflow
DEREncoderAddNull: %d
RELEASE
secure_boot
GL0
CHIP_CRYPTEX1_MOBILE_ASSET_VMA2
panic: Img4DecodeRestoreInfoExists: %d
panic: no decode implementation available for chip: %s
unexpected tag found while decoding
CHIP_AP_SOFTWARE_FF01
_restore_runtime_roll_nonce
panic: failed to get chosen node
kImg4DecodeSecureBootRsa3kSha384
incoming parameter error
booted manifest
v
panic: digest buffer overflow: actual = %lu, expected >= %lu
%s: failed to parse root: %d
__DATA_CONST
AP_LOCAL_
failed to allocate item sequence encoder: %d
resolved: %s
 [INFO] 
%Y%m%d%H%M%SZ
property not present: %s: %d
p_where
love
_darwin_runtime_dealloc_type
%s: decode selection: static
odometer[%s:%s]: manifest self-entitled for mix-n-match; relaxing all odometer policy
_restore_runtime_get_identifier_bool
CHIP_AP_PDI_SHA2_384
boot nonce
odometer[%s:%s]: environment allows mix-n-match; relaxing chain integrity policy
CHIP_BOOTPC_SHA2_224
odometer[%s:%s]: anti-replay violation: %d
CHIP_VMA2_DDI
manifest
Img4DecodeGetPropertyInteger64: %d
found object: %s
%s: failed to encode property node: %d
entitlement not present in chip
[ERROR] 
odometer[%s:%s]: no manifest constraint for policy selection
secureboot key scheme
cryptex1 key scheme
object
DDI
%s: found unique tag
cryptex1 boot nonce
odometer[%s]: manifest is live and boot chain is intact
local policy
security.mac.image4.nonce.unroll
ACDC-VMA2
failed to parse manifest for boot: %d
not a manifest property
not an expert property
CHIP_CRYPTEX1_BOOT_VMA2_CLONE_VERIFICATION
CHIP_BOOTPC_SHA2_256
integer
trust evaluation succeeded for payload: %s
manifest property: %s
security.mac.image4.kmod.copy_version
panic: version property iterated during instantiation: p = %s, fourcc = %s
Darwin Image4 Library Version 7.0.0: Sat Oct  3 16:24:37 PDT 2026; root:AppleImage4_libraries-374~9642/libimage4/RELEASE_ARM64E
%F
ucrt
panic: type not available
bool
CRYPTEX0
boot manifest
md0
panic: property not present in chip instance: %s
374
prospective local policy generation
kImg4DecodeSecureBootRsa4kSha384DDI
%s: decode selection: trust store [0x%llx]
security.mac.image4.nonce.roll
panic: should never be called
restoreOS
trust evaluation failed: coprocessor = %s, sequence number = %lu, chain length = %lu: %d
panic: failed to get product node
unrecognized manifest property: %s
chip has custom constraint for property: %s
constraint->type
CHIP_AP_LOCAL_PROSPECTIVE
[error decoding data %d]
odometer[%s]: failed to query odometer cylinder: %s: %d
odometer[%s:%s]: manifest is consistent with boot chain
failed to query property: %s: %d
esdm-fuses
_darwin_runtime_init
lp-smb0
panic: invalid secure boot state: %#x
failed to prepare anti-replay: %d
trust evaluation: dr = %d, ct = 0x%x, error = %d
preparing custom boot manifest hash: %s
kImg4DecodeSecureBootGlobalG1Rsa4kSha384IM4C
panic: illegal chip definition: trust store cannot override static decode implementation: %s
certificate properties invalid length: actual = %lu, expected > 0
security.mac.image4.nonce.peek_hash
SHA2_512
_restore_runtime_init
panic: failed to query expert: expert = %s, p = %s, fourcc = %s, code = %llu: %d
%s: read: bad read: actual = %ld, requested = %lu, chunk length = %lu: %d
Yonkers - Factory
panic: optional not set
init
manifest boot failed: %s: %d
performing trust evaluation: type = %s %s, chip = %s, chip type = 0x%llx, chip expert = %s, payload = %s
manifest replay denied: %d
restore info
kImg4DecodeSecureBootRsa4kSha384AVP
odometer[%s:%s]: chip has no associated dfu policy
boot-manifest-hash
Cryptex1 mobile asset [AP host]
x86 certificate production status
CHIP_VMA3
DERImg4DecodeProperty: %s: %d
len
_restore_runtime_get_identifier_uint64
CHIP_CRYPTEX1_MOBILE_ASSET_CODE_INSTALL_AP
panic: failed to get defaults node
rsa3072
bad certificate tag: actual = 0x%llx, expected = 0x%llx
VMA2
panic: attempt to deallocate static buffer
%s: enforcing[%s %s %s]: 0x%x %s 0x%x: %d
_t_preference
odometer[%s:%s]: sideload chip has no notary
object properties
,
kext and dylib are out of sync: v = %hx, how = %s, trap = %s: %d
panic: nonce length overflow: actual = %lu, expected >= %lu
queried property: %s => 0x%llx
chip-id
panic: failed to resolve expert for runtime
%s: decode selection: dynamic
AP-SECURE-BOOT
cryptex1
CRYPTEX1-BOOT-SECURE-BOOT
CHIP_BOOTPC_SHA2_512
no boolean property callback
%s: failed to query anchor: 0x%llx: %d
generic error
odometer[%s:%s]: boot object has no restore info
odometer[%s:%s]: enforcing strict mix-n-match behavior
panic: memset_s: %d
_restore_runtime_get_identifier_cstr
odometer[%s:%s]: no caller-supplied boot manifest hash
panic: unsupported struct version: actual = %hu, expected <= %u
CHIP_CRYPTEX1_MOBILE_ASSET_CODE_LOAD_AP
failed to parse payload: %d
%s property not imposable on chip: %s
panic: iteration overflow: idx = 0x%lx, %lu
panic: kernel nonce overflows bounds: actual = %u, expected <= %u
VMA2_PDI
pc
panic: invalid offset: %lld
DEREncoderAddPrivateFromEncoder: %d
asn1type
Cryptex1 boot [vma2 host]
X86_
engineering use-only unit
odometer[%s]: Img4DecodeGetPropertyInteger64: %d
%s: fstat: %d
%s: stall while reading file
user client not supported on this target
panic: could not resolve chip for environment
id4->id_p->p_type->pt_switchable
failed to get boot nonce from callback: %d
querying custom runtime for mix-n-match policy
:
odometer[%s]: nonce hash supplied; simulating first-stage boot
Repair UCRT
panic: invalid secure boot level: actual = %llu, expected <= %llu
panic: illegal chip definition: no dynamic decode implementation: %s | %d
uniq
%s: tag not in unique list
secure boot
failed to parse manifest: %d
application processor
factory pre-release global trust
Cryptex1 boot [vma2 host clone]
trap failed: v = %hx, how = %s, trap = %s: %d
known-constant allocation
mix-n-match-prevention-status
cryptex1-product-class
cryptex1 chip type
sb
%s constraint satisfied: property = %s, type = %s
initialized trap: %s
PDI-VMA2
queried property: %s => %s
sha2-384
panic: Img4DecodeCopyPayloadDigest: %d
img4_nonce_domain_preroll_nonce: %d
iokit
boot uuid
panic: error not set to valid posix code: %d
null
no boolean record for tag: %s
forcing sideload anti-replay policy due to subsequent stage firmware evaluation
pqc validation flags
Cryptex1 prospective boot [AP host]
x86
entangled boot nonce
panic: unsupported container for posting: %u
im4c
mfr
panic: illegal chip definition: sideload and pivot policies defined: %s
Cryptex1 mobile asset code install [AP host]
uint32
panic: bogus digest length: %lu
security-domain
failed to query mix-n-match identifier: %d
failed to add MANP node: %d
transform not applied: p = %s, kind = %s: %d
BOOT_PRECOMP
certificate-production-status
%s: finding digest algorithm for oid: %s
panic: digest length overflow: actual = %lu, expected <= %lu
odometer[%s:%s]: mix-n-match god mode not set; enforcing strict mix-n-match behavior
odometer[%s]: expert boots chip
panic: operation not supported on this structure version: actual = %hu, expected >= %hu
trust evaluation succeeded; manifest is live
Img4DecodeGetPropertyData: %s: %d
auditing manifest; ignoring validation result: %d
unexpected certificate property type: tag = %s, type = 0x%llx
PDI
vma2
AP [software ff01]
CHAIN_FUTURE
forcing failure after audit completion: %d
_darwin_runtime_roll_nonce
security.mac.image4.image.dfu
panic: digest length overflow: actual = %lu, expected >= %lu
%s: enforcing[%s %s %s]: %s %s %s: %d
odometer[%s:%s]: allowing cross-group policy: engineering use
secure enclave processor
SEP_
crypto-hash-method
Cryptex1 prospective boot [reduced-security AP host]
darwin userspace
img4_nonce_domain_roll_nonce: %d
%s: enforcing[%s %s %s]: 0x%x %s 0x%x: success
CHAIN_PIVOT
payload
Img4DecodeGetPropertyInteger64: %s: %d
certificate chain verification failed: %d
security.mac.image4.kmod.test_firebloom
FF06
%s: enforcing[%s %s %s]: %s %s %s: success
odometer[%s]: versions directly comparable; allowing enforcement decision to stand
unprivileged limit
BOOT
panic
BOOT_STATIC
odometer[%s:%s]: chip has no properties for policy
Darwin Userspace [arm64]
_darwin_runtime_set_nonce
chip environment not booted: %s: %d
<null>
odometer[%s:%s]: allowing cross-group policy: production status
/Library/Caches/com.apple.xbs/DA468FD9-0FD8-4F31-A85C-FDEDC90B7D37/TemporaryDirectory.AVOBqm/Binaries/AppleImage4_libraries/install/Symbols/image4
pi->p_type->pt_switchable
panic: critical trust evaluation failure: chip = %s, p = %s, payload = %s
cryptex1 auxilliary boot nonce hash
%s does not exist
payload properties
kImg4DecodeLocalPolicyEc384Sha384QA
chp->chp_type
odometer[%s:%s]: manifest has no chained hash constraint
release type
returning secure boot state: %#llx
vmm-present
Cryptex1 boot verification [AP host]
validation
security.mac.image4.image.copy_active
d->d_len
pdi nonce hash
  🔥🌸 
effective-security-mode-ap
x509
hybridscheme3
panic: cstring is not a fourcc: length = %lu
<
panic: property is not constrainable: %s
.
CHIP_VMA2
error
%6s  %-36s : 0x%llx
sha1
_darwin_runtime_get_identifier_uint64
AP_LOCAL
panic: length not expressible as unsigned 32-bit integer: %lu
<=
CHIP_AP_SRDP
odometer[%s]: manifest is current
payload->i4b_len
trap failed: %s: %d
panic: digest length overflow: actual = %u, expected >= %lu
DEREncoderCreateEncodedBuffer: %d
GENERIC
panic: length not expressible as ssize_t: %lu
panic: null coprocessor handle
AP_
non-executable privilege level
unique tag entry[%zu] = %s
MOBILE_ASSET_CODE_INSTALL
panic: non-sensical property digest specification: %s
%s: enforcing length[%s %s %s]: %lu %s %lu: success
odometer[%s:%s]: boot manifest hash is caller-supplied
panic: sysctlnametomib: %s%d
%s: removing node
_restore_runtime_dealloc_type
panic: specialist not set after runtime entry
odometer[%s]: restore info nonce too large: actual = %lu, expected <= %lu
DEREncoderAddBoolean: %d
CHIP_CRYPTEX1_BOOT_AP_REDUCED_VERIFICATION
%s: read: %d
panic: nonce too large: actual = %lu, expected <= %ld
effective-production-status-ap
CHIP_CRYPTEX1_SAFARI_DOWNLEVEL_AP
firmware
misc. decoding error (badly formatted DER)
DEREncoderCreateImage4Dictionary: %d
%s: enforcing[%s %s %s]: 0x%llx %s 0x%llx: %d
failed to resolve chip environment: %d
effective production status
allow mix-n-match
panic: invalid min/max: min = %u, max = %u
cryptex1 certificate format
cryptex1 boot nonce hash
%s constraint violated: property = %s, type = %s: %d
CHIP_CRYPTEX1_MOBILE_ASSET_AP
BOOTPC
DEREncoderAddSequenceFromEncoder: %d
AP [software ff06]
bad argument vector provided to kext: v = %hx, how = %s, trap = %s: %d
panic: invalid mode trying to open console
odometer[%s:%s]: manifest has no pivot constraint
property failed to impose on environment: %s: %d
effective security mode
computing nonce digest: chip = %s, digest length = %lu
Cryptex1 boot verification [VMA2 clone host]
%s: stalled out: %d
kext cannot parse argument vector: v = %hx, how = %s, trap = %s: %d
%y%m%d%H%M%SZ
lp-smb1
secureboot-certificate-format
custom chip
img4_nonce_domain_copy_nonce: %d
**
cryptex1 chip subtype
panic: illegal odometer consumption configuration
%s: AppleImage4 %s
_darwin_runtime_get_identifier_cstr
stack
panic: invalid trap number: actual = %#llx, expected < %#llx
wrap
odometer[%s]: Img4DecodeGetPropertyInteger: %d
panic: nonce cannot fit into 64-bit integer: actual = %lu, expected <= %lu
panic: iteration underflow: idx = 0x%lx, %ld
AP [software ff00]
ASSET_BRAIN
odometer[%s:%s]: manifest inconsistent with restore info: %d
failed to boot expert for user client call: %d
user client method failed: v = %hx, trap = %s, kr = %#x, sys = %#x, sub = %#x, code = %#x
environment not supported: coprocessor = %s, handle = %llx: %d
i4p->type
signature verification failed: %d
DEREncoderAddSetFromEncoder: %d
MOBILE_ASSET_CODE_LOAD
panic: buffer not large enough for digest: actual = %lu, expected >= %lu
odometer[%s:%s]: nonce is bootstrapping; using boot nonce hash
Savage - Factory
kmod connection
2006-05-31
panic: insufficient memory for expert: actual = %lu, expected >= %lu
info
%s %-36s : 0x%x
unconstrain
Img4DecodePerformTrustEvaluationWithCallbacks: %d
VMA2_
CHIP_AP_UNSUPPORTED
entitlement present for chip
incomplete sequence
X86
use AVP secure boot
_restore_runtime_log
selected property expert: property = %s, selected = %s, base = %s
Img4DecodeGetPropertyData: %d
CRYPTEX1_
failed to allocate DER encoder
object digest
set resolver
%#x
odometer[%s:%s]: internal unit; not enforcing policy
boot chip
panic: illegal chip definition: provided static decode implementation: %s
found unique tag list: cnt = %u
SAFARI_DOWNLEVEL
cryptex1 chip identifier
panic: failed to get secure boot: %d
preflight
odometer[%s:%s]: boot chain integrity violation: %d
%s %-36s
EL2
kern.osreleasetype
_darwin_runtime_get_identifier_uint32
property callback: tag = %s, type = %d, asn1 type = %s, v length = 0x%x
boot
odometer[%s:%s]: chip has no property for policy
id4->id_p->p_constraint->pc_code
apfs-preboot-uuid
chip identifier
CHIP_AP_SOFTWARE_FF00
panic: boot object has no restore info
failed to allocate closure node
IM4M
boot closure hash
internal use-only unit
odometer[%s:%s]: no caller-supplied nonce hash
allow-ecid-mismatch
panic: no cryptex1 guests for %s
FF01
panic: illegal property definition: %s
odometer[%s]: restore info has no boot nonce
failed to compute closure: %d
panic: bogus property container input: actual = %u, expected < %u
p->p_container
virtual machine monitor present
failed to allocate node
!=
odometer[%s:%s]: failed to query expert: p = %s: %d
CHIP_CRYPTEX1_BOOT_VMA2_CLONE
no data record for tag: %s
Img4DecodeGetPropertyInteger: %d
cannot select chip with first-stage boots
image
Img4DecodePerformManifestTrustEvaluation: %d
host application processor
restore
post-process
syscall: %s
kImg4DecodeSecureBootRsa4kSha384
HACKTIVATE_RSA
CHAIN_SIDELOAD
security domain
>
%s: cur offset = %lld
BOOT_SIDELOAD
sysctlbyname[kern.bootsessionuuid]: %d
property callback: tag = %s, type = %d, asn1 type = %s, v = 0x%x
failed to query manifest hash identifier: %d
__image4_chp
SRDP
GENERIC_CRYPTEX0
odometer[%s:%s]: constraint violation: %s: %d
odometer[%s:%s]: failed to query nonce: %d
INFO
CHIP_CRYPTEX1_BOOT_AP_REDUCED
engineering-use-only-unit
^~
set specialist
odometer[%s]: nonce supplied; simulating first-stage boot
HOST_
panic: non-sensical crypto hash method: %s
heap
user client method success
panic: unexpected expert: op = %s, actual = %s, expected = %s
0x%x
panic: illegal chip definition: no static decode implementation: %s
DEREncoderAddOctetString: %d
%s: chip has no associated dfu policy: %d
expert
odometer[%s:%s]: using caller-provided nonce hash
performing audit trust evaluation: coprocessor = %s, handle = %llx, secure boot level = %llx, evaluation type = %s
ACDC
version
odometer[%s]: failed to query chip boot: %s: %d
CHIP_CRYPTEX1_ASSET_BRAIN_AP
property callback: tag = %s, type = %d, asn1 type = %s, v = 0x%llx
failed to decode property: container = %s, type = %x, p = %s: %d
certificate production status
MOBILE_ASSET
get chip instance
CHIP_BOOTPC_SHA2_384
CHIP_AP_KCINSTALL
panic: unexpected trust evaluation entry: i = %lu
uses-avp-root-ca
manifest matches chip: %s
panic: unsupported digest type: oid len = %lu
MANB
odometer[%s:%s]: expert does not boot chip; relaxing chain integrity policy
certificate trust evaluation failed
Img4DecodePerformManifestTrustEvaluationWithCallbacks: %d
%s: decode selection: dynamic | %s
kImg4DecodeLocalPolicyEc384Sha384Hacktivate
[error decoding bool %d]
|>
manifest matches coproc: %s
panic: invalid Image4 tag: %s
lvl
prepared custom nonce hash
preparing mix-n-match policy: 0x%x
falling back to base expert for property: %s
odometer allocated on %s
research mode
VMA2_DDI
recording property for closure computation: %s%s%s
DEREncoderAddImage4Tag: IM4M: %d
p->p_constraint->pc_code
HOST
internal use-only build
expert state
posting property callback: container = %x, type = %x, tag = %s
IOServiceGetMatchingService failed
trust evaluation failed: %d
CHAIN
panic: four-character codes must be four characters long
n/a
no manifest with which to select chip
%s: retrieved pinned root from trust store: type = 0x%llx, length = %lu, oid = %s, oid length = %lu
security.mac.image4.nonce.copy_hash
Cryptex1 generic content [AP host]
odometer[%s:%s]: manifest has mix-n-match entitlement and environment allows mix-n-match; relaxing chain integrity policy
failed to entangle nonce: %d
[DEBUG] 
decode failure
0
chip
%s: unexpected payload type: actual = %s, expected = %s
panic: non-%s property set: property = %s, type = %s
BOOT_EPHEMERAL
Cryptex1 mobile asset code load [AP host]
crypto method: %s
failed to copy kcinstall nonce hash: %d
HACKTIVATE_ECDSA
CHAIN_MANIFEST
panic: failed to read property: %s: %d
unexpected section tag: %s
SHA2_256
VMA3_
digest
odometer[%s:%s]: environment is a first-stage booter
panic: illegal coprocessor map: canonical handle has no static or dynamic decode implementation
panic: bogus nonce length: actual = %lu, expected <= %lu
function not implemented in this configuration
bootpc
&
cps->cps_type
pti->pt_switchable
certificate-security-mode
factory-prerelease-global-trust
unique-chip-id
decode context allocated on %s
panic: Img4DecodeCopyManifestDigest: %d
MUST EXIST
loan
queried cylinder: p = %s, v = 0x%x
failed to boot expert for chip selection: %d
rsa4096
panic: digest computation failed: %d
CHIP_CRYPTEX1_BOOT_AP
==
Cryptex1 mobile asset [VMA2 host]
no callbacks present
failed to initialize compute context: %d
extended security domain
manifest boot succeeded: %s
posting properties for container: 0x%x
com.apple.security.libimage4
no asmb
unrecognized object property: %s
CHIP_CRYPTEX1_BOOT_VMA2
security.mac.image4.kmod.evaluate_trust
odometer[%s:%s]: boot object has restore info
panic: invalid coprocessor handle: actual = %llu, expected < %u
stock runtime; not querying for boot manifest hash
Cryptex1 Safari downlevel [AP host]
certificate
odometer[%s:%s]: environment allows mix-n-match; relaxing all odometer policy
panic: attempt to deallocate loaned buffer without returning
img4_nonce_domain_peek_nonce: %d
odometer[%s:%s]: switch constraint not satisfied
Img4DecodeGetPropertyBoolean: %s: %d
chained manifest hash
VMA2_ACDC
panic: close%d
/dev/console
bounds safety
p->p_type->pt_switchable
supported chip
%s: inserting item node
unique chip identifier
odometer[%s]: expert does not boot chip
odometer[%s]: failed to query restore info for boot nonce: %d
panic: no anti-replay policy selected
panic: illegal %s property: %s
%#llx
NULL
DEBUG
sysctlbyname[kern.osreleasetype]: %d
prospective cryptex1 manifest hash
panic: closure measurement requires a parsed manifest
finding entitlement for chip: entitlement = %s, chip = %s
odometer[%s:%s]: failed to entangle nonce: %d
INIT
pqc-validation-flags
Img4DecodeInitAsManifest: %d
unexpected certificate dictionary type: actual = 0x%llx, expected = 0x%llx
Img4DecodeIterateObjectItems: %d
_restore_runtime_get_identifier_digest
uint64
execute
MUST NOT EXIST
AP
[error decoding uint %d]
panic: buffer not sufficient for digest: actual = %lu, expected >= %lu
CHIP_AP_SOFTWARE_FF06
w
sign
CHIP_CRYPTEX1_MOBILE_ASSET_DFU_AP
trap not present trap: %s: %d
failed to query expert: expert = %s, p = %s, fourcc = %s, code = %llu: %d
DEREncoderAddUInt64: %d
0x%llx
board-id
level
nonce domain
DERImg4DecodeProperty: %d
security.mac.image4.kmod.copy_abi_version
pseudo
boot nonce hash
panic: function should never be called: %s
%s: Img4DecodeGetPayloadType: %d
SHA2_224
odometer[%s:%s]: policy is enforceable
_darwin_runtime_alloc_type
panic: unreachable
cryptex1 auxilliary boot nonce
panic: integer cast underflow: v = %s, actual = %lld, expected >= 0
failed to impose manifest for boot: %d
DEREncoderAddImage4TagUInt32: %d
panic: insufficient nonce buffer length: actual = %lu, expected >= %lu
odometer[%s:%s]: chip is not secondary-stage dfu policy
panic: illegal chip/expert configuration
odometer[%s:%s]: manifest is current
internal-use-only-unit
cryptex1-certificate-format
BOOTPC_
_restore_runtime_log_handle
software update freshness nonce
odometer[%s:%s]: internal use-only unit entitlement found
odometer[%s:%s]: enforcing nonce hash directly
darwin-user
Img4DecodeGetPropertyBoolean: %d
pmap data
odometer[%s:%s]: manifest self-entitled for mix-n-match; relaxing chain integrity policy
DEREncoderCreate: %d
DEREncoderAddUInt: manifest version: %d
panic: illegal chip definition: anti-reply and sideload policies defined: %s
no integer record for tag: %s
panic: failed to get manifest properties
IOServiceOpen: %d
CHIP_CRYPTEX1_BOOT_AP_REDUCED_PROSPECTIVE
panic: bogus exit from enforcement loop: pdr = %d
CHIP_AP_REDUCED
KCINSTALL
ERROR
GL1
security.mac.image4.nonce.verify
AP-DIGEST
CHIP_CRYPTEX1_BOOT_AP_PROSPECTIVE
BOOT_LIVE
_restore_runtime_alloc_type
VMA3
board identifier
debug level
%s: DERDecodeItem: %d
panic: incomplete coprocessor map: handle = %lld, expected < %lld
odometer[%s:%s]: allowing cross-group policy: mix-n-match
odometer[%s]: Img4DecodeGetPropertyData: %d
cryptex1 manifest hash
CHIP_AP_SHA2_384
odometer[%s:%s]: development silicon; not enforcing policy
queried property: %s => 0x%x
failed to parse boot session uuid: %s: %d
manifest trust evaluation succeeded: %s
imposing object digest
%s: simulating chip boot for reduced-security virtual chip policy
querying custom runtime for boot manifest hash
kImg4DecodeLocalPolicyEc384Sha384
get kmod connection
secure boot state: smb0 = %#x, smb1 = %#x, secure boot = %#x
research-enabled
lp-spih
stock runtime; not querying for mix-n-match policy
security.mac.image4.nonce.generate_proposal
%s: enforcing[%s %s %s]: 0x%llx %s 0x%llx: success
@(#)VERSION:Darwin Image4 Library Version 7.0.0: Sat Oct  3 16:24:37 PDT 2026; root:AppleImage4_libraries-374~9642/libimage4/RELEASE_ARM64E
lp-stng
failed to boot expert for syscall: %d
CHIP_VMA2_CLONE
treating payload as non-Image4 wrapped
AppleImage4
%s: encoding closure property: p = %s, item = %s, type = %llx, val = %s
loanee
set supervisor
0.0.0.0.0,0
odometer[%s]: enforcing anti-replay
 [INIT] 
panic: failed to get secure boot level: %d
absence
applied transform: p = %s, type = %s, xf kind = %s, value = [%s => 0x%x], error = [%d => %d]
panic: trust chain length exceeded: %lu
IMAGE4_LOG_FD
failed to copy active cryptex0 root: %d
property does not exist: container = %s, type = %x, p = %s
forcing sideload anti-replay policy
booter environment not supported: %s: %d
property callback: tag = %s, type = %d, asn1 type = %s, v length = %lu
audit
QA
DERDecodeSeqInit: %d
%s: failed to encode item node: %d
%s: inserting node: %s
panic: attempt to destroy already destroyed buffer
CHIP_VMA2_PDI
expert magic
exception level
panic: illegal chip definition: invalid manifest type for dynamic selection: %s
panic: attempt to deallocate loaned buffer
none
CHIP_CRYPTEX1_BOOT_VMA2_VERIFICATION
odometer[%s:%s]: failed to query boot nonce hash: %d
debug
diagnostic level
use-ddi-secure-boot
CHIP_CRYPTEX1_BOOT_AP_VERIFICATION
unable to load object via Image4: %u
data
panic: unreachable case: %s = 0x%llx
_restore_runtime_get_identifier_uint32
EL1
sysctl
trying chip: %s
manx section constraints not implemented
security.mac.image4.kmod.pin_root
FF00
panic: closure node deallocated while still in list
_restore_runtime_copy_nonce
EL0
no integer property callback
chip has no static or dynamic decode implementation: %s
CHIP_AP_LOCAL
secureboot certificate format
performing normalization trust evaluation: coprocessor = %s, handle = %llx, evaluation type = %s
Cryptex1 asset brain [AP host]
panic: Img4DecodeGetManifest: %d
kImg4DecodeSecureBootRsa1kSha1
panic: Img4DecodeGetPayload: %d
panic: exited enforcement loop with bogus value: dr = %d
success
odometer[%s:%s]: failed to query restore info nonce: %d
boot manifest hash
panic: invalid log file descriptor
_darwin_runtime_log
octet string
PDI-DIGEST
Cryptex1 boot [AP host]
odp->odp_type
static
%6s  %-36s : %s
performing boot trust evaluation: coprocessor = %s, type = %s
CHIP_AP_DDI_SHA2_384
no data property callback
cryptex1 live nonce hash
invalid unique tag list: actual length = %u, expected %% %lu == 0
%s: encoding closure item: %s
generic
Cryptex1 boot [reduced-security AP host]
%s: %s\n
posted property: container = %s, type = %x, p = %s
security.mac.image4.image.activate
vma3
unexpected type: actual = %s, expected = %s
odometer[%s]: Img4DecodeGetPropertyBoolean: %d
rd
certificate epoch
performing leaf trust evaluation: coprocessor = %s, handle = %llx, evaluation type = %s
kern.bootsessionuuid
_darwin_runtime_log_handle
anti-replay property consumed by odometer: %s
1
security.mac.image4.kmod.evaluate_trust_dlxk
failed to allocate item node
unconstrained absence
panic: no more property record slots
failed to check for %s: %d
found %s; skipping
SHA2_384
cryptex1 product class
>=
*=
applied transform: p = %s, type = %s, xf kind = %s, value = [%s => 0x%llx], error = [%d => %d]
IOServiceOpen: success
object property: %s
DERDecodeSeqContentInit: %d
%s: enforcing length[%s %s %s]: %lu %s %lu: %d
manifest properties
normalize
\n
GL2
panic: version property iterated during identification: p = %s, fourcc = %s
manifest trust evaluation succeeded
rsa1024
end of sequence or set
BOOT_FLASH_SECONDARY
odometer[%s]: querying restore info for boot nonce: %s
panic: illegal chip definition: anti-replay and static lifetime policies defined: %s
SEP
certificate security mode
object property failed to impose on environment: %d
panic: object overflows buffer: object = firmware, length = %lu, required = %lu
kImg4DecodeSecureBootRsa4kSha384DDIGlobal
security.mac.image4.kmod.evaluate_trust_vn
CHIP_CRYPTEX1_GENERIC_AP
volume group uuid
asmb
odometer[%s:%s]: manifest has no constraint for policy
secureboot-key-scheme
%d
<data: %u bytes>
srd nonce hash
resolving environment: coproc = %s, handle = %llx, secure boot = %llx
odometer[%s]: fetched boot nonce from restore info
kcinstall nonce hash
%s: Img4DecodeInitAsPayload: %d
error printing buffer: %s
allocation failed: obj = %s, size = %lu, error = %s
assertion failure: \"fclose(f_old)\" -> %{errno}d
```
