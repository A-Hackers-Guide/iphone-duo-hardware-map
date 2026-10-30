# `com.apple.driver.DCPAVFamilyProxy`

- Name: DCPAVFamilyProxy
- Version: `1`
- UUID: `C293ECCB-E4DE-37BC-BA10-8BF8E2D535E5`
- Source version: `452.40.4.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleFirmwareKit`](com.apple.driver.AppleFirmwareKit.md) 1.0.0, [`com.apple.iokit.IOAVFamily`](com.apple.iokit.IOAVFamily.md) 1.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 14.0

## Device-tree nodes it binds (4) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/dp-audio0`](../devicetree/root__arm-io__dp-audio0.md) | `DCPAVAudioDMADelegate` | `dp-audio0` |
| [`/arm-io/dcp-sac-controller`](../devicetree/root__arm-io__dcp-sac-controller.md) | `DCPAVSACController` | `dcp-sac-controller` |
| [`/arm-io/dcpsec-sac-controller`](../devicetree/root__arm-io__dcpsec-sac-controller.md) | `DCPAVSACController` | `dcp-sac-controller` |
| [`/arm-io/dp-audio1`](../devicetree/root__arm-io__dp-audio1.md) | `DCPAVAudioDMADelegate` | `dp-audio1` |

## IOKit personalities (13) [KC]

### DCPAVAudioDMADelegate
- `CFBundleIdentifier`: `com.apple.driver.DCPAVFamilyProxy`
- `IOClass`: `DCPAVAudioDMADelegate`
- `IONameMatch`:
  - `dp-audio`
  - `dp-audio0`
  - `dp-audio1`
  - `dp-audio2`
  - `dp-audio3`
  - `dp-audio4`
  - `dp-audio5`
  - `dp-audio6`
  - `dp-audio7`
  - `dp-audio8`
  - `dp-audio9`
- `IOPersonalityPublisher`: `com.apple.driver.DCPAVFamilyProxy`
- `IOProviderClass`: `AppleARMIODevice`

### DCPAVAudioDriver
- `CFBundleIdentifier`: `com.apple.driver.DCPAVFamilyProxy`
- `IOClass`: `DCPAVAudioDriver`
- `IOPersonalityPublisher`: `com.apple.driver.DCPAVFamilyProxy`
- `IOProviderClass`: `DCPAVAudioInterfaceProxy`

### DCPAVAudioInterfaceProxy
- `CFBundleIdentifier`: `com.apple.driver.DCPAVFamilyProxy`
- `IOClass`: `DCPAVAudioInterfaceProxy`
- `IOPersonalityPublisher`: `com.apple.driver.DCPAVFamilyProxy`
- `IOPropertyMatch`:
  - `EPICName`: `dcpav-audio-interface-epic`
- `IOProviderClass`: `AFKEndpointInterface`

### DCPAVCECController
- `CFBundleIdentifier`: `com.apple.driver.DCPAVFamilyProxy`
- `IOClass`: `DCPAVCECController`
- `IOMatchCategory`: `CEC`
- `IONameMatch`: `cec-controller`
- `IOPersonalityPublisher`: `com.apple.driver.DCPAVFamilyProxy`
- `IOProviderClass`: `AppleARMIODevice`

### DCPAVCECInterfaceProxy
- `CFBundleIdentifier`: `com.apple.driver.DCPAVFamilyProxy`
- `IOClass`: `DCPAVCECInterfaceProxy`
- `IOPersonalityPublisher`: `com.apple.driver.DCPAVFamilyProxy`
- `IOPropertyMatch`:
  - `EPICName`: `dcpav-cec-interface-epic`
- `IOProviderClass`: `AFKEndpointInterface`

### DCPAVControllerProxy
- `CFBundleIdentifier`: `com.apple.driver.DCPAVFamilyProxy`
- `IOClass`: `DCPAVControllerProxy`
- `IOPersonalityPublisher`: `com.apple.driver.DCPAVFamilyProxy`
- `IOPropertyMatch`:
  - `EPICName`: `dcpav-controller-epic`
- `IOProviderClass`: `AFKEndpointInterface`

### DCPAVDeviceProxy
- `CFBundleIdentifier`: `com.apple.driver.DCPAVFamilyProxy`
- `IOClass`: `DCPAVDeviceProxy`
- `IOPersonalityPublisher`: `com.apple.driver.DCPAVFamilyProxy`
- `IOPropertyMatch`:
  - `EPICName`: `dcpav-device-epic`
