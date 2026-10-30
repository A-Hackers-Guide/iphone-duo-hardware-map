# `com.apple.driver.AppleDCPDPTXProxy`

- Name: AppleDCPDPTXProxy
- Version: `1.0.0`
- UUID: `12C8D408-52A9-33F0-BD8E-E8D82E6A29F1`
- Source version: `440.52.1.0.0`
- Depends on: [`com.apple.driver.AppleDCP`](com.apple.driver.AppleDCP.md) 1.0, [`com.apple.driver.AppleFirmwareKit`](com.apple.driver.AppleFirmwareKit.md) 1.0.0, [`com.apple.driver.DCPAVFamilyProxy`](com.apple.driver.DCPAVFamilyProxy.md) 1.0.0, [`com.apple.driver.DCPDPFamilyProxy`](com.apple.driver.DCPDPFamilyProxy.md) 1.0.0, [`com.apple.iokit.IOAVFamily`](com.apple.iokit.IOAVFamily.md) 1.0, [`com.apple.iokit.IOAccessoryManager`](com.apple.iokit.IOAccessoryManager.md) 1.0, [`com.apple.iokit.IODisplayPortFamily`](com.apple.iokit.IODisplayPortFamily.md) 1.0, [`com.apple.iokit.IOHDCPFamily`](com.apple.iokit.IOHDCPFamily.md) 1.0, [`com.apple.iokit.IOPortFamily`](com.apple.iokit.IOPortFamily.md) 1.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 19.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 19.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 19.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (4) [KC]

### AppleDCPDPTXRemoteHDCPAuthSessionProxy
- `CFBundleIdentifier`: `com.apple.driver.AppleDCPDPTXProxy`
- `IOClass`: `AppleDCPDPTXRemoteHDCPAuthSessionProxy`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDCPDPTXProxy`
- `IOPropertyMatch`:
  - `EPICName`: `dcpdptx-hdcp-auth-session`
- `IOProviderClass`: `AFKEndpointInterface`

### AppleDCPDPTXRemoteHDCPInterfaceProxy
- `CFBundleIdentifier`: `com.apple.driver.AppleDCPDPTXProxy`
- `IOClass`: `AppleDCPDPTXRemoteHDCPInterfaceProxy`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDCPDPTXProxy`
- `IOPropertyMatch`:
  - `EPICName`: `dcpdptx-hdcp-interface`
- `IOProviderClass`: `AFKEndpointInterface`

### AppleDCPDPTXRemotePortProxy
- `CFBundleIdentifier`: `com.apple.driver.AppleDCPDPTXProxy`
- `IOClass`: `AppleDCPDPTXRemotePortProxy`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDCPDPTXProxy`
- `IOPropertyMatch`:
  - `EPICName`: `dcpdptx-port-epic`
- `IOProviderClass`: `AFKEndpointInterface`

### AppleDCPLPDPTXPortProxy
- `CFBundleIdentifier`: `com.apple.driver.AppleDCPDPTXProxy`
- `IOClass`: `AppleDCPLPDPTXPortProxy`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDCPDPTXProxy`
- `IOPropertyMatch`:
  - `EPICName`: `dcp-lpdptx-port-epic`
- `IOProviderClass`: `AFKEndpointInterface`


