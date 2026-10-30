# `MTLTensorSPI` (protocol)

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
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
