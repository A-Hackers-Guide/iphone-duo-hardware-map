# `MPSCNNLocalContrastNormalizationGradient`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNGradientKernel`
- 6 instance variables, 6 properties, 18 instance methods, 1 class methods

## Instance variables

```
f _alpha;
f _beta;
f _delta;
f _p0;
f _pm;
f _ps;
```

## Properties

```
@property (Tf,N,V_alpha) alpha;
@property (Tf,N,V_beta) beta;
@property (Tf,N,V_delta) delta;
@property (Tf,N,V_p0) p0;
@property (Tf,N,V_pm) pm;
@property (Tf,N,V_ps) ps;
```

## Class methods

```
+[MPSCNNLocalContrastNormalizationGradient libraryInfo:];
```

## Instance methods

```
-[MPSCNNLocalContrastNormalizationGradient initWithDevice:];
-[MPSCNNLocalContrastNormalizationGradient pm];
-[MPSCNNLocalContrastNormalizationGradient debugDescription];
-[MPSCNNLocalContrastNormalizationGradient setAlpha:];
-[MPSCNNLocalContrastNormalizationGradient copyWithZone:device:];
-[MPSCNNLocalContrastNormalizationGradient setPm:];
-[MPSCNNLocalContrastNormalizationGradient initWithCoder:device:];
-[MPSCNNLocalContrastNormalizationGradient encodeWithCoder:];
-[MPSCNNLocalContrastNormalizationGradient alpha];
-[MPSCNNLocalContrastNormalizationGradient delta];
-[MPSCNNLocalContrastNormalizationGradient setDelta:];
-[MPSCNNLocalContrastNormalizationGradient setBeta:];
-[MPSCNNLocalContrastNormalizationGradient beta];
-[MPSCNNLocalContrastNormalizationGradient initWithDevice:kernelWidth:kernelHeight:];
-[MPSCNNLocalContrastNormalizationGradient p0];
-[MPSCNNLocalContrastNormalizationGradient ps];
-[MPSCNNLocalContrastNormalizationGradient setP0:];
-[MPSCNNLocalContrastNormalizationGradient setPs:];
```
