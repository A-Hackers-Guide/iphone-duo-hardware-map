# `MPSCNNUpsamplingGradient`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNGradientKernel`
- 3 instance variables, 2 properties, 9 instance methods, 1 class methods

## Instance variables

```
Q _filterType;
d _scaleFactorX;
d _scaleFactorY;
```

## Properties

```
@property (Td,R,N,V_scaleFactorX) scaleFactorX;
@property (Td,R,N,V_scaleFactorY) scaleFactorY;
```

## Class methods

```
+[MPSCNNUpsamplingGradient libraryInfo:];
```

## Instance methods

```
-[MPSCNNUpsamplingGradient initWithDevice:];
-[MPSCNNUpsamplingGradient debugDescription];
-[MPSCNNUpsamplingGradient copyWithZone:device:];
-[MPSCNNUpsamplingGradient initWithCoder:device:];
-[MPSCNNUpsamplingGradient encodeWithCoder:];
-[MPSCNNUpsamplingGradient scaleFactorX];
-[MPSCNNUpsamplingGradient scaleFactorY];
-[MPSCNNUpsamplingGradient destinationImageDescriptorForSourceImages:sourceStates:];
-[MPSCNNUpsamplingGradient initWithDevice:filterType:integerScaleFactorX:integerScaleFactorY:];
```
