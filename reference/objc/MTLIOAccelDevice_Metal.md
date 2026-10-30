# `MTLIOAccelDevice`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLDevice`
- 25 instance variables, 14 properties, 65 instance methods, 0 class methods

## Instance variables

```
^{__IOAccelDevice=} _deviceRef;
^{__IOAccelShared=} _sharedRef;
I _acceleratorPort;
{?="segmentListShmemPool"@"MTLIOAccelDeviceShmemPool""kernelCommandShmemPool"@"MTLIOAccelDeviceShmemPool""hwResourcePools"^@"hwResourcePoolCount"I"akResourceListPool"@"MTLResourceListPool""akPrivateResourceListPool"@"MTLResourceListPool"} _storageCreateParams;
^{MTLIOAccelCommandBufferStoragePool={storageQueue=^{MTLIOAccelCommandBufferStorage}^^{MTLIOAccelCommandBufferStorage}}{os_unfair_lock_s=I}iAi@} _commandBufferStoragePool;
I _configBits;
I _deviceBits;
Q _textureRam;
Q _videoRam;
Q _sharedMemorySize;
I _accelID;
Ai _numCommandBuffers;
Q _segmentByteThreshold;
[16{MTLIOAccelBufferHeap="buffers"[64@"MTLIOAccelBuffer"]"allocators"[64{MTLRangeAllocator="elements"^{MTLRangeAllocatorElement}"numElements"I"capacity"Q"capacityIncrement"Q"defaultAlignmentMask"Q}]"allocations"[64I]"count"I}] _bufferHeaps;
@"NSObject<OS_dispatch_queue>" _device_dispatch_queue;
@"NSObject<OS_dispatch_queue>" _device_pool_cleanup_queue;
@"NSObject<OS_dispatch_source>" _device_pool_cleanup_source;
B _device_pool_cleanup_scheduled;
I _fenceAllocatedCount;
I _fenceMaximumCount;
I _fenceBitmapSearchStart;
I _fenceBitmapCount;
^Q _fenceAllocationBitmap;
Q _registryID;
@"<MTLDeviceSPI>" _deviceWrapper;
```

## Properties

```
@property (T^@,R) hwResourcePools;
@property (TI,R) hwResourcePoolCount;
@property (Ti,R,D) numCommandBuffers;
@property (TI,R,V_acceleratorPort) acceleratorPort;
@property (TQ,R) sharedMemorySize;
@property (TQ,R) dedicatedMemorySize;
@property (TQ,R) recommendedMaxWorkingSetSize;
@property (TQ,R) registryID;
@property (TB,R) hasUnifiedMemory;
@property (TB,R) supportsVertexAmplification;
@property (TB,R) supportPriorityBand;
@property (TQ,R) currentAllocatedSize;
@property (T@"MTLIOMemoryInfo",R,D) memoryInfo;
@property (TB,R,D) supportLazyInitialization;
```

## Instance methods

```
-[MTLIOAccelDevice newUncachedIOFileHandleWithURL:compressionMethod:error:];
-[MTLIOAccelDevice _setDeviceWrapper:];
-[MTLIOAccelDevice newArgumentEncoderWithLayout:];
-[MTLIOAccelDevice dedicatedMemorySize];
-[MTLIOAccelDevice akResourceListPool];
-[MTLIOAccelDevice newEventWithOptions:];
-[MTLIOAccelDevice currentAllocatedSize];
-[MTLIOAccelDevice newUncachedIOHandleWithURL:error:];
-[MTLIOAccelDevice setComputePipelineStateCommandShmemSize:];
-[MTLIOAccelDevice newIOFileHandleWithURL:compressionMethod:error:];
-[MTLIOAccelDevice newIOFileHandleWithURL:error:];
-[MTLIOAccelDevice initWithAcceleratorPort:];
-[MTLIOAccelDevice newCommandQueueWithDescriptor:];
-[MTLIOAccelDevice newIOHandleWithURL:error:];
-[MTLIOAccelDevice newUncachedIOFileHandleWithURL:error:];
-[MTLIOAccelDevice newIOHandleWithURL:compressionType:error:];
-[MTLIOAccelDevice acceleratorPort];
-[MTLIOAccelDevice newUncachedIOHandleWithURL:compressionType:error:];
-[MTLIOAccelDevice supportsVertexAmplification];
-[MTLIOAccelDevice newAccelerationStructureWithSize:withDescriptor:];
-[MTLIOAccelDevice newEvent];
-[MTLIOAccelDevice _purgeDevice];
-[MTLIOAccelDevice newAccelerationStructureWithBuffer:offset:];
-[MTLIOAccelDevice newIOHandleWithURL:compressionMethod:error:];
-[MTLIOAccelDevice newAccelerationStructureWithBuffer:offset:resourceIndex:];
-[MTLIOAccelDevice _deviceWrapper];
-[MTLIOAccelDevice newIOCommandQueueWithDescriptor:error:];
-[MTLIOAccelDevice setHwResourcePool:count:];
-[MTLIOAccelDevice newAccelerationStructureWithSize:];
-[MTLIOAccelDevice hwResourcePoolCount];
-[MTLIOAccelDevice deallocBufferSubData:heapIndex:bufferIndex:bufferOffset:length:];
-[MTLIOAccelDevice numCommandBuffers];
-[MTLIOAccelDevice supportsVertexAmplificationCount:];
-[MTLIOAccelDevice akPrivateResourceListPool];
-[MTLIOAccelDevice newIndirectCommandBufferWithDescriptor:maxCommandCount:options:];
-[MTLIOAccelDevice newAccelerationStructureWithSize:resourceIndex:];
-[MTLIOAccelDevice dealloc];
-[MTLIOAccelDevice lazyInitialize];
-[MTLIOAccelDevice initialKernelCommandShmemSize];
-[MTLIOAccelDevice newFence];
-[MTLIOAccelDevice setSegmentListShmemSize:];
-[MTLIOAccelDevice supportLazyInitialization];
-[MTLIOAccelDevice setIndirectArgumentBufferDecodingData:];
-[MTLIOAccelDevice hwResourcePools];
-[MTLIOAccelDevice newIntersectionFunctionTableWithDescriptor:];
-[MTLIOAccelDevice initialSegmentListShmemSize];
-[MTLIOAccelDevice memoryInfo];
-[MTLIOAccelDevice newIndirectArgumentEncoderWithLayout:];
-[MTLIOAccelDevice sharedRef];
-[MTLIOAccelDevice allocBufferSubDataWithLength:options:alignment:heapIndex:bufferIndex:bufferOffset:];
-[MTLIOAccelDevice hasUnifiedMemory];
-[MTLIOAccelDevice _addResource:];
-[MTLIOAccelDevice heapIndexWithOptions:];
-[MTLIOAccelDevice deviceRef];
-[MTLIOAccelDevice sharedMemorySize];
-[MTLIOAccelDevice releaseFenceIndex:];
-[MTLIOAccelDevice registryID];
-[MTLIOAccelDevice recommendedMaxWorkingSetSize];
-[MTLIOAccelDevice kickCleanupQueue];
-[MTLIOAccelDevice indirectArgumentBufferDecodingData];
-[MTLIOAccelDevice newIndirectArgumentBufferLayoutWithStructType:];
-[MTLIOAccelDevice maxBufferLength];
-[MTLIOAccelDevice updateResourcePoolPurgeability];
-[MTLIOAccelDevice supportPriorityBand];
-[MTLIOAccelDevice _removeResource:];
```
