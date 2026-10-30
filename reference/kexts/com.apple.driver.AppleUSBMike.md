# `com.apple.driver.AppleUSBMike`

- Name: AppleUSBMike
- Version: `1.0.0d1`
- UUID: `5F1C6E25-43F3-33A4-99D9-D3E5BF5F2726`
- Source version: `76.0.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.usb.AppleUSBCommon`](com.apple.driver.usb.AppleUSBCommon.md) 1.0, [`com.apple.iokit.IOAudio2Family`](com.apple.iokit.IOAudio2Family.md) 1.0, [`com.apple.iokit.IOUSBDeviceFamily`](com.apple.iokit.IOUSBDeviceFamily.md) 2.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0.0b2, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0.0b2, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (2) [KC]

### USB Mike
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBMike`
- `IOClass`: `AppleUSBMike`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBMike`
- `IOPropertyMatch`:
  - `USBDeviceFunction`: `USBAudioControl`
- `IOProviderClass`: `IOUSBDeviceInterface`

### USB Mike Streaming
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBMike`
- `IOClass`: `AppleUSBMike`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBMike`
- `IOPropertyMatch`:
  - `USBDeviceFunction`: `USBAudioStreaming`
- `IOProviderClass`: `IOUSBDeviceInterface`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleUSBMike` | 0x820 | IOAudio2Device → IOService → IORegistryEntry |
| `AppleUSBSampleBufferMonitor` | 0x28 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001c58 off=0x008db150-0x008dcda8 addr=0xfffffe00078df150-0xfffffe00078e0da8 r--/r--   __TEXT            
	sz=0x00000028 off=0x008db7c8-0x008db7f0 addr=0xfffffe00078df7c8-0xfffffe00078df7f0               __TEXT.__const            
	sz=0x00000cda off=0x008db7f0-0x008dc4ca addr=0xfffffe00078df7f0-0xfffffe00078e04ca               __TEXT.__cstring          (CstringLiterals)
	sz=0x000008de off=0x008dc4ca-0x008dcda8 addr=0xfffffe00078e04ca-0xfffffe00078e0da8               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00006278 off=0x02b4bef0-0x02b52168 addr=0xfffffe0009b4fef0-0xfffffe0009b56168 r-x/r-x   __TEXT_EXEC       
	sz=0x00005f18 off=0x02b4bef0-0x02b51e08 addr=0xfffffe0009b4fef0-0xfffffe0009b55e08          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000360 off=0x02b51e08-0x02b52168 addr=0xfffffe0009b55e08-0xfffffe0009b56168          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000150 off=0x049d18e8-0x049d1a38 addr=0xfffffe000b9d58e8-0xfffffe000b9d5a38 rw-/rw-   __DATA            
	sz=0x000000ec off=0x049d18e8-0x049d19d4 addr=0xfffffe000b9d58e8-0xfffffe000b9d59d4               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b9d59d8-0xfffffe000b9d5a38               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000b48 off=0x012aeff0-0x012afb38 addr=0xfffffe00082b2ff0-0xfffffe00082b3b38 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x012aeff0-0x012aeff8 addr=0xfffffe00082b2ff0-0xfffffe00082b2ff8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x012aeff8-0x012af000 addr=0xfffffe00082b2ff8-0xfffffe00082b3000         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000800 off=0x012af000-0x012af800 addr=0xfffffe00082b3000-0xfffffe00082b3800         __DATA_CONST.__const            
	sz=0x00000100 off=0x012af800-0x012af900 addr=0xfffffe00082b3800-0xfffffe00082b3900         __DATA_CONST.__kalloc_type      
	sz=0x000001b0 off=0x012af900-0x012afab0 addr=0xfffffe00082b3900-0xfffffe00082b3ab0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000088 off=0x012afab0-0x012afb38 addr=0xfffffe00082b3ab0-0xfffffe00082b3b38         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 125 at 0x04aec734
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     5F1C6E25-43F3-33A4-99D9-D3E5BF5F2726
008: LC_SOURCE_VERSION           76.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab7a58 size=0x68
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleUSBMike`
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBMike`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleUSBMike`
- `CFBundleNumericVersion`: `16785409`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.0d1`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.0d1`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleUSBMike.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896512688`
- `_PrelinkExecutableRelativePath`: `AppleUSBMike`
- `_PrelinkExecutableSize`: `35688`
- `_PrelinkExecutableSourceAddr`: `-2198896512688`
- `_PrelinkKmodInfo`: `-2198828394264`

## Strings (153) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `%s: %s::%s: buffer-debug enabled\n`
- `%s: %s::%s: super::start failed\n`
- `%s: %s::%s: IOAudio2Device::startIOEngine failed with error 0x%08x\n`
- `%s: %s::%s: newSampleRate %d currentSampleRate %d\n`
- `%s: %s::%s: estimated safety offset %d ms\n`
- `timestampWdtHandler`
- `AppleUSBSampleBufferMonitor`
- `12122`
- `site.AppleUSBMike`
- `device manufacturer`
- `output safety offset`
- `%s: %s::%s: kIOUSBDeviceInterfaceMessageTypeSetAlternateSetting - %d\n`
- `%s: %s::%s: invalid alternate setting %d\n`
- `stopIOEngine`
- `%s: %s::%s: ChangeSampleRate\n`
- `USBAudioControl`
- `AppleUSBMike`
- `12111112122212121212222111221122222222222212222222222221222222222222122222222222212222222222221222222222222122222222222212222222222221222222222222122222222222212222222222221222222222222122222222222212222222222221222222222222122222222222212211212112222222222121`
- `site.IOStatistics`
- `%s: %s::%s: Unable to allocate serializer\n`
- `transport type`
- `%s: %s::%s: received sample rate %d (%s)\n`
- `is valid`
- `%s: %s::%s: returning 0x%08x (status 0x%08x, rxSize %lld)\n`
- `%s: %s::%s: as AudioStreaming\n`
- `startIOEngine`
- `not valid`
- `AudioEnabled`
- `BufferChecksum`
- `%s: %s::%s: returned status 0x%08x\n`
- `%s: %s::%s: could not allocate sample buffer of %d samples\n`
- `Full`
- `%s: %s::%s: The new stream format is invalid\n`
- `EstSafetyOffset`
- `doTransfer`
- `%s: %s::%s: Sending a real timestamp - %lld\n`
- `%s: %s::%s: as AudioControl\n`
- `%s: %s::%s: failed to allocate statistics block\n`
- `%s: %s::%s: \n`
- `handleChangeSampleRate`
- `%s: %s::%s: ChangeStreamFormat\n`
- `FakeTimestamps`
- `%s: %s::%s: status 0x%08x totalSize %d pending %d IOs\n`
- `%s: %s::%s: Streaming silence (enabled: %d sample rate host: %d device: %d)\n`
- `%s: %s::%s: failed to allocate sample buffer lock\n`
- `output latency`
- `%s: %s::%s: kIOUSBDeviceInterfaceMessageTypeWasDeactivated\n`
- `%s: %s::%s: called (audioEnabled %d)\n`
- `helperChangeSampleRate`
- `resyncAudio`
- `%s: %s::%s: requesting config change after timestamp WDT\n`
- `completeAudioData`
- `AppleUSBMike-buffer-debug`
- `%s: %s::%s: invalid provider\n`
- `%s: %s::%s: finalizeConfiguration failed\n`
- `buffer-options`
- `%s: %s::%s: interface is not active, cannot startIOEngine\n`
- `%s: %s::%s: failed to resyncAudio 0x%08x\n`
- `%s: %s::%s: IOAudio2Device::stopIOEngine failed with error 0x%08x\n`
- `handleChangeStreamFormat`
- `%s: %s::%s: failed to allocate timestamp watchdog timer\n`
- `messageGated`
- `%s: %s::%s: called (_interfaceActive %d, audioEnabled %d)\n`
- `%s: %s::%s: PerformConfigChange done\n`
- `%s: %s::%s: resyncing audio\n`
- `HostSampleRate`
- `AudioSampleRate`
- `AudioIOs`
- `%s: %s::%s: _ioBufferOptions is 0x%08x\n`
- `MapperPageSize`
- `USB Audio Output`
- `SilentIOs`
- `%s: %s::%s: Sending real samples at rate %d\n`
- `%s: %s::%s: timestamp WDT fired\n`
- `%s: %s::%s: Sending a fake timestamp - %lld\n`
- `init`
- `%s: %s::%s: failed to create commandGate\n`
- `CurrentState`
- `Apple Computer, Inc.`
- `High`
- `%s: %s::%s: new sample rate %lld\n`
- `PendingIOs`
- `BufferDump`
- `ScatterGatherSupport`
- `%s: %s::%s: failed\n`
- `asyncWriteCompletion`
- `getAudioData`
- `AppleUSBMike-debug`
- `start`
- `device UID`
- `device name`
- `sample rate`
- `AltSetting`
- `%s: %s::%s: Unable to allocate silence buffer\n`
- `output streams`
- `performConfigChange`
- `site.AppleUSBSampleBufferMonitor`
- `%s: %s::%s: kIOUSBDeviceInterfaceMessageTypeWasActivated at %sspeed\n`
- `controlRequestCompleted`
- `StreamingSilence`
- `RealTimestamps`
- `%s: %s::%s: with status 0x%08x pending IO count %d\n`
- `%s: %s::%s: Sending silence after timestamp WDT\n`
- `io buffer frame size`
- `%s: %s::%s: returning 0x%08x\n`
- `USBDeviceFunction`

**[__TEXT.__os_log]**

- `%s: %s::%s: called (_interfaceActive %d, audioEnabled %d)\n`
- `%s: %s::%s: \n`
- `%s: %s::%s: received sample rate %d (%s)\n`
- `%s: %s::%s: newSampleRate %d currentSampleRate %d\n`
- `%s: %s::%s: status 0x%08x totalSize %d pending %d IOs\n`
- `%s: %s::%s: Sending real samples at rate %d\n`
- `%s: %s::%s: returned status 0x%08x\n`
- `%s: %s::%s: failed to allocate sample buffer lock\n`
- `%s: %s::%s: Unable to allocate serializer\n`
- `%s: %s::%s: IOAudio2Device::stopIOEngine failed with error 0x%08x\n`
- `%s: %s::%s: Sending a fake timestamp - %lld\n`
- `%s: %s::%s: failed to create commandGate\n`
- `%s: %s::%s: _ioBufferOptions is 0x%08x\n`
- `%s: %s::%s: failed to resyncAudio 0x%08x\n`
- `%s: %s::%s: The new stream format is invalid\n`
- `%s: %s::%s: ChangeSampleRate\n`
- `%s: %s::%s: with status 0x%08x pending IO count %d\n`
- `%s: %s::%s: Streaming silence (enabled: %d sample rate host: %d device: %d)\n`
- `%s: %s::%s: timestamp WDT fired\n`
- `%s: %s::%s: invalid provider\n`
- `%s: %s::%s: as AudioControl\n`
- `%s: %s::%s: as AudioStreaming\n`
- `%s: %s::%s: failed to allocate statistics block\n`
- `%s: %s::%s: failed to allocate timestamp watchdog timer\n`
- `%s: %s::%s: Unable to allocate silence buffer\n`
- `%s: %s::%s: returning 0x%08x\n`
- `%s: %s::%s: requesting config change after timestamp WDT\n`
- `%s: %s::%s: finalizeConfiguration failed\n`
- `%s: %s::%s: could not allocate sample buffer of %d samples\n`
- `%s: %s::%s: IOAudio2Device::startIOEngine failed with error 0x%08x\n`
- `%s: %s::%s: called (audioEnabled %d)\n`
- `%s: %s::%s: Sending a real timestamp - %lld\n`
- `%s: %s::%s: Sending silence after timestamp WDT\n`
- `%s: %s::%s: estimated safety offset %d ms\n`
- `%s: %s::%s: buffer-debug enabled\n`
- `%s: %s::%s: kIOUSBDeviceInterfaceMessageTypeSetAlternateSetting - %d\n`
- `%s: %s::%s: interface is not active, cannot startIOEngine\n`
- `%s: %s::%s: PerformConfigChange done\n`
- `%s: %s::%s: new sample rate %lld\n`
- `%s: %s::%s: super::start failed\n`
- `%s: %s::%s: failed\n`
- `%s: %s::%s: kIOUSBDeviceInterfaceMessageTypeWasActivated at %sspeed\n`
- `%s: %s::%s: invalid alternate setting %d\n`
- `%s: %s::%s: ChangeStreamFormat\n`
- `%s: %s::%s: returning 0x%08x (status 0x%08x, rxSize %lld)\n`
- `%s: %s::%s: resyncing audio\n`
- `%s: %s::%s: kIOUSBDeviceInterfaceMessageTypeWasDeactivated\n`
