# `MPSCNNSpatialNormalizationGradientNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNGradientFilterNode`
- 5 instance variables, 5 properties, 13 instance methods, 1 class methods

## Instance variables

```
Q _kernelWidth;
Q _kernelHeight;
f _alpha;
f _beta;
f _delta;
```

## Properties

```
@property (TQ,N,V_kernelWidth) kernelWidth;
@property (TQ,N,V_kernelHeight) kernelHeight;
@property (Tf,N,V_alpha) alpha;
@property (Tf,N,V_beta) beta;
@property (Tf,N,V_delta) delta;
```

## Class methods

```
+[MPSCNNSpatialNormalizationGradientNode nodeWithSourceGradient:sourceImage:gradientState:kernelSize:];
```

## Instance methods

```
-[MPSCNNSpatialNormalizationGradientNode setAlpha:];
-[MPSCNNSpatialNormalizationGradientNode alpha];
-[MPSCNNSpatialNormalizationGradientNode delta];
-[MPSCNNSpatialNormalizationGradientNode setDelta:];
-[MPSCNNSpatialNormalizationGradientNode kernelHeight];
-[MPSCNNSpatialNormalizationGradientNode kernelWidth];
-[MPSCNNSpatialNormalizationGradientNode setBeta:];
-[MPSCNNSpatialNormalizationGradientNode beta];
-[MPSCNNSpatialNormalizationGradientNode setKernelWidth:];
-[MPSCNNSpatialNormalizationGradientNode setKernelHeight:];
-[MPSCNNSpatialNormalizationGradientNode initWithGradientImages:forwardFilter:];
-[MPSCNNSpatialNormalizationGradientNode initWithSourceGradient:sourceImage:gradientState:kernelSize:];
-[MPSCNNSpatialNormalizationGradientNode newFilterNode];
```
