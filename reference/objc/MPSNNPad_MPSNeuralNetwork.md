# `MPSNNPad`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNKernel`
- 5 instance variables, 3 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"<MTLBuffer>" _aBuf;
Q _aBufFP32Len;
f _fillValue;
{MPSImageCoordinate="x"Q"y"Q"channel"Q} _paddingSizeBefore;
{MPSImageCoordinate="x"Q"y"Q"channel"Q} _paddingSizeAfter;
```

## Properties

```
@property (T{MPSImageCoordinate=QQQ},N,V_paddingSizeBefore) paddingSizeBefore;
@property (T{MPSImageCoordinate=QQQ},N,V_paddingSizeAfter) paddingSizeAfter;
@property (Tf,N,V_fillValue) fillValue;
```

## Class methods

```
+[MPSNNPad libraryInfo:];
```

## Instance methods

```
-[MPSNNPad initWithDevice:];
-[MPSNNPad debugDescription];
-[MPSNNPad dealloc];
-[MPSNNPad resultStateForSourceImage:sourceStates:destinationImage:];
-[MPSNNPad copyWithZone:device:];
-[MPSNNPad initWithCoder:device:];
-[MPSNNPad temporaryResultStateForCommandBuffer:sourceImage:sourceStates:destinationImage:];
-[MPSNNPad encodeWithCoder:];
-[MPSNNPad isResultStateReusedAcrossBatch];
-[MPSNNPad fillValue];
-[MPSNNPad destinationImageDescriptorForSourceImages:sourceStates:];
-[MPSNNPad initWithDevice:paddingSizeBefore:paddingSizeAfter:];
-[MPSNNPad initWithDevice:paddingSizeBefore:paddingSizeAfter:fillValueArray:];
-[MPSNNPad paddingSizeAfter];
-[MPSNNPad paddingSizeBefore];
-[MPSNNPad setFillValue:];
-[MPSNNPad setPaddingSizeAfter:];
-[MPSNNPad setPaddingSizeBefore:];
```
