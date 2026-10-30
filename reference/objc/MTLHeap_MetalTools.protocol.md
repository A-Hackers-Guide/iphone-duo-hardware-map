# `MTLHeap` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLAllocation`
- 0 instance variables, 10 properties, 21 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R) device;
@property (TQ,R) storageMode;
@property (TQ,R) cpuCacheMode;
@property (TQ,R) hazardTrackingMode;
@property (TQ,R) resourceOptions;
@property (TQ,R) size;
@property (TQ,R) usedSize;
@property (TQ,R) currentAllocatedSize;
@property (Tq,R) type;
```

## Instance methods

```
-[MTLHeap resourceOptions];
-[MTLHeap currentAllocatedSize];
-[MTLHeap usedSize];
-[MTLHeap hazardTrackingMode];
-[MTLHeap cpuCacheMode];
-[MTLHeap newAccelerationStructureWithSize:];
-[MTLHeap storageMode];
-[MTLHeap newTextureWithDescriptor:offset:];
-[MTLHeap newAccelerationStructureWithDescriptor:offset:];
-[MTLHeap device];
-[MTLHeap label];
-[MTLHeap newBufferWithLength:options:offset:];
-[MTLHeap newAccelerationStructureWithDescriptor:];
-[MTLHeap setLabel:];
-[MTLHeap newAccelerationStructureWithSize:offset:];
-[MTLHeap newTextureWithDescriptor:];
-[MTLHeap size];
-[MTLHeap type];
-[MTLHeap setPurgeableState:];
-[MTLHeap maxAvailableSizeWithAlignment:];
-[MTLHeap newBufferWithLength:options:];
```
