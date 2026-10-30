# `MTLTensor` (protocol)

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLResource`
- 0 instance variables, 8 properties, 12 instance methods, 0 class methods

## Properties

```
@property (T{MTLResourceID=Q},R) gpuResourceID;
@property (T@"<MTLBuffer>",R) buffer;
@property (TQ,R) bufferOffset;
@property (T@"MTLTensorExtents",R) strides;
@property (T@"MTLTensorExtents",R) dimensions;
@property (Tq,R) dataType;
@property (TQ,R) usage;
@property (T@"NSArray",R) auxiliaryPlanes;
```

## Instance methods

```
-[MTLTensor usage];
-[MTLTensor buffer];
-[MTLTensor dimensions];
-[MTLTensor strides];
-[MTLTensor dataType];
-[MTLTensor bufferOffset];
-[MTLTensor gpuResourceID];
-[MTLTensor auxiliaryPlanes];
-[MTLTensor getBytes:strides:fromSliceOrigin:sliceDimensions:];
-[MTLTensor getBytes:strides:fromSliceOrigin:sliceDimensions:plane:];
-[MTLTensor replaceSliceOrigin:sliceDimensions:plane:withBytes:strides:];
-[MTLTensor replaceSliceOrigin:sliceDimensions:withBytes:strides:];
```
