# `MPSCNNLocalContrastNormalizationGradientNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNGradientFilterNode`
- 8 instance variables, 8 properties, 17 instance methods, 1 class methods

## Instance variables

```
Q _kernelWidth;
Q _kernelHeight;
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
@property (TQ,R,N,V_kernelWidth) kernelWidth;
@property (TQ,R,N,V_kernelHeight) kernelHeight;
```

## Class methods

```
+[MPSCNNLocalContrastNormalizationGradientNode nodeWithSourceGradient:sourceImage:gradientState:kernelWidth:kernelHeight:];
```

## Instance methods

```
-[MPSCNNLocalContrastNormalizationGradientNode pm];
-[MPSCNNLocalContrastNormalizationGradientNode setAlpha:];
-[MPSCNNLocalContrastNormalizationGradientNode setPm:];
-[MPSCNNLocalContrastNormalizationGradientNode alpha];
-[MPSCNNLocalContrastNormalizationGradientNode delta];
-[MPSCNNLocalContrastNormalizationGradientNode setDelta:];
-[MPSCNNLocalContrastNormalizationGradientNode kernelHeight];
-[MPSCNNLocalContrastNormalizationGradientNode kernelWidth];
-[MPSCNNLocalContrastNormalizationGradientNode setBeta:];
-[MPSCNNLocalContrastNormalizationGradientNode beta];
-[MPSCNNLocalContrastNormalizationGradientNode initWithGradientImages:forwardFilter:];
-[MPSCNNLocalContrastNormalizationGradientNode initWithSourceGradient:sourceImage:gradientState:kernelWidth:kernelHeight:];
-[MPSCNNLocalContrastNormalizationGradientNode newFilterNode];
-[MPSCNNLocalContrastNormalizationGradientNode p0];
-[MPSCNNLocalContrastNormalizationGradientNode ps];
-[MPSCNNLocalContrastNormalizationGradientNode setP0:];
-[MPSCNNLocalContrastNormalizationGradientNode setPs:];
```
