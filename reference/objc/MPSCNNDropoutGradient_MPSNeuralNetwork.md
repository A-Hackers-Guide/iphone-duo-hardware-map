# `MPSCNNDropoutGradient`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNGradientKernel`
- 3 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
f _keepProbability;
Q _seed;
{?="width"Q"height"Q"depth"Q} _maskStrideInPixels;
```

## Properties

```
@property (Tf,R,N,V_keepProbability) keepProbability;
@property (TQ,R,N,V_seed) seed;
@property (T{?=QQQ},R,N,V_maskStrideInPixels) maskStrideInPixels;
```

## Class methods

```
+[MPSCNNDropoutGradient libraryInfo:];
```

## Instance methods

```
-[MPSCNNDropoutGradient seed];
-[MPSCNNDropoutGradient debugDescription];
-[MPSCNNDropoutGradient maxBatchSize];
-[MPSCNNDropoutGradient copyWithZone:device:];
-[MPSCNNDropoutGradient initWithCoder:device:];
-[MPSCNNDropoutGradient encodeWithCoder:];
-[MPSCNNDropoutGradient initWithDevice:keepProbability:seed:maskStrideInPixels:];
-[MPSCNNDropoutGradient keepProbability];
-[MPSCNNDropoutGradient maskStrideInPixels];
```
