# `MTLToolsTensor`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsResource`
- Protocols: `MTLTensorSPI`
- 4 instance variables, 29 properties, 34 instance methods, 0 class methods

## Instance variables

```
@"<MTLBuffer>" _internalMTLBuffer;
@"<MTLTensor>" _parentTensor;
@"MTLTensorBufferAttachments" _attachments;
@"NSArray" _auxiliaryPlanes;
```

## Properties

```
@property (T@"<MTLTensor>",R,V_parentTensor) parentTensor;
@property (T@"<MTLBuffer>",R) buffer;
@property (T@"MTLTensorBufferAttachments",R,V_attachments) attachments;
@property (TQ,R,N) resourceIndex;
@property (TQ,R) offset;
@property (T{MTLResourceID=Q},R) gpuResourceID;
@property (TQ,R) bufferOffset;
@property (T@"MTLTensorExtents",R) strides;
@property (T@"MTLTensorExtents",R) dimensions;
@property (Tq,R) dataType;
@property (TQ,R) usage;
@property (T@"NSArray",R) auxiliaryPlanes;
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R) device;
@property (TQ,R) cpuCacheMode;
@property (TQ,R) storageMode;
@property (TQ,R) hazardTrackingMode;
@property (TQ,R) resourceOptions;
@property (T@"<MTLHeap>",R) heap;
@property (TQ,R) heapOffset;
@property (TQ,R) allocatedSize;
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
-[MTLToolsTensor usage];
-[MTLToolsTensor buffer];
-[MTLToolsTensor resourceIndex];
-[MTLToolsTensor dimensions];
-[MTLToolsTensor dealloc];
-[MTLToolsTensor attachments];
-[MTLToolsTensor strides];
-[MTLToolsTensor dataType];
-[MTLToolsTensor bufferOffset];
-[MTLToolsTensor gpuResourceID];
-[MTLToolsTensor offset];
-[MTLToolsTensor auxiliaryPlanes];
-[MTLToolsTensor replaceSlice:withBytes:strides:];
-[MTLToolsTensor getBytes:strides:fromSlice:];
-[MTLToolsTensor getBytes:strides:fromSliceOrigin:sliceDimensions:];
-[MTLToolsTensor getBytes:strides:fromSliceOrigin:sliceDimensions:plane:];
-[MTLToolsTensor initWithBaseObject:parent:];
-[MTLToolsTensor internalMTLBuffer];
-[MTLToolsTensor isTensorViewableWithReshapedDescriptor:];
-[MTLToolsTensor newTensorViewWithReshapedDescriptor:error:];
-[MTLToolsTensor newTensorViewWithSlice:error:];
-[MTLToolsTensor parentTensor];
-[MTLToolsTensor replaceSliceOrigin:sliceDimensions:plane:withBytes:strides:];
-[MTLToolsTensor replaceSliceOrigin:sliceDimensions:withBytes:strides:];
-[MTLToolsTensor _initAuxiliaryPlanes];
-[MTLToolsTensor _initInternalBuffers];
-[MTLToolsTensor initWithBaseObject:buffer:offset:];
-[MTLToolsTensor initWithBaseObject:buffer:offset:initializeInternalBuffers:];
-[MTLToolsTensor initWithBaseObject:device:attachments:];
-[MTLToolsTensor initWithBaseObject:device:attachments:initializeInternalBuffers:];
-[MTLToolsTensor initWithBaseObject:parent:initializeInternalBuffers:];
-[MTLToolsTensor initWithBaseObject:parentTensor:];
-[MTLToolsTensor initWithBaseObject:parentTensor:initializeInternalBuffers:];
-[MTLToolsTensor wrapChildTensor:];
```
