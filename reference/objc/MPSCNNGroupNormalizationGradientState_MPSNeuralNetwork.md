# `MPSCNNGroupNormalizationGradientState`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNGradientState`
- 3 instance variables, 5 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"MPSCNNGroupNormalization" _groupNormalization;
Q _numberOfFeatureChannels;
Q _numberOfGroups;
```

## Properties

```
@property (T@"MPSCNNGroupNormalization",R,&,N,V_groupNormalization) groupNormalization;
@property (T@"<MTLBuffer>",R,N) gamma;
@property (T@"<MTLBuffer>",R,N) beta;
@property (T@"<MTLBuffer>",R,N) gradientForGamma;
@property (T@"<MTLBuffer>",R,N) gradientForBeta;
```

## Class methods

```
+[MPSCNNGroupNormalizationGradientState temporaryStateWithCommandBuffer:numberOfFeatureChannels:groupNormalization:];
```

## Instance methods

```
-[MPSCNNGroupNormalizationGradientState gamma];
-[MPSCNNGroupNormalizationGradientState debugDescription];
-[MPSCNNGroupNormalizationGradientState dealloc];
-[MPSCNNGroupNormalizationGradientState beta];
-[MPSCNNGroupNormalizationGradientState gradientForBeta];
-[MPSCNNGroupNormalizationGradientState gradientForGamma];
-[MPSCNNGroupNormalizationGradientState groupNormalization];
-[MPSCNNGroupNormalizationGradientState initWithDevice:numberOfFeatureChannels:groupNormalization:];
```
