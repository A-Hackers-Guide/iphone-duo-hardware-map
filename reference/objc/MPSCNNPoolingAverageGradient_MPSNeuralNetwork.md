# `MPSCNNPoolingAverageGradient`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNPoolingGradient`
- 2 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
Q _zeroPadSizeX;
Q _zeroPadSizeY;
```

## Properties

```
@property (TQ,N,V_zeroPadSizeX) zeroPadSizeX;
@property (TQ,N,V_zeroPadSizeY) zeroPadSizeY;
```

## Instance methods

```
-[MPSCNNPoolingAverageGradient debugDescription];
-[MPSCNNPoolingAverageGradient copyWithZone:device:];
-[MPSCNNPoolingAverageGradient initWithCoder:device:];
-[MPSCNNPoolingAverageGradient initWithDevice:kernelWidth:kernelHeight:strideInPixelsX:strideInPixelsY:];
-[MPSCNNPoolingAverageGradient encodeWithCoder:];
-[MPSCNNPoolingAverageGradient setZeroPadSizeX:];
-[MPSCNNPoolingAverageGradient setZeroPadSizeY:];
-[MPSCNNPoolingAverageGradient zeroPadSizeX];
-[MPSCNNPoolingAverageGradient zeroPadSizeY];
```
