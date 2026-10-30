# `MPSCNNDropoutGradientNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNGradientFilterNode`
- 3 instance variables, 3 properties, 6 instance methods, 1 class methods

## Instance variables

```
f _keepProbability;
Q _seed;
{?="width"Q"height"Q"depth"Q} _maskStride;
```

## Properties

```
@property (Tf,R,N,V_keepProbability) keepProbability;
@property (TQ,R,N,V_seed) seed;
@property (T{?=QQQ},R,N,V_maskStride) maskStrideInPixels;
```

## Class methods

```
+[MPSCNNDropoutGradientNode nodeWithSourceGradient:sourceImage:gradientState:keepProbability:seed:maskStrideInPixels:];
```

## Instance methods

```
-[MPSCNNDropoutGradientNode seed];
-[MPSCNNDropoutGradientNode keepProbability];
-[MPSCNNDropoutGradientNode initWithGradientImages:forwardFilter:];
-[MPSCNNDropoutGradientNode initWithSourceGradient:sourceImage:gradientState:keepProbability:seed:maskStrideInPixels:];
-[MPSCNNDropoutGradientNode maskStrideInPixels];
-[MPSCNNDropoutGradientNode newFilterNode];
```
