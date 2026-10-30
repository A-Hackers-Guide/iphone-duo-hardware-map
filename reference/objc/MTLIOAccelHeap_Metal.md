# `MTLIOAccelHeap`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLHeap`
- 5 instance variables, 12 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"MTLIOAccelResource" _resource;
@"MTLIOAccelDevice<MTLDevice>" _device;
{MTLRangeAllocator="elements"^{MTLRangeAllocatorElement}"numElements"I"capacity"Q"capacityIncrement"Q"defaultAlignmentMask"Q} _allocator;
{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]} _mutex;
Q _size;
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
@property (TQ,R,D) hazardTrackingMode;
@property (TQ,R,D) resourceOptions;
@property (TQ,R,D) unfilteredResourceOptions;
@property (TQ,R,N) protectionOptions;
@property (Tq,R,D) type;
```

## Instance methods

```
-[MTLIOAccelHeap currentAllocatedSize];
-[MTLIOAccelHeap usedSize];
-[MTLIOAccelHeap initWithDevice:size:options:args:argsSize:];
-[MTLIOAccelHeap newAccelerationStructureWithSize:];
-[MTLIOAccelHeap newAccelerationStructureWithDescriptor:offset:];
-[MTLIOAccelHeap newAccelerationStructureWithSize:offset:resourceIndex:];
-[MTLIOAccelHeap protectionOptions];
-[MTLIOAccelHeap device];
-[MTLIOAccelHeap newAccelerationStructureWithDescriptor:];
-[MTLIOAccelHeap newAccelerationStructureWithSize:offset:];
-[MTLIOAccelHeap newAccelerationStructureWithSize:resourceIndex:];
-[MTLIOAccelHeap dealloc];
-[MTLIOAccelHeap gpuAddress];
-[MTLIOAccelHeap unpinMemoryAtOffset:withLength:];
-[MTLIOAccelHeap size];
-[MTLIOAccelHeap initWithDevice:size:options:args:argsSize:desc:];
-[MTLIOAccelHeap newSubResourceAtOffset:withLength:alignment:options:];
-[MTLIOAccelHeap setPurgeableState:];
-[MTLIOAccelHeap deallocHeapSubResource];
-[MTLIOAccelHeap newSubResourceWithLength:alignment:options:offset:];
-[MTLIOAccelHeap maxAvailableSizeWithAlignment:];
```
