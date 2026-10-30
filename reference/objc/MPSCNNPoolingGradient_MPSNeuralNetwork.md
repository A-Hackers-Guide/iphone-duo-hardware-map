# `MPSCNNPoolingGradient`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNGradientKernel`
- 1 instance variables, 1 properties, 10 instance methods, 1 class methods

## Instance variables

```
{?="width"Q"height"Q"depth"Q} _sourceSize;
```

## Properties

```
@property (T{?=QQQ},N,V_sourceSize) sourceSize;
```

## Class methods

```
+[MPSCNNPoolingGradient libraryInfo:];
```

## Instance methods

```
-[MPSCNNPoolingGradient initWithDevice:];
-[MPSCNNPoolingGradient maxBatchSize];
-[MPSCNNPoolingGradient copyWithZone:device:];
-[MPSCNNPoolingGradient initWithCoder:device:];
-[MPSCNNPoolingGradient initWithDevice:kernelWidth:kernelHeight:strideInPixelsX:strideInPixelsY:];
-[MPSCNNPoolingGradient encodeWithCoder:];
-[MPSCNNPoolingGradient initWithDevice:kernelWidth:kernelHeight:];
-[MPSCNNPoolingGradient setSourceSize:];
-[MPSCNNPoolingGradient sourceSize];
-[MPSCNNPoolingGradient setKernelWidth:kernelHeight:strideInPixelsX:strideInPixelsY:];
```