## C++ classes (5) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleDCPDPTXRemoteHDCPAuthSessionProxy` | 0x638 | DCPAVProxy → IOService → IORegistryEntry |
| `AppleDCPDPTXRemoteHDCPInterfaceProxy` | 0x610 | DCPAVProxy → IOService → IORegistryEntry |
| `AppleDCPDPTXRemotePortProxy` | 0x638 | DCPAVProxy → IOService → IORegistryEntry |
| `AppleDCPDPTXRemotePortUFP` | 0x280 | IODPSwitchUFP → IODPTXPort → IOService → IORegistryEntry |
| `AppleDCPLPDPTXPortProxy` | 0x630 | DCPAVProxy → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000020f2 off=0x00414b50-0x00416c42 addr=0xfffffe0007418b50-0xfffffe000741ac42 r--/r--   __TEXT            
	sz=0x00000048 off=0x004151c8-0x00415210 addr=0xfffffe00074191c8-0xfffffe0007419210               __TEXT.__const            
	sz=0x00001028 off=0x00415210-0x00416238 addr=0xfffffe0007419210-0xfffffe000741a238               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000a0a off=0x00416238-0x00416c42 addr=0xfffffe000741a238-0xfffffe000741ac42               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00008378 off=0x01b63fc0-0x01b6c338 addr=0xfffffe0008b67fc0-0xfffffe0008b70338 r-x/r-x   __TEXT_EXEC       
	sz=0x00008068 off=0x01b63fc0-0x01b6c028 addr=0xfffffe0008b67fc0-0xfffffe0008b70028          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000310 off=0x01b6c028-0x01b6c338 addr=0xfffffe0008b70028-0xfffffe0008b70338          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000001a0 off=0x0493c590-0x0493c730 addr=0xfffffe000b940590-0xfffffe000b940730 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x0493c590-0x0493c658 addr=0xfffffe000b940590-0xfffffe000b940658               __DATA.__data             
	sz=0x000000d8 off=0x00000000-0x000000d8 addr=0xfffffe000b940658-0xfffffe000b940730               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00002f70 off=0x01048920-0x0104b890 addr=0xfffffe000804c920-0xfffffe000804f890 rw-/rw-   __DATA_CONST      
	sz=0x00000028 off=0x01048920-0x01048948 addr=0xfffffe000804c920-0xfffffe000804c948         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000028 off=0x01048948-0x01048970 addr=0xfffffe000804c948-0xfffffe000804c970         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00002bd0 off=0x01048970-0x0104b540 addr=0xfffffe000804c970-0xfffffe000804f540         __DATA_CONST.__const            
	sz=0x00000140 off=0x0104b540-0x0104b680 addr=0xfffffe000804f540-0xfffffe000804f680         __DATA_CONST.__kalloc_type      
	sz=0x00000188 off=0x0104b680-0x0104b808 addr=0xfffffe000804f680-0xfffffe000804f808         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000088 off=0x0104b808-0x0104b890 addr=0xfffffe000804f808-0xfffffe000804f890         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 115 at 0x04ad6a90
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     12C8D408-52A9-33F0-BD8E-E8D82E6A29F1
008: LC_SOURCE_VERSION           440.52.1.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9d0e0 size=0x198
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleDCPDPTXProxy`
- `CFBundleIdentifier`: `com.apple.driver.AppleDCPDPTXProxy`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleDCPDPTXProxy`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.0`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91018`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91018`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleDCPDPTXProxy.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901519536`
- `_PrelinkExecutableRelativePath`: `AppleDCPDPTXProxy`
- `_PrelinkExecutableSize`: `54650`
- `_PrelinkExecutableSourceAddr`: `-2198901519536`
- `_PrelinkKmodInfo`: `-2198829005424`

