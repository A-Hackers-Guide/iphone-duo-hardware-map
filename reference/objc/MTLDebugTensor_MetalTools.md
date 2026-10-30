# `MTLDebugTensor`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsTensor`
- Protocols: `MTLDebugResourcePurgeable`
- 3 instance variables, 0 properties, 19 instance methods, 0 class methods

## Instance variables

```
{atomic<int>="__a_"{__cxx_atomic_impl<int, std::__cxx_atomic_base_impl<int>>="__a_value"Ai}} _purgeableStateToken;
B _purgeableStateHasBeenSet;
@"MTLTensorDescriptor" _descriptor;
```

## Instance methods

```
-[MTLDebugTensor dealloc];
-[MTLDebugTensor setPurgeableState:];
-[MTLDebugTensor getBytes:strides:fromSliceOrigin:sliceDimensions:];
-[MTLDebugTensor getBytes:strides:fromSliceOrigin:sliceDimensions:plane:];
-[MTLDebugTensor internalMTLBuffer];
-[MTLDebugTensor newTensorViewWithReshapedDescriptor:error:];
-[MTLDebugTensor newTensorViewWithSlice:error:];
-[MTLDebugTensor replaceSliceOrigin:sliceDimensions:plane:withBytes:strides:];
-[MTLDebugTensor replaceSliceOrigin:sliceDimensions:withBytes:strides:];
-[MTLDebugTensor purgeableStateValidForRendering];
-[MTLDebugTensor _initInternalBuffers];
-[MTLDebugTensor hasPlane:];
-[MTLDebugTensor initWithBaseObject:buffer:offset:descriptor:];
-[MTLDebugTensor initWithBaseObject:device:attachments:descriptor:];
-[MTLDebugTensor initWithBaseObject:device:descriptor:];
-[MTLDebugTensor initWithBaseObject:parentTensor:descriptor:];
-[MTLDebugTensor lockPurgeableState];
-[MTLDebugTensor tensorDataTypeForPlane:];
-[MTLDebugTensor unlockPurgeableState];
```
