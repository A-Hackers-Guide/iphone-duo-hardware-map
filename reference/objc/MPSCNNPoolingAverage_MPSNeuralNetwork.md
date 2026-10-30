# `MPSCNNPoolingAverage`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNPooling`
- 2 instance variables, 2 properties, 12 instance methods, 0 class methods

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
-[MPSCNNPoolingAverage debugDescription];
-[MPSCNNPoolingAverage newPlugin];
-[MPSCNNPoolingAverage copyWithZone:device:];
-[MPSCNNPoolingAverage initWithCoder:device:];
-[MPSCNNPoolingAverage initWithDevice:kernelWidth:kernelHeight:strideInPixelsX:strideInPixelsY:];
-[MPSCNNPoolingAverage encodeWithCoder:];
-[MPSCNNPoolingAverage isResultStateReusedAcrossBatch];
-[MPSCNNPoolingAverage setZeroPadSizeX:];
-[MPSCNNPoolingAverage setZeroPadSizeY:];
-[MPSCNNPoolingAverage pluginSupportsBatchEncode];
-[MPSCNNPoolingAverage zeroPadSizeX];
-[MPSCNNPoolingAverage zeroPadSizeY];
```
