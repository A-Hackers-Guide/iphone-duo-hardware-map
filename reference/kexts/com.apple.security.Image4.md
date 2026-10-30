# `com.apple.security.Image4`

- Name: Image4
- Version: `1.0.0`
- UUID: `3B1F6B46-DD5B-3DDE-9401-82CF8E22F96D`
- Source version: `27.0.3.0.0`
- Depends on: [`com.apple.iokit.IOCryptoAcceleratorFamily`](com.apple.iokit.IOCryptoAcceleratorFamily.md) 1.0.0, [`com.apple.kec.corecrypto`](com.apple.kec.corecrypto.md) 1.0.0, [`com.apple.kext.CoreTrust`](com.apple.kext.CoreTrust.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 15.0.0, [`com.apple.kpi.dsep`](com.apple.kpi.dsep.md) 21.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 15.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0.0, [`com.apple.security.AppleImage4`](com.apple.security.AppleImage4.md) 3.0.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/defaults`](../devicetree/root__defaults.md) | `Image4` | `defaults` |

## IOKit personalities (1) [KC]

### Image4
- `CFBundleIdentifier`: `com.apple.security.Image4`
- `IOClass`: `Image4`
- `IOMatchCategory`: `Image4`
- `IONameMatch`: `defaults`
- `IOPersonalityPublisher`: `com.apple.security.Image4`
- `IOProviderClass`: `IOPlatformDevice`
- `IOUserClientClass`: `Image4UserClient`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `Image4` | 0x88 | IOService → IORegistryEntry |
| `Image4UserClient` | 0xd8 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000ba20 off=0x00b8ba10-0x00b97430 addr=0xfffffe0007b8fa10-0xfffffe0007b9b430 r--/r--   __TEXT            
	sz=0x000039cd off=0x00b8c088-0x00b8fa55 addr=0xfffffe0007b90088-0xfffffe0007b93a55               __TEXT.__cstring          (CstringLiterals)
	sz=0x000079d0 off=0x00b8fa60-0x00b97430 addr=0xfffffe0007b93a60-0xfffffe0007b9b430               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x000113a8 off=0x038eba70-0x038fce18 addr=0xfffffe000a8efa70-0xfffffe000a900e18 r-x/r-x   __TEXT_EXEC       
	sz=0x00010eb8 off=0x038eba70-0x038fc928 addr=0xfffffe000a8efa70-0xfffffe000a900928          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000004f0 off=0x038fc928-0x038fce18 addr=0xfffffe000a900928-0xfffffe000a900e18          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000007a0 off=0x04a1d628-0x04a1ddc8 addr=0xfffffe000ba21628-0xfffffe000ba21dc8 rw-/rw-   __DATA            
	sz=0x00000678 off=0x04a1d628-0x04a1dca0 addr=0xfffffe000ba21628-0xfffffe000ba21ca0               __DATA.__data             
	sz=0x00000128 off=0x00000000-0x00000128 addr=0xfffffe000ba21ca0-0xfffffe000ba21dc8               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00003290 off=0x01485cd8-0x01488f68 addr=0xfffffe0008489cd8-0xfffffe000848cf68 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x01485cd8-0x01485ce8 addr=0xfffffe0008489cd8-0xfffffe0008489ce8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x01485ce8-0x01485cf8 addr=0xfffffe0008489ce8-0xfffffe0008489cf8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00002ee8 off=0x01485cf8-0x01488be0 addr=0xfffffe0008489cf8-0xfffffe000848cbe0         __DATA_CONST.__const            
	sz=0x00000080 off=0x01488be0-0x01488c60 addr=0xfffffe000848cbe0-0xfffffe000848cc60         __DATA_CONST.__kalloc_type      
	sz=0x00000278 off=0x01488c60-0x01488ed8 addr=0xfffffe000848cc60-0xfffffe000848ced8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000068 off=0x01488ed8-0x01488f40 addr=0xfffffe000848ced8-0xfffffe000848cf40         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000028 off=0x01488f40-0x01488f68 addr=0xfffffe000848cf40-0xfffffe000848cf68         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 171 at 0x04afc6a0
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     3B1F6B46-DD5B-3DDE-9401-82CF8E22F96D
008: LC_SOURCE_VERSION           27.0.3.0.0
009: LC_FUNCTION_STARTS          offset=0x004acb398 size=0x2b0
```

## Info.plist keys [KC]

- `AppleSecurityExtension`: `True`
- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `Image4`
- `CFBundleIdentifier`: `com.apple.security.Image4`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `Image4`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.0`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2025-2026 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleLibraries_x86_64`:
  - `com.apple.kec.corecrypto`: `1.0.0`
  - `com.apple.kext.CoreTrust`: `1.0.0`
  - `com.apple.kpi.bsd`: `15.0.0`
  - `com.apple.kpi.dsep`: `21.0.0`
  - `com.apple.kpi.iokit`: `15.0`
  - `com.apple.kpi.libkern`: `8.0.0`
  - `com.apple.kpi.mach`: `8.0.0`
  - `com.apple.kpi.private`: `8.0.0`
  - `com.apple.kpi.unsupported`: `8.0.0`
  - `com.apple.security.AppleImage4`: `3.0.0`
- `OSBundleRequired`: `Local-Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/Image4.kext`
- `_PrelinkExecutableLoadAddr`: `-2198893692400`
- `_PrelinkExecutableRelativePath`: `Image4`
- `_PrelinkExecutableSize`: `133112`
- `_PrelinkExecutableSourceAddr`: `-2198893692400`
- `_PrelinkKmodInfo`: `-2198828083672`

## Strings (343) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `Image4: manifest evaluation: unexpected property\n`
- `Image4: payload evaluation: starting trust evaluation\n`
- `Image4:  resetting: %s\n`
- `Image4: manifest evaluation: attempting 'rpnh' policy\n`
- `Image4: manifest evaluation: unable to get domain from manifest: %u\n`
- `\"Image4: unable to allocate memory descriptor for cipher-text: %lu\" @%s:%d`
- `UserClient_ObjectLoad.cpp`
- `internal-use-only-unit`
- `chip-id`
- `\"Image4: nonce digest too large for PPL: %lu\" @%s:%d`
- `Image4: payload evaluation: '%c%c%c%c' mismtch\n`
- `Image4: payload evaluation: auxiliary evaluation successful\n`
- `Image4: system does not have a supported legacy blob\n`
- `Image4: platform does not support NVRAM\n`
- `static IOReturn Image4UserClient::objectLoad(OSObject *, void *, IOExternalMethodArguments *)`
- `Image4: manifest evaluation: unable to obtain previous stage digest: %u\n`
- `LocalPolicy|AntiReplayNone`
- `40A0DDD2-77F8-4392-B4A3-1E7304206516:krn.c1sm`
- `com.apple.private.image4.user-client`
- `factory-prerelease-global-trust`
- `im4c`
- `Image4: unable to acquire Diavlo Root CA from expert: %u\n`
- `Image4: unexpected version of legacy digest: %u\n`
- `Image4: unexpected length for legacy digest: %llu\n`
- `Image4: unable to load local policy: %u\n`
- `/chosen/manifest-properties`
- `\"Image4: unable to setup /chosen/manifest-properties node\" @%s:%d`
- `AP|SRDP`
- `Image4: manifest evaluation: failed: %d, %u\n`
- `121111121222121211111111111`
- `Software|FF06`
- `Image4: manifest evaluation: failed subsequent stage anti-replay: %u\n`
- `Image4: unable to hash cipher-text: %u\n`
- `Image4: unable to read nonce data from storage: %u\n`
- `Image4: unexpected version for nonce seed blob: V2 | %u\n`
- `Image4: error generating proposal with AppleImage4: %d\n`
- `apfs-preboot-uuid`
- `boot-manifest-hash`
- `Image4: manifest evaluation: unable to obtain environment OS version: %u\n`
- `40A0DDD2-77F8-4392-B4A3-1E7304206516:krn.pdmg`
- `Image4: %s: unable to copyin payload\n`
- `Image4: manifest evaluation: nonce type: %u\n`
- `Image4: unable to parse digest for nonce seed blob: V2 | %u\n`
- `\"Image4: unable to cast service as IODTNVRAM\" @%s:%d`
- `Cryptex1|SemiSplat`
- `Image4: manifest evaluation: restore-info tag: '%c%c%c%c'\n`
- `AP|OSManifest`
- `com.apple.private.img4.nonce-seed`
- `AP|PDI`
- `Image4: manifest evaluation: starting anti-replay evaluation\n`
- `Image4: payload evaluation: property mismatch: %u\n`
- `gid-aes-key`
- `personalized.cryptex1.update-brain`
- `pqc-validation-flags`
- `\"Image4: unable to setup /defaults node in PPL\" @%s:%d`
- `rsa1024`
- `Image4: manifest evaluation: nonce tag: '%c%c%c%c'\n`
- `Image4: manifest evaluation: unable to resolve a valid decode implementation\n`
- `Image4: successfully loaded local policy on the system\n`
- `Image4: owning task is not entitled for user-client access\n`
- `x509`
- `\"Image4: attempted to set nonce digest without PPL mutable buffer\" @%s:%d`
- `40A0DDD2-77F8-4392-B4A3-1E7304206516:krn.c1bt`
- `lp-spih`
- `\"Image4: attempted to get product without PPL context\" @%s:%d`
- `Image4: payload evaluation: starting signature evaluation: %s\n`
- `40A0DDD2-77F8-4392-B4A3-1E7304206516:krn.zine`
- `\"Image4: unable to prepare memory descriptor for plain-text: %d\" @%s:%d`
- `c1ai`
- `Image4: unable to allocate legacy environment\n`
- `Image4: manifest evaluation: insufficient space for manifest hash\n`
- `\"Image4: unable to allocate memory descriptor for plain-text: %lu\" @%s:%d`
- `Image4: supplementary Root CA already exists: %u\n`
- `\"Image4: unexpected length of PPL mutable buffer: %lu\" @%s:%d`
- `\"Image4: invalid nonce type for setting digest: %u\" @%s:%d`
- `Image4: manifest evaluation: domain tag: '%c%c%c%c'\n`
- `Image4: manifest evaluation: manifest tag: '%c%c%c%c'\n`
- `Image4: manifest evaluation: attempting subsequent stage anti-replay policy: %u\n`
- `Image4: unable to parse digest for nonce seed blob: V1 | %u\n`
- `Image4: unable to allocate kernel thread for NVRAM write\n`
- `AP|SubsequentStage`
- `Image4: manifest evaluation: '%c%c%c%c' mismatch\n`
- `Image4: manifest evaluation: manifest enables mix-and-match\n`
- `Image4: platform booting under NeRD\n`
- `entangle-nonce`
- `40A0DDD2-77F8-4392-B4A3-1E7304206516:krn.c1ab`
- `Image4: darwin pseudo-expert: unable to provide UniqueDeviceID [ChipID]\n`
- `Image4: manifest evaluation: enforcing cryptex1 nonce\n`
- `\"Image4: attempted to get defaults without PPL context\" @%s:%d`
- `Ap|PersistentDiavlo`
- `Image4: manifest evaluation: unable to obtain manifest version: %u\n`
- `Image4: payload evaluation: failed to get payload type: %d\n`
- `Image4: platform requires immutable NVRAM [Mix-N-Match]\n`
- `IOAESAccelerator`
- `\"Image4: attempted to get expert without PPL context\" @%s:%d`
- `\"Image4: unable to setup /chosen node in PPL\" @%s:%d`
- `Image4: payload evaluation: payload type: '%c%c%c%c'\n`
- `Image4: unsupported key-algorithm: %u | %u\n`
- `Image4: platform supports and enables slot encryption\n`
- `Ap|EphemeralDiavlo`
- `Image4: manifest evaluation: no policy for first stage anti-replay\n`
- `Image4: payload evaluation: starting auxiliary evaluation\n`
- `Image4: unable to resolve signing authority for slot: %u | %u\n`
- `Image4: unable to entangle nonce proposal: %u | slot: %s\n`
- `\"Image4: unable to initialize super class\" @%s:%d`
- `/chosen`
- `\"Image4: attempted to get manifest properties without PPL context\" @%s:%d`
- `Image4: manifest evaluation: unable to get nonce from manifest: %u\n`
- `\"Image4: unable to complete memory descriptor for plain-text: %d\" @%s:%d`
- `uses-avp-root-ca`
- `Cryptex1|GenericDiavlo`
- `Image4: unable to build decode implementation for Diavlo: %u\n`
- `Image4: manifest evaluation: 'EPRO' and 'ESEC' ignored for satellite evaluation\n`
- `Image4: unable to write magazine: %u\n`
- `com.apple.private.img4.set-supplemental-root`
- `Image4: unable to load Diavlo Root CA: %u\n`
- `PPL`
- `\"Image4: unable to setup /chosen/manifest-properties node in PPL\" @%s:%d`
- `unique-chip-id`
- `security-domain`
- `\"Image4: attempted to set mutable buffer again\" @%s:%d`
- `Image4: manifest evaluation: restore-info seed too large: %lu\n`
- `Image4: manifest evaluation: unable to compute nonce with expert: %u\n`
- `Image4: manifest evaluation: signature and identity evaluation successful\n`
- `Image4: manifest evaluation: 'data' ignored for satellite evaluation\n`
- `Kernel.cpp`
- `site.Image4`
- `cryptex1-product-class`
- `Cryptex1|SemiSplatGlobal`
- `Software|FF00`
- `Image4: manifest evaluation: auxiliary evaluation successful\n`
- `Image4: manifest evaluation: coreTrustVerifyChain failure: 0x%0X\n`
- `d1ma`
- `\"Image4: attempted to set nonce digest without PPL context\" @%s:%d`
- `Cryptex1|Splat`
- `Image4: payload evaluation: trust evaluation successful\n`
- `osenvironment`
- `Image4: platform does not enable slot encryption [%s]\n`
- `Image4: error rolling nonce with AppleImage4: %d\n`
- `Image4: invalid user-client selector: %u\n`
- `/product`
- `Cryptex1|SecureMobileAssetLoad`
- `Image4: manifest evaluation: unable to get seed from restore-info: %u\n`
- `Image4: manifest evaluation: failed environment specific policy: %u\n`
- `Image4: manifest evaluation: '%c%c%c%c'\n`
- `Image4: manifest evaluation: attempting first stage anti-replay policy: %u\n`
- `c1gn`
- `Image4`
- `Image4: unable to get nonce digest for slot: %u | %u\n`
- `lp-smb0`
- `lp-stng`
- `\"Image4: unable to setup /chosen node\" @%s:%d`
- `Kernelspace.cpp`
- `Image4: unexpected length of proposed seed: %lu\n`
- `site.Image4UserClient`
- `\"Image4: unable to setup /product node in PPL\" @%s:%d`
- `hybridscheme3`
- `Image4: manifest evaluation: manifest does not have anti-replay nonce\n`
- `Image4: manifest evaluation: trust evaluation successful\n`
- `IODTNVRAM`
- `rsa4096`
- `Image4: manifest evaluation: nonce tag:  '%c%c%c%c'\n`
- `40A0DDD2-77F8-4392-B4A3-1E7304206516:krn.c1ai`
- `Image4: darwin pseudo-expert: invalid VolumeUuid [Encoding]\n`
- `LocalPolicy|Linked`
- `environment`
- `Image4: manifest evaluation: enforcing subsequent stage policy: %u\n`
- `Image4: manifest evaluation: coreTrustVerifySignature failure: 0x%0X\n`
- `Image4: platform requires immutable NVRAM [Horizon]\n`
- `\"Image4: unable to complete memory descriptor for cipher-text: %d\" @%s:%d`
- `Image4: unable to read gid-aes-key from /chosen: %u\n`
- `Image4: manifest evaluation: 'iuob' ignored for satellite evaluation\n`
- `12111112122212121`
- `cryptex1-certificate-format`
- `AP`
- `Image4: payload evaluation: failed security mode check: %u\n`
- `recovery`
- `BNCH`
- `com.apple.private.security.AppleImage4.user-client`
- `Image4: darwin pseudo-expert: invalid VolumeUuid [Length]\n`
- `esdm-fuses`
- `Cryptex1|SecureMobileAssetBrain`
- `Image4: manifest evaluation: no policy for subsequent stage anti-replay\n`
- `Image4: manifest evaluation: starting signature and identity evaluation: %s\n`
- `Image4: manifest evaluation: failed first stage anti-replay: %u\n`
- `Image4: platform does not enable slot encryption [GID]\n`
- `cryptex1-key-scheme`
- `Image4: darwin pseudo-expert: unable to provide UniqueDeviceID [UniqueChipID]\n`
- `Image4: unable to encrypt plain-text: %u\n`
- `Image4: unable to write nonce slot: %u\n`
- `Image4: unable to decode legacy blob: V2 | %u\n`
- `cptx`
- `40A0DDD2-77F8-4392-B4A3-1E7304206516:krn.c1er`
- `\"Image4: unable to initialize magazine: %u\" @%s:%d`
- `PPL.c`
- `rsa2048`
- `Image4: unable to acquire mix-and-match status: %u\n`
- `Image4: magazine status: %u\n`
- `Image4:           epoch: %u\n`
- `Image4: unexpected length for nonce seed blob: V2 | %llu | %lu\n`
- `Image4: unable to write NVRAM: %s | %u\n`
- `00000000-0000-0000-0000-000000000000`
- `Image4: platform requires immutable NVRAM [OTA]\n`
- `Image4: unable to read boot-command from /chosen: %u\n`
- `c1ge`
- `c1ab`
- `\"Image4: attempted to get chosen without PPL context\" @%s:%d`
- `AP|DDI`
- `Image4: manifest evaluation: no environment specific auxiliary policy\n`
- `c1er`
- `c1al`
- `\"Image4: failed to load Diavlo Root CA with code-signing-monitor: %u\" @%s:%d`
- `lp-smb1`
- `boot-command`
- `\"Image4: attempted to set nonce digest again: %u\" @%s:%d`
- `LocalPolicy`
- `Image4: manifest evaluation: failed to compute manifest digest: %d\n`
- `Image4: payload evaluation: insufficient space for payload hash\n`
- `secureboot-certificate-format`
- `engineering-use-only-unit`
- `Image4: manifest evaluation: using nonce type:  %u\n`
- `Image4: payload evaluation: failed to compute payload digest: %d\n`
- `Image4: unable to read nonce data from legacy blob: %u\n`
- `Image4: using legacy blob: V0\n`
- `Image4: unable to parse digest for nonce seed blob: V0 | %u\n`
- `Image4: unexpected version for nonce seed blob: V1 | %u\n`
- `Image4: manifest evaluation: starting trust evaluation\n`
- `Image4: unexpected seed count for nonce seed blob: V2 | %llu\n`
- `Image4: unable to read osenvironment from /chosen: %u\n`
- `\"Image4: unable to encrypt plain-text using the AES service\" @%s:%d`
- `Image4: using the ApBootNonce for type: %u\n`
- `\"Image4: attempted to get ASMB without PPL context\" @%s:%d`
- `Image4: manifest evaluation: 'vnum' mismatch: build tuple %u\n`
- `Image4: unable to entangle nonce slot: %u | slot: %s\n`
- `Image4: unable to decode legacy blob: V1 | %u\n`
- `com.apple.private.pmap.load-trust-cache`
- `Cryptex1|SplatGlobal`
- `Image4: manifest evaluation: unable to get type from domain: %u\n`
- `Image4: manifest evaluation: environment enables mix-and-match\n`
- `40A0DDD2-77F8-4392-B4A3-1E7304206516:krn.c1ge`
- `Image4: successfully loaded Diavlo Root CA on the system\n`
- `Image4: darwin pseudo-expert: invalid VolumeUuid [Termination]\n`
- `Image4: manifest evaluation: anti-replay evaluation successful\n`
- `dvdi`
- `c1sm`
- `manifest`
- `Image4: manifest evaluation: manifest does not have an attached restore-info\n`
- `Image4: manifest evaluation: 'vuid' ignored for satellite evaluation\n`
- `Image4: manifest evaluation: property matched\n`
- `Image4: unable to update boot manifest hash: %u\n`
- `Image4: platform requires immutable NVRAM [Deconflicting]\n`
- `pdmg`
- `Image4: %s: unable to copyin manifest\n`
- `cryptex1-chip-id`
- `Cryptex1|SecureMobileAssetWithCodeLoad`
- `Image4: unable to acquire key-algorithm: :%u | %u\n`
- `40A0DDD2-77F8-4392-B4A3-1E7304206516:nonce-seeds`
- `effective-security-mode-ap`
- `Image4: payload evaluation: unable to resolve a valid decode implementation\n`
- `Image4: unable to initialize nonce slot: %lu: %u\n`
- `Image4: using legacy blob: V2\n`
- `\"Image4: unable to initialize magazine slots: %u\" @%s:%d`
- `Image4: %s: unable to allocate manifest\n`
- `Image4: manifest evaluation: attempting 'vnum' policy\n`
- `Image4: using legacy blob: V1\n`
- `Image4: platform requires immutable NVRAM [Other]\n`
- `Image4: platform does not support slot encryption\n`
- `vmm-present`
- `\"Image4: attempted to roll nonce without PPL context\" @%s:%d`
- `%u.%u.%u.%u.%u,%u`
- `Software|FF01`
- `IOKit.cpp`
- `com.apple.private.img4.set-local-policy`
- `Cryptex1|SafariDownlevel`
- `name`
- `chip-epoch`
- `\"Image4: attempted to initialize PPL expert without a PPL\" @%s:%d`
- `Image4: manifest evaluation: property mismatch: %u\n`
- `Image4: payload evaluation: '%c%c%c%c'\n`
- `Image4: payload evaluation: property matched\n`
- `Image4: error querying nonce from AppleImage4: %d\n`
- `40A0DDD2-77F8-4392-B4A3-1E7304206516:krn.c1gn`
- `Image4UserClient`
- `mix-n-match-prevention-status`
- `Image4: unable to setup /chosen/asmb node\n`
- `\"Image4: invalid nonce type for rolling: %u\" @%s:%d`
- `rsa3072`
- `Cryptex1|SecureMobileAssetWithCodeInstall`
- `Image4: manifest evaluation: property ignored\n`
- `Image4: payload evaluation: property ignored\n`
- `effective-production-status-ap`
- `love`
- `Image4: manifest evaluation: enforcing boot nonce\n`
- `Image4: manifest evaluation: signing-authority: %u\n`
- `Image4: manifest evaluation: 'lobo' ignored for satellite evaluation\n`
- `Image4: satellite trust evaluation disallowed with type: 0x%08X\n`
- `Image4:      slot count: %lu\n`
- `Image4: allowed to mutate NVRAM: %u\n`
- `Image4: manifest evaluation: 'vnum' ignored for satellite evaluation\n`
- `Image4: manifest evaluation: unable to get nonce from expert: %u\n`
- `Image4: payload evaluation: signature evaluation successful\n`
- `\"Image4: memory descriptor larger than cipher-text: %llu\" @%s:%d`
- `40A0DDD2-77F8-4392-B4A3-1E7304206516:krn.dvdi`
- `40A0DDD2-77F8-4392-B4A3-1E7304206516:krn.d1ma`
- `40A0DDD2-77F8-4392-B4A3-1E7304206516:krn.c1al`
- `Image4: unexpected length of proposed digest: %lu\n`
- `Image4: unable to query ApBootNonce digest: %u\n`
- `c1bt`
- `\"Image4: failed to load local policy with code-signing-monitor: %u\" @%s:%d`
- `Cryptex1|UpdateBrain`
- `\"Image4: unable to entangle magazine slots: %u\" @%s:%d`
- `/defaults`
- `/chosen/asmb`
- `\"Image4: attempted to get darwin-data without PPL context\" @%s:%d`
- `Image4: manifest evaluation: enforcing restore-info nonce\n`
- `darwinos-ramdisk`
- `\"Image4: unable to prepare memory descriptor for cipher-text: %d\" @%s:%d`
- `\"Image4: unable to setup /product node\" @%s:%d`
- `Kernelspace`
- `Image4: manifest evaluation: starting auxiliary evaluation\n`
- `Image4: payload evaluation: failed fusing policy: %u\n`
- `board-id`
- `\"Image4: attempted to roll nonce without PPL mutable buffer\" @%s:%d`
- `Cryptex1|Generic`
- `Image4: payload evaluation: attempting fusing policy: '%c%c%c%c'\n`
- `Image4: manifest evaluation: previous stage digest mismatch\n`
- `Image4: unexpected data of proposed digest\n`
- `40A0DDD2-77F8-4392-B4A3-1E7304206516:krn.cptx`
- `certificate-security-mode`
- `Cryptex1|SecureMobileAssetInstall`
- `Image4: payload evaluation: failed production status check: %u\n`
- `Image4: unable to read legacy blob: %u\n`
- `Image4: unable to decode legacy blob: V0 | %u\n`
- `Image4: unable to resolve AppleImage4 environment: %u\n`
- `AP|Global`
- `Image4: manifest evaluation: 'stng' ignored for satellite evaluation\n`
- `Image4: payload evaluation: failed: %d, %u\n`
- `\"Image4: unable to cast service as %s\" @%s:%d`
- `Image4: %s: unable to allocate payload\n`
- `secureboot-key-scheme`
- `certificate-production-status`
- `\"Image4: unable to setup /defaults node\" @%s:%d`
- `Image4: unable to setup /chosen/asmb node in PPL\n`