- `IOProviderClass`: `AFKEndpointInterface`

### DCPAVPowerControllerProxy
- `CFBundleIdentifier`: `com.apple.driver.DCPAVFamilyProxy`
- `IOClass`: `DCPAVPowerControllerProxy`
- `IOPersonalityPublisher`: `com.apple.driver.DCPAVFamilyProxy`
- `IOPropertyMatch`:
  - `EPICName`: `dcpav-power-epic`
- `IOProviderClass`: `AFKEndpointInterface`

### DCPAVRemoteSACControllerProxy
- `CFBundleIdentifier`: `com.apple.driver.DCPAVFamilyProxy`
- `IOClass`: `DCPAVRemoteSACControllerProxy`
- `IOPersonalityPublisher`: `com.apple.driver.DCPAVFamilyProxy`
- `IOPropertyMatch`:
  - `EPICName`: `dcpav-sac-epic`
- `IOProviderClass`: `AFKEndpointInterface`

### DCPAVSACController
- `CFBundleIdentifier`: `com.apple.driver.DCPAVFamilyProxy`
- `IOClass`: `DCPAVSACController`
- `IONameMatch`:
  - `dcp-sac-controller`
  - `dcp0-sac-controller`
  - `dcp1-sac-controller`
- `IOPersonalityPublisher`: `com.apple.driver.DCPAVFamilyProxy`
- `IOProviderClass`: `IOService`

### DCPAVServiceProxy
- `CFBundleIdentifier`: `com.apple.driver.DCPAVFamilyProxy`
- `IOClass`: `DCPAVServiceProxy`
- `IOPersonalityPublisher`: `com.apple.driver.DCPAVFamilyProxy`
- `IOPropertyMatch`:
  - `EPICName`: `dcpav-service-epic`
- `IOProviderClass`: `AFKEndpointInterface`

### DCPAVVideoInterfaceProxy
- `CFBundleIdentifier`: `com.apple.driver.DCPAVFamilyProxy`
- `IOClass`: `DCPAVVideoInterfaceProxy`
- `IOPersonalityPublisher`: `com.apple.driver.DCPAVFamilyProxy`
- `IOPropertyMatch`:
  - `EPICName`: `dcpav-video-interface-epic`
- `IOProviderClass`: `AFKEndpointInterface`

### DCPFirmwareService
- `CFBundleIdentifier`: `com.apple.driver.AppleFirmwareKit`
- `IOClass`: `AFKFirmwareService`
- `IOPersonalityPublisher`: `com.apple.driver.DCPAVFamilyProxy`
- `IOPropertyMatch`:
  - `role`: `DCP`
- `IOProviderClass`: `RTBuddyService`