## Strings (200) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `runActionBlock ret=0x%08x\n`
- `dispext0`
- `lpdptx`
- `SetDriveSettings`
- `GetDownspread`
- `-restore`
- `PairingInfoAvailable`
- `%s SoC Vmax for dcp index %u\n`
- `SetDisplayHints`
- `ResourceAvailableDefault`
- `enter: %s -> %s (role=%u, supportsHPD=%u)\n`
- `121111121222121211222221122122111121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212221111`
- `State`
- `disable`
- `GetMaxLinkRate`
- `start`
- `dispext2`
- `core1`
- `dptx`
- `HDCP suppressed per -restore`
- `failed to init IODPPortService\n`
- ` (ignored)`
- `ValidateKSVList`
- `site.AppleDCPDPTXRemotePortUFP`
- `IOAVController`
- `12111112122212121111122222111111111111222222222222222222222222222222222222221112`
- `called while dfp == NULL!\n`
- `GetLinkRate`
- `failed to create UFP\n`
- `failed to attach UFP\n`
- `failed to set owner for UFP\n`
- `displayRelease_block_invoke`
- `validateConnection`
- `_provider->connectTo(*dfp) ret=0x%08x; skipping super::displayRequest()\n`
- `enter: powerstate = %lx, current = %x\n`
- `atc1`
- `AppleDCPDPTXRemoteHDCPAuthSessionProxy`
- `GetAuthenticatedContentType`
- `DeviceNotResponding`
- `Failed super::start\n`
- `DidChangeLinkConfiguration`
- `powerChangeDone_block_invoke`
- `hdcp-fuse-mask`
- `md0`
- `NO matching found for IOAVControllerUserInterface!\n`
- `GetContentTypeCapability`
- `site.AppleDCPDPTXRemotePortProxy`
- `1211111212221212112222211221221111212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112122211122`
- `HDCPProtocolType`
- `Negotiating`
- `enableSoCVmaxPerfState`
- `warning: Redundant DisplayRelease detected!\n`
- `???`
- `AppleDCPLPDPTXPortProxy`
- `super::handleStart() failed\n`
- `Activate`
- `InactiveSinkDetected`
- `ret=0x%08x\n`
- `HPrimeAvailable`
- `ForceHotPlugDetect`
- `DeviceNotStarted`
- `exit: %s -> %s: ret=0x%08x\n`
- `HDCP suppressed per disable-av-content-protection`
- `i8@?0`
- `SetActiveLaneCount`
- `GetVirtualDeviceMode`
- `Failed to allocate command gate\n`
- `sleepWhileCondition`
- `die0`
- `dpphy`
- `HDCP suppressed per ramrod_disable_sep_load`
- `warning: _socVmaxIndex for port %u is 0 (invalid)\n`
- `enable`
- `failed to start UFP\n`
- `exit: ret=0x%08x, powerstate = %lx\n`
- `dispext3`
- `GetLaneOrientation`
- `failed to allocate IODPPortService\n`
- `Unknown`
- `GetSupportsLaneMapping`
- `DisplayRelease IPC failed with ret=0x%08x\n`
- `ReceiverConnected`
- `AuthOpen`
- `VmaxFailSafeTimerAction`
- `SetLinkRate`
- `disable-av-content-protection`
- `rd`
- `SetHPDState`
- `None`
- `Unplug`
- `site.AppleDCPDPTXRemoteHDCPAuthSessionProxy`
- `MaxActivePixelRate`
- `MaxTotalPixelRate`
- `HDCPMessageTransportType`
- `AppleDCPDPTXRemotePortUFP`
- `dpin0`
- `GetDriveSettings`
- `%s -> %s (role=%u, supportsHPD=%u)\n`
- `%.4s::%.8s::%.5s`
- `AppleDCPDPTXRemoteHDCPInterfaceProxy`
- `HDCP1 is required, but SoC is not HDCP1 fused!`
- `AuthClose`
- `_armIOProvider not found\n`
- `GetMaxLaneCount`
- `setPowerState_block_invoke`
- `dispext1`
- `1211111212221212112222211221221111212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112122211111`
- `CPDesired`
- `displayRequest`
- `GetSupportsDownspread`
- `%s -> noconnect`
- `HDCP suppressed per rd=md0`
- `handleStart`
- `Deactivate`
- `die1`
- `core0`
- `%.4s::%.6s::%.5s`
- `Ignoring %s for Native PHY based DP port`
- `12111112122212121122222112212211112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121222`
- `hdcp_fuse_mask`
- `DeviceBusyTimeout`
- `AppleDCPDPTXRemotePortProxy`
- `GetActiveLaneCount`
- `SetDownspread`
- `enter: powerstate = %lx, _displayRequested = %u\n`
- `exit: powerstate = %lx, _displayRequested = %u, ret=0x%08x%s\n`
- `Wrong provider type\n`
- `SetResourceAvailable`
- `MaxPixelWidth`
- `connectTo`
- `atc2`
- `atc3`
- `ramrod_disable_sep_load`
- `Plug`
- `GetMaxDriveSettings`
- `waiting for power state change -> powerstate = %lx...\n`
- `handlePortMessage`
- `IRQ`
- `Authenticated`
- `WillChangeLinkConfiguration`
- `SetLaneMap`
- `synchronousChangeDPTXPowerStateTo`
- `atc0`
- `dpin1`
- `site.AppleDCPDPTXRemoteHDCPInterfaceProxy`
- `ReadRandom`
- `ValidateKSV`
- `_socVmaxIndex = %u, socVmaxIndexCount = %zu, port = %u\n`
- `HDCP2 is required, but SoC is not HDCP2 fused!`
- `ReceiverIDListAvailable`
- `GetSupportsHPD`
- `powerstate %lx -> %lx\n`
- `ret = 0x%x\n`
- `powerChangeDone`
- `site.AppleDCPLPDPTXPortProxy`
- `EPICUnit`
- `dcp-soc-vmax-index`
- `Vmax fail safe timer fired!\n`
- `failed to init UFP\n`

