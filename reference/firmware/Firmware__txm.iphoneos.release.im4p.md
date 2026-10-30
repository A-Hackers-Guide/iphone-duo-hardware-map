# `Firmware/txm.iphoneos.release.im4p`

- File size: 224,171 bytes
- IM4P: Tag: IM4P  Type: trxm  Version: 1
- BuildManifest components that use it: `Ap,RestoreTrustedExecutionMonitor`, `Ap,TrustedExecutionMonitor`

## IM4P header [FW]

```
IM4P (Payload):
  Tag:          IM4P
  Type:         trxm
  Version:      1
  Data:         224 kB (223851 bytes)
  Compression:  LZFSE
  Uncompressed: 557 kB (557088 bytes)
  Properties:
    kcbf: 507904
    kcbz: 32768
    kcep: 18446744005376491520
    kclz: 32
    kcrf: 0
    kcrz: 180224
    kcwf: 540672
    kcxf: 180224
    kcev: 491520
    kclf: 557056
    kclo: 18446744005375967232
    kcwz: 16384
    kcxz: 327680
```

## Payload [FW]

- Size after IM4P unwrap / decompression: 557,088 bytes
- Format: Mach-O 64-bit

## Identity strings (versions, build tags) [FW]

- ` 2017-2024 Apple Inc. All rights reserved.</string></dict></plist>`
- `@(#)VERSION:Code Signing Monitor Image4 Module Version 7.0.0: Sat Oct  3 15:31:47 PDT 2026; root:AppleImage4_txm-374~8641/libimage4_TXM/RELEASE_ARM64E`
- `Apple Inc.1`
- `Apple Inc.1&0$`

## Strings (918) [FW]

Printable runs of 6+ characters with at least three letters, in file order, with payload offset. For RTKit co-processor firmware these are the log formats, task names, endpoint names and assertions that describe what the processor does.