## C++ classes (19) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `DCPAVAudioDMADelegate` | 0x110 | IOAVAudioDMADelegate → IOService → IORegistryEntry |
| `DCPAVAudioDriver` | 0x258 | IOAVAudioDriver → IOAudio2Device → IOService → IORegistryEntry |
| `DCPAVAudioInterfaceProxy` | 0x670 | DCPAVProxy → IOService → IORegistryEntry |
| `DCPAVAudioInterfaceProxyUserClient` | 0x108 | IOAVAudioInterfaceUserClient → IOAVUserClient → IOUserClient → IOService → IORegistryEntry |
| `DCPAVCECController` | 0xf8 | IOService → IORegistryEntry |
| `DCPAVCECInterfaceProxy` | 0x658 | DCPAVProxy → IOService → IORegistryEntry |
| `DCPAVControllerProxy` | 0x638 | DCPAVProxy → IOService → IORegistryEntry |
| `DCPAVControllerProxyUserClient` | 0x108 | IOAVControllerUserClient → IOAVUserClient → IOUserClient → IOService → IORegistryEntry |
| `DCPAVDeviceProxy` | 0x618 | DCPAVProxy → IOService → IORegistryEntry |
| `DCPAVDeviceProxyUserClient` | 0x108 | IOAVDeviceUserClient → IOAVUserClient → IOUserClient → IOService → IORegistryEntry |
| `DCPAVPowerControllerProxy` | 0x610 | DCPAVProxy → IOService → IORegistryEntry |
| `DCPAVProxy` | 0x610 | IOService → IORegistryEntry |
| `DCPAVRemotePowerController` | 0xa0 | IOService → IORegistryEntry |
| `DCPAVRemoteSACControllerProxy` | 0x618 | DCPAVProxy → IOService → IORegistryEntry |
| `DCPAVSACController` | 0x120 | IOService → IORegistryEntry |
| `DCPAVServiceProxy` | 0x618 | DCPAVProxy → IOService → IORegistryEntry |
| `DCPAVServiceProxyUserClient` | 0x108 | IOAVServiceUserClient → IOAVUserClient → IOUserClient → IOService → IORegistryEntry |
| `DCPAVVideoInterfaceProxy` | 0x620 | DCPAVProxy → IOService → IORegistryEntry |
| `DCPAVVideoInterfaceProxyUserClient` | 0x108 | IOAVVideoInterfaceUserClient → IOAVUserClient → IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1720)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000404d off=0x009120e0-0x0091612d addr=0xfffffe00079160e0-0xfffffe000791a12d r--/r--   __TEXT            
	sz=0x00000278 off=0x00912800-0x00912a78 addr=0xfffffe0007916800-0xfffffe0007916a78               __TEXT.__const            
	sz=0x00002461 off=0x00912a78-0x00914ed9 addr=0xfffffe0007916a78-0xfffffe0007918ed9               __TEXT.__cstring          (CstringLiterals)
	sz=0x00001254 off=0x00914ed9-0x0091612d addr=0xfffffe0007918ed9-0xfffffe000791a12d               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x000162bc off=0x02c13f30-0x02c2a1ec addr=0xfffffe0009c17f30-0xfffffe0009c2e1ec r-x/r-x   __TEXT_EXEC       
	sz=0x00015c9c off=0x02c13f30-0x02c29bcc addr=0xfffffe0009c17f30-0xfffffe0009c2dbcc          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000620 off=0x02c29bcc-0x02c2a1ec addr=0xfffffe0009c2dbcc-0xfffffe0009c2e1ec          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000003d8 off=0x049db550-0x049db928 addr=0xfffffe000b9df550-0xfffffe000b9df928 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049db550-0x049db618 addr=0xfffffe000b9df550-0xfffffe000b9df618               __DATA.__data             
	sz=0x00000308 off=0x00000000-0x00000308 addr=0xfffffe000b9df618-0xfffffe000b9df920               __DATA.__common           (Zerofill)
	sz=0x00000008 off=0x00000000-0x00000008 addr=0xfffffe000b9df920-0xfffffe000b9df928               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x000091f0 off=0x012c9028-0x012d2218 addr=0xfffffe00082cd028-0xfffffe00082d6218 rw-/rw-   __DATA_CONST      
	sz=0x00000098 off=0x012c9028-0x012c90c0 addr=0xfffffe00082cd028-0xfffffe00082cd0c0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000098 off=0x012c90c0-0x012c9158 addr=0xfffffe00082cd0c0-0xfffffe00082cd158         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00008690 off=0x012c9158-0x012d17e8 addr=0xfffffe00082cd158-0xfffffe00082d57e8         __DATA_CONST.__const            
	sz=0x000004c0 off=0x012d17e8-0x012d1ca8 addr=0xfffffe00082d57e8-0xfffffe00082d5ca8         __DATA_CONST.__kalloc_type      
	sz=0x00000140 off=0x012d1ca8-0x012d1de8 addr=0xfffffe00082d5ca8-0xfffffe00082d5de8         __DATA_CONST.__kalloc_var       
	sz=0x00000310 off=0x012d1de8-0x012d20f8 addr=0xfffffe00082d5de8-0xfffffe00082d60f8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000120 off=0x012d20f8-0x012d2218 addr=0xfffffe00082d60f8-0xfffffe00082d6218         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 232 at 0x04aede2c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     C293ECCB-E4DE-37BC-BA10-8BF8E2D535E5
008: LC_SOURCE_VERSION           452.40.4.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab9140 size=0x480
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `DCPAVFamilyProxy`
- `CFBundleIdentifier`: `com.apple.driver.DCPAVFamilyProxy`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `DCPAVFamilyProxy`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
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
- `NSHumanReadableCopyright`: `Copyright © 2019-2021 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/DCPAVFamilyProxy.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896287520`
- `_PrelinkExecutableRelativePath`: `DCPAVFamilyProxy`
- `_PrelinkExecutableSize`: `145617`
- `_PrelinkExecutableSourceAddr`: `-2198896287520`
- `_PrelinkKmodInfo`: `-2198828354224`

