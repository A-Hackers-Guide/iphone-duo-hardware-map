# `_MTLHeap`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLAllocation`
- 3 instance variables, 9 properties, 27 instance methods, 0 class methods

## Instance variables

```
Q _heapResourceOptions;
q _heapType;
Q _gpuAddress;
```

## Properties

```
@property (Tq,R) type;
@property (TQ,R) cpuCacheMode;
@property (TQ,R) storageMode;
@property (TQ,R) hazardTrackingMode;
@property (TQ,R) resourceOptions;
@property (TQ,R) unfilteredResourceOptions;
@property (TQ,R) memoryPoolId;
@property (TQ,R) allocatedSize;
@property (TQ,R,N,V_gpuAddress) gpuAddress;
```

## Instance methods

```
-[_MTLHeap resourceOptions];
-[_MTLHeap hazardTrackingMode];
-[_MTLHeap detachBacking];
-[_MTLHeap cpuCacheMode];
-[_MTLHeap newBufferWithDescriptor:offset:];
-[_MTLHeap newAccelerationStructureWithSize:];
-[_MTLHeap memoryPoolId];
-[_MTLHeap storageMode];
-[_MTLHeap unfilteredResourceOptions];
-[_MTLHeap newTextureWithDescriptor:offset:];
-[_MTLHeap newAccelerationStructureWithDescriptor:offset:];
-[_MTLHeap newTextureWithDescriptor:atOffset:];
-[_MTLHeap newAccelerationStructureWithSize:offset:resourceIndex:];
-[_MTLHeap replaceBackingWithRanges:readOnly:];
-[_MTLHeap formattedDescription:];
-[_MTLHeap newBufferWithDescriptor:];
-[_MTLHeap init];
-[_MTLHeap newBufferWithLength:options:offset:];
-[_MTLHeap newAccelerationStructureWithDescriptor:];
-[_MTLHeap initWithType:options:];
-[_MTLHeap allocatedSize];
-[_MTLHeap newAccelerationStructureWithSize:offset:];
-[_MTLHeap newAccelerationStructureWithSize:resourceIndex:];
-[_MTLHeap gpuAddress];
-[_MTLHeap type];
-[_MTLHeap newBufferWithLength:options:atOffset:];
-[_MTLHeap description];
```
