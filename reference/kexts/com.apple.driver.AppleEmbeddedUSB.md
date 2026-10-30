# `com.apple.driver.AppleEmbeddedUSB`

- Name: AppleEmbeddedUSB
- Version: `1`
- UUID: `723A9EF9-9A96-321B-8B3A-45FC6C1B7C7C`
- Source version: `717.40.5.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.iokit.IOAccessoryManager`](com.apple.iokit.IOAccessoryManager.md) 1.0.0, [`com.apple.iokit.IOPortFamily`](com.apple.iokit.IOPortFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0.0b1, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0.0b2, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0.0b2, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0.0b2, [`com.apple.kpi.private`](com.apple.kpi.private.md) 16.5.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleEmbeddedUSBArbitrator
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedUSB`
- `IOClass`: `AppleEmbeddedUSBArbitrator`
- `IONameMatch`: `usb-complex,s5l8900x`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedUSB`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (6) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleEmbeddedUSBArbitrator` | 0x1f0 | IOService → IORegistryEntry |
| `AppleEmbeddedUSBNub` | 0xc0 | IOService → IORegistryEntry |
| `AppleUSBCableChangeEventSource` | 0x70 | IOInterruptEventSource → IOEventSource |
| `AppleUSBPhy` | 0xd0 | IOService → IORegistryEntry |
| `AppleUSBPhyServiceClient` | 0x50 |  |
| `IOUSBArbitratorCommandGate` | 0x50 | IOCommandGate → IOEventSource |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001700 off=0x0045f9f0-0x004610f0 addr=0xfffffe00074639f0-0xfffffe00074650f0 r--/r--   __TEXT            
	sz=0x000010bb off=0x00460018-0x004610d3 addr=0xfffffe0007464018-0xfffffe00074650d3               __TEXT.__cstring          (CstringLiterals)
	sz=0x0000001c off=0x004610d4-0x004610f0 addr=0xfffffe00074650d4-0xfffffe00074650f0               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00008050 off=0x01c90be0-0x01c98c30 addr=0xfffffe0008c94be0-0xfffffe0008c9cc30 r-x/r-x   __TEXT_EXEC       
	sz=0x00007c60 off=0x01c90be0-0x01c98840 addr=0xfffffe0008c94be0-0xfffffe0008c9c840          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000003f0 off=0x01c98840-0x01c98c30 addr=0xfffffe0008c9c840-0xfffffe0008c9cc30          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000003b0 off=0x04940620-0x049409d0 addr=0xfffffe000b944620-0xfffffe000b9449d0 rw-/rw-   __DATA            
	sz=0x00000270 off=0x04940620-0x04940890 addr=0xfffffe000b944620-0xfffffe000b944890               __DATA.__data             
	sz=0x00000140 off=0x00000000-0x00000140 addr=0xfffffe000b944890-0xfffffe000b9449d0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00001d40 off=0x0108fc40-0x01091980 addr=0xfffffe0008093c40-0xfffffe0008095980 rw-/rw-   __DATA_CONST      
	sz=0x00000020 off=0x0108fc40-0x0108fc60 addr=0xfffffe0008093c40-0xfffffe0008093c60         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000020 off=0x0108fc60-0x0108fc80 addr=0xfffffe0008093c60-0xfffffe0008093c80         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001808 off=0x0108fc80-0x01091488 addr=0xfffffe0008093c80-0xfffffe0008095488         __DATA_CONST.__const            
	sz=0x00000200 off=0x01091488-0x01091688 addr=0xfffffe0008095488-0xfffffe0008095688         __DATA_CONST.__kalloc_type      
	sz=0x000001f8 off=0x01091688-0x01091880 addr=0xfffffe0008095688-0xfffffe0008095880         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000100 off=0x01091880-0x01091980 addr=0xfffffe0008095880-0xfffffe0008095980         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 158 at 0x04ad92ac
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     723A9EF9-9A96-321B-8B3A-45FC6C1B7C7C
008: LC_SOURCE_VERSION           717.40.5.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9f6f0 size=0x110
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleEmbeddedUSB`
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedUSB`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleEmbeddedUSB`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2000-2017 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleEmbeddedUSB.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901212688`
- `_PrelinkExecutableRelativePath`: `AppleEmbeddedUSB`
- `_PrelinkExecutableSize`: `47168`
- `_PrelinkExecutableSourceAddr`: `-2198901212688`
- `_PrelinkKmodInfo`: `-2198828988896`

## Strings (127) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `%06lu.%06u %s::%s: invalid input, phyService = NULL\n`
- `%06lu.%06u %s::%s: failed to allocate _ref\n`
- `%s::%s: failed to allocate lock\n`
- `site.IOUSBArbitratorCommandGate`
- `site.AppleUSBCableChangeEventSource`
- `site.AppleEmbeddedUSBNub`
- `%06lu.%06u %s::%s: provider is not arbitrator\n`
- `powerStateDidChangeToGated`
- `setProperties`
- `enablePhyPower`
- `12111112122212121211211111111111111111111111111111111111121111`
- `%06lu.%06u %s::%s: failed to start super class\n`
- `AAPL,power-supply`
- `1222111212`
- `free`
- `AppleEmbeddedUSBArbitrator-force-usbhost`
- `%s::%s: unable to locate AppleEmbeddedUSBArbitrator service\n`
- `site.AppleUSBPhyServiceClient`
- `AppleUSBPhyServiceClient[%p]::%s: calling clearPortReset(%p, %d)\n\n`
- `%06lu.%06u %s::%s: service %p\n`
- `%06lu.%06u %s::%s: %s is no longer busy\n`
- `clock-mask`
- `kAppleUSBPhyServiceDisabledAndClocked`
- `kAppleUSBPhyServiceEnabledAndClocked`
- `setOTGConnectionSpeed`
- `publish-criteria`
- `%06lu.%06u %s::%s: terminating nub %p for %s\n`
- `requestPhyServiceLevel`
- `%06lu.%06u %s::%s: failed to create nub for %s\n`
- `initWithServicesPhyPortAndOptions`
- `AppleUSBPhyServiceClient[%p]::%s: enable: calling enablyPhyPower(%p, 0x%08x)\n`
- `IOUSBArbitratorCommandGate`
- `%06lu.%06u %s::%s: failed to allocate _workLoop\n`
- `AppleUSBPhy`
- `start`
- `site.AppleEmbeddedUSBArbitrator`
- `%06lu.%06u %s::%s: _forceCableType %s\n`
- `AppleUSBPhyServiceClient`
- `AppleEmbeddedUSBNub-debug`
- `%s::%s: failed to allocate client array\n`
- `%06lu.%06u %s::%s: provider is not AppleARMIODevice\n`
- `forcePowerGated`
- `waitForTerminatingNubs`
- `AppleEmbeddedUSBNub`
- `%06lu.%06u %s::%s: capabilities 0x%08lx, stateNumber %ld, whatDevice %p\n`
- `%06lu.%06u %s::%s: enable index %d\n`
- `\"Invalid phyID\" @%s:%d`
- `AppleUSBPhyServiceClient[%p]::%s: \n`
- `systemPowerChangeThreadCallGated`
- `powerStateWillChangeTo`
- `%06lu.%06u %s::%s: cable type is %s\n`
- `%s::%s: setProperties: %p\n`
- `systemPowerChange`
- `AppleUSBCableChangeEventSource`
- `121111121222121212112112`
- `reg`
- `%06lu.%06u %s::%s: power transition completed with result 0x%08x\n`
- `hsic-enabled`
- `AppleUSBPhyServiceClient[%p]::%s: disable: calling enableDeviceClock(%p, 0)\n`
- `AppleUSBPhyServiceClient[%p]::%s: port %d of phy %p is now %s\n`
- `AppleEmbeddedUSBArbitrator-force-usbdevice`
- `site.tSystemPowerNotifyParams`
- `AppleEmbeddedUSBArbitrator`
- `AppleEmbeddedUSBArbitrator-debug`
- `%06lu.%06u %s::%s: publishing nub %p for %s\n`
- `enableDeviceClock`
- `hsic`
- `%06lu.%06u %s::%s: failed to allocate _commandGate\n`
- `211`
- `phy-id`
- `%s::%s: %p with mask 0x%08x\n`
- `AppleUSBPhyServiceClient[%p]::%s: calling assertPortReset(%p, %d)\n`
- `%06lu.%06u %s::%s: handleStart failed\n`
- `%06lu.%06u %s::%s: _systemPowerChangeThread is already scheduled\n`
- `%06lu.%06u %s::%s: %s is busy\n`
- `%06lu.%06u %s::%s: asserting _powerEnable\n`
- `function-power_enable`
- `kAppleUSBPhyServiceSuspended`
- `powerStateDidChangeTo`
- `12111211112211`
- `AppleUSBPhy-debug`
- `\"Unable to initialize AppleUSBPhyServiceNotifier members\" @%s:%d`
- `updatePublishedNubs`
- `%s::%s: \n`
- `applySDBTunables`
- `%06lu.%06u %s::%s: failed to allocate client array\n`
- `no-pmu`
- `%06lu.%06u %s::%s: failed to allocate interrupt source\n`
- `%06lu.%06u %s::%s: _powerStateChangeThread is already scheduled\n`
- `power-level`
- `force-usb-device`
- `force-usb-host`
- `location`
- `%06lu.%06u %s::%s: deasserting _powerEnable\n`
- `AppleUSBPhyServiceClient[%p]::%s: enable: calling enableDeviceClock(%p, 0x%08x)\n`
- `NULL`
- `%06lu.%06u %s::%s: powerstate %ld\n`
- `%06lu.%06u %s::%s: %p with mask 0x%08x\n`
- `systemPowerChangeThreadCall`
- `%06lu.%06u %s::%s: type 0x%08x\n`
- `powerStateChangeThreadCall`
- `%06lu.%06u %s::%s: disable index %d\n`
- `%06lu.%06u %s::%s: failed to allocate _lock\n`
- `AppleUSBPhyServiceClient[%p]::%s: calling setOTGConnectionSpeed(%p, %d)\n\n`
- `%06lu.%06u %s::%s: powerStateChangeThread allocate failed\n`
- `%06lu.%06u %s::%s: \n`
- `setPowerState`
- `%06lu.%06u %s::%s: stateNumber %d\n`
- `%06lu.%06u %s::%s: super init failed\n`
- `force-usb-test-mode`
- `AppleUSBPhy.cpp`
- `kAppleUSBPhyServiceDisabledAndNotClocked`
- `1211121111`
- `12111112122212121212111111`
- `%s::%s: hsic disabled\n`
- `AppleUSBPhyServiceClient[%p]::%s: port %d of phy %p requesting a service level of %s\n`
- `AppleEmbeddedUSBArbitrator-force-usb3host`
- `registerPhy`
- `setPowerStateGated`
- `enableDevicePower`
- `AppleUSBPhyServiceClient[%p]::%s: initialized AppleUSBPhyServiceClient %p for phy %p\n`
- `%06lu.%06u %s::%s: unable to get power states array`
- `handleUSBCableTypeChange`
- `initWithProvider`
- `site.AppleUSBPhy`
- `kAppleUSBPhyServiceEnabledAndNotClocked`
- `AppleUSBPhyServiceClient[%p]::%s: disable: calling enablePhyPower(%p, 0)\n`
