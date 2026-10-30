# `MTLTensorSPI` (protocol)

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLTensor`, `MTLResourceSPI`
- 0 instance variables, 3 properties, 11 instance methods, 0 class methods

## Properties

```
@property (TQ,R,N) resourceIndex;
@property (TQ,R) offset;
@property (T@"<MTLTensor>",R) parentTensor;
```

## Instance methods

```
-[MTLTensorSPI resourceIndex];
-[MTLTensorSPI offset];
-[MTLTensorSPI replaceSlice:withBytes:strides:];
-[MTLTensorSPI getBytes:strides:fromSlice:];
-[MTLTensorSPI internalMTLBuffer];
-[MTLTensorSPI isTensorViewableWithReshapedDescriptor:];
-[MTLTensorSPI newTensorViewWithReshapedDescriptor:error:];
-[MTLTensorSPI newTensorViewWithSlice:error:];
-[MTLTensorSPI parentTensor];
-[MTLTensorSPI setShaderValidationDataBufferIndex:];
-[MTLTensorSPI setShaderValidationScalesBufferIndex:];
```
