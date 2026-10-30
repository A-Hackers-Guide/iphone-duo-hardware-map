# `MPSNNLocalCorrelation`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNReduceBinary`
- 4 instance variables, 4 properties, 14 instance methods, 0 class methods

## Instance variables

```
Q _windowInX;
Q _windowInY;
Q _strideInX;
Q _strideInY;
```

## Properties

```
@property (TQ,N,V_windowInX) windowInX;
@property (TQ,N,V_windowInY) windowInY;
@property (TQ,N,V_strideInX) strideInX;
@property (TQ,N,V_strideInY) strideInY;
```

## Instance methods

```
-[MPSNNLocalCorrelation initWithDevice:];
-[MPSNNLocalCorrelation copyWithZone:device:];
-[MPSNNLocalCorrelation initWithCoder:device:];
-[MPSNNLocalCorrelation encodeWithCoder:];
-[MPSNNLocalCorrelation initWithDevice:windowInX:windowInY:strideInX:strideInY:];
-[MPSNNLocalCorrelation setStrideInX:];
-[MPSNNLocalCorrelation setStrideInY:];
-[MPSNNLocalCorrelation strideInX];
-[MPSNNLocalCorrelation strideInY];
-[MPSNNLocalCorrelation destinationImageDescriptorForSourceImages:sourceStates:paddingMethod:primaryOffset:secondaryOffset:kernelOffset:];
-[MPSNNLocalCorrelation setWindowInX:];
-[MPSNNLocalCorrelation setWindowInY:];
-[MPSNNLocalCorrelation windowInX];
-[MPSNNLocalCorrelation windowInY];
```
