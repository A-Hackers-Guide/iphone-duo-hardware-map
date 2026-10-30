# `com.apple.iokit.IOGPUFamily`

- Name: IOGPUFamily
- Version: `162.16.1`
- UUID: `BEBC575D-83BF-35F8-A4CF-E789DF197BE2`
- Source version: `162.16.1.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleMobileFileIntegrity`](com.apple.driver.AppleMobileFileIntegrity.md) 1.0.1, [`com.apple.iokit.IOReportFamily`](com.apple.iokit.IOReportFamily.md) 1.0, [`com.apple.iokit.IOSurface`](com.apple.iokit.IOSurface.md) 52.6.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 9.0.0b1, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 9.0.0b1, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 9.0.0b1, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 9.0.0b1, [`com.apple.kpi.private`](com.apple.kpi.private.md) 9.0.0b1, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 9.0.0b1

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (51) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOAccelGPURestartReport` | 0x88 | IOService → IORegistryEntry |
| `IOAcceleratorES` | 0x88 | IOService → IORegistryEntry |
| `IOGPU` | 0x2f0 | IOAcceleratorES → IOService → IORegistryEntry |
| `IOGPUAllocationInfo` | 0x430 |  |
| `IOGPUBlockFence` | 0x130 | IOGPUEventFence |
| `IOGPUBlockFencePort` | 0x58 |  |
| `IOGPUBufferMemoryDescriptor` | 0xe8 | IOBufferMemoryDescriptor → IOGeneralMemoryDescriptor → IOMemoryDescriptor |
| `IOGPUChannel` | 0x38 |  |
| `IOGPUClientSharedMachine` | 0x60 |  |
| `IOGPUCommandDescriptor` | 0x140 | IOGPUObject |
| `IOGPUCommandQueue` | 0x5d0 | IOGPUObject |
| `IOGPUDevice` | 0x120 | IOGPUObject |
| `IOGPUDeviceAssertion` | 0x28 | IOGPUObject |
| `IOGPUDeviceShmem` | 0x68 | IOGPUKernelMappedMemory → IOGPUObject |
| `IOGPUDeviceUserClient` | 0x130 | IOUserClient → IOService → IORegistryEntry |
| `IOGPUEventFence` | 0xd0 |  |
| `IOGPUEventMachine` | 0x1450 |  |
| `IOGPUFenceMachine` | 0x78 |  |
| `IOGPUGroupMemory` | 0x130 | IOGPUMemory → IOGPUObject |
| `IOGPUIOCommandBuffer` | 0x70 | IOGPUObject |
| `IOGPUIOCommandDescriptor` | 0x58 | IOGPUObject |
| `IOGPUIOCommandQueue` | 0xb0 | IOGPUObject |
| `IOGPUKernelMappedMemory` | 0x40 | IOGPUObject |
| `IOGPUMTLEvent` | 0x290 | IOGPUObject |
| `IOGPUMTLFence` | 0x120 | IOGPUObject |
| `IOGPUMTLLateEvalEvent` | 0x28 | IOGPUObject |
| `IOGPUMappingCommand` | 0x40 | IOGPUObject |
| `IOGPUMappingCommandDescriptor` | 0x180 | IOGPUCommandDescriptor → IOGPUObject |
| `IOGPUMappingFence` | 0xd8 | IOGPUEventFence |
| `IOGPUMemory` | 0x80 | IOGPUObject |
| `IOGPUMemoryInfoUserClient` | 0xe8 | IOUserClient → IOService → IORegistryEntry |
| `IOGPUMemoryMap` | 0x48 | IOGPUObject |
| `IOGPUMultiMemoryDescriptor` | 0x78 | IOMultiMemoryDescriptor → IOMemoryDescriptor |
| `IOGPUNamespace` | 0x38 | IOGPUWeakNamespace |
| `IOGPUNotificationQueue` | 0x30 | IOGPUObject |
| `IOGPUObject` | 0x10 |  |
| `IOGPUResource` | 0xa0 | IOGPUObject |
| `IOGPUResourceSet` | 0x30 |  |
| `IOGPUScheduler` | 0x250 |  |
| `IOGPUSegmentResourceList` | 0x10 |  |
| `IOGPUSharedEventFence` | 0xe0 | IOGPUEventFence |
| `IOGPUStatistics` | 0x30 |  |
| `IOGPUSubMemoryDescriptor` | 0x78 | IOSubMemoryDescriptor → IOMemoryDescriptor |
| `IOGPUSysMemory` | 0xe8 | IOGPUMemory → IOGPUObject |
| `IOGPUTask` | 0x1d0 | IOGPUObject |
| `IOGPUVirtualMemory` | 0xd8 | IOGPUMemory → IOGPUObject |
| `IOGPUVnioDesc` | 0x28 | IOGPUObject |
| `IOGPUWeakNamespace` | 0x38 |  |
| `IOGPUWeakResourceSet` | 0x30 | IOGPUResourceSet |
| `IOGPUWorkQueue` | 0x100 | IOGPUObject |
| `IOGPUWorkQueueState` | 0xb8 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1880)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000bdec off=0x009da440-0x009e622c addr=0xfffffe00079de440-0xfffffe00079ea22c r--/r--   __TEXT            
	sz=0x000062b2 off=0x009dabf8-0x009e0eaa addr=0xfffffe00079debf8-0xfffffe00079e4eaa               __TEXT.__cstring          (CstringLiterals)
	sz=0x000052f6 off=0x009e0eaa-0x009e61a0 addr=0xfffffe00079e4eaa-0xfffffe00079ea1a0               __TEXT.__os_log           
	sz=0x0000008c off=0x009e61a0-0x009e622c addr=0xfffffe00079ea1a0-0xfffffe00079ea22c               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x000434c0 off=0x030f3b70-0x03137030 addr=0xfffffe000a0f7b70-0xfffffe000a13b030 r-x/r-x   __TEXT_EXEC       
	sz=0x00042700 off=0x030f3b70-0x03136270 addr=0xfffffe000a0f7b70-0xfffffe000a13a270          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000dc0 off=0x03136270-0x03137030 addr=0xfffffe000a13a270-0xfffffe000a13b030          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000d01 off=0x049efdd0-0x049f0ad1 addr=0xfffffe000b9f3dd0-0xfffffe000b9f4ad1 rw-/rw-   __DATA            
	sz=0x00000460 off=0x049efdd0-0x049f0230 addr=0xfffffe000b9f3dd0-0xfffffe000b9f4230               __DATA.__data             
	sz=0x00000898 off=0x00000000-0x00000898 addr=0xfffffe000b9f4230-0xfffffe000b9f4ac8               __DATA.__common           (Zerofill)
	sz=0x00000009 off=0x00000000-0x00000009 addr=0xfffffe000b9f4ac8-0xfffffe000b9f4ad1               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00009c38 off=0x0136d6b8-0x013772f0 addr=0xfffffe00083716b8-0xfffffe000837b2f0 rw-/rw-   __DATA_CONST      
	sz=0x00000100 off=0x0136d6b8-0x0136d7b8 addr=0xfffffe00083716b8-0xfffffe00083717b8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000100 off=0x0136d7b8-0x0136d8b8 addr=0xfffffe00083717b8-0xfffffe00083718b8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00006fd8 off=0x0136d8b8-0x01374890 addr=0xfffffe00083718b8-0xfffffe0008378890         __DATA_CONST.__const            
	sz=0x000011c0 off=0x01374890-0x01375a50 addr=0xfffffe0008378890-0xfffffe0008379a50         __DATA_CONST.__kalloc_type      
	sz=0x00001090 off=0x01375a50-0x01376ae0 addr=0xfffffe0008379a50-0xfffffe000837aae0         __DATA_CONST.__kalloc_var       
	sz=0x00000028 off=0x01376ae0-0x01376b08 addr=0xfffffe000837aae0-0xfffffe000837ab08         __DATA_CONST.__assert           
	sz=0x000006e0 off=0x01376b08-0x013771e8 addr=0xfffffe000837ab08-0xfffffe000837b1e8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000100 off=0x013771e8-0x013772e8 addr=0xfffffe000837b1e8-0xfffffe000837b2e8         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000008 off=0x013772e8-0x013772f0 addr=0xfffffe000837b2e8-0xfffffe000837b2f0         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 472 at 0x04af1994
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     BEBC575D-83BF-35F8-A4CF-E789DF197BE2
008: LC_SOURCE_VERSION           162.16.1.0.0
009: LC_FUNCTION_STARTS          offset=0x004abf238 size=0x9d0
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `IOGPUFamily`
- `CFBundleIdentifier`: `com.apple.iokit.IOGPUFamily`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOGPUFamily`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `162.16.1`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `162.16.1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2010-2019 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `2.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOGPUFamily.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895467456`
- `_PrelinkExecutableRelativePath`: `IOGPUFamily`
- `_PrelinkExecutableSize`: `367589`
- `_PrelinkExecutableSourceAddr`: `-2198895467456`
- `_PrelinkKmodInfo`: `-2198828270128`

## Strings (922) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `1211111211221`
- `12211111121111222211`
- `IOGPUDeviceAssertion`
- `IOReturn IOGPUDevice::resource_replace_backing_bytes(sIOGPUReplaceBackingBytesData *)`
- `IOGPUStatistics`
- `Devices`
- `12111111111`
- `12111111212112222222222111122211122222111112111222222111122212222122222221`
- `In use system memory`
- `IOGPUFamily Parameters`
- `Dynamic Wired Low Water Mark Enable`
- `AppPath`
- `IOGPU Completion`
- `iogpu_disable_restart_limit`
- `virtual void IOGPUCommandQueue::submitCommandBuffer(const sIOGPUCommandQueueCommandBufferArgs *)`
- `static OSSharedPtr<IOMemoryDescriptor> IOGPUSysMemory::memoryDescriptorWithClientBuffer(task_t, mach_vm_address_t, uint64_t)`
- `nbits > 0`
- `\"Memory object must be Resident\" @%s:%d`
- `\"Merge from non-scrubbed src event %p\\n\" @%s:%d`
- `IOGPUKernelMappedMemory`
- `\"IOGPUResource::free called for resource still owned by an IOGPUDevice\" @%s:%d`
- `IOReturn IOGPUResource::replace_backing_ranges(task_t, mach_vm_address_t, uint64_t, bool, bool, uint64_t *)`
- `IOGPU Submission`
- `[idx:%d, %d]`
- `com.apple.private.iogpu.disable_wired_collector`
- `IOGPU`
- `site.IOGPUFenceMachine`
- `virtual bool IOGPUResource::init(IOGPU *, IOGPUDevice *, uint32_t)`
- `\"decrement_gart_collector_disable_count() fGARTCollectorDisableCount underflow\" @%s:%d`
- `Stamps`
- `wq_timeout_sec`
- `virtual void IOGPUCommandQueue::processCommandBuffer(const sIOGPUCommandQueueCommandBufferArgs *)`
- `virtual void IOGPUCommandQueue::processKernelCommand(const sIOGPUKernelCommand *, const sIOGPUKernelCommand *)`
- `IOGPUCommandQueue.cpp`
- `bool IOGPUIOCommandBuffer::getIOCommands(sIOGPUIOCommandListHead *)`
- `\"pending memory object unexpectedly found in non pending hash\" @%s:%d`
- `IOGPUCommandDescriptor`
- `metal4_disable_async_mapping`
- `site.struct HashEntry`
- `IOAccelSurfaceBufferIndex`
- `Virtual`
- `IOReturn IOGPUScheduler::freeToWireMemory(IOGPUMemory *)`
- `12212`
- `Metal Device Shmem`
- `Trying to restart GPU (%s)...\n`
- `IOGPUVnioDesc`
- `com.apple.private.agx.rt-priority-spi`
- `void IOGPUIOCommandBuffer::processKernelCommands(uint32_t)`
- `site.IOGPUTask`
- `com.apple.private.ioaccelmemoryinfo`
- `IOGPUObject.cpp`
- `IOGPUResource`
- `site.IOGPUWorkQueueState`
- `IOReturn IOGPUDevice::resource_replace_backing_ranges(sIOGPUReplaceBackingRangesData *, uint64_t *)`
- `1211111212221212121111111212211121222221111112112211122111112122222222222222222222222222122212`
- `\"IOGPU::systemPagingOff() timeout. %d threads still stuck. addCommandToTail_slow %u, waitForAllSubmitted %u, workQueuesDisabled %u, waitingOnResources %u, waitForStamp %u, wireMemory %u\\n\" @%s:%d`
- `IOReturn IOGPUDeviceUserClient::t_signal_shared_event(uintptr_t, uintptr_t, uintptr_t, uintptr_t)`
- `IOGPUBlockFence`
- `site.IOGPUSegmentResourceList`
- `com.apple.iokit.IOGPUFamily.API`
- `\"Timeout SharedEvent: %s: Shared event wait timed out for value : %llx\" @%s:%d`
- `IOReturn IOGPUDeviceUserClient::t_signal_mtl_event(uintptr_t, uintptr_t, uintptr_t, uintptr_t)`
- `site.IOAcceleratorES`
- `site.IOGPUKernelMappedMemory`
- `\"Unexpected memory type\" @%s:%d`
- `IOGPUSysMemory.cpp`
- `\"failed to allocate memory\" @%s:%d`
- `static IOReturn IOGPUDeviceUserClient::s_submit_command_buffers(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `virtual int32_t IOGPUEventMachine::requestStampIndexForChannel(IOGPUChannel *, IOGPUDevice *)`
- `Metal 4 Disable Async Mapping`
- `Size`
- `site.IOGPUChannel`
- `site.IOGPUEventMachine`
- `IOGPUIOCommandQueue`
- `wired_limit_mb`
- `GARTReclaimInterval`
- `virtual OSPtr<IOGPUMemoryMap> IOGPUMemory::createGPUMappingInTaskAtAddressLengthAlignment(IOGPUTask *, uint64_t, uint64_t, uint64_t, uint32_t)`
- `\"IOGPUMemory::detach() memory still prepared\\n\" @%s:%d`
- `IOGPUMemoryDecriptor.cpp`
- `dynamic_lwm`
- `IOGPUMetalEvent.cpp`
- `static OSPtr<IOGPUResource> IOGPUResource::newResourceWithIOSurfaceDeviceCache(IOGPU *, IOSurfaceDeviceCache *)`
- `\"add_group_resources_fast() count overflow\" @%s:%d`
- `\n`
- `IOGPUScheduler.cpp`
- `gpu`
- `122112211`
- `\"IOGPUMemory::dealloc() memory still prepared\\n\" @%s:%d`
- `MemoryPool`
- `12112121212212132213211121212`
- `IOReturn IOGPUIOCommandQueue::performIO()`
- `SchedulerState`
- `Immunity for`
- `IOReturn IOGPUCommandQueue::schedule_shared_event(mach_port_name_t, uint64_t, bool, uint32_t)`
- `\"IOGPUResidentMemorySet unable to expand\" @%s:%d`
- `DirtySize`
- `virtual IOReturn IOGPUVirtualMemory::updateMemoryAtIndexLocked(uint32_t, IOMemoryDescriptor *)`
- `IOGPUSharedEventFence`
- `IOReturn IOGPUIOCommandQueue::destroyIOCommandBuffer(uint32_t)`
- `IOGPUWorkQueue`
- `IOGPUWorkQueueState`
- `com.apple.developer.gpu-restricted`
- `recoveryCount`
- `bits.h`
- `%s idx%d`
- `IOGPUClientSharedMachine`
- `\"%s: active mapping list not empty\\n\" @%s:%d`
- `IOAcceleratorES`
- `debug_flags`
- `12111112122212121111111111121`
- `\"m_count not zero after releaseValue()\" @%s:%d`
- `\"Unable to move pending memory object to main hash\" @%s:%d`
- `GPURestartReport`
- `\"os_refcnt: underflow (rc=%p)\\n\" @%s:%d`
- `\"Illegal resource type\" @%s:%d`
- `\"increment_gart_collector_disable_count() fGARTCollectorDisableCount overflow\" @%s:%d`
- `\"Didn't complete expected number of memory objects\" @%s:%d`
- `IOGPUSegmentResourceList`
- `hw.memsize_physical`
- `IOReturn IOGPUSysMemory::replace_backing_bytes_locked(task_t, mach_vm_address_t, uint64_t)`
- `IOSurface`
- `\"Unable to remove just added resource after addMemoryFromResources failure\" @%s:%d`
- `virtual bool IOGPUIOCommandBuffer::init(IOGPUIOCommandQueue *)`
- `virtual bool IOGPUIOCommandQueue::init(IOGPUDevice *, uint32_t, uint32_t)`
- `\"Timeout MTLEvent: waiting for signal (%llu) for event (%u) to be scheduled\" @%s:%d`
- `\"Didn't move expected number of pending objects.\" @%s:%d`
- `iogpu_force_mapped_memory`
- `\"Timeout SharedEvent: Cmd queue %p sleep port_name %d value: %08llx timed out!\" @%s:%d`
- `IOGPUMappingFence`
- `121222222222222222222211121`
- `\"%s: IOGPUTask unexpectedly freed\\n\" @%s:%d`
- `virtual IOReturn IOGPUVirtualMemory::wire()`
- `\"IOGPUBufferMemoryDescriptor does not support taggedRelease with when != 1\" @%s:%d`
- `12111112122212121111111111112211211212`
- `121112122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111211211211211211211211211211211211`
- `IOGPUEventFence`
- `Unknown`
- `\"Didn't remove expected number of objects from the main hash.\" @%s:%d`
- `iogpu_no_throttled_multi_kick`
- `IOGPUIOCommandBuffer`
- `IOGPUDevice`
- `disable_wired_collector`
- `Metal`
- `\"IOGPUMTLEvent::clean_ring() read overflow\" @%s:%d`
- `NO`
- `GL/CL`
- `site.IOAddressRange`
- `AppUsage`
- `site.IOGPUEventFence`
- `12122222222222222222221112`
- `IOReturn IOGPUSysMemory::replace_backing_ranges_locked(task_t, IOAddressRange *, uint32_t, bool)`
- `SysMemShared`
- `void IOGPUAllocationInfo::declareIOSurfaceBackingStoreWithName(IOMemoryDescriptor *, OSString *, uint32_t, int *, int)`
- `\"%s: Failed to complete memory descriptor(%p) at index %u\" @%s:%d`
- `virtual void IOGPUVirtualMemory::updateResidencyData(uint32_t, uint8_t)`
- `site.IOGPUSharedEventFence`
- `Group`
- `API`
- `\"IOGPUMultiMemoryDescriptor does not support taggedRelease with when != 1\" @%s:%d`
- `site.IOGPUSubMemoryDescriptor`
- `\"Active Command Buffer Not Empty on IOGPUIOCommandQueue free\" @%s:%d`
- `IOGPUCommandDescriptor.cpp`
- `ANE Buffer id 0x%x`
- `IOGPUVirtualMemory`
- `IOGPUSysMemory *IOGPUResource::owns_replaceable_backing() const`
- `added`
- `121121211211112222222222222222222212222211121120`
- `IOGPUWeakResourceSet`
- `wq_stall_panic_seconds`
- `IOGPUSysMemory`
- `IOGPUObject`
- `121111121111112`
- `iogpu`
- `ResidentSize`
- `static IOReturn IOGPUDeviceUserClient::s_create_vniodesc(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `12212222111211`
- `site.IOGPUWorkQueue`
- `PerformanceStatistics`
- `hw.memsize`
- `AllocationIdentifiers`
- `site.IOGPUDevice`
- `\"%s: 0x%X mapping is not valid for wireRange, cannot unwire PTEs\" @%s:%d`
- `IOGPUEventMachine.cpp`
- `state`
- `IOGPUMTLEvent`
- `site.sIOGPUUserEvents`
- `lastRecoveryTime`
- `bool IOGPUResourceSet::add_resource_slow(IOGPUResource *)`
- `Listing all allocated maps:\n`
- `Descriptions`
- `site.struct IOGPUDeviceUserClientPrivate`
- `IOReturn IOGPUDevice::resource_detach_backing(uint32_t)`
- `iogpu_single_sysmem_pct`
- `site.IOGPUCommandQueuePrivate`
- `static OSSharedPtr<IOMemoryDescriptor> IOGPUSysMemory::memoryDescriptorWithClientRanges(task_t, IOAddressRange *, uint32_t, bool)`
- `Aliased Virtual Resource (Virtual Size = %llu bytes)`
- `IOGPUFenceMachine`
- `[idx:%d, stamp:%d]`
- `Idle`
- `IOGPUMappingCommand`
- `static OSPtr<IOGPUResource> IOGPUResource::newResourceWithIOSurface(IOGPU *, IOGPUDevice *, IOSurface *, uint32_t, uint32_t)`
- `virtual void IOGPUScheduler::progressTimerCheckInterrupt()`
- `IOGPUTask`
- `IOSurface Backing Store`
- `site.IOGPUMemoryMap *`
- `\"completeMemory() prepare count underflow\" @%s:%d`
- `IOReturn IOGPUDeviceUserClient::t_wait_shared_event(uintptr_t, uintptr_t, uintptr_t, uintptr_t, uintptr_t)`
- `IOGPUDeviceAssertion.cpp`
- `OSPtr<OSArray> IOGPU::createAllocationList()`
- `\"shmemOffset value is corrupt\" @%s:%d`
- `site.IOGPUVnioDesc`
- `Alloc system memory`
- `kernel_task`
- `site.IOGPUIOCommandQueue`
- `virtual void IOGPUCommandQueue::signalSharedEvent(IOSurfaceSharedEvent *, uint64_t)`
- `IOAccelSurfaceWidth`
- `static IOReturn IOGPUDeviceUserClient::s_destroy_io_command_queue(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `12111111222122222222222212200000`
- `%s enter: fRingBuffer=%p, fNumRingEntries=%u, fRingGPUFinishedCount=%u, fRingGPUSubmittedCount=%u.\n`
- `\"Memory object not found in fMemoryCountedSet or fPendingMemorySet\" @%s:%d`
- `PID`
- `IOAccelSurfaceHeight`
- `site.IOGPUSysMemory`
- `IOGPUMemory`
- `Undefined`
- `\"IOGPUFenceMachine: block fence %p appears stuck after creation\" @%s:%d`
- `IOReturn IOGPUIOCommandQueue::createIOCommandBuffer(uint64_t *, uint64_t *)`
- `\"Unable to remove just added key\" @%s:%d`
- `\"Unexpected number of memory objects completed\" @%s:%d`
- `IOReturn IOGPUResource::updateMappings(OSSharedPtr<IOGPUResource>, sIOGPUMappingOp *, uint32_t, IOOptionBits)`
- `1211211222222222222222222222222222222221111111111111111112`
- `IOGPUDevice.cpp`
- `gpu_no_zero_fill`
- `virtual IOMemoryDescriptor **IOGPUSysMemory::get_memory_descriptors(uint32_t, IOOptionBits, uint32_t *)`
- `IOAccelGPURestartReport`
- `site.IOGPUMappingFence`
- `virtual void *IOGPUKernelMappedMemory::getKernelData()`
- `\"Unexpected pending memory objects\" @%s:%d`
- `122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211222211111112222222222222222212111222222211222222222`
- `site.IOGPUMemoryInfoUserClient`
- `1`
- `112`
- `static OSPtr<IOGPUResource> IOGPUResource::newResourceWithClientAddressRanges(IOGPU *, IOGPUDevice *, mach_vm_address_t *, IOGPUNewResourceArgs *)`
- `12111112122212121`
- `IOGPUResource.cpp`
- `\"IOGPUDeviceAssertion::initWithAccelerator Unsupported assertionType %lld\" @%s:%d`
- `bool IOGPUScheduler::init(IOGPU *)`
- `Internal Statistics`
- `\tmapping=%p, address=0x%llx, size=0x%llx\n`
- `%s`
- `site.IOGPUNotificationQueue`
- `IOGPUGroupMemory.cpp`
- `\"Invalid Mapping Command\" @%s:%d`
- `site.IOGPUMappingCommandDescriptor`
- `121222222121112222212111112`
- `IOGPUWeakNamespace`
- `12`
- `site.IOClientSharedListEntry`
- `bool IOGPUCommandDescriptor::retainObject(const OSObject *)`
- `virtual void IOGPUCommandQueue::waitSharedEvent(IOSurfaceSharedEvent *, uint64_t, uint32_t)`
- `IOAccelSurfacePixelFormat`
- `bool IOGPUFenceMachine::init(IOGPU *)`
- `site.IOGPUIOCommandDescriptor`
- `Last GPU Restart`
- `IOGPUCommandQueue`
- `site.IOMemoryDescriptor *`
- `virtual void IOGPUVirtualMemory::unwire()`
- `static IOReturn IOGPUDeviceUserClient::s_group_add_resources(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `\"os_refcnt: overflow (rc=%p)\\n\" @%s:%d`
- `111122222`
- `Mappings`
- `\"IOGPUMultiMemoryDescriptor does not support release with when != 1\" @%s:%d`
- `IOGPUSubMemoryDescriptor`
- `void IOGPUScheduler::hardware_error_interrupt(IOInterruptEventSource *, int)`
- `spin_wait_for_gpu`
- `GPUSubmissionTraceID`
- `121121212122122`
- `static IOReturn IOGPUDeviceUserClient::s_set_io_notification_queue(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `com.apple.private.graphics-restart-no-kill`
- `%llx`
- `IOGPUResidentSet.cpp`
- `static OSPtr<IOGPUSysMemory> IOGPUSysMemory::withOptions(IOGPU *, task_t, IOGPUDevice *, IOGPUResource *, IOOptionBits, uint64_t, uint64_t, task_t)`
- `virtual IOReturn IOGPUSysMemory::wire()`
- `IOGPUNamespace.cpp`
- `IOGPUMTLFence`
- `\"IOGPUFenceMachine: block fence %p appears stuck after starting\" @%s:%d`
- `IOGPUCountedMap.h`
- `IOReturn IOGPUDeviceUserClient::t_wait_mtl_event(uintptr_t, uintptr_t, uintptr_t, uintptr_t, uintptr_t)`
- `submitted`
- `iogpu_sysmem_mb`
- `void IOGPU::terminateQueues()`
- `IOReturn IOGPUCommandQueue::setNotificationQueue(IOGPUNotificationQueue *)`
- `virtual void IOGPUCommandQueue::processSegmentKernelCommand(IOGPUSegmentResourceList *, const sIOGPUKernelCommand *, const sIOGPUKernelCommand *, const uint8_t *, const uint8_t *, const sIOGPUCommandQueueCommandBufferArgs *)`
- `IOGPUWorkQueue.cpp`
- `12122222222222222222222`
- `int32_t IOGPUScheduler::registerCommandQueue(const IOGPUCommandQueue *)`
- `site.IOGPUResourceSet`
- `panic_on_gpu_hang`
- `GARTCacheSize`
- `\"sideband buffer shmem no longer mapped\" @%s:%d`
- `virtual bool IOGPUVirtualMemory::init(IOGPU *, uint64_t, uint32_t, bool, uint64_t, uint64_t, task_t)`
- `SysMemPrivate`
- `IOAccelSurfaceID`
- `const sIOGPUEvent *IOGPUResource::gartEvent() const`
- `iogpu_wired_lwm_mb`
- `12122222212111222112121112221`
- `site.IOBufferMemoryDescriptor *`
- `site.IOGPUMappingCommand`
- `121`
- `1211222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `1212122`
- `IOGPUMultiMemoryDescriptor`
- `\"Excessive time stalled (>%ds) in IOGPUWorkQueue::waitForAllSubmitted()\" @%s:%d`
- `site.IOGPUClientSharedMachine`
- `IOGPUTask.cpp`
- `site.IOGPUCountedMap`
- `BusyWorkQueues`
- `virtual void IOGPUCommandQueue::processSegmentKernelCommands(IOGPUSegmentResourceList *, const sIOGPUKernelCommand *, const sIOGPUKernelCommand *, const uint8_t *, const uint8_t *, const sIOGPUCommandQueueCommandBufferArgs *)`
- `virtual void IOGPUVirtualMemory::describeAllocation(OSDictionary *)`
- `bool IOGPU::validateConfigStructure()`
- `site.IOGPUMultiMemoryDescriptor`
- `site.IOGPUResource *`
- `id`
- `iogpu_no_check_descriptor_size`
- `\"Timeout SharedEvent: Cmd queue %p sleep port_name %d value: %08llx timed out waiting for prior signals!\" @%s:%d`
- `IOReturn IOGPUResource::copyMappings(OSSharedPtr<IOGPUResource>, sIOGPUMappingOp *, uint32_t, IOOptionBits)`
- `\"Unbalanced call to enableWorkQueues() %d\\n\" @%s:%d`
- `foreground`
- `12122222212111221111122222211111222222`
- `iogpu_debug`
- `Report`
- `IOReturn IOGPUVirtualMemory::copyMemoryAtIndexAndLength(IOGPUVirtualMemory *, uint32_t, uint32_t, uint32_t)`
- `site.IOGPUBufferMemoryDescriptor`
- `121122`
- `site.IOGPUWeakResourceSet`
- `lastSubmittedTime`
- `\"segment list shmem no longer mapped\" @%s:%d`
- `\"IOGPUEventMachine::waitForStamp: Stamp test failed, but all submitted stamps are finished.  stamp[%08x]: %08x gpu_stamp: %08x\" @%s:%d`
- `static OSPtr<IOGPUResource> IOGPUResource::newResourceGroup(IOGPU *, IOGPUDevice *, uint32_t)`
- `\"Excessive time stalled (>%ds) in IOGPUWorkQueue::addCommandToTail_slow()\" @%s:%d`
- `v16@?0^{IOTimerEventSource=^^?i^{IOEventSource}^{OSObject}^?B^{IOWorkLoop}^v^{ExpansionData}^vQ^{ExpansionData}}8`
- `IOCoreSurfaceRoot`
- `site.ResidentEntry`
- `12111112`
- `virtual void IOGPUSysMemory::describeAllocation(OSDictionary *)`
- `12122222222222222222221112222121222222`
- `virtual void IOGPUIOCommandBuffer::processKernelCommand(const sIOGPUIOKernelCommand *, const sIOGPUIOKernelCommand *)`
- `11111222222`
- `In use system memory (driver)`
- `site.OSObject *`
- `Wired Limit Megabytes`
- `IOGPUAllocationInfo`
- `static OSPtr<IOGPUSysMemory> IOGPUSysMemory::withClientBuffer(IOGPU *, task_t, IOGPUDevice *, mach_vm_address_t, uint64_t)`
- `site.IOGPUMemory`
- `site.IOGPUObject *`
- `\"os_refcnt: attempted resurrection (rc=%p)\\n\" @%s:%d`
- `site.IOGPUMemory *`
- `iogpu_pagingoff_timeout`
- `static OSPtr<IOGPUSysMemory> IOGPUSysMemory::withClientRanges(IOGPU *, task_t, IOAddressRange *, uint32_t, bool)`
- `IOGPUVirtualMemory.cpp`
- `\"Unexpected number of pending objects prepared: %d != %d\" @%s:%d`
- `void IOGPU::reportGPURestart(const IOGPUCommandQueue *, const char *, uint32_t, uint64_t)`
- `IOGPUMemoryMap`
- `YES`
- `iogpu_panic_on_event_timeout`
- `OSPtr<IOMemoryMap> IOGPUSysMemory::retainCPUWireMapping(IOOptionBits)`
- `IOGPUDeviceUserClient`
- `\"IOGPUSysMemory::makeUntracked() called while resident\\n\" @%s:%d`
- `site.IOGPUCommandQueue`
- `1212222221211122`
- `site.IOGPUWeakNamespace`
- `bool IOGPUBlockFence::IOPerfControlAddResponsibleTaskID(uint32_t)`
- `barrier`
- `GPU Restart Count`
- `bool IOGPUCommandDescriptor::addMemory(IOGPUMemory *)`
- `virtual bool IOGPUDeviceUserClient::deviceUserClientStart()`
- `IOGPUEventMachine`
- `site.IOAccelGPURestartReport`
- `site.IOGPUBlockFencePort`
- `void IOGPUScheduler::signalHardwareError(eRestartRequest, int32_t)`
- `1111112`
- `121111122111212111111112221211121112`
- `IOReturn IOGPUMemory::detach()`
- `static IOReturn IOGPUDeviceUserClient::s_create_io_command_buffer(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `Graphics`
- `CachedCopy`
- `CommandQueueCount`
- `IOGPUBlockFence.cpp`
- `IOGPUIOCommandQueue.cpp`
- `stamp[idx:%d, %d]`
- `model`
- `Deny submissions/ignore`
- `%s exit\n`
- `AppleMobileFileIntegrity`
- `IOGPUMappingCommandDescriptor`
- `wired_limit`
- `iogpu_gart_interval_ms`
- `IOReturn IOGPUMemoryInfoUserClient::gather_memory_data(uint32_t, uint32_t *, uint32_t *, void *)`
- `SysMem`
- `static OSPtr<IOGPUResource> IOGPUResource::newResourceWithOptions(IOGPU *, IOGPUDevice *, enum eIOGPUResType, uint64_t, IOByteCount, IOOptionBits, mach_vm_address_t *, IOGPUNewResourceArgs *, uint64_t &, uint64_t &)`
- `site.T`
- `site.IOGPUIOCommandBuffer`
- `N`
- `bool IOGPUMemoryMap::update_pte(uint32_t, IOMemoryDescriptor *, IOMemoryDescriptor *)`
- `\"gpu_refcnt: overflow (rc=%p)\\n\" @%s:%d`
- `Ready`
- `Preempted`
- `IOReturn IOGPUDevice::new_resource(IOGPUNewResourceArgs *, struct IOGPUNewResourceReturnData *, IOByteCount, uint32_t *)`
- `virtual bool IOGPU::start(IOService *)`
- `OSPtr<IOSurfaceDeviceCache> IOGPU::deviceCacheForIOSurface(IOSurface *, uint32_t)`
- `IOGPUMemory.cpp`
- `gpurefcnt.c`
- `submit`
- `12111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111`
- `IOGPUNotificationQueue`
- `virtual void IOGPUTask::free()`
- `Vendor failed to provide GPURestartReport`
- `site.IOGPUBlockFence`
- `virtual IOReturn IOGPUCommandDescriptor::prepare(uint32_t)`
- `site.IOGPU`
- `Wired Low Water Mark Megabytes`
- `virtual bool IOGPUResource::mapAtAddressLength(uint64_t, uint64_t, uint64_t)`
- `i8@?0`
- `static IOReturn IOGPUDeviceUserClient::s_perform_io(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `\"IOGPUObject does not support release with when != 1\" @%s:%d`
- `\"IO Procssing Queue IO list Not Empty on IOGPUIOCommandQueue free\" @%s:%d`
- `\"Trying to add NULL memory\" @%s:%d`
- `\"IOGPUGroupMemory::remove_memory_object() memory object not found\" @%s:%d`
- `KDebugVersion`
- `\"IOGPUResidentMemorySet::repack() out of bounds\" @%s:%d`
- `site.IOGPUMTLEvent`
- `static IOReturn IOGPUDeviceUserClient::s_async_signal_mtlLateEvalevent(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `site.IOGPUMTLLateEvalEvent`
- `static OSPtr<IOGPUResource> IOGPUResource::newVirtualResource(IOGPU *, IOGPUDevice *, IOGPUNewResourceArgs *)`
- `121112211122`
- `site.IOGPUGroupMemory`
- `121111`
- `Application`
- `IOGPUBlockFencePort`
- `2222222211112`
- `wired_lwm_mb`
- `iogpu_event_timeout_secs`
- `Signature`
- `IOGPU::systemPagingOff() timeout. %d threads still stuck. addCommandToTail_slow %u, waitForAllSubmitted %u, workQueuesDisabled %u, waitingOnResources %u, waitForStamp %u, wireMemory %u\n`
- `kIOGPUKernelCommandDebugLog:%s\n`
- `\"%s: 0x%X mapping is not valid for wireRange, cannot wire PTEs\" @%s:%d`
- `static IOReturn IOGPUDeviceUserClient::s_create_io_command_queue(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `void IOGPUResource::setPurgeable(IOOptionBits, IOOptionBits)`
- `IOReturn IOGPUDevice::set_resource_purgeable(const uint32_t, eIOGPUResourcePurgeable, eIOGPUResourcePurgeable *)`
- `static IOReturn IOGPUDeviceUserClient::s_destroy_io_command_buffer(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `site.IOGPUDeviceAssertion`
- `IOReturn IOGPUGroupMemory::addMemoryFromResources(IOGPUResource **const, const unsigned int)`
- `Debug Flags`
- `Processes`
- `\"IOGPUSubMemoryDescriptor does not support release with when != 1\" @%s:%d`
- `static IOReturn IOGPUDeviceUserClient::s_group_remove_resources(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `\"IOGPUClientSharedMachine::getClientSharedAddressForId unable to find client map for id %08x\\n\" @%s:%d`
- `GARTReclaimTimeout`
- `static OSPtr<IOGPUSysMemory> IOGPUSysMemory::withMemoryDescriptor(IOGPU *, IOGPUResource *, IOMemoryDescriptor *)`
- `\"Mem object in pending hash found in main memory hash\" @%s:%d`
- `site.IOGPUStatistics`
- `static IOReturn IOGPUDeviceUserClient::s_query_mtlLateEvalevent(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `12111233212`
- `\"GPU hang (boot-args contains \\\"panic_on_gpu_hang=1\\\")\" @%s:%d`
- `IOGPUMemoryInfoUserClient`
- `static IOReturn IOGPUDeviceUserClient::s_new_command_queue(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `IOReturn IOGPUDevice::create_notificationqueue(uint32_t, uint32_t, sIOGPUDeviceNotificationQueueData *)`
- `1211212112111122222222222222222222122222`
- `AlwaysResident`
- `finished`
- `\"IOGPUMemory::dealloc() eviction failed\\n\" @%s:%d`
- `12122`
- `IOGPUScheduler`
- `sub`
- `Disable wired memory collector`
- `1212222222222222222222111212`
- `site.IOGPUDeviceShmem`
- `site.struct sGPURestartRegisteredCommandQueue`
- `void IOGPUMappingCommand::execute()`
- `iogpu_no_prepare_avoid_throttling`
- `virtual IOReturn IOGPUCommandQueue::schedulePostMappingWaitEvent(IOSurfaceSharedEvent *, uint64_t, uint32_t)`
- `1222112122211121111112`
- `\tfRingBuffer[%d]=[ctx:%p, gputask:%p, stamp[idx:%d, stamp:%d]`
- `\"Didn't complete expected number of objects from the pending array.\" @%s:%d`
- `site.IOGPUCountedSet`
- `IOGPUResourceSet`
- `1111111111111111111111111111111111111111121111111111111111111111111111111111111111212`
- `IOGPUBufferMemoryDescriptor`
- `static IOReturn IOGPUDeviceUserClient::s_submit_io_commands(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `virtual bool IOGPUResource::map(uint64_t, uint32_t)`
- `site.stamp_t *`
- `site.IOGPUNamespace`
- `static IOReturn IOGPUDeviceUserClient::s_try_cancel_io_command_buffer(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `aborted`
- `IOGPUCountedSet.h`
- `\"Unable to remove just added resource\" @%s:%d`
- `static IOReturn IOGPUDeviceUserClient::s_delete_command_queue(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `CommandQueueCountMax`
- `iogpu_no_abort`
- `%x`
- `void IOGPUAllocationInfo::declareDeviceShmem(pid_t, IOMemoryDescriptor *, mach_vm_address_t)`
- `\"trying to get apparently bogus resource handle %d\" @%s:%d`
- `\"IOGPUSubMemoryDescriptor does not support taggedRelease with when != 1\" @%s:%d`
- `static IOReturn IOGPUDeviceUserClient::s_io_command_buffer_barrier_complete(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `site.IOGPUMTLFence`
- `void IOGPUCommandQueue::retireCommandBuffer(IOGPUEventFence *)`
- `IOGPUChannel`
- `site.IOGPUScheduler`
- `122`
- `IU`
- `failed to`
- `IOReturn IOGPUResource::replace_backing_bytes(task_t, mach_vm_address_t, uint64_t)`
- `\"Non-resident group memory has %u pending memory objects\" @%s:%d`
- `accumulatedGPUTime`
- `IOGPUFamily`
- `virtual void IOGPUCommandQueue::processKernelCommands(const sIOGPUKernelCommand *, const sIOGPUKernelCommand *)`
- `\"IOGPUResidentMemorySet::repack() count mismatch\" @%s:%d`
- `Purgeable`
- `IOGPUDeviceShmem`
- `idx`
- `IOGPUGroupMemory`
- `void IOGPUMappingCommandDescriptor::performMappings()`
- `\"kernel command shmem no longer mapped\" @%s:%d`
- `\"IOGPUObject does not support taggedRelease with when != 1\" @%s:%d`
- `site.IOGPUResource`
- `SysMemShared(IOSurface)`
- `\"group_add_resources_trap() count overflow\" @%s:%d`
- `IOReturn IOGPUMemory::prepare_memory_slow(uint32_t, bool, uint64_t)`
- `site.IOGPUDeviceUserClient`
- `site.IOGPUObject`
- `\"Pending object not found in main hash\" @%s:%d`
- `site.IOGPUCommandDescriptor`
- `static OSPtr<IOGPUResource> IOGPUResource::newResourceWithClientBuffer(IOGPU *, IOGPUDevice *, enum eIOGPUResType, IOByteCount, mach_vm_address_t, mach_vm_address_t, mach_vm_address_t *)`
- `bool IOGPUIOCommandBuffer::processCommands(uint32_t, uint64_t, bool)`
- `com.apple.private.ggdsw.GPUProcessProtectedContent`
- `\"Unexpected number of objects moved from pending to main hash\" @%s:%d`
- `site.struct sIOGPUStartTimes`
- `IOGPU Default WorkLoop`
- `IOGPU: Wired low water mark overridden to %d MB\n`
- `site.IOGPUVirtualMemory`
- `IOReturn IOGPUResource::detach_backing()`
- `4@>]2AA=6]AC:G2E6]x~$FC7246]AC@E64E65\\2446DD`
- `com.apple.private.gpu-restricted`
- `virtual void IOGPUSysMemory::unwire()`
- `\"IOGPUBufferMemoryDescriptor does not support release with when != 1\" @%s:%d`
- `Wired`
- `Internal`
- `121222222222222222222222222222222222`
- `Blocked`
- `B16@?0^{OSObject=^^?i}8`
- `IOGPUNamespace`
- `IOGPUMTLLateEvalEvent`
- `12112`
- `site.IOGPUCommandDescriptor *`
- `Failed to reallocate/truncate vendor's (too-long) GPURestartReport`
- `IOGPU.cpp`
- `1211122`
- `void *IOGPUResource::getKernelData()`
- `IOGPUIOCommandDescriptor`
- `virtual void IOGPUWorkQueue::logRingBuffer()`
- `iogpu_gart_timeout_ms`
- `site.IOGPUAllocationInfo`
- `IOSurfaceID`
- `site.IOGPUMemoryMap`
- `static IOReturn IOGPUDeviceUserClient::s_new_resource(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn IOGPUDeviceUserClient::s_io_command_buffer_complete(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `static OSPtr<IOGPUResource> IOGPUResource::newResourceWithParentResourceID(IOGPU *, IOGPUDevice *, enum eIOGPUResType, uint64_t, IOByteCount, mach_vm_address_t, mach_vm_address_t, mach_vm_address_t *, uint32_t)`
- `const sIOGPUEvent *IOGPUResource::gartWriteEvent() const`
- `\"Command Buffer Command List Not Empty on IOGPUIOCommandBuffer free\" @%s:%d`
- `virtual void IOGPUWorkQueue::restart()`
- `IOReturn IOGPUNotificationQueue::setNotificationPort(mach_port_t)`

**[__TEXT.__os_log]**

- `%s: invalid arguments\n`
- `%s: Invalid Arguments\n`
- `%s: failed to create client map for meta data\n`
- `%s: Invalid command_size (%u) min=%lu currentCommand=%p kernelCommandEnd=%p\n`
- `%s: Failed to create queue Lock\n`
- `%s: Failed to IO processing queue Lock\n`
- `%s: GARTReclaimInterval set to non default value (%d) milisec\n`
- `%s: IOMemoryDescriptor::getPageCounts returned 0x%08x\n`
- `%s: newCommandQueue failed\n`
- `%s: Failed to create Command Buffer Lock\n`
- `%s: segmentListShmem (PID=%d) failed to map into kernel\n`
- `Cmd queue %p sleep port_name %d value: %08llx timed out!\n`
- `%s failed to map arguments\n`
- `%s: Couldn't allocate object_handle\n\n`
- `%s: device handle is null and failed to add texture buffer size to device allocation size\n`
- `%s: overflow\n`
- `IOGPUScheduler: increment_gart_collector_disable_count -> %d`
- `%s:kIOGPUKernelCommandPostMappingWaitEvent: Failed to schedule post mapping event\n`
- `%s: failed to get the memory descriptor\n`
- `%s: Failed to rehash\n`
- `%s <%s>: preparedBytes != requiredBytes : preparedBytes = <%llu> requiredBytes = <%llu> maxWired = <%llu> preWiring = <%llu> currentWired = <%llu> wiring delta = <%llu>\n\n`
- `%s: Failed to mark virtual memory non-volatile err 0x%x\n`
- `%s: failed to add into name space\n`
- `%s: Invalid Command (%u) of bytes (%llu)\n`
- `%s: failed to initialize\n`
- `%s null queue\n`
- `%s: The number of queues (%d) exceeding limit (%d), failing IOGPUCommandQueue creation\n`
- `%s: IO Command Queue init failed\n`
- `%s: sleeping %llu miliseconds %s find stamp index %d.\n`
- `%s: source resource memory is not a sys memory\n`
- `%s maxSingleSysMemoryPercent override = %u\n`
- `%s: Failed to allocate shared event fence\n`
- `%s: Failed to allocate residency data kernel map\n`
- `%s: Failed to prepare metadata (%p)\n`
- `%s: getStampMemory failed\n`
- `%s: command list length less than zero\n`
- `%s: completion gate alloc failure\n`
- `%s fMaxSingleSysMemoryPercent = %u fMaxSysMemoryWiredSize[API] = %llu fMaxSingleSysMemory = %llu\n`
- `%s: Disallowing executable page\n`
- `%s: Invalid arguments : numEntries = %u, entrySize = %u \n`
- `%s: Failed to prepare memory descriptor(%p) at index %u\n`
- `%s: failed to create a device cache\n`
- `%s: Failed to create Submit IO Thread\n`
- `MTLEvent: timed out while waiting, GPU is up now, extending deadline by <%llu>\n`
- `%s: Failed to allocate array of sub memory descriptors\n`
- `%s: Unsupported protecton options (%016llx) bytes\n`
- `%s: parent_resource_id is 0\n`
- `%s: newResourceGroup failed to initialize resource map\n`
- `%s: Insufficient bytes (%llu) for sIOGPUIOKernelCommandBarrierArgs (%lu)\n`
- `%s: fGPURestartRegisteredCommandQueueLock alloc fail\n`
- `%s: fGARTCollectorLock alloc fail\n`
- `%s: newResourceGroup bad initial capacity: %d\n`
- `%s invalid plane %d in IOSurface with %d planes\n`
- `%s: Update Mappings Failed(0x%x)\n`
- `%s:kIOGPUKernelCommandDebugSleep: Insufficient bytes (%llu) for sIOGPUKernelCommandDebugSleepArgs (%lu)\n`
- `%s:kIOGPUKernelCommandResponsibleTaskIDs: Insufficient bytes (%llu) or size overflow for sIOGPUKernelCommandResponsibleTaskIDArgs (%lu)\n`
- `%s: Shared event wait timed out for value : %llx\n`
- `%s: Failed to create IO Command Descriptor (kIOGPUIOCommandDescriptorTypeSignalEvent)\n`
- `%s: GPURestartSkipped\n`
- `%s: setting global restart type to %d\n`
- `%s: failed to prepare memory status = 0x%X\n`
- `%s: createKernelGPUTask failed\n`
- `Duplicate command buffer resource group tokens\n`
- `%s: child resource (offset=0x%llx, size=0x%llx) exceeds parent memory size 0x%llx.\n`
- `%s maxSysMemoryWiredSizeAPI override = %llu\n`
- `%s:kIOGPUKernelCommandResponsibleTaskIDs: Submit Fence failed to add PID\n`
- `%s: Failed to allocate descriptor bitmap\n`
- `%s: fStampMemoryMap creation failed\n`
- `%s: newResourceGroup failed - initial capacity (%u) less than minimum required (%u)\n`
- `%s: Failed to allocate resource object\n`
- `%s: fSubmissionTimer alloc fail\n`
- `%s: failed to create sleep lock\n`
- `%s: Overflow aligning residency data length\n`
- `%s: no memory. resType=0x%x\n`
- `%s: command timeout detected - GPU start time %lld ms, now %lld ms, priority=%d\n`
- `%s: configureDevice failed\n`
- `%s: GARTReclaimInterval set to non default value (%u) milisec\n`
- `%s: Failed to allocate sub memory descriptors at index %u\n`
- `%s: Failed to prepare residency data (%p)\n`
- `%s: Failed to set purgeable state 0x%x\n`
- `%s: command list length less insufficient (%zd)\n`
- `%s: failed to create fDeviceNamespace\n`
- `%s: Failed to evict for detach\n`
- `%s: virtual_page_size(%u) is not minimum VirtualPageSize(%u) aligned\n`
- `%s: fFenceLock alloc fail\n`
- `%s: Failed to create Submit IO Thread Lock\n`
- `%s null device\n`
- `%s: failed to make allocation\n`
- `%s: Refusing to create mapping for readonly memory\n`
- `%s: Can't pin global ro resources to fixed address\n`
- `%s: memory is not a sysmemory\n`
- `%s: Failed to update memory at index %u\n`
- `%s: Unsupported purgeability option (%u)\n`
- `%s: IOPerfControlClient::copyClient failed\n`
- `%s: attempted to reset notification port!\n`
- `%s: VnioDesc add namespace failed\n`
- `%s: failed to allocate fRestartTypeAsync\n`
- `%s: Invalid resource ID\n`
- `%s:kIOGPUKernelCommandCopyMappings: Invalid source resourceID %08x\n`
- `%s: createResource failed\n`
- `%s: Failed to allocate IOGPUVirtualMemory object\n`
- `%s: busy lock alloc failure\n`
- `%s: failed to wire down memory %p. needed %lld, used %lld, size %lld bytes.\n`
- `%s: failed to create mapping.\n`
- `%s: waitForGPUTimeoutSeconds can not be zero.\n`
- `%s: GARTReclaimTimeout set to non default value (%d) milisec\n`
- `%s: API Allocation Name allocation failed\n`
- `%s: Could not find event_id %u\n`
- `%s: Incompatible virtual page sizes source(%u), destination(%u)\n`
- `IOGPU::start: Failure exit\n`
- `%s:kIOGPUKernelCommandSetProtectionOptions: Unsupported protecton options (%016llx) bytes\n`
- `%s:kIOGPUKernelCommandCopyMappings: Insufficient bytes (%llu) for sIOGPUCopyMappings (%lu)\n`
- `%s: allocIOGPUResource failed to alloc texture object\n`
- `%s: Failed to create IO Command Descriptor (kIOGPUIOCommandDescriptorTypeIO)\n`
- `%s mapping descriptor prepare failed (0x%X)\n\n`
- `%s: numEventChannels must at least 1\n`
- `%s:kIOGPUKernelCommandUpdateMappings: Insufficient bytes (%llu) or size overflow for sIOGPUUpdateMappings (%lu)\n`
- `Invalid resource group count\n`
- `%s: Failed to allocate metadata memory descriptor\n`
- `%s: alloc_info->init failed\n`
- `%s: attempted to reset notification queue\n`
- `%s: Failed to create BufferMemoryDescriptor for partial backing\n`
- `%s: Cannot store 64-bit protection options\n`
- `%s: Failed to create IO Command Descriptor (kIOGPUIOKernelCommandWaitSharedEvent)\n`
- `%s: Failed to create Active Command Buffers Lock\n`
- `%s: Size mismatch\n`
- `%s: failed to create mapping. resType=0x%x\n`
- `%s: createDevice failed\n`
- `%s: GPURestartEnd stampIdx=%d type=%d\n`
- `%s: PID %d may be leaking IOGPUResource (count=%d)\n`
- `%s: kernelCommandBufferShmem (PID=%d) failed to map into kernel\n`
- `%s: Unsupported for memory from IOSurfaceMemoryPool\n`
- `%s: Failed to allocate residency data memory descriptor\n`
- `%s: fMemory is NULL.\n`
- `%s: failing. parent_resource_id only works with standard texture. resType=0x%x.\n`
- `%s: resource does not own its backing (resType=0x%x child=%u device_cache=%s)\n`
- `Can't upgrade IOGPUMemory.protectionOptions while still wired (0x%x->0x%x)\n`
- `%s: Failed to find command queue\n`
- `%s: parent resource type mismatch.\n`
- `%s: failed to create mapping\n`
- `%s: Failed to create uio\n`
- `%s: IO Command Buffer add to namespace failed\n`
- `IOGPU:start() [%s: fConfig.debugBits=0x%x]\n`
- `%s:kIOGPUKernelCommandPostMappingWaitEvent: Invalid signal event port name: %d obj: %p\n`
- `%s: Overflow adding residency data length to byte count\n`
- `%s: IOMemoryDescriptor::getPageCounts returned 0x%08x for residency data\n`
- `%s: total size overflow (%llu * %llu)\n`
- `%s: fCompletionInterrupt alloc fail\n`
- `MTLEvent: timed out while waiting. Sleep/wake occurred while waiting. Extend deadline by <%llu>\n`
- `%s: IO Command Queue add to namespace failed\n`
- `%s: Insufficient input struct size (%llu)\n`
- `%s: fGARTCollectorThread alloc fail\n`
- `IOMalloc failed to alloc handles\n`
- `%s: Can't allocate GPURestartReport nub.  Skipping...\n`
- `%s: Insufficient space (%lu) to hold sIOGPUKernelCommand (%lu)\n`
- `%s:kIOGPUKernelCommandPurgeResources: Insufficient bytes (%llu) or size overflow for sIOGPUKernelCommandPurgeResourcesArgs (%lu)\n`
- `%s: failed to lookup parent resource from shared.\n`
- `%s: Invalid IO Commmand Buffer ID (%u)\n`
- `%s: failed to create event machine\n`
- `%s: Can't allocate GPURestartReport dictionary.  Skipping....\n`
- `%s:kIOGPUKernelCommandWaitSharedEvent: bad event port name: %d obj: %p\n`
- `%s: client_buffer (0x%llx) precedes client_base (0x%llx).\n`
- `%s: failed to allocate HW error interrupt\n`
- `%s <%s>: requiredBytes = <%llu> maxWired = <%llu> preparedBytes : <%llu> remainingBytes : <%lld> remainingPages = <%lld>\n\n`
- `%s: statistics object alloc fail\n`
- `%s: registerPrioritySleepWakeIntererest failed\n`
- `%s: virtual_page_size(%u) is not a power of 2\n`
- `%s: Too many queues (%d) created, possibly leaking?\n`
- `%s: failed to create client map\n`
- `%s: provider is not the right device\n`
- `%s:kIOGPUKernelCommandSignalSharedEvent: couldn't allocate signal object\n`
- `%s:kIOGPUKernelCommandCopyMappings: Failed to allocated Async Mapping Descriptor \n`
- `%s: failed to map memory for CPU wire mapping\n`
- `%s has reached a high water mark of %d gpu command queues.`
- `%s: input memory descriptor map failed\n`
- `%s: initialize failed\n`
- `%s:kIOGPUKernelCommandUpdateMappings: Insufficient bytes (%llu) for sIOGPUUpdateMappings (%lu)\n`
- `%s: Overflow in range\n`
- `%s: Vendor failed to provide GPURestarrReport\n`
- `%s: Protection violation\n`
- `%s: failed to alloc array\n`
- `%s: Failed to realloc/truncate vendor's (too-long) GPURestartReport from %ld to %d\n`
- `%s:kIOGPUKernelCommandPostMappingWaitEvent: Insufficient bytes (%llu) for sIOGPUKernelCommandSignalOrWaitEventArgs (%lu)\n`
- `%s: Invalid arguments\n`
- `%s: bad structureInputSize (%lld != %llu)\n`
- `%s:kIOGPUKernelCommandSignalSharedEvent: Insufficient bytes (%llu) for sIOGPUKernelCommandSignalOrWaitEventArgs (%lu)\n`
- `Invalid resource group ID %08x\n`
- `%s: workloop alloc fail\n`
- `%s invalid cache_mode 0x%x\n`
- `%s: newResourceGroup failed to alloc texture object\n`
- `%s: Failed to allocate array of descriptors\n`
- `%s: Overflow adding metadata length to byte count\n`
- `%s: Residency data length(%llu) less than required minimum size(%llu)\n`
- `IONewZero failed to alloc Handles\n`
- `%s: Insufficient bytes (%llu) for sIOGPUIOKernelCommandSignalOrWaitEventArgs (%lu)\n`
- `%s: IOMemoryDescriptor::getPageCounts returned 0x%08x for meta data\n`
- `trying to remove apparently bogus texture handle %d\n`
- `%s: Invalid IO Queue ID (%u)\n`
- `%s: Invalid Notification Queue ID (%u)\n`
- `%s: Invalid IO Queue Type (%u)\n`
- `Trying to restart GPU (%s)...\n`
- `%s:kIOGPUKernelCommandUpdateMappings: Failed to add mapping command to descriptor \n`
- `MTLEvent: timed out but sleep started after deadline <%llu>. This is a real timeout\n`
- `%s: IOPerfControlClient::registerDevice failed.\n`
- `%s:kIOGPUKernelCommandDebugLog: Insufficient bytes (%llu) for sIOGPUKernelCommandDebugLogArgs (%lu)\n`
- `%s:kIOGPUKernelCommandResponsibleTaskIDs: Insufficient bytes (%llu) for sIOGPUKernelCommandResponsibleTaskIDArgs (%lu)\n`
- `%s:kIOGPUKernelCommandSetResourceGroups: group count (%u) invalid\n`
- `%s:kIOGPUKernelCommandCopyMappings: Failed to add mapping command to descriptor \n`
- `%s: %s app[%s] with %d GPURestarts in %d submissions.\n`
- `%s: Failed to allocate temporary ranges\n`
- `%s: Attempting to prepare detached resource\n`
- `%s: Failed to create IOGPUVnioDesc\n`
- `%s: Command buffer count mismatch (%lld - %u)\n`
- `%s: GPURestartBegin %s type=%d\n`
- `%s: Clean slate for app[%s] with %d GPURestarts in %d submissions.\n`
- `%s: Failed to create fKernelMap for data buffer\n`
- `%s: Bogus texture of type %s on GART list\n\n`
- `%s: failed to create fWorkQueueNamespace\n`
- `%s: Invalid eIOGPUKernelCommands enum (command_id=%u command_size=%llubytes)\n`
- `%s:kIOGPUKernelCommandSignalSharedEvent: bad event port name: %d obj: %p\n`
- `%s: failed to create descriptor\n`
- `Timeout MTLEvent: waiting for signal (%llu) for event (%u) to be scheduled\n`
- `%s: Overflow aligning metadata length\n`
- `GPU hang: %s\n\n`
- `%s suballocation flag is set without parent resource id\n`
- `Failed to create the ktrace callback\n`
- `%s: invalid segment shmem\n`
- `%s: global restart. type=%d\n`
- `IOMallocType failed to alloc client_shared\n`
- `%s failed: try to wire down too much memory : %llu > %llu\n`
- `%s: sidebandBufferShmem (PID=%d) failed to map into kernel\n`
- `%s:kIOGPUKernelCommandSetProtectionOptions: Insufficient bytes (%llu) for sIOGPUKernelCommandSetProtectionOptionsArgs (%lu)\n`
- `%s: failed to create rw Lock\n`
- `%s: setting channel %d restart type to %d\n`
- `%s: maxSchedulerPriorityCount can not exceed %d\n`
- `Process %s (%d) does not have the entitlement to use MTLGPUPriorityRealTime, using MTLGPUPriorityHigh instead\n`
- `%s:kIOGPUKernelCommandSetResourceGroups: Insufficient bytes (%llu) for sIOGPUKernelCommandSetResourceGroupsArgs (%lu)\n`
- `%s: Failed to find shared event reference\n`
- `%s: updateGPUPageTable failed\n`
- `%s: memory larger than maximum system memory size\n`
- `%s: init failed\n`
- `%s: IO Command Queue creation failed\n`
- `%s: pid count is greater than or equal to the max allowed (%u)\n`
- `%s: Unkown resource type. resType=0x%x\n`
- `%s: Failed to create memory descriptors\n`
- `%s: ring is empty and all finished. Nothing to do.\n\n`
- `%s: minVirtualPageSize is not a power of 2\n`
- `IOGPU: Wired low water mark overridden to %d MB`
- `%s: resource does not own its backing (resType=0x%x)\n`
- `%s: Invalid command list header, commands_start=%u commands_end=%u cmdListShmemLength=%ld\n`
- `%s: failed to allocate HW progress interrupt\n`
- `%s: kernelCommandStart(%u) or kernelCommandEnd(%u) exceeds kernelCommandDataSize(%lu)\n`
- `%s:kIOGPUKernelCommandUpdateMappings: Update Mappings Failed\n`
- `%s:kIOGPUKernelCommandCopyMappings: Insufficient bytes (%llu) or size overflow for sIOGPUUpdateMappings (%lu)\n`
- `%s: Could not find event_id %u (value %llu)\n`
- `%s: IO Command Buffer init failed\n`
- `%s: fail to get IOSurface root\n`
- `%s: failed to create memory descriptor from IOSurfaceMemoryPool\n`
- `%s: ByteCount is not virtualPageSize(%u) aligned\n`
- `%s: failed for id %d\n`
- `%s: Invalid Descriptor Type (%u)\n`
- `%s: IOGPU event scrubber thread setup failed\n`
- `%s: work queue indicates empty/idle - Forcing restart\n`
- `%s: Redundant hardware error stampIdx=%d type=%d\n`
- `%s: GPURestartDequeued stampIdx=%d type=%d\n`
- `%s: Copy Mappings Failed(0x%x)\n`
- `%s: fGPUTaskList alloc fail\n`
- `%s: IOGPUScheduler alloc or init failed\n`
- `%s:kIOGPUKernelCommandPostMappingWaitEvent: Async Mapping Disabled\n`
- `%s: fAccelerator->createBufferMemoryDescriptorInTaskWithOptions failed\n`
- `%s: Not detached\n`
- `%s: Failed to replace memory\n`
- `%s: failed to reserve the GPUVM address 0x%llx length 0x%llx\n`
- `IOBufferMemoryDescriptor::inTaskWithOptions failed to allocate a client_shared block.\n`
- `%s: setOwnership with no footprint failed: %08x\n`
- `%s:kIOGPUKernelCommandPostMappingWaitEvent: Async Mapping Descriptor not allocated\n`
- `%s: Post Mapping wait failed\n`
- `MTLEvent: timed out while waiting, GPU is not up yet\n`
- `%s: Command Buffer Processing Error\n`
- `%s: Invalid IO Queue Priority (%u)\n`
- `%s: sGPURestartRegisteredCommandQueue alloc fail\n`
- `%s <%s> FAILED To Free, should return error: <0x%X> total accelerator = 0x%llX max = 0x%llX\n`
- `%s failed to create resource\n`
- `%s: Insufficient bytes (%llu) for sIOGPUIOKernelArgs (%lu)\n`
- `%s: command already GPU finished, skipping restart call\n`
- `%s: Bogus resType = %d\n`
- `%s: Overflow\n`
- `%s: accelName must not NULL\n`
- `%s:kIOGPUKernelCommandPurgeResources: Invalid resourceID %08x\n`
- `%s:kIOGPUKernelCommandPostMappingWaitEvent: Failed to allocated Mapping fence\n`
- `%s: Invalid Index (%u), Capacity (%u)\n`
- `%s failed to add resources to group\n`
- `%s: Failed to create Command Buffer Namespace\n`
- `%s: failed to allocate HW progress timer\n`
- `Cmd queue %p sleep port_name %d value: %08llx timed out waiting for prior signals!\n`
- `%s:kIOGPUKernelCommandUpdateMappings: Failed to allocated Async Mapping Descriptor \n`
- `%s: resource already has a map\n`
- `%s: Invalid virtual_page_size(%u)\n`
- `%s: Invalid newCommandQueueArgsSize (%u) expected (%u)\n`
- `%s: fail. request=%llu, current=%d, max=%d\n`
- `%s: disallowing protected resource\n`
- `%s: Invalid command list shmem ID\n`
- `%s:kIOGPUKernelCommandUpdateMappings: Invalid destinationResourceID %08x\n`
- `%s: Out of bounds access to residency data\n`
- `%s: GARTReclaimTimeout set to non default value (%u) milisec\n`
- `%s: Hole in address ranges\n`
- `%s: memory %p failed to prepare. Error 0x%x\n`
- `%s: Overflow aligning virtual length\n`
- `%s: IO Command Buffer already processed\n`
- `%s: Insufficient bytes (%lu) to hold sIOGPUIOKernelCommand (%lu)\n`
- `%s: kIOGPUIOKernelCommandSignalSharedEvent: Invalid event port name: %d obj: %p\n`
- `%s: GPURestartBegin stampIdx=%d type=%d\n`
- `%s: GPURestartEnd %s type=%d\n`
- `%s:kIOGPUKernelCommandCopyMappings: Copy Mappings Failed\n`
- `%s: Overflow when adding excess capacity\n`
- `%s waitForEventTimeoutSeconds = %u\n`
- `%s: failed to allocate\n`
- `%s: new IOGPUAllocationInfo failed\n`
- `%s:kIOGPUKernelCommandCollectTimeStamp: Insufficient bytes (%llu) for sIOGPUKernelCommandCollectTimeStampArgs (%lu)\n`
- `%s: Failed to make new descriptor\n`
- `%s: memory is not a virtual memory\n`
- `%s: Failed to create IO Command Descriptor (kIOGPUIOCommandDescriptorTypeBarrier)\n`
- `%s: GPURestartSignaled stampIdx=%d type=%d prevType=%d numStamps=%d\n`
- `%s: failed to create mapping at address 0x%llx with length 0x%llx.\n`
- `%s: Truncated vendor's (too-long) GPURestartReport from %ld to %d\n`
- `%s: IOGPUAllocationInfo->copyToArray returned nil\n`
- `%s: failed to mark memory %p non-volatile Error 0x%x\n`
- `IOMallocZeroData failed to alloc Handles Map\n`
- `%s: cmdBufArgSize does not match config (%llu != %u)\n`
- `%s: Failed to make client map\n`
- `%s: destination resoource memory is not a virtual memory\n`
- `%s: IO Command Buffer creation failed\n`
- `%s: submission gate alloc failure\n`
- `%s: IOGPUFenceMachine alloc or init failed\n`
- `%s:kIOGPUKernelCommandCopyMappings: Invalid destination resourceID %08x\n`
- `%s: kIOGPUIOKernelCommandWaitSharedEvent: Invalid event port name: %d obj: %p\n`
- `%s: Invalid virtualPageSize(%u)\n`
- `%s: Resource still busy\n`
- `%s: IOGPUSysMemory::withOptions failed\n`
- `%s: Failed to detach memory\n`
- `%s: failed to allocate Hardware lock\n`
- `IOGPUScheduler: decrement_gart_collector_disable_count -> %d`
- `%s <%s> (%p) : required > max : requiredBytes = <%llu> preparedBytes : <%llu> maxWired = <%llu> maxWiredInternal = <%llu> currentWired = <%llu>\n`
- `%s: Can't allocate GPURestartReport keys/objects.  Skipping...\n`
- `%s:kIOGPUKernelCommandPurgeResources: Insufficient bytes (%llu) for sIOGPUKernelCommandPurgeResourcesArgs (%lu)\n`
- `%s: scheduler lock alloc failure\n`
- `%s: GPURestartEnqueued stampIdx=%d type=%d\n`
- `%s invalid IOSurface ID 0x%x\n`
- `IOGPUStatistics couldn't allocate an IOLock.\n`
- `MTLEvent: while waiting, sleep occurred, but woken up from an unknown event <%d>\n`
- `%s: failed to serialize memory data\n`
