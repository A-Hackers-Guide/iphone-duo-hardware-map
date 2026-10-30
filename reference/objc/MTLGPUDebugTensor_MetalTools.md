# `MTLGPUDebugTensor`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsTensor`
- Protocols: `MTLGPUDebugResource`
- 1 instance variables, 21 properties, 13 instance methods, 0 class methods

## Instance variables

```
Q _identifier;
```

## Properties

```
@property (T@"<MTLResource>",R,N) baseObject;
@property (TQ,R,N) length;
@property (TQ,R,N) gpuAddress;
@property (TQ,R,N) underlyingGPUAddress;
@property (Ti) responsibleProcess;
@property (TQ,R) allocationID;
@property (TQ,R) protectionOptions;
@property (TQ,R) unfilteredResourceOptions;
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
```

## Instance methods

```
-[MTLGPUDebugTensor setLabel:];
-[MTLGPUDebugTensor dealloc];
-[MTLGPUDebugTensor initWithBaseObject:parent:];
-[MTLGPUDebugTensor internalMTLBuffer];
-[MTLGPUDebugTensor newTensorViewWithReshapedDescriptor:error:];
-[MTLGPUDebugTensor newTensorViewWithSlice:error:];
-[MTLGPUDebugTensor _initInternalBuffers];
-[MTLGPUDebugTensor initWithBaseObject:buffer:offset:];
-[MTLGPUDebugTensor initWithBaseObject:device:attachments:];
-[MTLGPUDebugTensor initWithBaseObject:parentTensor:];
-[MTLGPUDebugTensor initializeTensorStackTrace];
-[MTLGPUDebugTensor useWithComputeEncoder:usage:];
-[MTLGPUDebugTensor useWithRenderEncoder:usage:stages:];
```
