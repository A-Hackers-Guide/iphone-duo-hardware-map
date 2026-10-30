# `com.apple.iokit.AppleARMIISAudio`

- Name: AppleARMIISAudio
- Version: `610.2`
- UUID: `5018E8A2-797F-36C4-9C2E-60D61303CB39`
- Source version: `610.2.0.0.0`
- Depends on: [`com.apple.driver.AppleEmbeddedAudioLibs`](com.apple.driver.AppleEmbeddedAudioLibs.md) 1.0, [`com.apple.driver.IISAudioIsolatedStreamECProxy`](com.apple.driver.IISAudioIsolatedStreamECProxy.md) 1.0, [`com.apple.iokit.IOAudio2Family`](com.apple.iokit.IOAudio2Family.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleARMDMAAudioDevice` | 0x1c8 | IOAudio2Device → IOService → IORegistryEntry |
| `AppleARMIISAudioDevice` | 0x258 | AppleARMDMAAudioDevice → IOAudio2Device → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1720)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000063b8 off=0x001634d0-0x00169888 addr=0xfffffe00071674d0-0xfffffe000716d888 r--/r--   __TEXT            
	sz=0x000029d7 off=0x00163be8-0x001665bf addr=0xfffffe0007167be8-0xfffffe000716a5bf               __TEXT.__os_log           
	sz=0x00003218 off=0x001665bf-0x001697d7 addr=0xfffffe000716a5bf-0xfffffe000716d7d7               __TEXT.__cstring          (CstringLiterals)
	sz=0x000000a8 off=0x001697e0-0x00169888 addr=0xfffffe000716d7e0-0xfffffe000716d888               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00014b70 off=0x016bf7a0-0x016d4310 addr=0xfffffe00086c37a0-0xfffffe00086d8310 r-x/r-x   __TEXT_EXEC       
	sz=0x00014540 off=0x016bf7a0-0x016d3ce0 addr=0xfffffe00086c37a0-0xfffffe00086d7ce0          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000630 off=0x016d3ce0-0x016d4310 addr=0xfffffe00086d7ce0-0xfffffe00086d8310          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000208 off=0x0492f3d0-0x0492f5d8 addr=0xfffffe000b9333d0-0xfffffe000b9335d8 rw-/rw-   __DATA            
	sz=0x000001a8 off=0x0492f3d0-0x0492f578 addr=0xfffffe000b9333d0-0xfffffe000b933578               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b933578-0xfffffe000b9335d8               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000019f0 off=0x00faad68-0x00fac758 addr=0xfffffe0007faed68-0xfffffe0007fb0758 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x00faad68-0x00faad78 addr=0xfffffe0007faed68-0xfffffe0007faed78         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x00faad78-0x00faad88 addr=0xfffffe0007faed78-0xfffffe0007faed88         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001160 off=0x00faad88-0x00fabee8 addr=0xfffffe0007faed88-0xfffffe0007fafee8         __DATA_CONST.__const            
	sz=0x00000240 off=0x00fabee8-0x00fac128 addr=0xfffffe0007fafee8-0xfffffe0007fb0128         __DATA_CONST.__kalloc_type      
	sz=0x00000280 off=0x00fac128-0x00fac3a8 addr=0xfffffe0007fb0128-0xfffffe0007fb03a8         __DATA_CONST.__kalloc_var       
	sz=0x00000318 off=0x00fac3a8-0x00fac6c0 addr=0xfffffe0007fb03a8-0xfffffe0007fb06c0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000090 off=0x00fac6c0-0x00fac750 addr=0xfffffe0007fb06c0-0xfffffe0007fb0750         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000008 off=0x00fac750-0x00fac758 addr=0xfffffe0007fb0750-0xfffffe0007fb0758         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 216 at 0x04ad1a48
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     5018E8A2-797F-36C4-9C2E-60D61303CB39
008: LC_SOURCE_VERSION           610.2.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004a97140 size=0x1f0
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleARMIISAudio`
- `CFBundleIdentifier`: `com.apple.iokit.AppleARMIISAudio`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleARMIISAudio`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `610.2`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `610.2`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2022 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleARMIISAudio.kext`
- `_PrelinkExecutableLoadAddr`: `-2198904343344`
- `_PrelinkExecutableRelativePath`: `AppleARMIISAudio`
- `_PrelinkExecutableSize`: `117536`
- `_PrelinkExecutableSourceAddr`: `-2198904343344`
- `_PrelinkKmodInfo`: `-2198829059120`

## Strings (417) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `Causal Count`
- `%s %s:%d stopDataTransfers failed for bufferIndex=%d ret=%s(%#x)\n`
- `%s:%s create injection control failed\n`
- `%s::%s:%d startByteCount cannot be zero. Overriding startByteCount with byteCount. direction=%#x byteCount=%lld startByteCount=%lld theAnswer=%s(%#x).\n`
- `stopIOEngineInternal`
- `\"%s: mismatched bytes per frame: input %lu output %lu\" @%s:%d`
- `zeroFillBufferForStreamID`
- `input stream injection`
- `extra-input-latency`
- `221112222`
- `IOReporters`
- `%s:%s setTransportSampleRate failed. inSampleRate=%lld currentSR=%lld ret=%s(%#x)\n`
- `%s:%s Failed to add mBidirInAheadOfOutHistogramReporter to legend. result=%s(%#x)\n`
- `site.AppleLEAPAudioStreamFormatter`
- `setTransportSampleRate`
- `%s:%s failed for %d. ret=%s(%#x)\n`
- `121111121222121212122221112211221222111221111111111111122111111222111121112`
- `Approximate samplerate`
- `%s:%s setDeviceFormat failed for kIODirectionIn. ret=%s(%#x) bufferIndex=%d validDirection=%#x inputChannels=%#x, bitsPerChannel=%d\n`
- `%s::%s [%u] unable to get phandle at index=%d [NumPhandles=%d]\n`
- `site.TransferData`
- `%s: Clearing buffer because audio client IO has fallen behind (I: %llu, O: %llu)\n`
- `setAudioFormat`
- `%s: User supplied safety offset is zero.\n`
- `safety-offset-seed-us`
- `\"%s::%s [%u] unable to allocate array of pointers (array size = %u)\\n\" @%s:%d`
- `stopIOEngineGated`
- `%s:%s Unsupported bufferIndex(%d), mNumBuffers(%d).\n`
- `output`
- `IODeviceTree:/product/audio`
- `%s:%s Unsupported inNewStreamFormatByteSize(%llu), expected(%lu).\n`
- `AppleARMIISAudioDevice.cpp`
- `_initExternalPowerDependency`
- `%s: AppleARMDMAAudioDevice::startDMAInternal:%d restart=%d. startTransport returned ret=kIOReturnNotReady but return kIOReturnSuccess.\n\n`
- `%s:%d::%s::Transaction timed out for direction:%s:: buffer index:%d\n`
- `%s:%s Failed to add mBidirOutAheadOfInHistogramReporter to legend. result=%s(%#x)\n`
- `%s:%s mIISController = NULL.ret=%s(%#x)\n`
- `%s:%s super::createIOReporters() failed result=%s(%#x)\n`
- `%u Hz`
- `MCA Run Times`
- `%s AppleARMDMAAudioDevice::%s:%d start failed.\n`
- `%s: AppleARMDMAAudioDevice::startIOEngineInternal could not start DMA: %s\n`
- `%s: Hardware timestamp (%llu) is ahead of current time (%llu).\n`
- `InExtraSafetyOffsetDivisor`
- `\"%s::%s attempting to release/re-allocate DMA buffer while DMA is streaming.\" @%s:%d`
- `%s:%s Failed to add mMCARuntimeReporter to legend. result=%s(%#x)\n`
- `handleChangeStreamFormat`
- `start`
- `waitAwake`
- `performConfigChangeGated`
- `Out-of-bounds start byte transfer`
- `%s AppleARMIISAudioDevice::start failed in super::start:%d\n`
- `%s:%s setDeviceFormat failed for kIODirectionIn. ret=%s(%#x) bufferIndex=%d validDirection=%#x dataFormatType=%#x\n`
- `%s::%s _externalPowerManager=%p failed to addPowerProvider(%s)\n`
- `!((inDevice) == nullptr)`
- `%s:%s performSampleRateChange failed. sampleRate=%lld ret=%s(%#x)\n`
- `%s:%s failed to allocate mBidirInAheadOfOutHistogramReporter. result=%s(%#x)\n`
- `%s:%s setDeviceFormat failed for kIODirectionOut. ret=%s(%#x) bufferIndex=%d validDirection=%#x dataFormatType=%#x\n`
- `external-power-provider`
- `IISAudioDevice::Helper`
- `%s::%s:%d invalid parameter. byteCount should be non-zero. direction=%#x byteCount=%lld startByteCount=%lld theAnswer=%s(%#x).\n`
- `%s:%s stopTransport failed. ret=%s(%#x)\n`
- `handleChangeSampleRate`
- `%s:%s getStreamFormatSupportedSampleRate failed, *inNewSampleRate=%lld\n`
- `%s::%s performConfigChangeGated(requestID=%d) requested while IOEngine is running. Forcing stopIOEngine()\n`
- `%s::%s() mIsolatedOutputStreamService->setupIO() failed ret=%s(%#x(\n`
- `\"AppleARMDMAAudioDevice::createStreamFormat dataFormat=%4s\" @%s:%d`
- `input`
- `%s:%s failed to add mBidirOutAheadOfInHistogramReporter to the local reporter set. result=%s(%#x)\n`
- `IOPlatformPanicAction`
- `%s: AppleARMDMAAudioDevice::startDataTransfers failed. bufferIndex=%u buffer=%p direction=%d byteCount=%u theAnswer=%s(%#x).\n\n`
- `input safety offset`
- `%s: Could not locate the DT path: %s.\n`
- `getIISControllerLatency`
- `%s:%s:%d setAudioStreamFormats failed. ret=%s(%#x) inSampleRate=%lld mIISValidDirection=%#x\n`
- `%s:%s mReporterList cannot be NULL. result=%s(%#x)\n`
- `sendBuffer`
- `%s AppleARMIISAudioDevice::%s Failed NULL IIS controller\n`
- `setTransportFormat`
- `%s:%s Unsupported inNewSampleRateByteSize(%llu), expected(%lu).\n`
- `%s: could not continue DMA: %s\n`
- `AppleARMIISAudioDevice`
- `isolated-audio-service-input`
- `!((inIISAudioDevice) == nullptr)`
- `startInternal`
- `extra-input-safety-offset`
- `%s:%s setAudioSampleRate failed. currentSampleRate=%lld ret=%s(%#x)\n`
- `AppleARMIISAudioDevice::init(%p, %d) failed in super::init\n`
- `\"%s::%s(direction=%#x) latency value out of supported (%lld)\" @%s:%d`
- `%s:%s IOAudio2Device::startIOEngine failed. theAnswer=%s(%#x)\n`
- `%s:%s stopIOEngineInternal failed. ret=%s(%#x)\n`
- `TS Prop Delay`
- `%s:%s startDataTransfers failed.ret=%s(%#x)\n`
- `performStreamFormatChange`
- `Misc. Debug Status`
- `Delta TS: in before out`
- `site.IONotifier*`
- `isolated-audio-service-output`
- `%s AppleARMIISAudioDevice %p: createIOReporters failed %s(%#x)\n`
- `%s:%s:%d failed. theAnswer=%s(%#x)\n`
- `%s:%s failed. kIOReturnNoMemory\n`
- `bidirectional`
- `%s:%s failed to allocate mNegativeInpDMAMarginHistogramReporter. result=%s(%#x)\n`
- `%s:%s setAudioStreamFormatInternal failed. ret=%s(%#x)\n`
- `%s:%s failed to add mTimestampPropagationDelayCausalityReporter to the local reporter set. result=%s(%#x)\n`
- `%s:%s failed to add mBidirInAheadOfOutHistogramReporter to the local reporter set. result=%s(%#x)\n`
- `stopAudioAndDataTransfers`
- `!((theControlList) == nullptr)`
- `%s:%s:%d failed. kIOReturnBusy\n`
- `%s: User supplied safety offset ignored due to potential negative value.\n`
- `Apple Inc.`
- `%s AppleARMDMAAudioDevice::%s:%d setAudioSampleRate failed. sampleRate=%lld err=%s(%#x)\n`
- `Negative Output DMA Margin`
- `%s:%s failed to allocate mBidirOutAheadOfInHistogramReporter. result=%s(%#x)\n`
- `%s:%s setAudioSampleRate failed.ret=%s(%#x) inSampleRate=%lld\n`
- `device UID`
- `%s: AppleARMDMAAudioDevice::startDMAInternal failed. restart=%d ret=%s(%#x)\n`
- `%s: AppleARMDMAAudioDevice::sendBuffer:%d failed. kIODirectionOut byteCount=%llu startBytes=%llu theAnswer=%s(%#x).\n\n`
- `%s:%s Failed to add the causal channel to the causality reporter. result=%s(%#x)\n`
- `/Library/Caches/com.apple.xbs/5D58D6FB-4B9B-48DB-AF57-4EB20C99A843/TemporaryDirectory.zSX0o6/Sources/AppleARMIISAudio/src/kext/AppleARMIISAudio/core/helper/IISAudioDeviceHelper.cpp`
- `Calculated buffer size of size %u for phyiscal sample rate %u, out of valid range %u < bufferSize < %u\n\n`
- `checkDMACompletion`
- `%s AppleARMIISAudioDevice::stopTransfer failed. bufferIndex=%u direction=%#x result=%s(%#x)\n`
- `\"zero\" @%s:%d`
- `_matchingNotificationHandlerGated`
- `%s:%s failed. ret=%s(%#x)\n`
- `setTransportDataFormat`
- `%s:%s Failed to add mInstSampleRateStatusReporter to legend. result=%s(%#x)\n`
- `%s AppleARMDMAAudioDevice::%s:%d setAudioStreamFormats failed.\n`
- `wants output trap`
- `site.BufferData`
- `%s AppleARMDMAAudioDevice::%s:%d startInternal failed.\n`
- `transferData`
- `%s:%s Failed to add mOutDMAMarginHistogramReporter to legend. result=%s(%#x)\n`
- `eso-out-us`
- `createIOReporters`
- `AppleARMDMAAudioDevice`
- `%s:%s Failed to add mNegativeInpDMAMarginHistogramReporter to legend. result=%s(%#x)\n`
- `1111`
- `%s:%s failed to allocate mDMACompletionTSPropDelayCausalityReporter. result=%s(%#x)\n`
- `is-development-only`
- `\"%s::%s(direction=%#x) unexpected latency (%lld) detected\" @%s:%d`
- `%s::transferData: mSuspend=%d, returning kIOReturnNotReady\n`
- `%s AppleARMIISAudioDevice::transferData failed. bufferIndex=%u direction=%#x byteCount=%llu byteOffset=%llu result=%s(%#x)\n`
- `%s:%s mMCARuntimeReporter failed init. result=%s(%#x)\n`
- `%s:%s failed to allocate OSSet. result=%s(%#x)\n`
- `%s:%s Failed to add mNegativeOutDMAMarginHistogramReporter to legend. result=%s(%#x)\n`
- `Delta TS: out before in`
- `transport type`
- `getTransportLatency`
- `%s:%s sampleRateIterator failed init. result=%s(%#x)\n`
- `createDebugControls`
- `extra-output-latency`
- `site.AppleARMDMAAudioDevice`
- `performConfigChange`
- `%s:%s setAudioSampleRate failed. ret=%s(%#x)\n`
- `mca-uses-iopm-overrides`
- `%s:%s mIsolatedOutputStreamService->setStreamDescription() failed ret=%s(%#x)\n`
- `%s::%s() mPowerStateCommandGate is nullptr [mSuspend=%d].\n`
- `device manufacturer`
- `%s:%s IOAudio2Device::stopIOEngine failed. theAnswer=%s(%#x)\n`
- `%s:%s setAudioStreamFormat failed. sampleRate=%lld ret=%s(%#x)\n`
- `Clamping buffer size to %u, which is not conducive to rate virtualization\n\n`
- `sample rate`
- `111222`
- `%s:%s mIsolatedInputStreamService->setStreamDescription() failed ret=%s(%#x)\n`
- `input streams`
- `Zero start byte transfers`
- `Negative Input DMA Margin`
- `%s:%s failed to add mTimestampPropagationDelayHistogramReporter to the local reporter set. result=%s(%#x)\n`
- `%s:%s failed to allocate mInpDMAMarginHistogramReporter. result=%s(%#x)\n`
- `allocateBuffers`
- `%s:%s Failed to add mMiscDebugStatusReporter to legend. result=%s(%#x)\n`
- `%s:%s failed to allocate mTimestampPropagationDelayHistogramReporter. result=%s(%#x)\n`
- `%s:%s setIISConfig failed.ret=%s(%#x)\n`
- `%s: AppleARMDMAAudioDevice::restartTransport failed. ret=%s(%#x)\n\n`
- `%s: AppleARMDMAAudioDevice::sendBuffer:%d failed. kIODirectionIn byteCount=%llu startBytes=%llu theAnswer=%s(%#x).\n\n`
- `%s:%s setTransportFormat failed. ret=%s(%#x)\n`
- `%s:%s setDeviceFormat failed for kIODirectionOut. ret=%s(%#x) bufferIndex=%d validDirection=%#x outputChannels=%d, bitsPerChannel=%d\n`
- `%s:%s startAudio failed.ret=%s(%#x)\n`
- `%s:%s mMCARunCountReporter failed init. result=%s(%#x)\n`
- `Output`
- `stopTransfer`
- `setAudioStreamFormats`
- `%s:%s super::gangAudioDevices failed. ret=%s(%#x) enable=%d\n`
- `Input`
- `1`
- `setAudioSampleRate`
- `%s::%s() mPowerStateCommandGate->getWorkloop()][%p] != getWorkloop()[%p] [mSuspend=%d].\n`
- `%s:%s couldn't allocate the status reporter. result=%s(%#x)\n`
- `performSampleRateChange`
- `%s:%s failed to allocate mNegativeOutDMAMarginHistogramReporter. result=%s(%#x)\n`
- `%s::%s() mIsolatedInputStreamService->setupIO() failed ret=%s(%#x(\n`
- `extra-output-safety-offset`
- `%s: AppleARMDMAAudioDevice::transferData:%d failed. direction=%#x byteCount=%lld startByteCount=%lld theAnswer=%s(%#x).\n\n`
- `%s:%s failed to allocate mOutDMAMarginHistogramReporter. result=%s(%#x)\n`
- `createAppleAudioStreamFormatter`
- `%s::%s() audioStreamFormatterDescription->getBytesNoCopy() =%p \n\n`
- `%s:%s getStreamFormatSupportedFormat failed.\n`
- `%s:%s failed. outputStreamList=%p inputStreamList=%p\n`
- `%s::setAudioStreamFormatInternal: setTransportDataFormat => %s\n`
- `%s:%s Failed to add mInpDMAMarginHistogramReporter to legend. result=%s(%#x)\n`
- `%s: Requested safety offset (%d) out of bounds (%d, %d).\n`
- `%s:%s mIsolatedInputStreamService->setupIO() failed ret=%s(%#x)\n`
- `%s:%s couldn't find device UID. result=%s(%#x)\n`
- `setAudioStreamFormat`
- `Bidirectional Device`
- `%s: Could not find the safety offset seed property.\n`
- `audio-stream-formatter`
- `\"%s::%s unimplemented\" @%s:%d`
- `output streams`
- `%s::%s:%d startTransportComplete failed ret=%s(%#x)\n`
- `gangAudioDevices`
- `MCA Run Counts`
- `site.StreamData`
- `setStreamActiveGated`
- `%s:%s failed to allocate IOSimpleReporter. result=%s(%#x)\n`
- `Non-causal Count`
- `so-seed-us`
- `output latency`
- `%s::setAudioStreamFormatInternal: setAudioFormat => %s\n`
- `%s:%s Failed to add mTimestampPropagationDelayHistogramReporter to legend. result=%s(%#x)\n`
- `%s:%s Failed to add mDMACompletionTSPropDelayCausalityReporter to legend. result=%s(%#x)\n`
- `startTransport`
- `%s:%s not ready.\n`
- `%s:%s Failed to add mMCARunCountReporter to legend. result=%s(%#x)\n`
- `clock domain`
- `%s:%s mIsolatedOutputStreamService->setupIO() failed ret=%s(%#x)\n`
- `controls`
- `hw.cachelinesize`
- `inout`
- `Input DMA Margin`
- `121111121222121212122221112211221222111221111111111111122`
- `clear-output-buffers`
- `%s.%s`
- `AppleARMIISAudioDevice::init(%p, %d) failed in AppleExternalPowerManager::withCapacity()\n`
- `%s:%s setAudioFormat failed. bufferIndex=%d bufferOutputChannels=%d bufferInputChannels=%d bitsPerChannel[bufferIndex]=%d ret=%s(%#x)\n`
- `getStreamFormatSupportedSampleRate`
- `input latency`
- `%s:%d::%s::mBufferData is NULL\n`
- `Sleep cycles with active streams`
- `Output DMA Margin`
- `%s:%s Failed to add the non-causal channel to the causality reporter. result=%s(%#x)\n`
- `site.AppleARMIISAudioDevice`
- `\"%s::%s() should not be called without owning workloop\" @%s:%d`
- `%s:%s Unsupported bufferIndex(%u), mNumBuffers(%u)\n`
- `eso-in-us`
- `zts-timeout-override-ms`
- `setupForIsolatedIO`
- `%s: sysctl reports possibly OOB mCPUCacheLineSize = %llu.\n`
- `site.AppleARMDMAAudioDevice::OverrideConfigs`
- `2122`
- `!((inRegistryEntry) == nullptr)`
- `%s::%s [%u] unable to create matching property index=%d [NumPhandles=%d]\n`
- `startIOEngineGated`
- `%s::%s:%d Unsupported Format. sampleRate=%lld exceptionDirection=%#x\n`
- `output safety offset`
- `%s::%s:%d startByteCount cannot be greater than startByteCount. Will proceed with truncated startByteCount. direction=%#x byteCount=%lld startByteCount=%lld theAnswer=%s(%#x).\n`
- `%s:%s startIOEngineInternal failed. theAnswer=%s(%#x)\n`
- `Physical sample rate is non-integral\n`
- `%s:%s allocateBuffers failed. inSampleRate=%lld currentSR=%lld, ret=%s(%#x)\n`
- `Timestamp Propagation`
- `%s:%s:%d gangIISDevices failed. ret=%s(%#x) enable=%d otherDevice=%p\n`
- `%s:%s startIOEngineInternal(true) failed. theAnswer=%s(%#x)\n`
- `io buffer frame size`
- `OutExtraSafetyOffsetDivisor`
- `%s:%s setDeviceSampleRate failed sampleRate=%lld.ret=%s(%#x)\n`
- `safety-offset-seed-divisor`
- `AppleARMDMAAudioDevice.cpp`

**[__TEXT.__os_log]**

- `%s::transferData: mSuspend=%d, returning kIOReturnNotReady`
- `%s:%s mMCARunCountReporter failed init. result=%s(%#x)`
- `%s AppleARMIISAudioDevice::%s Skipped (DT-allowed: %d)`
- `%s:%s super::gangAudioDevices failed. ret=%s(%#x) enable=%d`
- `%s:%s %p PanicAction Register`
- `%s AppleARMDMAAudioDevice::%s:%d startInternal failed.`
- `%s:%s startIOEngineInternal(true) failed. theAnswer=%s(%#x)`
- `%s: AppleARMDMAAudioDevice::startDMAInternal failed. restart=%d ret=%s(%#x)`
- `%s:%s couldn't find device UID. result=%s(%#x)`
- `%s::%s:%d invalid parameter. byteCount should be non-zero. direction=%#x byteCount=%lld startByteCount=%lld theAnswer=%s(%#x).`
- `%s:%s failed to allocate mDMACompletionTSPropDelayCausalityReporter. result=%s(%#x)`
- `%s:%s setDeviceFormat failed for kIODirectionIn. ret=%s(%#x) bufferIndex=%d validDirection=%#x dataFormatType=%#x`
- `%s:%s mReporterList cannot be NULL. result=%s(%#x)`
- `%s: AppleARMDMAAudioDevice::sendBuffer:%d failed. kIODirectionIn byteCount=%llu startBytes=%llu theAnswer=%s(%#x).\n`
- `%s: Hardware timestamp (%llu) is ahead of current time (%llu).`
- `%s:%s failed to allocate mBidirOutAheadOfInHistogramReporter. result=%s(%#x)`
- `%s: could not continue DMA: %s`
- `%s:%s allocateBuffers failed. inSampleRate=%lld currentSR=%lld, ret=%s(%#x)`
- `%s:%s failed to allocate mOutDMAMarginHistogramReporter. result=%s(%#x)`
- `%s:%s Failed to add mNegativeInpDMAMarginHistogramReporter to legend. result=%s(%#x)`
- `%s:%s failed to add mBidirOutAheadOfInHistogramReporter to the local reporter set. result=%s(%#x)`
- `%s: User supplied safety offset ignored due to potential negative value.`
- `AppleARMIISAudioDevice::init(%p, %d)`
- `%s::%s() mIsolatedInputStreamService->setupIO() failed ret=%s(%#x(`
- `%s:%s setAudioFormat failed. bufferIndex=%d bufferOutputChannels=%d bufferInputChannels=%d bitsPerChannel[bufferIndex]=%d ret=%s(%#x)`
- `%s::%s:%d startByteCount cannot be zero. Overriding startByteCount with byteCount. direction=%#x byteCount=%lld startByteCount=%lld theAnswer=%s(%#x).`
- `%s:%s stopIOEngineInternal failed. ret=%s(%#x)`
- `%s:%s Unsupported bufferIndex(%u), mNumBuffers(%u)`
- `%s:%d::%s::mBufferData is NULL`
- `%s: Clearing buffer because audio client IO has fallen behind (I: %llu, O: %llu)`
- `%s:%s startDataTransfers failed.ret=%s(%#x)`
- `%s::%s() thread awakened. [mSuspend=%d]`
- `%s::%s [%u] unable to get phandle at index=%d [NumPhandles=%d]`
- `%s::%s:%d startByteCount cannot be greater than startByteCount. Will proceed with truncated startByteCount. direction=%#x byteCount=%lld startByteCount=%lld theAnswer=%s(%#x).`
- `%s:%s setAudioStreamFormat failed. sampleRate=%lld ret=%s(%#x)`
- `%s: AppleARMDMAAudioDevice::startIOEngineInternal could not start DMA: %s`
- `%s: AppleARMDMAAudioDevice::startDMAInternal:%d restart=%d. startTransport returned ret=kIOReturnNotReady but return kIOReturnSuccess.\n`
- `%s: %s, %s file: %s, line: %d\n`
- `%s AppleARMIISAudioDevice::start failed in super::start:%d`
- `%s:%s mMCARuntimeReporter failed init. result=%s(%#x)`
- `%s AppleARMIISAudioDevice %p: createIOReporters failed %s(%#x)`
- `%s:%s Failed to add mBidirOutAheadOfInHistogramReporter to legend. result=%s(%#x)`
- `%s: Could not find the safety offset seed property.`
- `AppleARMIISAudioDevice::init(%p, %d) success`
- `%s:%s mIsolatedOutputStreamService->setStreamDescription() failed ret=%s(%#x)`
- `%s AppleARMIISAudioDevice::transferData failed. bufferIndex=%u direction=%#x byteCount=%llu byteOffset=%llu result=%s(%#x)`
- `%s:%s:%d gangIISDevices failed. ret=%s(%#x) enable=%d otherDevice=%p`
- `%s: sysctl reports possibly OOB mCPUCacheLineSize = %llu.`
- `%s AppleARMDMAAudioDevice::%s:%d start failed.`
- `%s AppleARMDMAAudioDevice::%s:%d setAudioSampleRate failed. sampleRate=%lld err=%s(%#x)`
- `%s: Zero time stamp captured ( %llu, %llu)\n`
- `%s AppleARMIISAudioDevice::stopTransfer failed. bufferIndex=%u direction=%#x result=%s(%#x)`
- `%s:%s getStreamFormatSupportedSampleRate failed, *inNewSampleRate=%lld`
- `%s:%s failed for %d. ret=%s(%#x)`
- `Clamping buffer size to %u, which is not conducive to rate virtualization\n`
- `%s:%s Failed to add mInpDMAMarginHistogramReporter to legend. result=%s(%#x)`
- `%s:%s setDeviceSampleRate failed sampleRate=%lld.ret=%s(%#x)`
- `%s:%s setDeviceFormat failed for kIODirectionIn. ret=%s(%#x) bufferIndex=%d validDirection=%#x inputChannels=%#x, bitsPerChannel=%d`
- `%s::%s() mPowerStateCommandGate->getWorkloop()][%p] != getWorkloop()[%p] [mSuspend=%d].`
- `%s:%s Failed to add mInstSampleRateStatusReporter to legend. result=%s(%#x)`
- `%s: AppleARMDMAAudioDevice::sendBuffer:%d failed. kIODirectionOut byteCount=%llu startBytes=%llu theAnswer=%s(%#x).\n`
- `%s:%s Unsupported inNewSampleRateByteSize(%llu), expected(%lu).`
- `%s:%s setTransportSampleRate failed. inSampleRate=%lld currentSR=%lld ret=%s(%#x)`
- `%s:%s Failed to add mBidirInAheadOfOutHistogramReporter to legend. result=%s(%#x)`
- `%s:%s Failed to add mMCARuntimeReporter to legend. result=%s(%#x)`
- `%s:%s:%d failed. theAnswer=%s(%#x)`
- `%s:%s failed to allocate IOSimpleReporter. result=%s(%#x)`
- `%s:%s Failed to add mNegativeOutDMAMarginHistogramReporter to legend. result=%s(%#x)`
- `%s: Requested safety offset (%d) out of bounds (%d, %d).`
- `%s: Could not locate the DT path: %s.`
- `%s::%s() audioStreamFormatterDescription->getBytesNoCopy() =%p \n`
- `%s:%s mIsolatedInputStreamService->setupIO() failed ret=%s(%#x)`
- `%s:%s not ready.`
- `+ %s stopTransport`
- `%s::setStreamActive inStreamID=%d inIsActive=%d`
- `%s:%d::%s::Transaction timed out for direction:%s:: buffer index:%d`
- `%s:%s IOAudio2Device::startIOEngine failed. theAnswer=%s(%#x)`
- `%s: AppleARMDMAAudioDevice::startDataTransfers failed. bufferIndex=%u buffer=%p direction=%d byteCount=%u theAnswer=%s(%#x).\n`
- `%s::setStreamActive inStreamID=%d inIsActive=%d ret=%s(%#x)`
- `%s:%s failed. outputStreamList=%p inputStreamList=%p`
- `%s:%s Failed to add the causal channel to the causality reporter. result=%s(%#x)`
- `%s:%s startAudio failed.ret=%s(%#x)`
- `%s:%s failed to allocate mNegativeOutDMAMarginHistogramReporter. result=%s(%#x)`
- `%s:%s failed to allocate mTimestampPropagationDelayHistogramReporter. result=%s(%#x)`
- `%s:%s create injection control failed`
- `%s:%s Failed to add the non-causal channel to the causality reporter. result=%s(%#x)`
- `%s:%s failed to add mBidirInAheadOfOutHistogramReporter to the local reporter set. result=%s(%#x)`
- `%s:%s mIsolatedInputStreamService->setStreamDescription() failed ret=%s(%#x)`
- `%s %s:%d stopDataTransfers failed for bufferIndex=%d ret=%s(%#x)`
- `%s::%s() mIsolatedOutputStreamService->setupIO() failed ret=%s(%#x(`
- `%s: AppleARMDMAAudioDevice::transferData:%d failed. direction=%#x byteCount=%lld startByteCount=%lld theAnswer=%s(%#x).\n`
- `+ %s startTransport\n`
- `%s::setAudioStreamFormatInternal: setAudioFormat => %s`
- `%s:%s Failed to add mDMACompletionTSPropDelayCausalityReporter to legend. result=%s(%#x)`
- `%s:%s Unsupported inNewStreamFormatByteSize(%llu), expected(%lu).`
- `%s:%s setIISConfig failed.ret=%s(%#x)`
- `%s:%s mIsolatedOutputStreamService->setupIO() failed ret=%s(%#x)`
- `%s AppleARMDMAAudioDevice::%s:%d setAudioStreamFormats failed.`
- `%s:%s startIOEngineInternal failed. theAnswer=%s(%#x)`
- `%s:%s getStreamFormatSupportedFormat failed.`
- `%s:%s setTransportFormat failed. ret=%s(%#x)`
- `%s:%s Failed to add mMiscDebugStatusReporter to legend. result=%s(%#x)`
- `%s: User supplied safety offset is zero.`
- `%s:%s setAudioSampleRate failed. currentSampleRate=%lld ret=%s(%#x)`
- `%s:%s setDeviceFormat failed for kIODirectionOut. ret=%s(%#x) bufferIndex=%d validDirection=%#x dataFormatType=%#x`
- `%s::%s() commandSleep(&_externalPowerManager) has been interrupted result=%#x [mSuspend=%d]. Will retry if necessary.`
- `%s:%s couldn't allocate the status reporter. result=%s(%#x)`
- `%s:%s sampleRateIterator failed init. result=%s(%#x)`
- `%s:%s Failed to add mMCARunCountReporter to legend. result=%s(%#x)`
- `%s:%s setAudioSampleRate failed. ret=%s(%#x)`
- `%s:%s failed. ret=%s(%#x)`
- `AppleARMIISAudioDevice::init(%p, %d) failed in super::init`
- `%s AppleARMIISAudioDevice::%s Failed NULL IIS controller`
- `%s:%s mIISController = NULL.ret=%s(%#x)`
- `- %s startTransport ret=%s(%#x)`
- `%s:%s setAudioSampleRate failed.ret=%s(%#x) inSampleRate=%lld`
- `%s::%s() mPowerStateCommandGate is nullptr [mSuspend=%d].`
- `%s:%s IOAudio2Device::stopIOEngine failed. theAnswer=%s(%#x)`
- `%s:%s performSampleRateChange failed. sampleRate=%lld ret=%s(%#x)`
- `Physical sample rate is non-integral`
- `%s::setAudioStreamFormatInternal: setTransportDataFormat => %s`
- `+ %s::%s()`
- `- %s stopTransport ret=%s(%#x)`
- `%s::%s [%u] unable to create matching property index=%d [NumPhandles=%d]`
- `%s::%s _externalPowerManager=%p failed to addPowerProvider(%s)`
- `%s:%s super::createIOReporters() failed result=%s(%#x)`
- `%s::%s:%d Unsupported Format. sampleRate=%lld exceptionDirection=%#x`
- `- %s::%s() ret=%s(%#x)`
- `%s::%s performConfigChangeGated(requestID=%d) requested while IOEngine is running. Forcing stopIOEngine()`
- `%s:%s failed to allocate OSSet. result=%s(%#x)`
- `%s:%s setDeviceFormat failed for kIODirectionOut. ret=%s(%#x) bufferIndex=%d validDirection=%#x outputChannels=%d, bitsPerChannel=%d`
- `%s:%s:%d setAudioStreamFormats failed. ret=%s(%#x) inSampleRate=%lld mIISValidDirection=%#x`
- `%s: AppleARMDMAAudioDevice::restartTransport failed. ret=%s(%#x)\n`
- `%s:%s stopTransport failed. ret=%s(%#x)`
- `%s:%s Unsupported bufferIndex(%d), mNumBuffers(%d).`
- `%s:%s failed. kIOReturnNoMemory`
- `%s::%s:%d startTransportComplete failed ret=%s(%#x)`
- `%s:%s failed to allocate mInpDMAMarginHistogramReporter. result=%s(%#x)`
- `%s:%s:%d failed. kIOReturnBusy`
- `%s:%s Failed to add mOutDMAMarginHistogramReporter to legend. result=%s(%#x)`
- `AppleARMIISAudioDevice::init(%p, %d) failed in AppleExternalPowerManager::withCapacity()`
- `Calculated buffer size of size %u for phyiscal sample rate %u, out of valid range %u < bufferSize < %u\n`
- `%s:%s failed to allocate mNegativeInpDMAMarginHistogramReporter. result=%s(%#x)`
- `%s:%s failed to add mTimestampPropagationDelayHistogramReporter to the local reporter set. result=%s(%#x)`
- `%s:%s Failed to add mTimestampPropagationDelayHistogramReporter to legend. result=%s(%#x)`
- `%s:%s failed to add mTimestampPropagationDelayCausalityReporter to the local reporter set. result=%s(%#x)`
- `%s:%s setAudioStreamFormatInternal failed. ret=%s(%#x)`
- `%s:%s failed to allocate mBidirInAheadOfOutHistogramReporter. result=%s(%#x)`
