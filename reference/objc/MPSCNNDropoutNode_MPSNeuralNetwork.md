# `MPSCNNDropoutNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNFilterNode`
- 3 instance variables, 3 properties, 8 instance methods, 3 class methods

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
+[MPSCNNDropoutNode nodeWithSource:keepProbability:];
+[MPSCNNDropoutNode nodeWithSource:];
+[MPSCNNDropoutNode nodeWithSource:keepProbability:seed:maskStrideInPixels:];
```

## Instance methods

```
-[MPSCNNDropoutNode initWithSource:];
-[MPSCNNDropoutNode seed];
-[MPSCNNDropoutNode keepProbability];
-[MPSCNNDropoutNode initWithSource:keepProbability:];
-[MPSCNNDropoutNode gradientClass];
-[MPSCNNDropoutNode initWithSource:keepProbability:seed:maskStrideInPixels:];
-[MPSCNNDropoutNode maskStrideInPixels];
-[MPSCNNDropoutNode newFilterNode];
```
