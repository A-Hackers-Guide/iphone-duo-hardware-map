# `com.apple.iokit.AppleSEPGenericTransfer`

- Name: AppleSEPGenericTransfer
- Version: `1`
- UUID: `7DF73363-321D-36DA-94C6-5C33E723FE08`
- Source version: `34.0.0.0.0`
- Depends on: [`com.apple.driver.AppleSEPManager`](com.apple.driver.AppleSEPManager.md) 1.0.0, [`com.apple.driver.IOSlaveProcessor`](com.apple.driver.IOSlaveProcessor.md) 1.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (3) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleSEPGenericTransfer` | 0xe8 |  |
| `GTCondition` | 0x18 |  |
| `GTGateLock` | 0x20 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001341 off=0x007326c0-0x00733a01 addr=0xfffffe00077366c0-0xfffffe0007737a01 r--/r--   __TEXT            
	sz=0x00000932 off=0x00732ce8-0x0073361a addr=0xfffffe0007736ce8-0xfffffe000773761a               __TEXT.__cstring          (CstringLiterals)
	sz=0x000003e7 off=0x0073361a-0x00733a01 addr=0xfffffe000773761a-0xfffffe0007737a01               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x000049c8 off=0x025d0cd0-0x025d5698 addr=0xfffffe00095d4cd0-0xfffffe00095d9698 r-x/r-x   __TEXT_EXEC       
	sz=0x00004768 off=0x025d0cd0-0x025d5438 addr=0xfffffe00095d4cd0-0xfffffe00095d9438          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000260 off=0x025d5438-0x025d5698 addr=0xfffffe00095d9438-0xfffffe00095d9698          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000150 off=0x04995560-0x049956b0 addr=0xfffffe000b999560-0xfffffe000b9996b0 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04995560-0x04995628 addr=0xfffffe000b999560-0xfffffe000b999628               __DATA.__data             
	sz=0x00000088 off=0x00000000-0x00000088 addr=0xfffffe000b999628-0xfffffe000b9996b0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000005c8 off=0x011e4498-0x011e4a60 addr=0xfffffe00081e8498-0xfffffe00081e8a60 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x011e4498-0x011e44a8 addr=0xfffffe00081e8498-0xfffffe00081e84a8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x011e44a8-0x011e44b8 addr=0xfffffe00081e84a8-0xfffffe00081e84b8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000378 off=0x011e44b8-0x011e4830 addr=0xfffffe00081e84b8-0xfffffe00081e8830         __DATA_CONST.__const            
	sz=0x000000c0 off=0x011e4830-0x011e48f0 addr=0xfffffe00081e8830-0xfffffe00081e88f0         __DATA_CONST.__kalloc_type      
	sz=0x00000130 off=0x011e48f0-0x011e4a20 addr=0xfffffe00081e88f0-0xfffffe00081e8a20         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000040 off=0x011e4a20-0x011e4a60 addr=0xfffffe00081e8a20-0xfffffe00081e8a60         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 84 at 0x04ae4114
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     7DF73363-321D-36DA-94C6-5C33E723FE08
008: LC_SOURCE_VERSION           34.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aaffc8 size=0x98
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleSEPGenericTransfer`
- `CFBundleIdentifier`: `com.apple.iokit.AppleSEPGenericTransfer`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleSEPGenericTransfer`
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
- `NSHumanReadableCopyright`: `Copyright © 2019 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleSEPGenericTransfer.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898252096`
- `_PrelinkExecutableRelativePath`: `AppleSEPGenericTransfer`
- `_PrelinkExecutableSize`: `25633`
- `_PrelinkExecutableSourceAddr`: `-2198898252096`
- `_PrelinkKmodInfo`: `-2198828640928`

## Strings (101) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `/Library/Caches/com.apple.xbs/A6862A20-E03E-49B6-AE46-DE7B69AB84A2/TemporaryDirectory.UkMP3N/Sources/AppleSEPGenericTransfer/common/gt_common.c`
- `context->transfer.state == kGTIdle`
- `\"Missing SEP output buffer.\" @%s:%d`
- `site.AppleSEPGenericTransfer`
- `_sepTransactResponse`
- `size == sizeof(sepDeviceServiceName) - 1`
- `_recvBuffer`
- `_statusCallback`
- `err == 0 `
- `12122111111211221222222111111`
- `com.apple.tracked.AppleSEPGenericTransfer`
- `disable`
- `handleSEPMessage`
- `_lockState != 0`
- `sep-endpoint,%c%c%c%c`
- `sepManager`
- `messageRef`
- `GTOutputBuffer.cpp`
- `AppleSEPGenericTransfer`
- `header.dataSize <= (oolBufferSize - sizeof(header))`
- `getEndpoint`
- `command == _gtContext.transfer.command`
- `outDataOut != nullptr`
- `bufferSize`
- `site.GTGateLock`
- `oolBuffer`
- `context->transfer.state == kGTWriting`
- `context->transfer.offset == header.offset`
- `sepManagerService`
- `endpoint`
- `_dataCallback`
- `GTCondition`
- `121`
- `_sepTransferLock`
- `transactToIOMD`
- `maxTransactionSize`
- `count == inLength`
- `header.offset == 0`
- `ret == 0 `
- `matching`
- `writeBytesToIOMD`
- `0`
- `oolBufferSize > sizeof(gt_packet_t)`
- `context->transfer.size == header.totalSize`
- `workLoop`
- `sepDevice`
- `_messageHandler != nullptr`
- `AppleSEPManager`
- `transact`
- `oolBufferSize > sizeof(header)`
- `_gtContext.memoryTag`
- `sepDeviceService`
- `sendRawMessage`
- `answerMessageOut`
- `transfer`
- `_commandGate`
- `sepMessageHandler`
- `ep`
- `(outDataOut && outLength) || (!outDataOut && !outLength)`
- `success`
- `_service`
- `sendMD`
- `1212`
- `site.GTCondition`
- `context->transfer.size >= (context->transfer.offset + header.dataSize)`
- `AssertMacros: %s, %s file: %s, line: %d, value: %lld\n`
- `header.version == (1)`
- `header.dataSize <= header.totalSize`
- `context->transfer.state == kGTReading`
- `_sepEndpointLock`
- `sep-endpoint'a4cc`
- `inLength <= outData->getLength()`
- `context`
- `header.totalSize <= gt_get_max_transaction_size_internal(context)`
- `_messageHandler`
- `_sendMemory`
- `locked && _sepEndpoint && _sepEndpoint->isEnabled()`
- `outData`
- `_sepEndpoint`
- `_sendBuffer`
- `my`
- `inBuffer`
- `context->transfer.command == header.command`
- `/Library/Caches/com.apple.xbs/A6862A20-E03E-49B6-AE46-DE7B69AB84A2/TemporaryDirectory.UkMP3N/Sources/AppleSEPGenericTransfer/AppleSEPGenericTransfer/AppleSEPGenericTransfer.cpp`
- `slaveEndpoint != nullptr`
- `_recvMemory`
- `recvMD`
- `context->transfer.data`
- `me`
- `inLength <= _sepMaxTransactSize`
- `GTGateLock`
- `/Library/Caches/com.apple.xbs/A6862A20-E03E-49B6-AE46-DE7B69AB84A2/TemporaryDirectory.UkMP3N/Sources/AppleSEPGenericTransfer/AppleSEPGenericTransfer/GTUtilities.cpp`

**[__TEXT.__os_log]**

- `AppleSEPGenericTransfer::%s: Enabling %c%c%c%c endpoint took %d ms.`
- `AppleSEPGenericTransfer::%s: Message to SEP, request = 0x%x, command = 0x%x, %d: %d = %d + %d\n`
- `AppleSEPGenericTransfer::%s: command:0x%x, inData:%p, inDataSize:%zu, outData:%p, outOptBytesWritten:%p, flags:0x%x`
- `AppleSEPGenericTransfer::%s: Disabling SEP`
- `AppleSEPGenericTransfer::%s: Warning: Getting SEP endpoint is taking more than %d ms.`
- `AppleSEPGenericTransfer::%s: -> %d, `
- `AppleSEPGenericTransfer::%s: Message from SEP, request = 0x%x, command = 0x%x, %d: %d = %d + %d\n`
- `AppleSEPGenericTransfer::%s: command:0x%x, inData:%p, inLength:%zu, outDataOut:%p, outLength:%p, flags:0x%x`
- `AppleSEPGenericTransfer::%s: outData:%p, inBuffer:%p, inLength:%zu, outOptBytesWritten:%p`
