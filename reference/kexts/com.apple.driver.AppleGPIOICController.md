# `com.apple.driver.AppleGPIOICController`

- Name: AppleGPIOICController
- Version: `1.0.2`
- UUID: `C4A12C85-26AA-34B5-A2D4-98386668A4AC`
- Source version: `68.0.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.iokit.IOReportFamily`](com.apple.iokit.IOReportFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 11.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (4) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/gpio0`](../devicetree/root__arm-io__gpio0.md) | `AppleT8101GPIOIC` | `gpio,t8101` |
| [`/arm-io/nub-gpio`](../devicetree/root__arm-io__nub-gpio.md) | `AppleT8101GPIOIC` | `gpio,t8101` |
| [`/arm-io/smc-gpio`](../devicetree/root__arm-io__smc-gpio.md) | `AppleT8101GPIOIC` | `gpio,t8101` |
| [`/arm-io/mtp-gpio`](../devicetree/root__arm-io__mtp-gpio.md) | `AppleT8101GPIOIC` | `gpio,t8101` |

## IOKit personalities (3) [KC]

### AppleS5L8960XGPIOIC
- `CFBundleIdentifier`: `com.apple.driver.AppleGPIOICController`
- `IOClass`: `AppleS5L8960XGPIOIC`
- `IONameMatch`: `gpio,s5l8960x`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGPIOICController`
- `IOPlatformActiveAction`: `5000`
- `IOPlatformPanicAction`: `500`
- `IOPlatformQuiesceAction`: `1000`
- `IOPlatformWakeAction`: `500`
- `IOProviderClass`: `IOService`
- `IOUserClientClass`: `AppleGPIOUserClient`

### AppleT8006GPIOIC
- `CFBundleIdentifier`: `com.apple.driver.AppleGPIOICController`
- `IOClass`: `AppleT8006GPIOIC`
- `IONameMatch`: `gpio,t8006`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGPIOICController`
- `IOPlatformActiveAction`: `5000`
- `IOPlatformPanicAction`: `500`
- `IOPlatformQuiesceAction`: `1000`
- `IOPlatformWakeAction`: `500`
- `IOProviderClass`: `AppleARMIODevice`
- `IOUserClientClass`: `AppleGPIOUserClient`

### AppleT8101GPIOIC
- `CFBundleIdentifier`: `com.apple.driver.AppleGPIOICController`
- `IOClass`: `AppleT8101GPIOIC`
- `IONameMatch`: `gpio,t8101`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGPIOICController`
- `IOPlatformActiveAction`: `5000`
- `IOPlatformPanicAction`: `500`
- `IOPlatformQuiesceAction`: `1000`
- `IOPlatformWakeAction`: `500`
- `IOProviderClass`: `AppleARMIODevice`
- `IOUserClientClass`: `AppleGPIOUserClient`


## C++ classes (8) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleARMGPICFunction` | 0x48 | AppleARMFunction |
| `AppleARMGPIOFunction` | 0x40 | AppleARMFunction |
| `AppleGPIODevice` | 0x28 |  |
| `AppleGPIOICController` | 0x168 | IOInterruptController → IOService → IORegistryEntry |
| `AppleGPIOUserClient` | 0xf8 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |
| `AppleS5L8960XGPIOIC` | 0x170 | AppleGPIOICController → IOInterruptController → IOService → IORegistryEntry |
| `AppleT8006GPIOIC` | 0x178 | AppleGPIOICController → IOInterruptController → IOService → IORegistryEntry |
| `AppleT8101GPIOIC` | 0x170 | AppleGPIOICController → IOInterruptController → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1720)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000018c4 off=0x00472fe0-0x004748a4 addr=0xfffffe0007476fe0-0xfffffe00074788a4 r--/r--   __TEXT            
	sz=0x00000f8a off=0x004736f8-0x00474682 addr=0xfffffe00074776f8-0xfffffe0007478682               __TEXT.__cstring          (CstringLiterals)
	sz=0x0000013b off=0x00474690-0x004747cb addr=0xfffffe0007478690-0xfffffe00074787cb               __TEXT.__const            
	sz=0x000000d9 off=0x004747cb-0x004748a4 addr=0xfffffe00074787cb-0xfffffe00074788a4               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x0000b6f0 off=0x01cff120-0x01d0a810 addr=0xfffffe0008d03120-0xfffffe0008d0e810 r-x/r-x   __TEXT_EXEC       
	sz=0x0000b2d0 off=0x01cff120-0x01d0a3f0 addr=0xfffffe0008d03120-0xfffffe0008d0e3f0          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000420 off=0x01d0a3f0-0x01d0a810 addr=0xfffffe0008d0e3f0-0xfffffe0008d0e810          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000230 off=0x04942308-0x04942538 addr=0xfffffe000b946308-0xfffffe000b946538 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04942308-0x049423d0 addr=0xfffffe000b946308-0xfffffe000b9463d0               __DATA.__data             
	sz=0x00000150 off=0x00000000-0x00000150 addr=0xfffffe000b9463d0-0xfffffe000b946520               __DATA.__common           (Zerofill)
	sz=0x00000018 off=0x00000000-0x00000018 addr=0xfffffe000b946520-0xfffffe000b946538               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00002c58 off=0x010afc88-0x010b28e0 addr=0xfffffe00080b3c88-0xfffffe00080b68e0 rw-/rw-   __DATA_CONST      
	sz=0x00000028 off=0x010afc88-0x010afcb0 addr=0xfffffe00080b3c88-0xfffffe00080b3cb0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000028 off=0x010afcb0-0x010afcd8 addr=0xfffffe00080b3cb0-0xfffffe00080b3cd8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00002688 off=0x010afcd8-0x010b2360 addr=0xfffffe00080b3cd8-0xfffffe00080b6360         __DATA_CONST.__const            
	sz=0x00000200 off=0x010b2360-0x010b2560 addr=0xfffffe00080b6360-0xfffffe00080b6560         __DATA_CONST.__kalloc_type      
	sz=0x000000f0 off=0x010b2560-0x010b2650 addr=0xfffffe00080b6560-0xfffffe00080b6650         __DATA_CONST.__kalloc_var       
	sz=0x00000210 off=0x010b2650-0x010b2860 addr=0xfffffe00080b6650-0xfffffe00080b6860         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000080 off=0x010b2860-0x010b28e0 addr=0xfffffe00080b6860-0xfffffe00080b68e0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 148 at 0x04ada310
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     C4A12C85-26AA-34B5-A2D4-98386668A4AC
008: LC_SOURCE_VERSION           68.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aa0800 size=0x168
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleGPIOICController`
- `CFBundleGetInfoString`: `Copyright © 2019 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.AppleGPIOICController`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleGPIOICController`
- `CFBundleNumericVersion`: `16941056`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.2`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.2`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleGPIOICController.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901133344`
- `_PrelinkExecutableRelativePath`: `AppleGPIOICController`
- `_PrelinkExecutableSize`: `65084`
- `_PrelinkExecutableSourceAddr`: `-2198901133344`
- `_PrelinkKmodInfo`: `-2198828981496`

## Strings (114) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__os_log]**

- `setDevice cannot be called twice`
- `Missing entitlement '%s'`
- `GPIO configuration not found (%s)`
- `0x%llx (0x%x)`
- `Provider is not AppleGPIOICController`
- `Cannot find 'defaults' node`
- `IOUserClient2022::start failed`

**[__TEXT.__cstring]**

- `site.T`
- `AppleT8101GPIOIC`
- `\"GPIO Interrupt Storm!! Controller=%s Top 5 Pin IrqCounts: Pin%u=%u, Pin%u=%u, Pin%u=%u, Pin%u=%u, Pin%u=%u _activeirqs (%p) _irqCount (%p) \\n\" @%s:%d`
- `AppleGPIOICController::start: this: %p, _gpioicBaseAddress: %#lx\n`
- `/arm-io`
- `no-resume-restore`
- `bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow.`
- `\"too many supported int groups\" @%s:%d`
- `%s: Marked %u pins in '%s' node as ASC only \n`
- `\"failed to allocate _intStatus[%d]\\n\" @%s:%d`
- `\"Invalid service matching\" @%s:%d`
- `site.AppleARMGPIOFunction`
- `AppleGPIOUserClient`
- `default`
- `\"GPIO vector #%d is using unsupported interrupt group: %d\\n\" @%s:%d`
- `The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range`
- `12`
- `\"GPIO Device Controller refers to pin #%d (zero-indexed), but there's only %d pins!\" @%s:%d`
- `AppleGPIOICController`
- `%s: Found no-restore-gpio-pins in provider to skip restoring.\n`
- `\"InterruptVector buffer allocation failed in start()\" @%s:%d`
- `IOUserClientDefaultLockingSetProperties`
- `site.AppleGPIODevice`
- `site.AppleGPIOICController`
- `#gpio-int-groups`
- `%s: Failed to get no-restore-gpio-pins from DT.\n`
- `\"InterruptController buffer allocation failed in start()\" @%s:%d`
- `applegpio`
- `\"GPIO AppleARMFunction refers to pin #%d (zero-indexed), but there's only %d pins!\" @%s:%d`
- `IOUserClientEntitlements`
- `\"GPIO Interrupt Storm!! Top 5 Pin IrqCounts: Pin%u=%u, Pin%u=%u, Pin%u=%u, Pin%u=%u, Pin%u=%u _activeirqs (%p) _irqCount (%p) \\n\" @%s:%d`
- `site.AppleT8101GPIOIC`
- `AppleGPIOICController.cpp`
- `\"IOInterruptController start function failed\" @%s:%d`
- `start`
- `defaults`
- `AppleS5L8960XGPIOIC.cpp`
- `\"Memory allocation failed\" @%s:%d`
- `\"!wl\" @%s:%d`
- `\"A GPIO interrupt was configured on pin (zero indexed) #%d, but there's only %d pins!\" @%s:%d`
- `bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally`
- `IOPlatformDevice`
- `\"initForPM\" @%s:%d`
- `1211111212221212111121122111222211111121212121`
- `AppleGPIOICController: wake event %d missing in device-tree\n`
- `AppleGPIODevice`
- `12212`
- `121111121222121211112112211122221111112121212`
- `\"wake-events improperly defined\" @%s:%d`
- `\"failed to allocate _intStatus\\n\" @%s:%d`
- `site.AppleT8006GPIOIC`
- `pin%u`
- `event_name-mask%d`
- `OSBoundedPtr.h`
- `\"GPIO(%zu): 0x%p: oldConfig(%x) != config(%x)\" @%s:%d`
- `#gpio-pins`
- `site.IOInterruptVector`
- `role`
- `\"_supportedIntGroups must be allocated before initPinsAndGroups\" @%s:%d`
- `\"%s\" @%s:%d`
- `\"This service does not support GPIO control in EDT\" @%s:%d`
- `site.AppleARMGPICFunction`
- `IOUserClientDefaultLockingSingleThreadExternalMethod`
- `AppleT8006GPIOIC.cpp`
- `AppleT8101GPIOIC.cpp`
- `\"malformed no-restore-gpio-pins devicetree data\" @%s:%d`
- `ie-fix`
- `wake-no-interrupt-group`
- `site.uint32_t *`
- `121111222`
- `IOProviderClass`
- `12111112122212121111211221112222111111212121221`
- `AppleT8006GPIOIC: wake event %d missing in device-tree\n`
- `site.AppleGPIOUserClient`
- `com.apple.applegpio`
- `AppleS5L8960XGPIOIC`
- `glitchless`
- `21121111`
- `\"interruptLock allocation failed in start()\" @%s:%d`
- `1`
- `1211111212221212111111111111111`
- `IONameMatch`
- `\"!_wakeEventSignal\" @%s:%d`
- `\"malformed supported-int-groups device tree data\" @%s:%d`
- `no-restore-gpio-pins`
- `wake-events`
- `\"missing role property or provider is not available\" @%s:%d`
- `IOUserClientDefaultLocking`
- `com.apple.applegpio-access`
- `IOHibernateState`
- `\"failed to allocate _supportedIntGroups or _isWakeupIntGroup\\n\" @%s:%d`
- `\" failed to allocate _ascOnlyGpioPins\" @%s:%d`
- `\"wake-no-interrupt-group isnt supported on this GPIO device. Requires an always on gpio block\" @%s:%d`
- `12111122`
- `site.AppleS5L8960XGPIOIC`
- `\"addEventSource\" @%s:%d`
- `\"failed to allocate intStatus\\n\" @%s:%d`
- `\"gcb(%d) >= _numGCBs(%d)\" @%s:%d`
- `supported-int-groups`
- `InterruptControllerName`
- `AppleT8006GPIOIC`
- `\"no InterruptController name found in start()\" @%s:%d`
- `\"failed to allocate _wakeEvents\\n\" @%s:%d`
- `AppleARMGPIOFunction`
- `AppleARMGPICFunction`
- `\"failed to allocate intStatus[%d]\\n\" @%s:%d`
- `This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.`