## Strings (283) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__os_log]**

- `IOAV[%d] %s<0x%llx>::%s: Command range verification failed!`
- `IOAV[%d] %s<0x%llx>::%s: Could not create the CEC Service\n`
- `IOAV[%d] %s<0x%llx>::%s: openGated failed, ret=0x%x\n`
- `IOAV[%d] %s<0x%llx>::%s: getTransport error, rc=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: warning: commandSleep(&_cecTransactionInProgress) ret=0x%08x (ignored)`
- `IOAV[%d] %s<0x%llx>::%s: enqueueResponse failed, ret=%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: IOAVAudioElement::elementArrayWithPropertyList() failed, returning null\n`
- `IOAV[%d] %s<0x%llx>::%s: waitForClose() failed, ret=0x%08x`
- `IOAV[%d] %s<0x%llx>::%s: Message size verification failed!`
- `IOAV[%d] %s<0x%llx>::%s: enter: powerstate = %lx, current = %x\n`
- `IOAV[%d] %s<0x%llx>::%s: cecInterfaceTerminateGated failed, ret=%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: initDataTransfers failed, ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: message failed, ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: Magic verification failed!`
- `IOAV[%d] %s<0x%llx>::%s: Variable payload verification failed!`
- `IOAV[%d] %s<0x%llx>::%s: Failed to allocate command gate\n`
- `IOAV[%d] %s<0x%llx>::%s: runActionBlock ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: _delegateService is not available`
- `IOAV[%d] %s<0x%llx>::%s: Can't find audio nub\n`
- `IOAV[%d] %s<0x%llx>::%s: delegate has wrong type?!\n`
- `IOAV[%d] %s<0x%llx>::%s: registration complete\n`
- `IOAV[%d] %s<0x%llx>::%s: Fixed payload verification failed!`
- `IOAV[%d] %s<0x%llx>::%s: unexpected type returned from DCPAVAudioInterfaceProxy::retrieveEDIDUUID(): %s\n`
- `IOAV[%d] %s<0x%llx>::%s: enqueueResponse failed, rc=%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: exit: powerstate = %lx, _controllerPowered = %u, ret=0x%08x%s\n`
- `IOAV[%d] %s<0x%llx>::%s: removeCECService failed\n`
- `IOAV[%d] %s<0x%llx>::%s: waiting for power state change -> powerstate = %lx...\n`
- `IOAV[%d] %s<0x%llx>::%s: _cecService termination failed\n`
- `IOAV[%d] %s<0x%llx>::%s: IOAVAudioElement::elementArrayWithPropertyList() produced empty array, returning null\n`
- `IOAV[%d] %s<0x%llx>::%s: powerstate %lx -> %lx, capabilities=%lx thisDevice?=%d\n`
- `IOAV[%d] %s<0x%llx>::%s: failed to get PMRootDomain!\n`
- `IOAV[%d] %s<0x%llx>::%s: cecInterfacePublishedGated failed, ret=%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: setCECInterface failed ret=%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: warning: out-of-order termination _cecInterface(0x%llx) != terminatedService(0x%llx)\n`
- `IOAV[%d] %s<0x%llx>::%s: unexpected type returned from DCPAVAudioInterfaceProxy::retrieveChannelLayoutElements(): %s\n`
- `IOAV[%d] %s<0x%llx>::%s: exit: powerstate = %lx, isOpen()=%u, ret=0x%08x%s\n`
- `IOAV[%d] %s<0x%llx>::%s: ok=%d, _dpAudioDevice=%s NULL, _audioDMADelegate=%s NULL\n`
- `IOAV[%d] %s<0x%llx>::%s: closeGated failed, ret=0x%x\n`
- `IOAV[%d] %s<0x%llx>::%s: Handler verification failed!`
- `IOAV[%d] %s<0x%llx>::%s: powerstate %lx -> %lx\n`
- `IOAV[%d] %s<0x%llx>::%s: ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: registerInterestedDriver() failed!\n`
- `IOAV[%d] %s<0x%llx>::%s: Unable to cast service \"%s\" to IOAVCECInterface\n`
- `IOAV[%d] %s<0x%llx>::%s: ok=%d\n`
- `IOAV[%d] %s<0x%llx>::%s: createObjectFromSerializedData(&DCPAVAudioInterfaceProxy::retrieveElements) ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: exit: ret=0x%08x, powerstate = %lx\n`
- `IOAV[%d] %s<0x%llx>::%s: enter: powerstate = %lx, _controllerPowered = %u\n`
- `IOAV[%d] %s<0x%llx>::%s: getLinkStatus error, rc=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: Can't find audio device\n`
- `IOAV[%d] %s<0x%llx>::%s: unexpected type returned from DCPAVAudioInterfaceProxy::retrieveElements(): %s\n`
- `IOAV[%d] %s<0x%llx>::%s: unexpected type returned from DCPAVAudioInterfaceProxy::retrieveProductAttributes(): %s\n`
- `IOAV[%d] %s<0x%llx>::%s: createObjectFromSerializedData(&DCPAVAudioInterfaceProxy::retrieveEDIDUUID) ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: audio DMA failed to open\n`
- `IOAV[%d] %s<0x%llx>::%s: Ambiguous power assertion settings!\n`
- `IOAV[%d] %s<0x%llx>::%s: isOpen=%d\n`
- `IOAV[%d] %s<0x%llx>::%s: %s Processed %s<%x>\n`
- `IOAV[%d] %s<0x%llx>::%s: Unable to allocate matchingDict\n`
- `IOAV[%d] %s<0x%llx>::%s: Unable to attach CEC Service\n`
- `IOAV[%d] %s<0x%llx>::%s: createObjectFromSerializedData(&DCPAVAudioInterfaceProxy::retrieveChannelLayoutElements) ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: createObjectFromSerializedData(&DCPAVAudioInterfaceProxy::retrieveProductAttributes) ret=0x%08x\n`
- `IOAV[%d] %s<0x%llx>::%s: runActionBlock ret=0x%08x (ignored)\n`
- `IOAV[%d] %s<0x%llx>::%s: dispatch failed, ret=0x%08x\n`

