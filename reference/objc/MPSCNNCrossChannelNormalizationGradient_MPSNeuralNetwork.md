# `MPSCNNCrossChannelNormalizationGradient`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNGradientKernel`
- 4 instance variables, 4 properties, 12 instance methods, 1 class methods

## Instance variables

```
Q _kernelSize;
f _alpha;
f _beta;
f _delta;
```

## Properties

```
@property (Tf,N,V_alpha) alpha;
@property (Tf,N,V_beta) beta;
@property (Tf,N,V_delta) delta;
@property (TQ,R,N,V_kernelSize) kernelSize;
```

## Class methods

```
+[MPSCNNCrossChannelNormalizationGradient libraryInfo:];
```

## Instance methods

```
-[MPSCNNCrossChannelNormalizationGradient initWithDevice:];
-[MPSCNNCrossChannelNormalizationGradient setAlpha:];
-[MPSCNNCrossChannelNormalizationGradient copyWithZone:device:];
-[MPSCNNCrossChannelNormalizationGradient initWithCoder:device:];
-[MPSCNNCrossChannelNormalizationGradient encodeWithCoder:];
-[MPSCNNCrossChannelNormalizationGradient alpha];
-[MPSCNNCrossChannelNormalizationGradient delta];
-[MPSCNNCrossChannelNormalizationGradient setDelta:];
-[MPSCNNCrossChannelNormalizationGradient initWithDevice:kernelSize:];
-[MPSCNNCrossChannelNormalizationGradient setBeta:];
-[MPSCNNCrossChannelNormalizationGradient beta];
-[MPSCNNCrossChannelNormalizationGradient kernelSize];
```
