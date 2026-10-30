# `com.apple.iokit.IOBiometricFamily`

- Name: IOBiometricFamily
- Version: `1`
- UUID: `1DCA8120-13C2-35A5-AB2E-2F9268B18621`
- Source version: `578.40.7.0.0`
- Depends on: [`com.apple.driver.AppleSEPManager`](com.apple.driver.AppleSEPManager.md) 1.0.0, [`com.apple.driver.IOSlaveProcessor`](com.apple.driver.IOSlaveProcessor.md) 1.0.0, [`com.apple.iokit.AppleSEPGenericTransfer`](com.apple.iokit.AppleSEPGenericTransfer.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (20) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `CachedSystemConfig` | 0x20 |  |
| `CachedUserContext` | 0x60 |  |
| `IOBioArrayQueue` | 0x40 | IOBioQueue |
| `IOBioCondition` | 0x18 |  |
| `IOBioPool` | 0x30 |  |
| `IOBioPoolItem` | 0x20 |  |
| `IOBioPoolItemFactory` | 0x18 |  |
| `IOBioQueue` | 0x28 |  |
| `IOBioSEPSharedBuffer` | 0x40 | IOBioPoolItem |
| `IOBioSEPSharedBufferFactory` | 0x30 | IOBioPoolItemFactory |
| `IOBioShareableMemoryObject` | 0x18 |  |
| `IOBioSharedMemoryTransferQueue` | 0x40 | IOBioArrayQueue → IOBioQueue |
| `IOBioUtils` | 0x10 |  |
| `IOBiometricSensorInterface` | 0x1d8 | IOSEPBiometricService → IOBiometricService → IOService → IORegistryEntry |
| `IOBiometricService` | 0x170 | IOService → IORegistryEntry |
| `IOBiometricUserClient` | 0xe0 | IOUserClient → IOService → IORegistryEntry |
| `IOGateLock` | 0x20 |  |
| `IOSEPBiometricService` | 0x1d8 | IOBiometricService → IOService → IORegistryEntry |
| `TaggedMemoryDescriptor` | 0xe8 | IOBufferMemoryDescriptor → IOGeneralMemoryDescriptor → IOMemoryDescriptor |
| `UserTimerEventSource` | 0x68 | IOTimerEventSource → IOEventSource |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1720)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00002c30 off=0x009c09b0-0x009c35e0 addr=0xfffffe00079c49b0-0xfffffe00079c75e0 r--/r--   __TEXT            
	sz=0x0000125b off=0x009c10c8-0x009c2323 addr=0xfffffe00079c50c8-0xfffffe00079c6323               __TEXT.__os_log           
	sz=0x0000129c off=0x009c2323-0x009c35bf addr=0xfffffe00079c6323-0xfffffe00079c75bf               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000020 off=0x009c35c0-0x009c35e0 addr=0xfffffe00079c75c0-0xfffffe00079c75e0               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x0000f678 off=0x03071cf0-0x03081368 addr=0xfffffe000a075cf0-0xfffffe000a085368 r-x/r-x   __TEXT_EXEC       
	sz=0x0000f278 off=0x03071cf0-0x03080f68 addr=0xfffffe000a075cf0-0xfffffe000a084f68          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000400 off=0x03080f68-0x03081368 addr=0xfffffe000a084f68-0xfffffe000a085368          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000420 off=0x049eed70-0x049ef190 addr=0xfffffe000b9f2d70-0xfffffe000b9f3190 rw-/rw-   __DATA            
	sz=0x000000cc off=0x049eed70-0x049eee3c addr=0xfffffe000b9f2d70-0xfffffe000b9f2e3c               __DATA.__data             
	sz=0x00000330 off=0x00000000-0x00000330 addr=0xfffffe000b9f2e40-0xfffffe000b9f3170               __DATA.__common           (Zerofill)
	sz=0x00000020 off=0x00000000-0x00000020 addr=0xfffffe000b9f3170-0xfffffe000b9f3190               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00003c20 off=0x01350ce8-0x01354908 addr=0xfffffe0008354ce8-0xfffffe0008358908 rw-/rw-   __DATA_CONST      
	sz=0x00000048 off=0x01350ce8-0x01350d30 addr=0xfffffe0008354ce8-0xfffffe0008354d30         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000048 off=0x01350d30-0x01350d78 addr=0xfffffe0008354d30-0xfffffe0008354d78         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00003200 off=0x01350d78-0x01353f78 addr=0xfffffe0008354d78-0xfffffe0008357f78         __DATA_CONST.__const            
	sz=0x00000680 off=0x01353f78-0x013545f8 addr=0xfffffe0008357f78-0xfffffe00083585f8         __DATA_CONST.__kalloc_type      
	sz=0x000000a0 off=0x013545f8-0x01354698 addr=0xfffffe00083585f8-0xfffffe0008358698         __DATA_CONST.__kalloc_var       
	sz=0x00000200 off=0x01354698-0x01354898 addr=0xfffffe0008358698-0xfffffe0008358898         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000070 off=0x01354898-0x01354908 addr=0xfffffe0008358898-0xfffffe0008358908         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 142 at 0x04af0c38
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     1DCA8120-13C2-35A5-AB2E-2F9268B18621
008: LC_SOURCE_VERSION           578.40.7.0.0
009: LC_FUNCTION_STARTS          offset=0x004abdf70 size=0x280
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `IOBiometricFamily`
- `CFBundleIdentifier`: `com.apple.iokit.IOBiometricFamily`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOBiometricFamily`
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
- `NSHumanReadableCopyright`: `Copyright © 2018 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOBiometricFamily.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895572560`
- `_PrelinkExecutableRelativePath`: `IOBiometricFamily`
- `_PrelinkExecutableSize`: `90856`
- `_PrelinkExecutableSourceAddr`: `-2198895572560`
- `_PrelinkKmodInfo`: `-2198828274320`

## Strings (278) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__os_log]**

- `IOBiometricService::%s <- inData:%p, outData:%p, outSize:%p\n`
- `IOBioSEPSharedBufferFactory::%s -> result:%d (_bufferSize:%lu)\n`
- `IOBioSharedMemoryTransferQueue::%s: <%d:%s> [QUEUED] obj:%d:%p\n`
- `IOBioArrayQueue::%s <- <%u:%s>\n`
- `IOBiometricUserClient::%s: cleanUpSharedMemoryTransfer\n`
- `Couldn't create OS Log for 'com.apple.BiometricKit.IOSEPBiometricService'!\n`
- `IOBiometricUtilities::%s -> err:0x%x\n`
- `IOBioArrayQueue::%s: <%u:%s> -X-> obj:%s:%p\n`
- `IOBioArrayQueue::%s: <%u:%s> [STATE] capacity:%u, count:%u, releaseWhenFull:%d\n`
- `MCDataMessaging::%s <- dataStruct:%p, dataStructSize:%lu\n`
- `IOBiometricService::%s: Dropping biometric tokens: timerType = %u, now = %llu (%llu s)\n\n`
- `IOBioSharedMemoryTransferQueue::%s -> obj:%d:%p -(%d)-> <%d:%s> (queued:%d)\n`
- `IOSEPBiometricService::%s <- \n`
- `MCDataMessaging::%s <- absoluteTimeId:%llu, outData:%p, outSize:%p\n`
- `MCDataMessaging::%s: Dropping head entry %llu - limit exceeded!\n`
- `IOBiometricService::%s <- \n`
- `IOBioSharedMemoryTransferQueue::%s -> <%d:%s> -X-> obj:%d:%p (queued:%d)\n`
- `IOBioArrayQueue::%s <- <%u:%s> count:%u\n`
- `IOSEPBiometricService::%s: userID = %d, lockState = %d\n`
- `IOBiometricService::%s -> err:0x%x\n`
- `IOSEPSharedBuffer::%s -> (_descriptor:%p, _sepAddress:%llu) -(%d)-> _pool:%p\n`
- `IOSEPBiometricService::%s -> result:%d\n`
- `IOBiometricService::%s <- provider:%p\n`
- `IOBiometricService::%s <- ioSourceEvent: OSP %p\n`
- `IOBioArrayQueue::%s: <%u:%s> [QUEUED] obj:%s:%p\n`
- `IOBiometricUserClient::%s <- type:%lu, options:%lu, memory:%p\n`
- `IOBiometricService::%s: forced:%d, _sharedMemoryTransferNotified:%d\n`
- `IOBiometricService::%s <- userID:%d\n`
- `IOBioSharedMemoryTransferQueue::%s <- <%d:%s> count:%u, type:%u\n`
- `IOBioSharedMemoryTransferQueue::%s: <%d:%s> -X-> obj:%d:%p\n`
- `IOBiometricUserClient::%s -> 0x%x\n`
- `IOSEPBiometricService::%s <- inData:%p\n`
- `MCDataMessaging::%s <- type:0x%lx, version:%lu, argument:%p, argSize:%lu, argData:%p, msgAbsTime:%llu -> err:0x%x\n`
- `IOBiometricService::%s <- inData:%p, outData:%p, outSize:%p --> performCommandGated\n`
- `IOBiometricService::%s: %s (%d) -> %s (%d)\n`
- `IOBiometricService::%s <- sender:%p\n`
- `IOSEPBiometricService::%s -> void\n`
- `MCDataMessaging::%s -> err:0x%x\n`
- `IOBiometricService::%s <- abcReason:%llu\n`
- `IOBiometricService::%s -> void\n`
- `IOBiometricService::%s -> result:%d\n`
- `IOBioSharedMemoryTransferQueue::%s: <%d:%s> [STATE] type:%u, capacity:%u, count:%u/%u\n`
- `IOBioArrayQueue::%s -> obj:%s:%p -(%d)-> <%u:%s> (queued:%d)\n`
- `IOBioArrayQueue::%s -> <%u:%s> -X-> obj:%s:%p (queued:%d)\n`
- `IOSEPBiometricService::%s -> err:0x%x\n`
- `IOSEPBiometricService::%s <- outData:%p\n`
- `IOSEPBiometricService::%s <- sender:%p\n`
- `IOBiometricService::%s: Bytes written = %d\n`
- `Couldn't create OS Log for 'com.apple.BiometricKit.IOBiometricService'!\n`
- `IOBiometricUtilities::%s <- outData:%p, inBuffer:%p, inLength:%zu, outOptBytesWritten:%p\n`
- `IOBioArrayQueue::%s <- <%u:%s> -X-X (count:%u)\n`
- `IOSEPBiometricService::%s <- provider:%p\n`
- `MCDataMessaging::%s <- \n`
- `MCDataMessaging::%s: Request %llu newer than head %llu, dropping head entry...\n`
- `IOBiometricService::%s: timerType = %u, seconds = %lu, now = %llu (%llu s)\n\n`
- `IOSEPSharedBuffer::%s <- _pool:%p -X-> (_descriptor:%p, _sepAddress:%llu)\n`
- `IOBioArrayQueue::%s -> <%u:%s>: result:%d (_capacity:%u, _releaseWhenFull:%d)\n`
- `IOBiometricUserClient::%s <- \n`

