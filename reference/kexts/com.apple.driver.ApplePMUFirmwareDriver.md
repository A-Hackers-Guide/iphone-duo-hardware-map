# `com.apple.driver.ApplePMUFirmwareDriver`

- Name: ApplePMUFirmwareDriver
- Version: `1.0.0`
- UUID: `6D935C35-5F86-38BC-8810-73B2C233E4B6`
- Source version: `7.0.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 9.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 9.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 9.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 9.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (2) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) | `ApplePMUFirmwareDriver` | `pmu,spmi` |
| [`/arm-io/nub-spmi0/pmu-main/sgpio-bridge-pmu-main/pmu-secondary`](../devicetree/root__arm-io__nub-spmi0__pmu-main__sgpio-bridge-pmu-main__pmu-secondary.md) | `ApplePMUFirmwareDriver` | `pmu,spmi` |

## IOKit personalities (1) [KC]

### ApplePMUFirmwareDriver
- `CFBundleIdentifier`: `com.apple.driver.ApplePMUFirmwareDriver`
- `IOClass`: `ApplePMUFirmwareDriver`
- `IONameMatch`: `pmu,spmi`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePMUFirmwareDriver`
- `IOPropertyMatch`:
  - `has-fw`: `<data 22 chars>`
- `IOProviderClass`: `AppleARMSPMIDevice`
- `IOUserClientClass`: `ApplePMUFirmwareDriverUserClient`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `ApplePMUFirmwareDriver` | 0xd0 | IOService → IORegistryEntry |
| `ApplePMUFirmwareDriverUserClient` | 0xe0 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000eec off=0x0069cef0-0x0069dddc addr=0xfffffe00076a0ef0-0xfffffe00076a1ddc r--/r--   __TEXT            
	sz=0x00000018 off=0x0069d570-0x0069d588 addr=0xfffffe00076a1570-0xfffffe00076a1588               __TEXT.__const            
	sz=0x00000854 off=0x0069d588-0x0069dddc addr=0xfffffe00076a1588-0xfffffe00076a1ddc               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00002ac0 off=0x0236ace0-0x0236d7a0 addr=0xfffffe000936ece0-0xfffffe00093717a0 r-x/r-x   __TEXT_EXEC       
	sz=0x00002910 off=0x0236ace0-0x0236d5f0 addr=0xfffffe000936ece0-0xfffffe00093715f0          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000001b0 off=0x0236d5f0-0x0236d7a0 addr=0xfffffe00093715f0-0xfffffe00093717a0          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000148 off=0x049840a8-0x049841f0 addr=0xfffffe000b9880a8-0xfffffe000b9881f0 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049840a8-0x04984170 addr=0xfffffe000b9880a8-0xfffffe000b988170               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b988170-0xfffffe000b9881d0               __DATA.__common           (Zerofill)
	sz=0x00000020 off=0x00000000-0x00000020 addr=0xfffffe000b9881d0-0xfffffe000b9881f0               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00000e78 off=0x01197120-0x01197f98 addr=0xfffffe000819b120-0xfffffe000819bf98 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x01197120-0x01197130 addr=0xfffffe000819b120-0xfffffe000819b130         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x01197130-0x01197140 addr=0xfffffe000819b130-0xfffffe000819b140         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000cb8 off=0x01197140-0x01197df8 addr=0xfffffe000819b140-0xfffffe000819bdf8         __DATA_CONST.__const            
	sz=0x00000080 off=0x01197df8-0x01197e78 addr=0xfffffe000819bdf8-0xfffffe000819be78         __DATA_CONST.__kalloc_type      
	sz=0x000000d8 off=0x01197e78-0x01197f50 addr=0xfffffe000819be78-0xfffffe000819bf50         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000048 off=0x01197f50-0x01197f98 addr=0xfffffe000819bf50-0xfffffe000819bf98         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 63 at 0x04ae1a48
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     6D935C35-5F86-38BC-8810-73B2C233E4B6
008: LC_SOURCE_VERSION           7.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aac978 size=0x70
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `ApplePMUFirmwareDriver`
- `CFBundleGetInfoString`: `ApplePMUFirmwareDriver version 1.0.0, Copyright © 2024 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.ApplePMUFirmwareDriver`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `ApplePMUFirmwareDriver`
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
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/ApplePMUFirmwareDriver.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898864400`
- `_PrelinkExecutableRelativePath`: `ApplePMUFirmwareDriver`
- `_PrelinkExecutableSize`: `18796`
- `_PrelinkExecutableSourceAddr`: `-2198898864400`
- `_PrelinkKmodInfo`: `-2198828711768`

## Strings (63) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `IOUserClientDefaultLockingSetProperties`
- `ApplePMUFWDUCHostIRQ`
- `(%s) %s::%s: failed to create IOInterruptEventSource\n`
- `(%s) %s::%s: extRegisterWriteLong(RECEIVE_EVENT) failed, rc=0x%x\n`
- `IOUserClientEntitlements`
- `(%s) %s::%s: failed to cast provider\n`
- `(%s) %s::%s: expected to find has_fw property\n`
- `writeHostIRQ`
- `(%s) %s::%s: millivolts=%d.%06d\n`
- `(%s) %s::%s: going to sleep\n`
- `(%s) %s::%s: [%s] = 0x%x\n`
- `1211111212221212111111111111`
- `i8@?0`
- `mailboxTransactionGated`
- `(%s) %s::%s: timed out waiting for response\n`
- `(%s) %s::%s: extRegisterReadLong(RECEIVE0) failed, rc=0x%x\n`
- `(%s) %s::%s: failed to add event source to work loop, rc = 0x%x\n`
- `root`
- `IOUserClientDefaultLocking`
- `(%s) %s::%s: started\n`
- `ApplePMUFirmwareDriverUserClient`
- `(%s) %s::%s: rc=0x%x, receive event=%d, data=0x%x\n`
- `(%s) %s::%s: extRegisterReadLong(HOST_IRQ) failed, address=0x%x, rc=0x%x\n`
- `com.apple.driver.ApplePMUFirmwareDriver.user-access`
- `ApplePMUFWDSetCPMSRate`
- `(%s) %s::%s: interrupted while waiting for response\n`
- `12111112122212121211112121`
- `ApplePMUFWDSetCPMSVDDDroopThreshold`
- `fw-mcom-int-index`
- `(%s) %s::%s: failed to create IOWorkLoop\n`
- `IOUserClientDefaultLockingSingleThreadExternalMethod`
- `ApplePMUFirmwareDriver`
- `PMUName`
- `(%s) %s::%s: failed to find property %s\n`
- `start`
- `(%s) %s::%s: setProperty failed\n`
- `setCPMSRate`
- `(%s) %s::%s: extRegisterReadLong(RECEIVE_EVENT) failed, rc=0x%x\n`
- `(%s) %s::%s: failed to find property with key %s\n`
- `setCPMSVDDDroopThreshold`
- `(%s) %s::%s: invalid event %d\n`
- `(%s) %s::%s: source=%p, index=%d, _mailboxSleeping=%d\n`
- `writeHostIRQGated`
- `site.ApplePMUFirmwareDriver`
- `(%s) %s::%s: failed to create IOCommandGate\n`
- `fw-mcom-address`
- `(%s) %s::%s: trigger_id=%d\n`
- `(%s) %s::%s: after sleep\n`
- `pmu-fw-debug`
- `(%s) %s::%s: mailbox is not supported\n`
- `mailboxTransaction`
- `(%s) %s::%s: milliseconds=%d\n`
- `handleMailboxInterrupt`
- `site.ApplePMUFirmwareDriverUserClient`
- `(%s) %s::%s: super::start() failed\n`
- `fw-host-irq-address`
- `(%s) %s::%s: transmit event=%d, data=0x%x\n`
- `(%s) %s::%s: extRegisterWriteLong(TRANSMIT0) failed, rc=0x%x\n`
- `(%s) %s::%s: extRegisterWriteLong(TRANSMIT_INTR) failed, rc=0x%x\n`
- `(%s) %s::%s: failed to get data from key %s\n`
- `ApplePMUFWDMailboxTransaction`
- `has-fw`
- `getDTProperty`
