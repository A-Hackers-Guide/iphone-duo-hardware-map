# `MPSNNPadNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNFilterNode`
- 4 instance variables, 1 properties, 5 instance methods, 1 class methods

## Instance variables

```
{MPSImageCoordinate="x"Q"y"Q"channel"Q} _paddingSizeBefore;
{MPSImageCoordinate="x"Q"y"Q"channel"Q} _paddingSizeAfter;
Q _edgeMode;
f _fillValue;
```

## Properties

```
@property (Tf,N,V_fillValue) fillValue;
```

## Class methods

```
+[MPSNNPadNode nodeWithSource:paddingSizeBefore:paddingSizeAfter:edgeMode:];
```

## Instance methods

```
-[MPSNNPadNode fillValue];
-[MPSNNPadNode gradientClass];
-[MPSNNPadNode initWithSource:paddingSizeBefore:paddingSizeAfter:edgeMode:];
-[MPSNNPadNode newFilterNode];
-[MPSNNPadNode setFillValue:];
```
