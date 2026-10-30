# `MPSCNNNormalizationNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNFilterNode`
- 3 instance variables, 3 properties, 7 instance methods, 1 class methods

## Instance variables

```
f _alpha;
f _beta;
f _delta;
```

## Properties

```
@property (Tf,N,V_alpha) alpha;
@property (Tf,N,V_beta) beta;
@property (Tf,N,V_delta) delta;
```

## Class methods

```
+[MPSCNNNormalizationNode nodeWithSource:];
```

## Instance methods

```
-[MPSCNNNormalizationNode initWithSource:];
-[MPSCNNNormalizationNode setAlpha:];
-[MPSCNNNormalizationNode alpha];
-[MPSCNNNormalizationNode delta];
-[MPSCNNNormalizationNode setDelta:];
-[MPSCNNNormalizationNode setBeta:];
-[MPSCNNNormalizationNode beta];
```
