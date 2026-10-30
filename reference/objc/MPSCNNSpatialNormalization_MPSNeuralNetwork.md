# `MPSCNNSpatialNormalization`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNKernel`
- 3 instance variables, 3 properties, 12 instance methods, 1 class methods

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
+[MPSCNNSpatialNormalization libraryInfo:];
```

## Instance methods

```
-[MPSCNNSpatialNormalization initWithDevice:];
-[MPSCNNSpatialNormalization debugDescription];
-[MPSCNNSpatialNormalization setAlpha:];
-[MPSCNNSpatialNormalization copyWithZone:device:];
-[MPSCNNSpatialNormalization initWithCoder:device:];
-[MPSCNNSpatialNormalization encodeWithCoder:];
-[MPSCNNSpatialNormalization alpha];
-[MPSCNNSpatialNormalization delta];
-[MPSCNNSpatialNormalization setDelta:];
-[MPSCNNSpatialNormalization setBeta:];
-[MPSCNNSpatialNormalization beta];
-[MPSCNNSpatialNormalization initWithDevice:kernelWidth:kernelHeight:];
```
