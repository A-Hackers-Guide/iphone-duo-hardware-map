# `MPSCNNUpsamplingBilinearGradientNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNGradientFilterNode`
- 2 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
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
+[MPSCNNUpsamplingBilinearGradientNode nodeWithSourceGradient:sourceImage:gradientState:scaleFactorX:scaleFactorY:];
```

## Instance methods

```
-[MPSCNNUpsamplingBilinearGradientNode scaleFactorX];
-[MPSCNNUpsamplingBilinearGradientNode scaleFactorY];
-[MPSCNNUpsamplingBilinearGradientNode initWithGradientImages:forwardFilter:];
-[MPSCNNUpsamplingBilinearGradientNode initWithSourceGradient:sourceImage:gradientState:scaleFactorX:scaleFactorY:];
-[MPSCNNUpsamplingBilinearGradientNode newFilterNode];
```
