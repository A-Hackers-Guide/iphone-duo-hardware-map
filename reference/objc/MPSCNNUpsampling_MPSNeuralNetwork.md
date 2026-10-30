# `MPSCNNUpsampling`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNKernel`
- 4 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
Q _filterType;
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
+[MPSCNNUpsampling libraryInfo:];
```

## Instance methods

```
-[MPSCNNUpsampling initWithDevice:];
-[MPSCNNUpsampling debugDescription];
-[MPSCNNUpsampling copyWithZone:device:];
-[MPSCNNUpsampling initWithCoder:device:];
-[MPSCNNUpsampling encodeWithCoder:];
-[MPSCNNUpsampling alignCorners];
-[MPSCNNUpsampling scaleFactorX];
-[MPSCNNUpsampling scaleFactorY];
-[MPSCNNUpsampling destinationImageDescriptorForSourceImages:sourceStates:paddingMethod:sourceOffset:];
-[MPSCNNUpsampling initWithDevice:filterType:integerScaleFactorX:integerScaleFactorY:alignCorners:];
```
