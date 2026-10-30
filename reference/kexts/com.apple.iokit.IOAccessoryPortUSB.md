# `com.apple.iokit.IOAccessoryPortUSB`

- Name: IOAccessoryPortUSB
- Version: `1.0.0`
- UUID: `AC474E74-CF6D-38F1-A9FD-1E07BE97EFB2`
- Source version: `1068.40.6.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleOnboardSerial`](com.apple.driver.AppleOnboardSerial.md) 1.0, [`com.apple.iokit.IOAccessoryManager`](com.apple.iokit.IOAccessoryManager.md) 1.0.0, [`com.apple.iokit.IOSerialFamily`](com.apple.iokit.IOSerialFamily.md) 1.0.4, [`com.apple.iokit.IOUSBDeviceFamily`](com.apple.iokit.IOUSBDeviceFamily.md) 2.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### IAP USB Port
- `CFBundleIdentifier`: `com.apple.iokit.IOAccessoryPortUSB`
- `IOAccessoryDevicePort`: `2`
- `IOClass`: `IOAccessoryPortUSB`
- `IOPersonalityPublisher`: `com.apple.iokit.IOAccessoryPortUSB`
- `IOPropertyMatch`:
  - `USBDeviceFunction`: `IapOverUsbHid`
- `IOProviderClass`: `IOUSBDeviceInterface`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOAccessoryPortUSB` | 0xf0 | IOAccessoryPort → IOAccessoryTransport → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1400)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000c29 off=0x009bc440-0x009bd069 addr=0xfffffe00079c0440-0xfffffe00079c1069 r--/r--   __TEXT            
	sz=0x00000651 off=0x009bca18-0x009bd069 addr=0xfffffe00079c0a18-0xfffffe00079c1069               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x0000276c off=0x0305c840-0x0305efac addr=0xfffffe000a060840-0xfffffe000a062fac r-x/r-x   __TEXT_EXEC       
	sz=0x0000248c off=0x0305c840-0x0305eccc addr=0xfffffe000a060840-0xfffffe000a062ccc          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000002e0 off=0x0305eccc-0x0305efac addr=0xfffffe000a062ccc-0xfffffe000a062fac          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000258 off=0x049ee8c8-0x049eeb20 addr=0xfffffe000b9f28c8-0xfffffe000b9f2b20 rw-/rw-   __DATA            
	sz=0x0000020a off=0x049ee8c8-0x049eead2 addr=0xfffffe000b9f28c8-0xfffffe000b9f2ad2               __DATA.__data             
	sz=0x00000048 off=0x00000000-0x00000048 addr=0xfffffe000b9f2ad8-0xfffffe000b9f2b20               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000840 off=0x0134c360-0x0134cba0 addr=0xfffffe0008350360-0xfffffe0008350ba0 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x0134c360-0x0134c368 addr=0xfffffe0008350360-0xfffffe0008350368         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x0134c368-0x0134c370 addr=0xfffffe0008350368-0xfffffe0008350370         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000640 off=0x0134c370-0x0134c9b0 addr=0xfffffe0008350370-0xfffffe00083509b0         __DATA_CONST.__const            
	sz=0x00000040 off=0x0134c9b0-0x0134c9f0 addr=0xfffffe00083509b0-0xfffffe00083509f0         __DATA_CONST.__kalloc_type      
	sz=0x00000170 off=0x0134c9f0-0x0134cb60 addr=0xfffffe00083509f0-0xfffffe0008350b60         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000040 off=0x0134cb60-0x0134cba0 addr=0xfffffe0008350b60-0xfffffe0008350ba0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 100 at 0x04af0828
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     AC474E74-CF6D-38F1-A9FD-1E07BE97EFB2
008: LC_SOURCE_VERSION           1068.40.6.0.0
009: LC_FUNCTION_STARTS          offset=0x004abdbd8 size=0x48
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `IOAccessoryPortUSB`
- `CFBundleIdentifier`: `com.apple.iokit.IOAccessoryPortUSB`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOAccessoryPortUSB`
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
- `NSHumanReadableCopyright`: `Copyright © 2019 Apple Inc. All rights reserved.`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOAccessoryPortUSB.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895590336`
- `_PrelinkExecutableRelativePath`: `IOAccessoryPortUSB`
- `_PrelinkExecutableSize`: `15917`
- `_PrelinkExecutableSourceAddr`: `-2198895590336`
- `_PrelinkKmodInfo`: `-2198828275512`

## Strings (51) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `usb-role-switch-delay-ms`
- `free`
- `%s::%s unknown request 0x%x bmReqType 0x%x configured(%d,%d)\n`
- `message`
- `%s::%s ignoreVBUS, pending role switch NOT cancelled\n`
- `IOAccessoryPortUSBRoleSwitchMaskValue`
- `IOAccessoryPortUSBRoleSwitchMaskIndex`
- `site.IOAccessoryPortUSB`
- `%s::%s error - no data\n`
- `%s::%s Ignore vbus drop active for %d ms \n`
- `%s::%s Starting role switch... (_roleSwitchDelayMS: %u)\n`
- `%s::%s role switch already scheduled\n`
- `%s::%s: %s: received usb speed = %s\n`
- `%s::%s could not create thread call\n`
- `%s::%s bad argument\n`
- `USB role switch configureUSBMode() failed %#x\n`
- `ignoreVbusDropThreadCall`
- `hs`
- `fs`
- `%s::%s could not create workloop\n`
- `%s::%s buffer was invalid (NULL)!\n`
- `acc_debug`
- `%s::%s _ignoreVbusDropThreadCall already scheduled\n`
- `%s::%s explicit stall bmReqType 0x%x, bmReq 0x%x configured(%d,%d)\n`
- `stop`
- `transmitDataGated`
- `%s::%s buffer was too small (%llu bytes)!\n`
- `%s::%s Ignore vbus drop was disabled\n`
- `%s::%s: %s: Request 0x%02x Index %d Value %d wLen %d bmReqType 0x%x configured(%d,%d)\n`
- `%s::%s role switch status 0x%x bmReqType 0x%x configured(%d,%d)\n`
- `%s::%s Index %d Value %d\n`
- `IOAccessoryPortUSB`
- `%s::%s could not create command gate\n`
- `%s::%s Invalid data for %s!`
- `function-ignore_vbus_drop`
- `waitSendDone`
- `%s::%s get supported cap mask status 0x%x bmReqType 0x%x configured(%d,%d)\n`
- `receiveNotification`
- `%s::%s: %s: received usb detach\n`
- `%s::%s\n`
- `start`
- `%s::%s createPipe failed for alternateSetting %d\n`
- `controlReceiveCompletion`
- `controlRequest`
- `(no provider)`
- `setUSBRoleSwitchMask`
- `%s::%s pending role switch cancelled\n`
- `acc_ignore_vbus_drop_window_ms`
- `acc_roleswap_delayms`
- `%s::%s error sending data (0x%x)\n`
- `121111121222121211111111221112`
