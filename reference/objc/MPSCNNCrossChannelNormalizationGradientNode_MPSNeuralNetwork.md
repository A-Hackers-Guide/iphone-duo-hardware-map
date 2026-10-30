# `MPSCNNCrossChannelNormalizationGradientNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNGradientFilterNode`
- 1 instance variables, 1 properties, 4 instance methods, 1 class methods

## Instance variables

```
Q _kernelSize;
```

## Properties

```
@property (TQ,R,N,V_kernelSize) kernelSize;
```

## Class methods

```
+[MPSCNNCrossChannelNormalizationGradientNode nodeWithSourceGradient:sourceImage:gradientState:kernelSize:];
```

## Instance methods

```
-[MPSCNNCrossChannelNormalizationGradientNode initWithGradientImages:forwardFilter:];
-[MPSCNNCrossChannelNormalizationGradientNode initWithSourceGradient:sourceImage:gradientState:kernelSize:];
-[MPSCNNCrossChannelNormalizationGradientNode kernelSize];
-[MPSCNNCrossChannelNormalizationGradientNode newFilterNode];
```
