# `MPSCNNUpsamplingNearestNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNFilterNode`
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
+[MPSCNNUpsamplingNearestNode nodeWithSource:integerScaleFactorX:integerScaleFactorY:];
```

## Instance methods

```
-[MPSCNNUpsamplingNearestNode scaleFactorX];
-[MPSCNNUpsamplingNearestNode scaleFactorY];
-[MPSCNNUpsamplingNearestNode gradientClass];
-[MPSCNNUpsamplingNearestNode initWithSource:integerScaleFactorX:integerScaleFactorY:];
-[MPSCNNUpsamplingNearestNode newFilterNode];
```
