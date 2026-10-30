# `AGXG19FamilyTensor`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetalTensor`
- 6 instance variables, 5 properties, 25 instance methods, 0 class methods

## Instance variables

```
^v _impl;
Q _usage;
@"<MTLBuffer>" _buffer;
@"NSArray" _auxiliaryPlanes;
@"<MTLBuffer>" _internalScalesMTLBuffer;
@"<MTLBuffer>" _internalMTLBuffer;
```

## Properties

```
@property (T@"<MTLBuffer>",R,V_buffer) buffer;
@property (TQ,R,V_usage) usage;
@property (T@"<MTLBuffer>",R,V_internalMTLBuffer) internalMTLBuffer;
@property (T@"<MTLBuffer>",R,V_internalScalesMTLBuffer) internalScalesMTLBuffer;
@property (T@"NSArray",R,V_auxiliaryPlanes) auxiliaryPlanes;
```

## Instance methods

```
-[AGXG19FamilyTensor usage];
-[AGXG19FamilyTensor buffer];
-[AGXG19FamilyTensor resourceIndex];
-[AGXG19FamilyTensor dimensions];
-[AGXG19FamilyTensor dealloc];
-[AGXG19FamilyTensor strides];
-[AGXG19FamilyTensor dataType];
-[AGXG19FamilyTensor bufferOffset];
-[AGXG19FamilyTensor gpuResourceID];
-[AGXG19FamilyTensor auxiliaryPlanes];
-[AGXG19FamilyTensor replaceSlice:withBytes:strides:];
-[AGXG19FamilyTensor getBytes:strides:fromSlice:];
-[AGXG19FamilyTensor getBytes:strides:fromSliceOrigin:sliceDimensions:];
-[AGXG19FamilyTensor getBytes:strides:fromSliceOrigin:sliceDimensions:plane:];
-[AGXG19FamilyTensor internalMTLBuffer];
-[AGXG19FamilyTensor replaceSliceOrigin:sliceDimensions:plane:withBytes:strides:];
-[AGXG19FamilyTensor replaceSliceOrigin:sliceDimensions:withBytes:strides:];
-[AGXG19FamilyTensor setShaderValidationDataBufferIndex:];
-[AGXG19FamilyTensor setShaderValidationScalesBufferIndex:];
-[AGXG19FamilyTensor internalScalesMTLBuffer];
-[AGXG19FamilyTensor initWithBuffer:device:rank:dims:strides:offset:dataType:usage:resourceIndex:];
-[AGXG19FamilyTensor initWithDevice:length:rank:dims:strides:offset:auxiliaryPlanes:dataType:usage:resourceIndex:storageMode:resourceOptions:];
-[AGXG19FamilyTensor initWithDevice:length:rank:dims:strides:offset:dataType:usage:];
-[AGXG19FamilyTensor initWithDevice:length:rank:dims:strides:offset:dataType:usage:resourceIndex:storageMode:resourceOptions:];
-[AGXG19FamilyTensor initWithDevice:rank:dims:strides:attachments:auxiliaryPlanes:dataType:usage:resourceIndex:];
```