**[__TEXT.__cstring]**

- `unexpected type returned from DCPAVAudioInterfaceProxy::retrieveEDIDUUID(): %s\n`
- `registration complete\n`
- `synchronousChangePowerStateTo`
- `\"%s: failed to create SAC aggressor function for lcd index %u\\n\" @%s:%d`
- `_registerSACAggressor`
- `AppleAgileDPDisplaySetCDIIndexCommand`
- `value for key '%s' is not a number!\n`
- `site.DCPAVVideoInterfaceProxy`
- `DCPAVVideoInterfaceProxyUserClient`
- `createObjectFromSerializedData(&DCPAVAudioInterfaceProxy::retrieveElements) ret=0x%08x\n`
- `enqueueResponse failed, ret=%08x\n`
- `powerStateWillChangeTo_block_invoke`
- `1211111212221212112222211112111111`
- `DCPAVSACController`
- `function-saca_lcd2`
- `1211111212221212112222211111112`
- `Unable to allocate matchingDict\n`
- `cecInterfacePublishedGated failed, ret=%08x\n`
- `Location`
- `close`
- `IOUserClientClass`
- `site.DCPAVRemoteSACControllerProxy`
- `121111121222121212122221112211222222111112222122111112222222222222222222221`
- `audio`
- `prepareLink`
- `copyElements`
- `powerChangeDone_block_invoke`
- `ret=0x%08x\n`
- `\"%s Could not create lock\" @%s:%d`
- `\"%s aggressor count mismatch after hibernation. registered count = %u, new count = %u\\n\" @%s:%d`
- `createObjectFromSerializedData(&DCPAVAudioInterfaceProxy::retrieveChannelLayoutElements) ret=0x%08x\n`
- `createObjectFromSerializedData(&DCPAVAudioInterfaceProxy::retrieveProductAttributes) ret=0x%08x\n`
- `site.DCPAVAudioInterfaceProxyUserClient`
- `12111112122212121122222112212211112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121222111111211112`
- `createObjectFromSerializedData(&DCPAVAudioInterfaceProxy::retrieveEDIDUUID) ret=0x%08x\n`
- `handleOpen`
- `audio DMA failed to open\n`
- `enqueueResponse failed, rc=%08x\n`
- `v64@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8^{AFKEndpointInterface=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInt`
- `initDataTransfers failed, ret=0x%08x\n`
- `copyChannelLayoutElements`
- `%s error: ret = %s\n`
- `cecInterfaceTerminateGated`
- `closeGated`
- `copyProductAttributes`
- `External`
- `IODeviceTree`
- `powerstate %lx -> %lx\n`
- `DCPAVRemoteSACControllerProxy failed to start\n`
- `static void DCPAVRemoteSACControllerProxy::handleRegisterSACAggressor(DCPAVRemoteSACControllerProxy * _Nonnull, const DCPAVIPC::Message * _Nonnull)`
- `site.DCPAVAudioDriver`
- `unexpected type returned from DCPAVAudioInterfaceProxy::retrieveChannelLayoutElements(): %s\n`
- `handleMessage`
- `DCPAVControllerProxy`
- `enter: powerstate = %lx, _controllerPowered = %u\n`
- `DCPAVControllerProxyUserClient`
- `warning: out-of-order termination _cecInterface(0x%llx) != terminatedService(0x%llx)\n`
- `DCPAVServiceProxyUserClient`
- `1211111212221212112222211221221111212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112122211`
- `site.DCPAVCECInterfaceProxy`
- `DCPAVProxy`
- `EPICLocation`
- `runActionBlock ret=0x%08x (ignored)\n`
- `\"%s OOB access\" @%s:%d`
- `DCPAVDeviceProxy`
- `site.DCPAVCECController`
- `12111112122212121122222112212211112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121222111121111`
- `EDIDCallback`
- `exit: powerstate = %lx, _controllerPowered = %u, ret=0x%08x%s\n`
- `site.DCPAVAudioDMADelegate`
- `site.UInt64`
- `cecInterfacePublishedGated`
- `DCPAVAudioDriver`
- `IOReturn DCPAVRemoteSACControllerProxy::bootCompleteGated()`
- `12111112122212121122222112212211112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121222`
- `v60@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8^{AFKEndpointInterface=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInt`
- `failed to create proxy interest notifier; proxy terminated?\n`
- `function-saca_lcd1`
- `AppleAgileDPDisplaySetEDPIndexCommand`
- `site.DCPAVDeviceProxyUserClient`
- `SetRemoteDevicePower`
- `openGated failed, ret=0x%x\n`
- `validateMessage`
- `Failed to allocate command gate\n`
- `powerStateWillChangeTo`
- `agile clocking is not enabled\n`
- `\"%s unsupported lcd index %u\\n\" @%s:%d`
- `site.DCPAVServiceProxy`
- `Unable to attach CEC Service\n`
- `enter: powerstate = %lx, current = %x\n`
- `DCPAVAudioDMADelegate`
- `display-sac`
- `Failed to select aggressor index %d for LCD %d\n`
- `site.DCPAVDeviceProxy`
- `setCECInterface failed ret=%08x\n`
- `cecInterfaceTerminate`
- `NOT`
- `recvMessageThreadCallFunc`
- `closeGated failed, ret=0x%x\n`
- `Handler verification failed!`
- `site.DCPAVControllerProxy`
- `SendDisplayMessage`
- `121111121222121211222221122122111121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212221`
- `site.DCPAVRemotePowerController`
- `virtual bool DCPAVRemotePowerController::start(IOService *)`
- `Ambiguous power assertion settings!\n`
- `waitForPowerChangeDone`
- `DCPAVRemoteSACControllerProxy.cpp`
- `removeCECService failed\n`
- `IOAVControlInterface`
- `function-device_reset_dpa`
- `IOAVAudioElement::elementArrayWithPropertyList() failed, returning null\n`
- `IOAVAudioElement::elementArrayWithPropertyList() produced empty array, returning null\n`
- `DCPAVRemoteSACControllerProxy`
- `DCPAVCECController`
- `site.DCPAVServiceProxyUserClient`
- `HPDCallback`
- `Command range verification failed!`
- `IOReturn DCPAVRemoteSACControllerProxy::selectSACAggressorIndexGated(UInt32 * _Nonnull, UInt32 * _Nonnull)`
- `DCPAVServiceProxy`
- `addCECService`
- `ok=%d, _dpAudioDevice=%s NULL, _audioDMADelegate=%s NULL\n`
- `message failed, ret=0x%08x\n`
- `copyEDIDUUID`
- `ForwardMessage`
- `1211111212221212112222211221221111212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112121121211212112122211121`
- `RequiresCommandDelegate`
- `registerInterestedDriver() failed!\n`
- `failed to create serializer for Power\n`
- `warning: commandSleep(&_cecTransactionInProgress) ret=0x%08x (ignored)`
- `IOAVAudioInterfaceUserInterfaceSupported`
- `completeLink`
- `Unit`
- `powerChangeDone`
- `121111121222121211111112221222122212`
- `virtual bool DCPAVSACController::start(IOService *)`
- `\"failed to create _setSACIndexAsyncEventSource\" @%s:%d`
- `cec_interface_mask`
- `IOAVAudioDMADelegate`
- `waitForClose() failed, ret=0x%08x`
- `site.DCPAVProxy`
- `EPICUnit`
- `sendDisplayMessage`
- `site.DCPAVControllerProxyUserClient`
- `site.UInt32`
- `cec_interface_level`
- `DCPAVAudioInterfaceProxy`
- ` (ignored)`
- `%s_lcd%u`
- `\"%s proxy mismatch\\n\" @%s:%d`
- `_cecService termination failed\n`
- `dispatch failed, ret=0x%08x\n`
- `DCPAVPowerControllerProxy`
- `site.DCPAVPowerControllerProxy`
- `i8@?0`
- `close_block_invoke`
- `Message size verification failed!`
- `start`
- `\"super::start() failed\" @%s:%d`
- `function-saca_lcd0`
- `cecInterfacePublished`
- `IOAVVideoInterface`
- `__sendMessage`
- `exit: ret=0x%08x, powerstate = %lx\n`
- `function-saca`
- `\"Unexpected: invalid aggressor LCD index\" @%s:%d`
- `Unable to cast service \"%s\" to IOAVCECInterface\n`
- `FrameReceiveCallback`
- `site.DCPAVAudioInterfaceProxy`
- `DCPAVRemotePowerController`
- `open`
- `isOpen=%d\n`
- `Could not create the CEC Service\n`
- `getLinkStatus error, rc=0x%08x\n`
- `getTransport`
- `Can't find audio nub\n`
- `Can't find audio device\n`
- `unexpected type returned from DCPAVAudioInterfaceProxy::retrieveProductAttributes(): %s\n`
- `handleCommand`
- `v56@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8^{AFKEndpointInterface=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInt`
- `Terminate`
- `\"failed to add _setDisplayAsyncEventSource to work loop\" @%s:%d`
- `\"_setSACIndexAsyncEventSource->signal() failed: 0x%08x (%s)\\n\" @%s:%d`
- `AppleAgileDPDisplaySetPCONIndexCommand`
- `RegisterSACAggressor`
- `getLinkStatus`
- `Variable payload verification failed!`
- `powerstate %lx -> %lx, capabilities=%lx thisDevice?=%d\n`
- `_delegateService is not available`
- `DCPAVSACController.cpp`
- `DCPAVDeviceProxyUserClient`
- `delegate has wrong type?!\n`
- `IOAVAudioInterface`
- `exit: powerstate = %lx, isOpen()=%u, ret=0x%08x%s\n`
- `Magic verification failed!`
- `Fixed payload verification failed!`
- `IOReturn DCPAVSACController::_registerSACAggressor(DCPAVRemoteSACControllerProxy *, UInt32, UInt32, const UInt64 *, const UInt32 *)`
- `DCPAVVideoInterfaceProxy`
- `ok=%d\n`
- `waitForClose`
- `DCPAVAudioInterfaceProxyUserClient`
- `12111112122212121111`
- `waiting for power state change -> powerstate = %lx...\n`
- `setPowerState_block_invoke`
- `DCP`
- `\"failed to create work loop\" @%s:%d`
- `removeCECService`
- `IOReturn DCPAVRemotePowerController::_setRemoteDevicePower(DCPAVPowerControllerProxy *, UInt32, UInt32)`
- `%s Processed %s<%x>\n`
- `role`
- `DCPAVRemotePowerController.cpp`
- `121111121222121211111111111112111`
- `site.DCPAVSACController`
- `DCPAVCECInterfaceProxy`
- `Power`
- `cecInterfaceTerminateGated failed, ret=%08x\n`
- `runActionBlock ret=0x%08x\n`
- `failed to get PMRootDomain!\n`
- `getTransport error, rc=0x%08x\n`
- `site.DCPAVVideoInterfaceProxyUserClient`
- `unexpected type returned from DCPAVAudioInterfaceProxy::retrieveElements(): %s\n`
