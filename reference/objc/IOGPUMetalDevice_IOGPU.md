# `IOGPUMetalDevice`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLDevice`
- 24 instance variables, 13 properties, 68 instance methods, 2 class methods

## Instance variables

```
^{__IOGPUDevice=} _deviceRef;
I _acceleratorPort;
{?="segmentListShmemPool"@"IOGPUMetalDeviceShmemPool""kernelCommandShmemPool"@"IOGPUMetalDeviceShmemPool""sidebandPool"@"IOGPUMetalDeviceShmemPool""hwResourcePools"^@"hwResourcePoolCount"I"akResourceListPool"@"MTLResourceListPool""akPrivateResourceListPool"@"MTLResourceListPool""debugBufferShmemPool"@"IOGPUMetalDeviceShmemPool"} _storageCreateParams;
^{IOGPUMetalCommandBufferStoragePool={gpuStorageQueue=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}{os_unfair_lock_s=I}iii@^{?}} _commandBufferStoragePool;
I _configBits;
I _deviceBits;
Q _textureRam;
Q _videoRam;
Q _sharedMemorySize;
I _accelID;
i _numCommandBuffers;
Q _segmentByteThreshold;
@"IOGPUMetalDeviceShmemPool" _ioKernelCommandListShmemPool;
B _disableGPUIO;
^{IOGPUMetalSuballocator=} _buffer_suballocator;
@"NSObject<OS_dispatch_queue>" _device_dispatch_queue;
@"NSObject<OS_dispatch_queue>" _device_pool_cleanup_queue;
@"NSObject<OS_dispatch_source>" _device_pool_cleanup_source;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _device_pool_cleanup_lock;
B _device_pool_cleanup_scheduled;
B _device_pool_cleanup_requested;
Q _registryID;
@"<MTLDeviceSPI>" _deviceWrapper;
@"NSObject<OS_dispatch_queue>" _mappingQueue;
```

## Properties

```
@property (T^@,R) hwResourcePools;
@property (TI,R) hwResourcePoolCount;
@property (Ti,R,V_numCommandBuffers) numCommandBuffers;
@property (TI,R,V_acceleratorPort) acceleratorPort;
@property (TQ,R) sharedMemorySize;
@property (TQ,R) dedicatedMemorySize;
@property (TQ,R) recommendedMaxWorkingSetSize;
@property (TQ,R) registryID;
@property (TB,R) hasUnifiedMemory;
@property (TB,R) supportsVertexAmplification;
@property (TB,R) supportPriorityBand;
@property (TQ,R) currentAllocatedSize;
@property (T@"IOGPUMemoryInfo",R,D) memoryInfo;
```

## Class methods

```
+[IOGPUMetalDevice registerService:];
+[IOGPUMetalDevice registerDevices];
```

## Instance methods