**[__TEXT.__os_log]**

- `IOAV[%d] %s<0x%llx>::%s: exit: powerstate = %lx, _displayRequested = %u, ret=0x%08x%s\n`
- `IOAV[%d] %s<0x%llx>::%s: %s -> noconnect`
- `IOAV[%d] %s<0x%llx>::%s: exit: %s -> %s: ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: HDCP1 is required, but SoC is not HDCP1 fused!`
- `IOAV[%d] %s<0x%llx>::%s: warning: _socVmaxIndex for port %u is 0 (invalid)\n`
- `IOAV[%d] %s<0x%llx>::%s: _provider->connectTo(*dfp) ret=0x%08x; skipping super::displayRequest()\n`
- `IOAV[%d] %s<0x%llx>::%s: ret = 0x%x\n`
- `IOAV[%d] %s<0x%llx>::%s: waiting for power state change -> powerstate = %lx...\n`
- `IOAV[%d] %s<0x%llx>::%s: NO matching found for IOAVControllerUserInterface!\n`
- `IOAV[%d] %s<0x%llx>::%s: Wrong provider type\n`
- `IOAV[%d] %s<0x%llx>::%s: failed to create UFP\n`
- `IOAV[%d] %s<0x%llx>::%s: HDCP2 is required, but SoC is not HDCP2 fused!`
- `IOAV[%d] %s<0x%llx>::%s: DisplayRelease IPC failed with ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: %s -> %s (role=%u, supportsHPD=%u)\n`
- `IOAV[%d] %s<0x%llx>::%s: Vmax fail safe timer fired!\n`
- `IOAV[%d] %s<0x%llx>::%s: exit: ret=0x%08x, powerstate = %lx\n`
- `IOAV[%d] %s<0x%llx>::%s: _armIOProvider not found\n`
- `IOAV[%d] %s<0x%llx>::%s: super::handleStart() failed\n`
- `IOAV[%d] %s<0x%llx>::%s: called while dfp == NULL!\n`
- `IOAV[%d] %s<0x%llx>::%s: failed to attach UFP\n`
- `IOAV[%d] %s<0x%llx>::%s: enter: powerstate = %lx, current = %x\n`
- `IOAV[%d] %s<0x%llx>::%s: HDCP suppressed per -restore`
- `IOAV[%d] %s<0x%llx>::%s: failed to allocate IODPPortService\n`
- `IOAV[%d] %s<0x%llx>::%s: _socVmaxIndex = %u, socVmaxIndexCount = %zu, port = %u\n`
- `IOAV[%d] %s<0x%llx>::%s: enter: powerstate = %lx, _displayRequested = %u\n`
- `IOAV[%d] %s<0x%llx>::%s: ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: enter: %s -> %s (role=%u, supportsHPD=%u)\n`
- `IOAV[%d] %s<0x%llx>::%s: HDCP suppressed per ramrod_disable_sep_load`
- `IOAV[%d] %s<0x%llx>::%s: warning: Redundant DisplayRelease detected!\n`
- `IOAV[%d] %s<0x%llx>::%s: failed to init IODPPortService\n`
- `IOAV[%d] %s<0x%llx>::%s: Ignoring %s for Native PHY based DP port`
- `IOAV[%d] %s<0x%llx>::%s: %s SoC Vmax for dcp index %u\n`
- `IOAV[%d] %s<0x%llx>::%s: Failed to allocate command gate\n`
- `IOAV[%d] %s<0x%llx>::%s: Failed super::start\n`
- `IOAV[%d] %s<0x%llx>::%s: failed to start UFP\n`
- `IOAV[%d] %s<0x%llx>::%s: powerstate %lx -> %lx\n`
- `IOAV[%d] %s<0x%llx>::%s: runActionBlock ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: HDCP suppressed per disable-av-content-protection`
- `IOAV[%d] %s<0x%llx>::%s: HDCP suppressed per rd=md0`
- `IOAV[%d] %s<0x%llx>::%s: failed to init UFP\n`
- `IOAV[%d] %s<0x%llx>::%s: failed to set owner for UFP\n`
