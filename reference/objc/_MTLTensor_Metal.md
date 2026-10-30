# `_MTLTensor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLResource`
- Protocols: `MTLTensorSPI`
- 11 instance variables, 30 properties, 34 instance methods, 0 class methods

## Instance variables

```
{MTLResourceID="_impl"Q} _gpuResourceID;
@"<MTLBuffer>" _buffer;
^{__IOSurface=} _iosurface;
@"MTLTensorExtents" _dimensions;
q _dataType;
Q _usage;
@"<MTLTensor>" _parentTensor;
Q _resourceIndex;
@"MTLTensorExtents" _strides;
Q _offset;
Q _plane;
```

## Properties

```
@property (T{MTLResourceID=Q},R,V_gpuResourceID) gpuResourceID;
@property (T@"<MTLBuffer>",R,V_buffer) buffer;
@property (T^{__IOSurface=},R,V_iosurface) iosurface;
@property (T@"MTLTensorExtents",R,V_dimensions) dimensions;
@property (Tq,R,V_dataType) dataType;
@property (TQ,R,V_usage) usage;
@property (T@"<MTLTensor>",R,V_parentTensor) parentTensor;
@property (TQ,R,N,V_resourceIndex) resourceIndex;
@property (T@"MTLTensorExtents",R,V_strides) strides;
@property (TQ,R,D) bufferOffset;
@property (TQ,R,V_offset) offset;
@property (TQ,R,V_plane) plane;
@property (T@"NSArray",R) auxiliaryPlanes;
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R,D) device;
@property (TQ,R,D) cpuCacheMode;
@property (TQ,R,D) storageMode;
@property (TQ,R,D) hazardTrackingMode;
@property (TQ,R,D) resourceOptions;
@property (T@"<MTLHeap>",R,D) heap;
@property (TQ,R,D) heapOffset;
@property (TQ,R) allocatedSize;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Ti,D) responsibleProcess;
@property (TQ,R) allocationID;
@property (TQ,R,D) protectionOptions;
@property (TQ,R,D) unfilteredResourceOptions;
```

## Instance methods

```
-[_MTLTensor usage];
-[_MTLTensor isComplete];
-[_MTLTensor buffer];
-[_MTLTensor resourceIndex];
-[_MTLTensor iosurface];
-[_MTLTensor dimensions];
-[_MTLTensor setOwnerWithIdentity:];
-[_MTLTensor waitUntilComplete];
-[_MTLTensor strides];
-[_MTLTensor setPurgeableState:];
-[_MTLTensor dataType];
-[_MTLTensor bufferOffset];
-[_MTLTensor isAliasable];
-[_MTLTensor gpuResourceID];
-[_MTLTensor makeAliasable];
-[_MTLTensor isPurgeable];
-[_MTLTensor offset];
-[_MTLTensor auxiliaryPlanes];
-[_MTLTensor replaceSlice:withBytes:strides:];
-[_MTLTensor isWriteComplete];
-[_MTLTensor doesAliasAllResources:count:];
-[_MTLTensor doesAliasAnyResources:count:];
-[_MTLTensor doesAliasResource:];
-[_MTLTensor getBytes:strides:fromSlice:];
-[_MTLTensor getBytes:strides:fromSliceOrigin:sliceDimensions:];
-[_MTLTensor getBytes:strides:fromSliceOrigin:sliceDimensions:plane:];
-[_MTLTensor internalMTLBuffer];
-[_MTLTensor isTensorViewableWithReshapedDescriptor:];
-[_MTLTensor newTensorViewWithReshapedDescriptor:error:];
-[_MTLTensor newTensorViewWithSlice:error:];
-[_MTLTensor parentTensor];
-[_MTLTensor plane];
-[_MTLTensor replaceSliceOrigin:sliceDimensions:plane:withBytes:strides:];
-[_MTLTensor replaceSliceOrigin:sliceDimensions:withBytes:strides:];
```
