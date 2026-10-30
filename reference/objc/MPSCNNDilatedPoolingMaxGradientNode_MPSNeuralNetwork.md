# `MPSCNNDilatedPoolingMaxGradientNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNPoolingGradientNode`
- 2 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
Q _dilationRateX;
Q _dilationRateY;
```

## Properties

```
@property (TQ,R,N,V_dilationRateX) dilationRateX;
@property (TQ,R,N,V_dilationRateY) dilationRateY;
```

## Class methods

```
+[MPSCNNDilatedPoolingMaxGradientNode nodeWithSourceGradient:sourceImage:gradientState:kernelWidth:kernelHeight:strideInPixelsX:strideInPixelsY:dilationRateX:dilationRateY:];
```

## Instance methods

```
-[MPSCNNDilatedPoolingMaxGradientNode dilationRateX];
-[MPSCNNDilatedPoolingMaxGradientNode dilationRateY];
-[MPSCNNDilatedPoolingMaxGradientNode initWithGradientImages:forwardFilter:];
-[MPSCNNDilatedPoolingMaxGradientNode initWithSourceGradient:sourceImage:gradientState:kernelWidth:kernelHeight:strideInPixelsX:strideInPixelsY:dilationRateX:dilationRateY:];
-[MPSCNNDilatedPoolingMaxGradientNode newFilterNode];
```
