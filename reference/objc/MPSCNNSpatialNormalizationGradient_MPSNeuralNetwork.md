# `MPSCNNSpatialNormalizationGradient`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNGradientKernel`
- 3 instance variables, 3 properties, 11 instance methods, 1 class methods

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
+[MPSCNNSpatialNormalizationGradient libraryInfo:];
```

## Instance methods

```
-[MPSCNNSpatialNormalizationGradient initWithDevice:];
-[MPSCNNSpatialNormalizationGradient setAlpha:];
-[MPSCNNSpatialNormalizationGradient copyWithZone:device:];
-[MPSCNNSpatialNormalizationGradient initWithCoder:device:];
-[MPSCNNSpatialNormalizationGradient encodeWithCoder:];
-[MPSCNNSpatialNormalizationGradient alpha];
-[MPSCNNSpatialNormalizationGradient delta];
-[MPSCNNSpatialNormalizationGradient setDelta:];
-[MPSCNNSpatialNormalizationGradient setBeta:];
-[MPSCNNSpatialNormalizationGradient beta];
-[MPSCNNSpatialNormalizationGradient initWithDevice:kernelWidth:kernelHeight:];
```