**[__TEXT.__cstring]**

- `site.CachedUserContext`
- `bioTokenExpirationHandler`
- `memory`
- `freeTimerEventSource`
- `site.IOBioPool`
- `_lockState != 0`
- `sksQueueEnqueue`
- `powerOff`
- `site.IOBiometricService`
- `bioMatchExpirationHandler`
- `IOBiometricUtilities.cpp`
- `free`
- `sepEndpoint->removeVisibleMemory(_sepMapping) == 0 `
- `dequeueShareableMemoryObject`
- `releaseAllObjects`
- `initWithService`
- `outMap`
- `allocName`
- `_shareableMemoryDescriptor`
- `inMap->getLength() <= 4294967295U`
- `ctx`
- `powerOn`
- `121`
- `site.IOBioUtils`
- `i16@?0Q8`
- `CachedSystemConfig`
- `site.CachedSystemConfig`
- `notifySharedMemoryTransfer`
- `writeBytesToIOMD`
- `headerBuffer->getLength() == (1 << PAGE_SHIFT_CONST)`
- `headerBuffer->prepare() == 0 `
- `transfer->count < kBufferCountLimit`
- `BgPresenceDetect`
- `site.IOBioPoolItem`
- `site.TaggedMemoryDescriptor`
- `descriptorCount == memoryDescriptors->getCount() + 1`
- `enqueueObject`
- `IOBiometricUserClient.cpp`
- `11`
- `dataStruct`
- `provider`
- `bounded_array_ref: Can't construct from a size greater than UINT32_MAX`
- `\"%s\" @%s:%d`
- `IOBioPool.cpp`
- `IOBioUtils`
- `outData`
- `122222221111`
- `_bioTokenExpirationEventSource`
- `count == inLength`
- `12121112`
- `sepEndpoint`
- `transfer->type != kBioSharedMemoryTransferNone`
- `headerBuffer->writeBytes(headerOffset, header, headerSize) == headerSize`
- `descriptors[descriptorCount]`
- `1211121`
- `_passcodeInputExpirationEventSource`
- `_commandGate`
- `*busyState != 0`
- `headerBuffer`
- `descriptors`
- `object`
- `B16@?0^{OSObject=^^?i}8`
- `site.UserTimerEventSource`
- `121211`
- `site.IOBioSEPSharedBufferFactory`
- `headerBuffer->complete() == 0 `
- `IOBiometricUserClient`
- `sksQueueDequeue`
- `sksLockStateChangeHandler`
- `_sksStateChangeEventSource`
- `source`
- `service`
- `performCommand`
- `getNextSharedMemoryTransfer`
- `forceBioLockout`
- `The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range`
- `IOBioMemorySharing.cpp`
- `releaseObjects`
- `MCDataMessagingKernel.cpp`
- `queue`
- `getLastSharedMemoryTransfer`
- `Unknown`
- `IOBioPool`
- `site.IOGateLock`
- `IOBioQueue`
- `site.MCDataQueueEntry`
- `None`
- `12112121212212132213211121212`
- `_descriptor`
- `init`
- `memoryDescriptors`
- `site.IOMemoryDescriptor *`
- `osLogQueue`
- `site.IOBioPoolItemFactory`
- `cmd`
- `Match`
- `Count`
- `12111112122212121121211111111111111111111121121122222222122`
- `inBuffer`
- `IOBioSEPSharedBuffer.cpp`
- `121112`
- `site.T`
- `err == 0 `
- `dropUnlockToken(ctx->getUserID()) == 0 `
- `userAccountsInfo->currentAccountUserID != 4294967295U`
- `IOBioShareableMemoryObject`
- `osLogObject`
- `removeObjectAtIndex`
- `_lock`
- `1211121111212`
- `inLength <= outData->getLength()`
- `TaggedMemoryDescriptor`
- `IOBioSEPSharedBufferFactory`
- `1`
- `IOBioSharedMemoryTransferQueue`
- `releaseObjects_block_invoke`
- `_service`
- `dataStructSize > argSize`
- `enqueueData`
- `_availableItems`
- `IOBioArrayQueue`
- `site.IOBiometricUserClient`
- `_sksQueueCount < 10`
- `sksQueueProcess`
- `Idle`
- `OSBoundedPtr.h`
- `bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally`
- `_availableItems->setObject(poolItem)`
- `site.IOBioQueue`
- `IOSEPBiometricService`
- `sksQueueInit`
- `IOBiometricService`
- `lockCommandAccess`
- `switchCommandMode`
- `pool`
- `IOBioPoolItem::init(pool)`
- `site.IOBioSharedMemoryTransferQueue`
- `IOBioQueue::init(name)`
- `site.IOSEPBiometricService`
- `matchingBlock`
- `IOSEPBiometricService.cpp`
- `_sep`
- `userID != 4294967295U`
- `_releaseWhenFull`
- `resetTimer`
- `IOGateLock`
- `site.IOBioSEPSharedBuffer`
- `0`
- `argument`
- `IOBiometricService.cpp`
- `_bioMatchExpirationEventSource`
- `inMap`
- `site.IOBiometricSensorInterface`
- `factory`
- `result`
- `unlockCommandAccess`
- `buffer`
- `releaseObjects(1)`
- `releaseMatchingObjects`
- `clientMemoryForType`
- `messageClients`
- `AssertMacros: %s (value = 0x%lx), version: BiometricKit-578.40.7~2324, %s file: %s, line: %d\n`
- `_sharedMemoryTransferObject`
- `sendAutoBugCaptureEvent`
- `site.IOBioShareableMemoryObject`
- `IOBioQueue.cpp`
- `pullMessageData`
- `1211111212221212112121111111111111111111112112`
- `cmd->magic == getBiometricCommandMagic()`
- `bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow.`
- `IOBioPoolItem`
- `B24@?0^{OSObject=^^?i}8^B16`
- `releaseAllObjects_block_invoke`
- `mem`
- `com.apple.BiometricKit`
- `_commandAccess`
- `poolItem`
- `IOBioSEPSharedBuffer`
- `size`
- `transfer->count > 0`
- `transferQueue`
- `name`
- `enqueueData(dataStruct, dataStructSize) == 0 `
- `CachedUserContext`
- `1222`
- `inData`
- `This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.`
- `IOBioCondition`
- `iteratorBlock`
- `1211111212221212111111111112`
- `userAccountsInfo`
- `headerOffset + headerSize <= headerBuffer->getLength()`
- `site.IOBioArrayQueue`
- `sksQueueProcessAsync`
- `v12@?0i8`
- `bounded_ptr<T>::discard_bounds: Discarding the bounds on this pointer would lose the fact that it is outside of the bounds set originally`
- `capacity`
- `~MCDataMessaging`
- `size >= sizeof(bm_cmd_t)`
- `passcodeInputExpirationHandler`
- `stop`
- `site.IOBioCondition`
- `12`
- `_array`
- `timer`
- `performCommandGated`
- `sender`
- `start`
- `IOBiometricSensorInterface`
- `1212`
- `_allocatedCount == 0`
- `smObject`
- `_cachedSysConfig`
- `UserTimerEventSource`
- `initialized`
- `Enroll`
- `PresenceDetect`
- `OSObject::init()`
- `IOBioPoolItemFactory`
- `12121`
