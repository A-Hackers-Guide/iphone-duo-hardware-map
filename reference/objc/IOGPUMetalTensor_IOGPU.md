# `IOGPUMetalTensor`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetalResource`
- Protocols: `MTLTensorSPI`
- 3 instance variables, 29 properties, 35 instance methods, 0 class methods

## Instance variables

```
@"<MTLTensor>" _parentTensor;
@"<MTLBuffer>" _buffer;
Q _allocatedSize;
```

## Properties

```
@property (T{MTLResourceID=Q},R,D) gpuResourceID;
@property (T@"<MTLBuffer>",R,V_buffer) buffer;
@property (T@"MTLTensorExtents",R,D) dimensions;
@property (Tq,R,D) dataType;
@property (TQ,R,D) usage;
@property (T@"<MTLTensor>",R,V_parentTensor) parentTensor;
@property (T@"NSArray",R,D) auxiliaryPlanes;
@property (TQ,R,D,N) resourceIndex;
@property (T@"MTLTensorExtents",R,D) strides;
@property (TQ,R,D) offset;
@property (TQ,R,D) plane;
@property (TQ,R) bufferOffset;
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R) device;
@property (TQ,R) cpuCacheMode;
@property (TQ,R) storageMode;
@property (TQ,R) hazardTrackingMode;
@property (TQ,R) resourceOptions;
@property (T@"<MTLHeap>",R) heap;
@property (TQ,R) heapOffset;
@property (TQ,R,V_allocatedSize) allocatedSize;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Ti) responsibleProcess;
@property (TQ,R) allocationID;
@property (TQ,R) protectionOptions;
@property (TQ,R) unfilteredResourceOptions;
```

## Instance methods

```
-[IOGPUMetalTensor usage];
-[IOGPUMetalTensor isComplete];
-[IOGPUMetalTensor buffer];
-[IOGPUMetalTensor resourceIndex];
-[IOGPUMetalTensor iosurface];
-[IOGPUMetalTensor dimensions];
-[IOGPUMetalTensor allocatedSize];
-[IOGPUMetalTensor dealloc];
-[IOGPUMetalTensor waitUntilComplete];
-[IOGPUMetalTensor strides];
-[IOGPUMetalTensor setPurgeableState:];
-[IOGPUMetalTensor dataType];
-[IOGPUMetalTensor isAliasable];
-[IOGPUMetalTensor gpuResourceID];
-[IOGPUMetalTensor makeAliasable];
-[IOGPUMetalTensor isPurgeable];
-[IOGPUMetalTensor offset];
-[IOGPUMetalTensor initWithBuffer:];
-[IOGPUMetalTensor replaceSlice:withBytes:strides:];
-[IOGPUMetalTensor isWriteComplete];
-[IOGPUMetalTensor doesAliasAllResources:count:];
-[IOGPUMetalTensor doesAliasAnyResources:count:];
-[IOGPUMetalTensor doesAliasResource:];
-[IOGPUMetalTensor getBytes:strides:fromSlice:];
-[IOGPUMetalTensor getBytes:strides:fromSliceOrigin:sliceDimensions:];
-[IOGPUMetalTensor getBytes:strides:fromSliceOrigin:sliceDimensions:plane:];
-[IOGPUMetalTensor internalMTLBuffer];
-[IOGPUMetalTensor isTensorViewableWithReshapedDescriptor:];
-[IOGPUMetalTensor newTensorViewWithReshapedDescriptor:error:];
-[IOGPUMetalTensor newTensorViewWithSlice:error:];
-[IOGPUMetalTensor parentTensor];
-[IOGPUMetalTensor plane];
-[IOGPUMetalTensor replaceSliceOrigin:sliceDimensions:plane:withBytes:strides:];
-[IOGPUMetalTensor replaceSliceOrigin:sliceDimensions:withBytes:strides:];
-[IOGPUMetalTensor internalScalesMTLBuffer];
```
