# `com.apple.driver.AppleSSE`

- Name: AppleSSE
- Version: `1.0`
- UUID: `CE344192-52EA-3E12-94BC-CB8FF3E7AE30`
- Source version: `332.0.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleSEPManager`](com.apple.driver.AppleSEPManager.md) 1.0.0, [`com.apple.driver.IOSlaveProcessor`](com.apple.driver.IOSlaveProcessor.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleSSE
- `CFBundleIdentifier`: `com.apple.driver.AppleSSE`
- `IOClass`: `AppleSSE`
- `IOMatchCategory`: `AppleSSE`
- `IONameMatch`: `sep-endpoint,sse`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSSE`
- `IOProviderClass`: `AppleSEPDeviceService`
- `IOUserClientClass`: `AppleSSEUserClient`


## C++ classes (3) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleSSE` | 0x4108 | AppleSSEInterface → IOService → IORegistryEntry |
| `AppleSSEInterface` | 0x88 | IOService → IORegistryEntry |
| `AppleSSEUserClient` | 0xe8 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001e40 off=0x0077f4e0-0x00781320 addr=0xfffffe00077834e0-0xfffffe0007785320 r--/r--   __TEXT            
	sz=0x000016fc off=0x0077fb58-0x00781254 addr=0xfffffe0007783b58-0xfffffe0007785254               __TEXT.__cstring          (CstringLiterals)
	sz=0x000000c8 off=0x00781258-0x00781320 addr=0xfffffe0007785258-0xfffffe0007785320               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x000083fc off=0x0271d730-0x02725b2c addr=0xfffffe0009721730-0xfffffe0009729b2c r-x/r-x   __TEXT_EXEC       
	sz=0x0000817c off=0x0271d730-0x027258ac addr=0xfffffe0009721730-0xfffffe00097298ac          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000280 off=0x027258ac-0x02725b2c addr=0xfffffe00097298ac-0xfffffe0009729b2c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000154 off=0x0499a0f0-0x0499a244 addr=0xfffffe000b99e0f0-0xfffffe000b99e244 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x0499a0f0-0x0499a1b8 addr=0xfffffe000b99e0f0-0xfffffe000b99e1b8               __DATA.__data             
	sz=0x00000088 off=0x00000000-0x00000088 addr=0xfffffe000b99e1b8-0xfffffe000b99e240               __DATA.__common           (Zerofill)
	sz=0x00000004 off=0x00000000-0x00000004 addr=0xfffffe000b99e240-0xfffffe000b99e244               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x000015a8 off=0x012251e8-0x01226790 addr=0xfffffe00082291e8-0xfffffe000822a790 rw-/rw-   __DATA_CONST      
	sz=0x00000018 off=0x012251e8-0x01225200 addr=0xfffffe00082291e8-0xfffffe0008229200         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000018 off=0x01225200-0x01225218 addr=0xfffffe0008229200-0xfffffe0008229218         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001328 off=0x01225218-0x01226540 addr=0xfffffe0008229218-0xfffffe000822a540         __DATA_CONST.__const            
	sz=0x000000c0 off=0x01226540-0x01226600 addr=0xfffffe000822a540-0xfffffe000822a600         __DATA_CONST.__kalloc_type      
	sz=0x00000140 off=0x01226600-0x01226740 addr=0xfffffe000822a600-0xfffffe000822a740         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000050 off=0x01226740-0x01226790 addr=0xfffffe000822a740-0xfffffe000822a790         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 90 at 0x04ae6a8c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     CE344192-52EA-3E12-94BC-CB8FF3E7AE30
008: LC_SOURCE_VERSION           332.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab2c48 size=0xc0
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleSSE`
- `CFBundleIdentifier`: `com.apple.driver.AppleSSE`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleSSE`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2013 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleSSE.kext`
- `_PrelinkExecutableLoadAddr`: `-2198897937184`
- `_PrelinkExecutableRelativePath`: `AppleSSE`
- `_PrelinkExecutableSize`: `47416`
- `_PrelinkExecutableSourceAddr`: `-2198897937184`
- `_PrelinkKmodInfo`: `-2198828621584`

## Strings (123) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `params->cardChallenge->getLength() == 8`
- `params->nonce`
- `handleSEPMessage`
- `clientEntitlement`
- `_workLoop`
- `dataSize`
- `_recvBuf`
- `The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range`
- `!params->cardCryptogram || (params->cardCryptogram->getLength() == 8)`
- `dataLength >= sizeof(confirm_sig_key_in_data)`
- `i8@?0`
- `com.apple.private.applesse.allow`
- `inData`
- `err == 0 `
- `(params->version >= 3) && (params->version <= 5)`
- `cmdDataLength >= sizeof(*cmd)`
- `getCertificateExpirationDate`
- `!params->seid || (params->seid->getLength() == 24)`
- `certificates`
- `outputBufferLength`
- `AppleSEPManager`
- `sepManagerService`
- `121111121222121211121122222111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `outSize >= sizeof(*outData) + outData->apSepScoresSize + outData->apSepScoresSignatureSize`
- `params->hostChallenge->getLength() == 8`
- `12111112122212121111111111111`
- `/Library/Caches/com.apple.xbs/FF83E7CC-A422-4417-A8D5-3AD7BBA47DD6/TemporaryDirectory.b4kgjH/Sources/AppleSSE/AppleSSE/AppleSSE.cpp`
- `issueNewCertificate`
- `outputBufferLength && (*outputBufferLength >= _sepContext.responseDataLength)`
- `site.AppleSSEUserClient`
- `getSignedSepScores`
- `(device == this)`
- `\"%s\" @%s:%d`
- `success`
- `sepManager`
- `This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.`
- `AssertMacros: %s (value: 0x%lx), %s file: %s, line: %d\n`
- `/Library/Caches/com.apple.xbs/FF83E7CC-A422-4417-A8D5-3AD7BBA47DD6/TemporaryDirectory.b4kgjH/Sources/AppleSSE/AppleSSE/AppleSSEUserClient.cpp`
- `outSize == sizeof(outData)`
- `_baaCertificateCreationStarted`
- `dataLength >= sizeof(*inData)`
- `ret`
- `*lock != 0`
- `ep`
- `result`
- `outBuffer`
- `ret == 0 `
- `params->apSepScoresSignature`
- `sendSEPCommProbe`
- `_sendBuf`
- `sepDeviceService`
- `outSize >= sizeof(*outData)`
- `*outputBufferLength >= sizeof(*outData)`
- `outputBuffer`
- `params->cardCryptogram`
- `inMap`
- `outMap`
- `buff`
- `cmd->header == 'SSEc'`
- `isInternalBuild()`
- `params->apSepScores`
- `_currentPMState == kPMStateOn`
- `buffer`
- `m.call.length <= 16384`
- `md`
- `sepDevice`
- `_wakeFromHibernateEventSource`
- `apSepScoresSignature->getLength() <= end - pos`
- `dataSize <= (buffEnd - buffPos)`
- `_sepEndpoint`
- `params`
- `AppleSSEInterface`
- `(params->hostChallenge && params->cardChallenge && params->cardCryptogram) || (!params->hostChallenge && !params->cardChallenge && !params->cardCryptogram)`
- `!params->hostChallenge || (params->hostChallenge->getLength() == 8)`
- `outData`
- `AppleSSE`
- `%s::%s returning, result = %u\n`
- `getCertificate`
- `%s::%s ignoring unsupported message from SEP, request = %d, info = %d, length = %d\n`
- `matchDict`
- `sep-endpoint,sse`
- `site.AppleSSEInterface`
- `size >= sizeof(sse_command_t)`
- `buffPos`
- `readFromSEP == m.call.length`
- `OSBoundedPtr.h`
- `bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow.`
- `AppleSSEUserClient`
- `12111112122212121`
- `%s::%s called\n`
- `0`
- `params->seid`
- `*outputBufferLength >= totalSize`
- `_sepContext.messageCode == request`
- `%s::%s received unexpected SEP comm probe response, messageCode = %u (expected %u), sn = %u (expected %u)\n`
- `params->cardChallenge`
- `!params->cardChallenge || (params->cardChallenge->getLength() == 8)`
- `sizeof(uint32_t) <= (end - pos)`
- `bounded_array_ref: n + m is larger than the size of any bounded_array_ref`
- `params->hostChallenge`
- `pos == buffer.data() + size`
- `expirationDate`
- `apSepScores->getLength() <= end - pos`
- `cert->getLength() <= (end - pos)`
- `writtenToSEP == dataLength`
- `site.AppleSSE`
- `params->cardCryptogram->getLength() == 8`
- `_commandGate`
- `params->version == 2`
- `params->nonce->getLength() == 16`
- `cmdData`
- `outArray`
- `sizeof(uint32_t) <= (buffEnd - buffPos)`
- `bounded_ptr<T>::discard_bounds: Discarding the bounds on this pointer would lose the fact that it is outside of the bounds set originally`
- `start`
- `params->apScores`
- `params->nonce->getLength() == 8`
- `size <= buffer.size()`
- `buffEnd`
- `params->seid->getLength() == 24`
- `bounded_array_ref: invalid slice provided, the indices are of bounds for the bounded_array_ref`
- `_powerOffEventSource`
- `data`