```
-[IOGPUMetalDevice newUncachedIOFileHandleWithURL:compressionMethod:error:];
-[IOGPUMetalDevice _setDeviceWrapper:];
-[IOGPUMetalDevice newArgumentEncoderWithLayout:];
-[IOGPUMetalDevice dedicatedMemorySize];
-[IOGPUMetalDevice akResourceListPool];
-[IOGPUMetalDevice newEventWithOptions:];
-[IOGPUMetalDevice currentAllocatedSize];
-[IOGPUMetalDevice newUncachedIOHandleWithURL:error:];
-[IOGPUMetalDevice newLateEvalEvent];
-[IOGPUMetalDevice setComputePipelineStateCommandShmemSize:];
-[IOGPUMetalDevice newIOFileHandleWithURL:compressionMethod:error:];
-[IOGPUMetalDevice newIOFileHandleWithURL:error:];
-[IOGPUMetalDevice initWithAcceleratorPort:];
-[IOGPUMetalDevice newCommandQueueWithDescriptor:];
-[IOGPUMetalDevice newIOHandleWithURL:error:];
-[IOGPUMetalDevice newUncachedIOFileHandleWithURL:error:];
-[IOGPUMetalDevice newIOHandleWithURL:compressionType:error:];
-[IOGPUMetalDevice acceleratorPort];
-[IOGPUMetalDevice newUncachedIOHandleWithURL:compressionType:error:];
-[IOGPUMetalDevice supportsVertexAmplification];
-[IOGPUMetalDevice supportsResourceDetachBacking];
-[IOGPUMetalDevice newEvent];
-[IOGPUMetalDevice initialIOKernelCommandListShmemSize];
-[IOGPUMetalDevice _purgeDevice];
-[IOGPUMetalDevice newAccelerationStructureWithBuffer:offset:];
-[IOGPUMetalDevice newIOHandleWithURL:compressionMethod:error:];
-[IOGPUMetalDevice newAccelerationStructureWithBuffer:offset:resourceIndex:];
-[IOGPUMetalDevice _deviceWrapper];
-[IOGPUMetalDevice newIOCommandQueueWithDescriptor:error:];
-[IOGPUMetalDevice setHwResourcePool:count:];
-[IOGPUMetalDevice newAccelerationStructureWithSize:];
-[IOGPUMetalDevice hwResourcePoolCount];
-[IOGPUMetalDevice deallocBufferSubData:heapIndex:bufferIndex:bufferOffset:length:];
-[IOGPUMetalDevice numCommandBuffers];
-[IOGPUMetalDevice supportsVertexAmplificationCount:];
-[IOGPUMetalDevice akPrivateResourceListPool];
-[IOGPUMetalDevice initialDebugBufferShmemSize];
-[IOGPUMetalDevice newIndirectCommandBufferWithDescriptor:maxCommandCount:options:];
-[IOGPUMetalDevice newAccelerationStructureWithSize:resourceIndex:];
-[IOGPUMetalDevice dealloc];
-[IOGPUMetalDevice cmdBufArgsSize];
-[IOGPUMetalDevice initialKernelCommandShmemSize];
-[IOGPUMetalDevice newFence];
-[IOGPUMetalDevice setSegmentListShmemSize:];
-[IOGPUMetalDevice supportsBackgroundAppRole];
-[IOGPUMetalDevice setIndirectArgumentBufferDecodingData:];
-[IOGPUMetalDevice hwResourcePools];
-[IOGPUMetalDevice newIntersectionFunctionTableWithDescriptor:];
-[IOGPUMetalDevice initialSegmentListShmemSize];
-[IOGPUMetalDevice allocBufferSubDataWithLength:options:alignment:heapIndex:bufferIndex:bufferOffset:parentAddress:parentLength:];
-[IOGPUMetalDevice initialSidebandShmemSize];
-[IOGPUMetalDevice memoryInfo];
-[IOGPUMetalDevice initWithAcceleratorPort:options:];
-[IOGPUMetalDevice newIndirectArgumentEncoderWithLayout:];
-[IOGPUMetalDevice newDevicePoolAliasedCommandAllocator];
-[IOGPUMetalDevice allocBufferSubDataWithLength:options:alignment:heapIndex:bufferIndex:bufferOffset:];
-[IOGPUMetalDevice hasUnifiedMemory];
-[IOGPUMetalDevice _addResource:];
-[IOGPUMetalDevice deviceRef];
-[IOGPUMetalDevice sharedMemorySize];
-[IOGPUMetalDevice registryID];
-[IOGPUMetalDevice recommendedMaxWorkingSetSize];
-[IOGPUMetalDevice launchMappingThread];
-[IOGPUMetalDevice indirectArgumentBufferDecodingData];
-[IOGPUMetalDevice newIndirectArgumentBufferLayoutWithStructType:];
-[IOGPUMetalDevice maxBufferLength];
-[IOGPUMetalDevice supportPriorityBand];
-[IOGPUMetalDevice _removeResource:];
```
