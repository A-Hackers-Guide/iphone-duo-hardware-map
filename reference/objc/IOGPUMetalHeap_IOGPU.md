# `IOGPUMetalHeap`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLHeap`
- 6 instance variables, 14 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"IOGPUMetalResource" _resource;
@"IOGPUMetalDevice<MTLDevice>" _device;
Q _size;
{MTLRangeAllocator="elements"^{MTLRangeAllocatorElement}"numElements"I"capacity"Q"capacityIncrement"Q"defaultAlignmentMask"Q} _allocator;
{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]} _mutex;
q _maxCompatiblePlacementSparsePageSize;
```

## Properties

```
@property (T@"NSString",C,D) label;
@property (T@"<MTLDevice>",R) device;
@property (TQ,R) size;
@property (TQ,R) usedSize;
@property (TQ,R,D) storageMode;
@property (TQ,R,D) cpuCacheMode;
@property (TQ,R) currentAllocatedSize;
@property (TQ,R) globalTraceObjectID;
@property (TQ,R,D) hazardTrackingMode;
@property (TQ,R,D) resourceOptions;
@property (TQ,R,D) unfilteredResourceOptions;
@property (TQ,R,N) protectionOptions;
@property (Tq,R,D) type;
@property (Tq,R,V_maxCompatiblePlacementSparsePageSize) maxCompatiblePlacementSparsePageSize;
```

## Instance methods

```
-[IOGPUMetalHeap currentAllocatedSize];
-[IOGPUMetalHeap usedSize];
-[IOGPUMetalHeap detachBacking];
-[IOGPUMetalHeap initWithDevice:size:options:args:argsSize:];
-[IOGPUMetalHeap newAccelerationStructureWithSize:];
-[IOGPUMetalHeap newAccelerationStructureWithDescriptor:offset:];
-[IOGPUMetalHeap newAccelerationStructureWithSize:offset:resourceIndex:];
-[IOGPUMetalHeap replaceBackingWithRanges:readOnly:];
-[IOGPUMetalHeap protectionOptions];
-[IOGPUMetalHeap device];
-[IOGPUMetalHeap newAccelerationStructureWithDescriptor:];
-[IOGPUMetalHeap setLabel:];
-[IOGPUMetalHeap globalTraceObjectID];
-[IOGPUMetalHeap newAccelerationStructureWithSize:offset:];
-[IOGPUMetalHeap newAccelerationStructureWithSize:resourceIndex:];
-[IOGPUMetalHeap dealloc];
-[IOGPUMetalHeap gpuAddress];
-[IOGPUMetalHeap unpinMemoryAtOffset:withLength:];
-[IOGPUMetalHeap size];
-[IOGPUMetalHeap initWithDevice:size:options:args:argsSize:desc:];
-[IOGPUMetalHeap newSubResourceAtOffset:withLength:alignment:options:];
-[IOGPUMetalHeap setPurgeableState:];
-[IOGPUMetalHeap deallocHeapSubResource];
-[IOGPUMetalHeap newSubResourceWithLength:alignment:options:offset:];
-[IOGPUMetalHeap maxAvailableSizeWithAlignment:];
-[IOGPUMetalHeap maxCompatiblePlacementSparsePageSize];
```