```
00000028  __TEXT
00000068  __cstring
00000078  __TEXT
000000b8  __const
000000c8  __TEXT
00000108  __binname
00000118  __TEXT
00000158  __info_plist
00000168  __TEXT
000001a8  __chain_starts
000001b8  __TEXT
00000200  __DATA_CONST
00000240  __const
00000250  __DATA_CONST
00000290  __auth_ptr
000002a0  __DATA_CONST
000002e8  __TEXT_EXEC
00000328  __text
00000338  __TEXT_EXEC
00000388  __TEXT_EXEC
000003d0  __TEXT_BOOT_EXEC
00000410  __text
00000420  __TEXT_BOOT_EXEC
00000460  __bootcode
00000470  __TEXT_BOOT_EXEC`@
000004b8  __DATA
000004f8  __data
00000508  __DATA
00000548  __common
00000558  __DATA
000005a8  __DATA
000005f0  __LINKEDIT
00000825  profile does not have a UUID
00000842  profile UUID is not a string
0000085f  profile does not have a standard length UUID
0000088c  fbe71da1-0834-4d49-9b41-d3fa7f9e4d4f
000008b1  9c0fab7e-93cf-4d83-8340-9ea33b5846cc
000008d6  d9d5fa63-7084-4346-bada-96e463ad1771
000008fb  c7854afa-6894-4864-8d3c-15f6ccc6728d
00000920  3d2a1eea-d1f8-42ab-af5a-545ce51054a7
0000096a  8f327bd3-89e8-46e5-bcf5-72a260f6dd36
0000098f  8c9a3b2d-c2a3-47f5-b7fc-ae7bcdc79cbf
000009d9  91c408d9-0fbe-44c4-aa74-37c7f734e159
00000a23  b9e61602-b1a2-4b73-b0f9-54cc3fff4244
00000a48  d1576fca-f736-46eb-8ac5-d5b4db7503ac
00000a92  3d98340d-a43f-4263-8645-51937b4bffd0
00000ab7  4a20c45a-2a99-4ad8-bdd2-c7ab4b0c1a8d
00000adc  bee84af7-d2ca-44e9-992b-54db447d20fc
00000b01  294be08b-487f-4020-a986-011dbc7a4fc8
00000b95  09fcf192-750c-4a39-9a0e-cfe6faa82275
00000bba  cbfd2102-86b1-4895-990f-dbaece4c63f2
00000c29  adaea588-c074-4b87-b8ea-26cb685b3443
00000c4e  attempted to initialize boot-args again
00000c76  allowing executable comm-page mapping
00000c9c  page enforcement failed (%u | %u): (%p | %u) --> %u | 0x%016llX
00000cdc  disallowed executable debug mapping
00000d00  disallowed writable debug mapping due to developer mode
00000d38  com.apple.private.cs.debugger
00000d56  disallowed writable debug mapping due to address space
00000d8d  attempted to initialize ASID table again
00000db6  com.apple.oah.runtime_arm_internal
00000dd9  com.apple.runtime_arm_internal
00000df8  %s: association spans outside of code limit
00000e24  %s: disallowed due to restricted execution mode
00000e54  %s: disallowed due to secure channel constraints
00000e85  dynamic-codesigning
00000e99  com.apple.developer.cs.allow-jit
00000eba  disallowed non-debugger initiated debug mapping
00000eea  research.com.apple.license-to-operate
00000f10  get-task-allow
00000f1f  attempted to initialize secure channel again
00000f4c  secure channel not supported on this platform
00000f7a  setup the shared page for the secure channel
00000fa7  SecureChannel: SCRD | Magic: 0x%04X
00000fcb  SecureChannel: SCRD |  xART: %u
00000feb  system SecureUI state: %u
00001005  developer mode enabled due to system policy configuration
0000103f  developer mode enabled due to PCC research build
00001070  developer mode disabled due to PCC release build
000010a1  developer mode disabled due to platform code strict policy
000010dc  developer mode enabled due to non-availability of xART
00001113  developer mode enabled based on user configuration
00001146  developer mode disabled based on user configuration
0000117a  SecureChannel: Lockdown Mode | %u
0000119c  SecureChannel: Demo Mode | %u
000011ba  SCVerifySignature for developer authorization: %u
000011ec  com.apple.PreBoard
000011ff  com.apple.springboard
00001215  com.apple.darwin-init
0000122b  com.apple.amfid
0000123b  security boot mode without SEP load: %u
00001263  build variant: %s
00001275  fusing: 0x%08X
00001284  virtualized: %u
00001294  build type: %u
000012a3  device type: %u
000012b3  research configuration: %u
000012ce  extended research configuration: %u
000012f2  entered lockdown mode for the read-only system policy
00001328  unable to decelerate entitlements: %u
0000134e  %s: unable to evaluate for acceleration: %d
0000137a  %s: unable to accelerate entitlements: %d
000013a4  %s: entitlements not marked as accelerated
000013cf  com.apple.private.enable-swift-playgrounds-validation
00001405  com.apple.private.amfi.can-load-cdhash
0000142c  unassignable system policy: %u
0000144b  platform code only policy: %u
00001469  restricted execution mode support: %u
0000148f  attempted to initialize logging again
000014b5  setup logging: %u bytes (%u | %u)
000014d7  TXM [Log]: 
000014e3  TXM [Log]: error adding log for this slot: %d
00001511  disallowed loading ERM trust cache on the system
00001542  com.apple.private.pmap.load-trust-cache
0000156a  com.apple.private.unload-trust-cache
0000158f  missing trust cache range from device tree
000015ba  trust cache range is 0 length
000015d8  failed to load external trust cache module: %u
00001607  loaded external trust cache modules: %u/%u
00001632  personalized.engineering-root
00001650  personalized.pdi
00001661  personalized.ddi
00001672  personalized.cryptex-research
00001690  global.ota-update-brain
000016a8  global.bootability-brain
000016c1  cryptex1.boot.os
000016d2  cryptex1.boot.app
000016e4  cryptex1.preboot.app
000016f9  global.pdi
00001704  personalized.mobile-asset-brain
00001724  cryptex1.safari-downlevel
0000173e  cryptex1.preboot.os
00001752  personalized.supplemental-persistent
00001777  personalized.supplemental-ephemeral
0000179b  cryptex1.generic
000017ac  cryptex1.generic.supplemental
000017ca  personalized.mobile-asset-code
000017e9  personalized.cryptex1.update-brain
0000180c  cryptex1.boot.rosetta
00001822  attempted to initialize boot memory again
0000184c  system supports DIT feature
00001868  unsupported device type: %u
00001884  resolved system platform identity: %u
000018aa  denying security-research-device configuration: %u | %u
000018e2  txm.iphoneos.release.TrustedExecutionMonitor_Guarded-217.0.2
0000191f  fatal abort condition issued from liblibc
00001949  trapped due to a sanitizer runtime violation: %d | %p
0000197f  [code: 0x%08X | %u]
00001993  TXM [Panic]: 
000019a1  Exception occurred at pc: 0x%016llx, lr: 0x%016llx
000019d4    x0:  0x%016llx  x1:  0x%016llx  x2:  0x%016llx  x3:  0x%016llx
00001a15    x4:  0x%016llx  x5:  0x%016llx  x6:  0x%016llx  x7:  0x%016llx
00001a56    x8:  0x%016llx  x9:  0x%016llx  x10: 0x%016llx  x11: 0x%016llx
00001a97    x12: 0x%016llx  x13: 0x%016llx  x14: 0x%016llx  x15: 0x%016llx
00001ad8    x16: 0x%016llx  x17: 0x%016llx  x18: 0x%016llx  x19: 0x%016llx
00001b19    x20: 0x%016llx  x21: 0x%016llx  x22: 0x%016llx  x23: 0x%016llx
00001b5a    x24: 0x%016llx  x25: 0x%016llx  x26: 0x%016llx  x27: 0x%016llx
00001b9b    x28: 0x%016llx  fp:  0x%016llx  lr:  0x%016llx  sp:  0x%016llx
00001bdc    pc:  0x%016llx  cpsr:0x%08llx          esr: 0x%016llx  far: 0x%016llx
00001c25  setup device tree range
00001c3d  /chosen
00001c45  debug-enabled
00001c53  unable to find debug-enabled property in /chosen
00001c84  invalid length for debug-enabled property: %u
00001cb2  esdm-fuses
00001cbd  unable to find esdm-fuses property in /chosen
00001ceb  invalid length for esdm-fuses property: %u
00001d16  acquired valid /chosen/esdm-fuses node: %u
00001d41  PlatformCode-Strict
00001d5b  unable to find /model property in device-tree
00001d8e  chip-id
00001d96  unable to find chip-id property in /chosen
00001dc1  invalid length for chip-id property: %u
00001de9  darwinos-security-environment
00001e07  invalid length for darwinos-security-environment property: %u
00001e45  darwinOS variant from device tree: %u
00001e6b  cs-system-policy
00001e7c  unable to find cs-system-policy property in /chosen
00001eb0  missing data for cs-system-policy property
00001edb  cs-system-policy property is not a NULL terminated string
00001f15  security-mode-change-enable
00001f31  invalid length for security-mode-change-enable property: %u
00001f6d  security boot mode environment: %u
00001f90  amfi-only-platform-code
00001fa8  unable to find amfi-only-platform-code property in /chosen
00001fe3  invalid length for amfi-only-platform-code property: %u
0000201b  research-enabled
0000202c  unable to find research-enabled property in /chosen
00002060  invalid length for research-enabled property: %u
00002091  sec-research-device-erm-enabled
000020b1  unable to find research ERM property in /chosen
000020e1  invalid length for ERM property: %u
00002105  /defaults
0000210f  vmm-present
0000211b  unable to find vmm-present property in /defaults
0000214c  invalid length for vmm-present property: %u
00002178  sepfw-load-at-boot
0000218b  unable to find sepfw-load-at-boot property in /chosen
000021c1  invalid length for sepfw-load-at-boot property: %u
000021f4  system is configured to not start the SEP at system boot
0000222d  sepfw-never-boot
0000223e  unable to find sepfw-never-boot property in /chosen
00002272  invalid length for sepfw-never-boot property: %u
000022a3  system is configured never to boot SEP
000022ca  osenvironment
000022d8  unable to find osenvironment property in /chosen
00002309  device-recovery
00002319  system is booted in device recovery environment
00002349  resolving to internal device variant due to fusing state
00002382  /chosen/memory-map
00002395  unable to find /chosen/memory-map in device tree
000023c6  TrustCache
000023d1  unable to find TrustCache property in /chosen/memory-map
0000240a  invalid length for TrustCache property: %u
00002435  /chosen/iBoot
00002443  unable to find /chosen/iBoot in device tree
0000246f  iboot-build-variant
00002483  unable to find iboot-build-variant property in /chosen/iBoot
000024c0  missing data for iboot-build-variant property
000024ee  development
00002500  /product
00002509  udid-version
00002516  unable to find udid-version property in /product
00002547  invalid length for udid-version property: %u
00002574  unsupported UniqueDeviceID version: %u
0000259b  unique-chip-id
000025aa  unable to find unique-chip-id property in /chosen
000025dc  invalid length for unique-chip-id property: %u
0000260b  %08X-%016llX
00002618  successfully queried the UniqueDeviceIDv2 from the device tree
00002657  invalid return from snprintf for UniqueDeviceIDv2: %d
0000268d  unique-device-id-string
000026a5  unable to find unique-device-id-string property in /chosen
000026e0  invalid length for for UniqueDeviceIDv3: %u
0000270c  denying executable mapping as the kernel has panicked
00002742  completed security boot mode: %u
00002763  system does not support restricted execution mode
00002795  successfully enabled restricted execution mode
000027c4  image4 dispatch: handler: %llu
000027e3  image4 dispatch: input size: %llu | %lu
0000280b  image4 dispatch: pin root not supported on this variant
00002843  image4 dispatch: evaluate trust not supported on this variant
00002884  TXM [Panic]: provided stack is not page-aligned
000028b4  TXM [Panic]: provided thread stack is already in use
000028e9  TXM [Panic]: provided thread stack cannot be resumed
0000291e  Assertion failed: %s, function %s, file %s, line %d.
00002954  (null)
0000295b  fmt->flags & FLAG_HAS_PRECISION
0000297b  src/libc/stdio/format.c
00002993  write_integer
000029a1  0123456789abcdef
000029b2  0123456789ABCDEF
000029c3  unknown scanf conversion
000029dc  Security assertion failed: %s, function %s, file %s, line %d.
00002a1b  (len) <= (dstlen)
00002a2d  __vsnprintf_chk
00002a3d  src/libc/stdio/vsnprintf.c
00002a58  __memcpy_chk
00002a65  src/libc/string/memcpy.c
00002a7e  __memmove_chk
00002a8c  src/libc/string/memmove.c
00002aa6  __memset_chk
00002ab3  src/libc/string/memset.c
00002acc  (smax) <= (obj_size)
00002ae1  __memset_s_chk
00002af0  src/libc/string/memset_s.c
00002b0b  __strlcpy_chk
00002b19  src/libc/string/strlcpy.c
00002b33  (!cpylen && !cpylen) || (cpylen == ~((size_t)0)) || !((uintptr_t)src < (uintptr_t)dst + cpylen && (uintptr_t)dst < (uintptr_t)src + cpylen)
00002bbf  stack check fail
00002bd0  [entitlements: %u] CEContextInitWithType: %d
00002bfd  failed CTAmfiInitializeContextWithOptions: %d
00002c2b  failed CTAmfiVerifyCMS: %d
00002c46  failed CTAmfiVerifyCertificateChain: %d
00002c6e  [profile] CEContextInitWithType: %d
00002c92  com.apple.developer.web-browser-engine.host
00002cbe  com.apple.developer.web-browser-engine.webcontent
00002cf0  TeamIdentifier
00002d20  859WDYTPW2
00002d2b  BDFWW8L6QE
00002d36  8HPC9RB4KE
00002d57  CTL9M94Q8X
00002d83  J465JVPK26
00002da4  9JA89QQLNQ
00002daf  4GDX6FKXZ3
00002dba  XPSUQMMH5W
00002dc5  WWDCDEMO14
00002ddb  ZL6BUSYGB3
00002de6  9B9BMM756K
00002df1  59GAB85EFG
00002dfc  DUMMYTEAM
00002e06  Developer
00002e10  TestFlight
00002e1b  Universal
00002e25  DemoMode
00002e2e  InternalBuild
00002e3c  NoExecute
00002e46  [%s] removing apple-internal capability
00002e6e  [%s] unknown apple-internal team
00002eaf  ProvisionedDevices
00002ed7  beta-reports-active
00002f00  Entitlements
00002f0d  AppAudience
00002f19  LOCALSPKEY
00002f24  com.apple.private.oop-jit.loader
00002f45  com.apple.private.oop-jit.runner
00002f66  com.apple.private.security-research-device.extended-research-mode
00002fa8  com.apple.private.security-research-device
00002fd3  task_for_pid-allow
00002fe6  com.apple.system-task-ports
00003002  com.apple.system-task-ports.control
00003026  com.apple.system-task-ports.token.control
00003050  previews
00003059  ml-compiler
00003065  com.apple.private.amfi.can-execute-cdhash
0000308f  com.apple.developer.swift-playgrounds-app.development-build
000030cb  com.apple.security.get-task-allow
00003125  alloc ws
0000312e  free ws
00003136  Bad tailq head %p first->prev != head @%d
00003160  DeviceTree overflow: %p, size %#zx
00003183  Device tree pointer outside of device tree region: pointer %p, region [0x%lx, 0x%lx]
000031dd  Device tree property overflow: prop %p, length 0x%x
00003211  CHIP_AP_PDI_SHA2_384
00003226  CHIP_CRYPTEX1_MOBILE_ASSET_CODE_INSTALL_AP
00003251  Cryptex1 mobile asset code install [AP host]
0000327e  chained manifest hash
00003294  CHIP_AP_SHA2_384
000032a5  CHIP_AP_SOFTWARE_FF00
000032bb  AP [software ff00]
000032ce  CHIP_CRYPTEX1_BOOT_AP_VERIFICATION
000032f1  Cryptex1 boot verification [AP host]
00003316  CHIP_AP_SOFTWARE_FF01
0000332c  AP [software ff01]
0000333f  CHIP_CRYPTEX1_MOBILE_ASSET_CODE_LOAD_AP
00003367  Cryptex1 mobile asset code load [AP host]
00003391  CHIP_AP_SOFTWARE_FF06
000033a7  AP [software ff06]
000033ba  CHIP_CRYPTEX1_GENERIC_AP
000033d3  Cryptex1 generic content [AP host]
000033f6  CHIP_VMA2
00003400  CHIP_CRYPTEX1_BOOT_VMA2_VERIFICATION
00003425  Cryptex1 boot verification [VMA2 host]
0000344c  CHIP_VMA2_CLONE
0000345c  CHIP_CRYPTEX1_ASSET_BRAIN_AP
00003479  Cryptex1 asset brain [AP host]
00003498  CHIP_CRYPTEX1_BOOT_AP
000034ae  Cryptex1 boot [AP host]
000034c6  panic: bogus digest length: %lu
000034eb  CHIP_VMA3
000034f8  panic: failed to boot expert: %d
00003519  libimage4
00003523  CHIP_CRYPTEX1_BOOT_VMA2
0000353b  Cryptex1 boot [vma2 host]
00003555  CHIP_CRYPTEX1_BOOT_VMA2_CLONE
00003573  Cryptex1 boot [vma2 host clone]
00003593  panic: should never be called
000035b1  set specialist
000035c0  generic
000035c8  panic: unreachable case: %s = 0x%llx
000035ed  p->p_type->pt_switchable
00003606  panic: failed to query expert: expert = %s, p = %s, fourcc = %s, code = %llu: %d
00003657  panic: failed to read property: %s: %d
0000367e  non-executable privilege level
0000369d  secureboot key scheme
000036b3  cryptex1 key scheme
000036c7  virtual machine monitor present
000036e7  use AVP secure boot
000036fc  panic: writing anti-replay state not supported in this environment
0000373f  default
00003751  panic: nonce slot prefix overflow: actual = %lu, expected <= %lu
00003792  magazine[%s]: failed to query boot manifest hash: %d
000037c7  panic: failed to query mix-n-match policy: %d
000037f5  panic: optional not set
0000380d  magazine[%s]: failed to query storage for nonce magazine: %d
0000384a  magazine[%s]: magazine data too small for version: actual = %lu, expected >= %lu
0000389b  magazine[%s]: future magazine is bogus: version = %u, actual = %lu, expected >= %lu
000038ef  magazine[%s]: magazine data has incorrect length: version = %u, actual = %lu, expected = %lu
0000394c  magazine[%s]: magazine data has invalid manifest hash length: actual = %u, expected <= %lu
000039a7  magazine[%s]: failed to read nonce slot data: %d
000039d8  magazine[%s]: invalid nonce slot data: %d
00003a08  panic: error not set to valid posix code: %d
00003a35  slot[%s]: slot data too small for slot version: actual = %lu, expected >= %lu
00003a83  slot[%s]: future slot is bogus: version = %u, actual = %lu, expected >= %lu
00003acf  slot[%s]: slot data has incorrect length: version = %u, actual = %lu, expected = %lu
00003b24  failed to derive nonce digest: nonce = %s: %d
00003b52  cryptex1 boot nonce
00003b66  cryptex1 product class
00003b7d  cryptex1 boot nonce hash
00003b9b  extended security domain
00003bb4  CHIP_CRYPTEX1_MOBILE_ASSET_DFU_VMA2
00003bd8  Cryptex1 mobile asset [VMA2 host]
00003bfa  secureboot certificate format
00003c18  cryptex1 certificate format
00003c34  cryptex1 chip identifier
00003c4d  nonce domain
00003c5a  research mode
00003c68  cryptex1 chip subtype
00003c7e  cryptex1 chip type
00003c91  long os version
00003ca1  boot uuid
00003cab  boot manifest hash
00003cbe  CHIP_CRYPTEX1_MOBILE_ASSET_DFU_AP
00003ce0  Cryptex1 mobile asset [AP host]
00003d00  certificate production status
00003d1e  certificate security mode
00003d38  effective production status
00003d54  failed to set release type: %d
00003d73  trap input has unexpected length: actual = %lu, expected = %lu, trap = 0x%llx: %d
00003dc5  no slot for handle: %llx: %d
00003de2  slot[%s]: caller not entitled to roll nonce: %d
00003e12  failed to set boot uuid: %d
00003e2e  effective security mode
00003e46  panic: illegal nonce descriptor configuration
00003e74  magazine pseudo-descriptor
00003e8f  CHIP_CRYPTEX1_MOBILE_ASSET_VMA2
00003eaf  pdi nonce hash
00003ebe  CHIP_CRYPTEX1_MOBILE_ASSET_AP
00003edc  personalized disk image
00003ef4  com.apple.private.img4.nonce.pdi
00003f15  srdp cryptex
00003f22  com.apple.private.img4.nonce.cryptex
00003f47  developer disk image
00003f5c  com.apple.private.img4.nonce.ddi
00003f7d  cryptex1 boot
00003f8b  com.apple.private.img4.nonce.cryptex1.boot
00003fb6  cryptex1 asset brain
00003fcb  com.apple.private.img4.nonce.cryptex1.asset
00003ff7  cryptex1 generic
00004008  com.apple.private.img4.nonce.cryptex1.generic
00004036  cryptex1 simulator
00004049  com.apple.private.img4.nonce.cryptex1.simulator
00004079  cryptex1 mobile asset dfu
00004093  com.apple.private.image4.nonce.propose.mobile-asset
000040c7  cryptex1 generic ephemeral
000040e2  cryptex1 generic erm
000040f7  com.apple.private.img4.nonce.cryptex1.generic.erm
00004129  cryptex1 mobile asset code install
0000414c  com.apple.private.img4.nonce.cryptex1.mobile-asset.code-install
0000418c  cryptex1 mobile asset code load
000041ac  com.apple.private.img4.nonce.cryptex1.mobile-asset.code-load
000041e9  slot[%s]: failed to query production fuse: %d
00004217  slot[%s]: failed to query research fuse: %d
00004243  allow mix-n-match
00004255  boot nonce hash
00004265  board identifier
00004276  set release type
00004287  set boot uuid
00004295  lock entry lock
000042a5  unlock entry lock
000042b7  lock subsystem lock
000042cb  unlock subsystem lock
000042e1  Trusted Execution Monitor
000042fb  /chosen/manifest-properties
00004317  /chosen/asmb
00004324  panic: failed to get chosen node: %d
00004349  panic: failed to get product node: %d
0000436f  panic: failed to get defaults node: %d
00004396  panic: failed to get manifest properties: %d
000043c3  40A0DDD2-77F8-4392-B4A3-1E7304206516:krn.
000043f4  %6s  %-36s : 0x%llx
00004410  lp-smb0
00004418  lp-smb1
00004420  panic: invalid secure boot state: %#x
00004446  use-ddi-secure-boot
0000445a  allow-ecid-mismatch
0000446e  uses-avp-root-ca
0000447f  tx monitor has no boot nonce: %d
000044a0  magazine[%s]: could not find nonce slot: chip = %s, domain = 0x%x: %d
000044e6  magazine[%s]: failed to get nonce: %d
0000450c  kernel supervisor has no boot nonce: %d
00004534  magazine[%s]: cannot entangle nonce; cleartext inconsistent: %d
00004574  certificate-production-status
00004592  certificate-security-mode
000045ac  effective-production-status-ap
000045cb  effective-security-mode-ap
000045e6  mix-n-match-prevention-status
00004604  internal-use-only-unit
0000461b  engineering-use-only-unit
00004635  factory-prerelease-global-trust
00004655  panic: illegal %s property: %s
00004674  chip-epoch
0000467f  board-id
00004688  security-domain
00004698  cryptex1-product-class
000046af  pqc-validation-flags
000046c4  boot-manifest-hash
000046d7  apfs-preboot-uuid
000046e9  lp-spih
000046f1  failed to copy kcinstall nonce hash: %d
00004719  magazine[%s]: failed to compute nonce digest for sideload chip: %s: %d
00004760  no boot uuid set
00004771  secureboot-certificate-format
0000478f  cryptex1-certificate-format
000047ab  secureboot-key-scheme
000047c1  cryptex1-key-scheme
000047da  failed to read from boot manifest: p = %s, name = %s: %d
00004813  panic: integer cast overflow: v = %s, actual = %llu, expected <= %llu
0000485b  boot nonce
00004866  certificate epoch
00004878  chip identifier
00004888  CHIP_AP_SRDP
00004895  object digest
000048a3  unique chip identifier
000048ba  CHIP_CRYPTEX1_BOOT_VMA2_CLONE_VERIFICATION
000048e5  Cryptex1 boot verification [VMA2 clone host]
00004912  cryptex1 live nonce hash
0000492b  security domain
0000493b  universal device identifier
00004957  panic: iteration underflow: idx = 0x%lx, %ld
00004984  panic: iteration overflow: idx = 0x%lx, %lu
000049b0  panic: illegal chip definition: provided static decode implementation: %s
000049fa  panic: illegal chip definition: invalid manifest type for dynamic selection: %s
00004a4f  rsa4096
00004a57  panic: illegal chip definition: no dynamic decode implementation: %s | %d
00004aa1  panic: illegal chip definition: no static decode implementation: %s
00004ae5  chp->chp_type
00004af3  rsa1024
00004afb  rsa3072
00004b08  hybridscheme3
00004b16  panic: illegal property definition: %s
00004b3d  panic: non-%s property set: property = %s, type = %s
00004b72  panic: property not present in chip instance: %s
00004ba3  CHIP_AP_DDI_SHA2_384
00004bb8  kcinstall nonce hash
00004bcd  CHIP_AP_KCINSTALL
00004bdf  TXM module
00004bea  panic: function should never be called: %s
00004c15  _txm_runtime_log
00004c26  _txm_runtime_log_handle
00004c3e  _txm_runtime_get_identifier_bool
00004c5f  _txm_runtime_get_identifier_uint32
00004c82  _txm_runtime_get_identifier_uint64
00004ca5  _txm_runtime_get_identifier_digest
00004cc8  _txm_runtime_get_identifier_cstr
00004ce9  _txm_runtime_alloc_type
00004d01  _txm_runtime_dealloc_type
00004d1b  _txm_runtime_set_nonce
00004d32  _txm_runtime_roll_nonce
00004d4a  _txm_runtime_copy_nonce
00004d62  0x%llx
00004d69  panic: digest length overflow: actual = %lu, expected <= %lu
00004da6  panic: digest length overflow: actual = %lu, expected >= %lu
00004de3  panic: unexpected expert: op = %s, actual = %s, expected = %s
00004e44  expert
00004e4f  expert magic
00004e6c  bounds safety
00004e7a  debug level
00004e86  diagnostic level
00004e97  secure boot
00004ea3  boot chip
00004ead  exception level
00004ebd  unprivileged limit
00004eda  pi->p_type->pt_switchable
00004efd  expert state
00004f10  failed to query property: %s: %d
00004f4e  manifest
00004f57  panic: nonce too large: actual = %lu, expected <= %ld
00004f92  uint32
00004f99  uint64
00004fa0  digest
00004fa7  version
00004fc1  panic: buffer not large enough for digest: actual = %lu, expected >= %lu
0000500a  failed to entangle nonce: %d
00005027  srd nonce hash
00005046  panic: invalid min/max: min = %u, max = %u
00005071  pqc validation flags
0000508a  Code Signing Monitor Image4 Module Version 7.0.0: Sat Oct  3 15:31:47 PDT 2026; root:AppleImage4_txm-374~8641/libimage4_TXM/RELEASE_ARM64E
00005115  RELEASE
0000511d  @(#)VERSION:Code Signing Monitor Image4 Module Version 7.0.0: Sat Oct  3 15:31:47 PDT 2026; root:AppleImage4_txm-374~8641/libimage4_TXM/RELEASE_ARM64E
000051b4  /Library/Caches/com.apple.xbs/D663580A-0B34-44CA-A93B-2DE79790A4E2/TemporaryDirectory.nJ3qZO/Binaries/AppleImage4_txm/install/Symbols/image4_TXM
00005245  Image4: supplementary Root CA already exists: %u
00005276  boot-command
00005283  Image4: darwin pseudo-expert: unable to provide UniqueDeviceID [ChipID]
000052cb  Image4: darwin pseudo-expert: unable to provide UniqueDeviceID [UniqueChipID]
00005319  Image4: darwin pseudo-expert: invalid VolumeUuid [Length]
00005353  Image4: darwin pseudo-expert: invalid VolumeUuid [Termination]
00005392  Image4: darwin pseudo-expert: invalid VolumeUuid [Encoding]
000053ce  cryptex1-chip-id
000053df  lp-stng
000053e7  LocalPolicy|AntiReplayNone
00005405  AP|Global
0000540f  AP|PDI
00005416  AP|DDI
0000541d  AP|SRDP
00005425  Cryptex1|Splat
00005434  Cryptex1|SplatGlobal
00005449  Cryptex1|SemiSplat
0000545c  Cryptex1|SemiSplatGlobal
00005475  Cryptex1|UpdateBrain
0000548a  Cryptex1|SafariDownlevel
000054a3  Cryptex1|SecureMobileAssetBrain
000054c3  Cryptex1|Generic
000054d4  Cryptex1|SecureMobileAssetInstall
000054f6  Cryptex1|SecureMobileAssetLoad
00005515  Cryptex1|SecureMobileAssetWithCodeInstall
0000553f  Cryptex1|SecureMobileAssetWithCodeLoad
00005566  Software|FF00
00005574  Software|FF01
00005582  Software|FF06
00005590  Ap|EphemeralDiavlo
000055a3  Ap|PersistentDiavlo
000055b7  Cryptex1|GenericDiavlo
000055ce  Image4: unable to acquire Diavlo Root CA from expert: %u
00005607  Image4: unable to build decode implementation for Diavlo: %u
00005644  Image4: invalid nonce type for setting digest: %u
00005676  Image4: nonce digest too large for TXM: %lu
000056a2  Image4: attempted to set nonce digest again: %u
000056d2  Image4: invalid nonce type for rolling: %u
000056fd  Image4: unable to setup /chosen node in TXM
00005729  Image4: unable to setup /product node in TXM
00005756  Image4: unable to setup /defaults node in TXM
00005784  Image4: unable to setup /chosen/manifest-properties node in TXM
000057c4  Image4: unable to setup /chosen/asmb node in TXM
0000580b  Image4: manifest evaluation: attempting 'rpnh' policy
00005841  Image4: manifest evaluation: attempting 'vnum' policy
00005877  Image4: manifest evaluation: 'vnum' ignored for satellite evaluation
000058bc  Image4: manifest evaluation: unable to obtain environment OS version: %u
00005905  Image4: manifest evaluation: unable to obtain manifest version: %u
00005948  Image4: manifest evaluation: 'vnum' mismatch: build tuple %u
00005985  environment
00005991  Image4: manifest evaluation: 'EPRO' and 'ESEC' ignored for satellite evaluation
000059e1  Image4: payload evaluation: failed to get payload type: %d
00005a1c  Image4: payload evaluation: failed production status check: %u
00005a5b  Image4: payload evaluation: failed security mode check: %u
00005a96  Image4: payload evaluation: attempting fusing policy: '%c%c%c%c'
00005ad7  Image4: payload evaluation: '%c%c%c%c' mismtch
00005b06  AP|SubsequentStage
00005b19  Image4: manifest evaluation: no policy for first stage anti-replay
00005b5c  Image4: manifest evaluation: attempting first stage anti-replay policy: %u
00005ba7  Image4: manifest evaluation: enforcing boot nonce
00005bd9  Image4: manifest evaluation: nonce tag: '%c%c%c%c'
00005c0c  Image4: manifest evaluation: nonce type: %u
00005c38  Image4: manifest evaluation: manifest does not have anti-replay nonce
00005c7e  Image4: manifest evaluation: unable to get nonce from manifest: %u
00005cc1  Image4: manifest evaluation: unable to get nonce from expert: %u
00005d02  Image4: manifest evaluation: '%c%c%c%c' mismatch
00005d33  Image4: manifest evaluation: enforcing cryptex1 nonce
00005d69  Image4: manifest evaluation: domain tag: '%c%c%c%c'
00005d9d  Image4: manifest evaluation: nonce tag:  '%c%c%c%c'
00005dd1  Image4: manifest evaluation: unable to get domain from manifest: %u
00005e15  Image4: manifest evaluation: unable to get type from domain: %u
00005e55  Image4: manifest evaluation: using nonce type:  %u
00005e88  Image4: manifest evaluation: enforcing restore-info nonce
00005ec2  Image4: manifest evaluation: signing-authority: %u
00005ef5  Image4: manifest evaluation: restore-info tag: '%c%c%c%c'
00005f2f  Image4: manifest evaluation: manifest tag: '%c%c%c%c'
00005f65  Image4: manifest evaluation: manifest does not have an attached restore-info
00005fb2  Image4: manifest evaluation: unable to get seed from restore-info: %u
00005ff8  Image4: manifest evaluation: restore-info seed too large: %lu
00006036  Image4: manifest evaluation: unable to compute nonce with expert: %u
0000607b  Image4: manifest evaluation: no policy for subsequent stage anti-replay
000060c3  Image4: manifest evaluation: attempting subsequent stage anti-replay policy: %u
00006113  Image4: manifest evaluation: enforcing subsequent stage policy: %u
00006156  Image4: manifest evaluation: unable to obtain previous stage digest: %u
0000619e  Image4: manifest evaluation: previous stage digest mismatch
000061da  Image4: manifest evaluation: manifest enables mix-and-match
00006216  Image4: manifest evaluation: environment enables mix-and-match
00006255  Image4: manifest evaluation: starting signature and identity evaluation: %s
000062a1  Image4: manifest evaluation: unable to resolve a valid decode implementation
000062ee  Image4: manifest evaluation: starting auxiliary evaluation
00006329  Image4: manifest evaluation: no environment specific auxiliary policy
0000636f  Image4: manifest evaluation: failed environment specific policy: %u
000063b3  Image4: manifest evaluation: auxiliary evaluation successful
000063f0  Image4: manifest evaluation: starting anti-replay evaluation
0000642d  Image4: manifest evaluation: failed first stage anti-replay: %u
0000646d  Image4: manifest evaluation: failed subsequent stage anti-replay: %u
000064b2  Image4: manifest evaluation: anti-replay evaluation successful
000064f1  Image4: payload evaluation: starting signature evaluation: %s
0000652f  Image4: payload evaluation: unable to resolve a valid decode implementation
0000657b  Image4: payload evaluation: starting auxiliary evaluation
000065b5  Image4: payload evaluation: failed fusing policy: %u
000065ea  Image4: payload evaluation: auxiliary evaluation successful
00006626  Image4: manifest evaluation: insufficient space for manifest hash
00006668  Image4: manifest evaluation: failed: %d, %u
00006694  Image4: manifest evaluation: failed to compute manifest digest: %d
000066d7  Image4: manifest evaluation: signature and identity evaluation successful
00006721  Image4: manifest evaluation: '%c%c%c%c'
00006749  Image4: manifest evaluation: unexpected property
0000677a  Image4: manifest evaluation: 'vuid' ignored for satellite evaluation
000067bf  Image4: manifest evaluation: 'stng' ignored for satellite evaluation
00006804  Image4: manifest evaluation: 'lobo' ignored for satellite evaluation
00006849  Image4: manifest evaluation: 'iuob' ignored for satellite evaluation
0000688e  Image4: manifest evaluation: 'data' ignored for satellite evaluation
000068d3  Image4: manifest evaluation: property ignored
00006901  Image4: manifest evaluation: property matched
0000692f  Image4: manifest evaluation: property mismatch: %u
00006962  Image4: manifest evaluation: coreTrustVerifyChain failure: 0x%0X
000069a3  Image4: manifest evaluation: coreTrustVerifySignature failure: 0x%0X
000069e8  Image4: payload evaluation: payload type: '%c%c%c%c'
00006a1d  Image4: payload evaluation: insufficient space for payload hash
00006a5d  Image4: payload evaluation: failed to compute payload digest: %d
00006a9e  Image4: payload evaluation: failed: %d, %u
00006ac9  Image4: payload evaluation: signature evaluation successful
00006b05  Image4: payload evaluation: '%c%c%c%c'
00006b2c  Image4: payload evaluation: property ignored
00006b59  Image4: payload evaluation: property matched
00006b86  Image4: payload evaluation: property mismatch: %u
00006bb8  Image4: manifest evaluation: starting trust evaluation
00006bef  Image4: manifest evaluation: trust evaluation successful
00006c28  Image4: payload evaluation: starting trust evaluation
00006c5e  Image4: payload evaluation: trust evaluation successful
00006c96  Image4: satellite trust evaluation disallowed with type: 0x%08X
00006cd6  rsa2048
00006ce0  CoreEntitlements: subset | %.*s: 0x%04X
00006d09  CoreEntitlements: validation | %.*s: 0x%04X
00006d6f  application-identifier
00006d87  LOCALSPKEY.swift-playgrounds-*0?
00006da8  )com.apple.developer.app-management-domain
00006dd4  swift-playgrounds*0.
00006de9  )com.apple.developer.swift-playgrounds-app
00006e19  ;com.apple.developer.swift-playgrounds-app.development-build
00006e5b  #com.apple.developer.team-identifier
00006e81  LOCALSPKEY
00006eca  AGKCTS
00006fac  0123456789ABCDEF
000072bd  COMPSIG-MLDSA87-RSA3072-PSS-SHA512
000075e0  chocolate stroob
0000772b  wQan#O
00007e31  COMPSIG-MLDSA87-RSA3072-PSS-SHA512
000085fb  Apple Secure Boot Root CA - G61
00008624  Apple Inc.1
00008668  Apple Secure Boot Root CA - G61
00008691  Apple Inc.1
00008715  n/wyo2
00009d81  Apple Inc.1&0$
00009d96  Apple Certification Authority1
00009dbe  Apple Root CA0
00009e05  Apple Inc.1&0$
00009e1a  Apple Certification Authority1
00009e42  Apple Root CA0
0000a00f  https://www.apple.com/appleca/0
0000a040  Reliance on this certificate by any party assumes acceptance of the then applicable standard terms and conditions of use, certificate policy and certification practice statements.0
0000a64f  6CCuvY
0000a99f  C\lmJ,
0000ae88  TEST UCRT ATTESTATION ROOT CA1
0000aeb0  Apple Inc.1
0000aec5  California0
0000aefc  TEST UCRT ATTESTATION ROOT CA1
0000af24  Apple Inc.1
0000af39  California0v0
0000b0bf  AVP Secure Boot Root CA - G11
0000b0e6  Apple Inc.1
0000b0fb  California0
0000b132  AVP Secure Boot Root CA - G11
0000b159  Apple Inc.1
0000b16e  California0
0000b621  )Apple Secure Boot Certification Authority
0000b68e  'Apple Extra Content Global Root CA - G11
0000b6c1  Apple Inc.1
0000b704  'Apple Extra Content Global Root CA - G11
0000b737  Apple Inc.1
0000b860  myX0_Ny="
0000be43  UsW;uKu
0000c051  /pdNe%
0000c4d8  jBb@.b6
0000ccb3  Apple Secure Boot Root CA - G21
0000ccdc  Apple Inc.1
0000cd20  Apple Secure Boot Root CA - G21
0000cd49  Apple Inc.1
0000d218  .img4 test secp384r1 Root Certificate Authority1
0000d252  Apple, Inc.1
0000d268  California0
0000d29e  .img4 test secp384r1 Root Certificate Authority1
0000d2d8  Apple, Inc.1
0000d2ee  California0v0
0000d48b  Apple Secure Boot Root CA - G31
0000d4b4  Apple Inc.1
0000d4f8  Apple Secure Boot Root CA - G31
0000d521  Apple Inc.1
0000d99f  ,qckD.
0000e052  ?Sfy.r=
0000e216  Xii[:e&
0000ecdf  EHmswO
0000f180  Basic Attestation User Root CA1
0000f1a9  Apple Inc.1
0000f1be  California0
0000f1f5  Basic Attestation User Root CA1
0000f21e  Apple Inc.1
0000f233  California0v0
0000f3b6  "Apple DDI Secure Boot Root CA - G11
0000f3e4  Apple Inc.1
0000f427  "Apple DDI Secure Boot Root CA - G11
0000f455  Apple Inc.1
0000f92a  "Apple X86 Secure Boot Root CA - G11
0000f958  Apple Inc.1
0000f99b  "Apple X86 Secure Boot Root CA - G11
0000f9c9  Apple Inc.1
0000fe80  Apple iPhone Certification Authority
0000fea5  Apple Code Signing Certification Authority
0000fed0  Apple Accessories Certification Authority - 
0000fefd  Apple Accessory Host Attestation Authority - 
0000ff2b  Apple Accessories Provisioning Authority - 
00010863  fCP?na
00011239  `@AwHxea
00011422  RMOpHjv{
000115bf  G'LFu s
000120f2  cLI0x2{ui
00012586  Z"+zeE(
00012a95  uBy@P*
00012ea4  MnN5/WZ
00013114  L?0sDMQ
000131f8  rc-`qFK
00013510  .9"BGR
000135ed  jsVc_C
00013c89  rOoqwl
00013cd5  pOaHL%$
00014c92  LpI=!fO
00015195  Hfh&)8
00015424  Frv.; 
00015e97  CoxrD[
00016049  Q+=Wxw
0001616f  _&f@l~tsZ-
000161d8  QiRp"r
00016c66  (gaw\d
00017a9d  E#6UKl
00017eea  *IjgzP&"
00018fe0  ORPEORPDCESECESD
00019078  txm.iphoneos.release
000190b8  <?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>
00019160  <key>CFBundleDisplayName</key>
0001917f  <string>Code Signing Monitor Image4 Module</string>
000191b3  <key>CFBundleExecutable</key>
000191d1  <string>libimage4_TXM.a</string>
000191f2  <key>CFBundleIdentifier</key>
00019210  <string>com.apple.security.libimage4.TXMonitor</string>
00019248  <key>CFBundleInfoDictionaryVersion</key>
00019271  <string>6.0</string>
00019286  <key>CFBundleName</key>
0001929e  <string>image4_TXM</string>
000192ba  <key>CFBundleShortVersionString</key>
000192e0  <string>7.0.0</string>
000192f7  <key>CFBundleVersion</key>
00019312  <string>374</string>
00019327  <key>DTCompiler</key>
0001933d  <string>com.apple.compilers.llvm.clang.1_0</string>
00019371  <key>DTPlatformName</key>
0001938b  <string>iphoneos</string>
000193a5  <key>DTPlatformVersion</key>
000193c2  <string>27.2</string>
000193d8  <key>DTSDKBuild</key>
000193ee  <string></string>
00019400  <key>DTSDKName</key>
00019415  <string>iphoneos27.2.internal</string>
0001943c  <key>DTXcode</key>
0001944f  <string>2700</string>
00019465  <key>DTXcodeBuild</key>
0001947d  <string>27A225b</string>
00019496  <key>DarwinBuilderBuild</key>
000194b4  <string>23A344017</string>
000194cf  <key>DarwinBuilderVersion</key>
000194ef  <string>14.0</string>
00019505  <key>DarwinVariant</key>
0001951e  <string>RELEASE</string>
00019537  <key>NSHumanReadableCopyright</key>
0001955b  <string>Copyright 
0001956f   2017-2024 Apple Inc. All rights reserved.</string></dict></plist>
00022460  HMHCCHMH
00024af0  ataddata
00024b58  skbssbks
00024c28  pmmvvmmp
00024c90  bsauuasb
00024d48  ncnccncn
00024db0  salcclas
00024e18  hcnccnch
00024e80  hcnccnch
00024f10  mdseesdm
000252d8  fcbssbcf
000253a8  phcffchp
00025410  modnndom
00025478  hcsrrsch
000254e0  pytsstyp
00025548  pytsstyp
000255b0  epyttype
00025618  munvvnum
00025680  munvvnum
000256e8  diobboid
00025750  hfmbbmfh
000257b8  mdnllndm
00025b80  ORPCCPRO
00025be8  CESCCSEC
00025c50  ORPEEPRO
00025cf0  CESEESEC
00025d48  enizzine
00026120  HCNBBNCH
000264d8  gmdppdmg
00026540  xtpccptx
000265a8  idvddvdi
000269c8  MNMAAMNM
00026a30  evollove
00026a98  HCNBBNCH
00026b00  HCNBBNCH
00026b68  DROBBORD
00026cf8  NCNBBNCN
00026db0  OPECCEPO
00026e18  PIHCCHIP
00026f90  ORPCCPRO
00026ff8  CESCCSEC
00027060  TSGDDGST
000270c8  DICEECID
00027130  DICEECID
000274f8  hcnllnch
00027560  ORPEEPRO
000275c8  CESEESEC
00027630  MODSSDOM
00027698  DIDUUDID
00027700  DIDUUDID
00027998  HCNBBNCH
00027cb0  HCNBBNCH
00027d18  fvqppqvf
0004b4a7  KNi+8k
0004dcfc  kki8Lki8
0004dd38  lkh8Mkh8
0004dd43  JLk*8J
00053275  :a.1:anT
000542b0  _h(8Hhi
000665b7  R_aUjZ
00088014  _start
```
