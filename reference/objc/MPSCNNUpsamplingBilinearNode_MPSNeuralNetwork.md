# `MPSCNNUpsamplingBilinearNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNFilterNode`
- 3 instance variables, 3 properties, 7 instance methods, 2 class methods

## Instance variables

```
d _scaleFactorX;
d _scaleFactorY;
B _alignCorners;
```

## Properties

```
@property (Td,R,N,V_scaleFactorX) scaleFactorX;
@property (Td,R,N,V_scaleFactorY) scaleFactorY;
@property (TB,R,N,V_alignCorners) alignCorners;
```

## Class methods

```
+[MPSCNNUpsamplingBilinearNode nodeWithSource:integerScaleFactorX:integerScaleFactorY:];
+[MPSCNNUpsamplingBilinearNode nodeWithSource:integerScaleFactorX:integerScaleFactorY:alignCorners:];
```

## Instance methods

```
-[MPSCNNUpsamplingBilinearNode alignCorners];
-[MPSCNNUpsamplingBilinearNode scaleFactorX];
-[MPSCNNUpsamplingBilinearNode scaleFactorY];
-[MPSCNNUpsamplingBilinearNode gradientClass];
-[MPSCNNUpsamplingBilinearNode initWithSource:integerScaleFactorX:integerScaleFactorY:];
-[MPSCNNUpsamplingBilinearNode initWithSource:integerScaleFactorX:integerScaleFactorY:alignCorners:];
-[MPSCNNUpsamplingBilinearNode newFilterNode];
```
