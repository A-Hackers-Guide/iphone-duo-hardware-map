# `MPSCNNInstanceNormalizationGradientState`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNGradientState`
- 2 instance variables, 5 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"MPSCNNInstanceNormalization" _instanceNormalization;
Q _numberOfFeatureChannels;
```

## Properties

```
@property (T@"MPSCNNInstanceNormalization",R,&,N,V_instanceNormalization) instanceNormalization;
@property (T@"<MTLBuffer>",R,N) gamma;
@property (T@"<MTLBuffer>",R,N) beta;
@property (T@"<MTLBuffer>",R,N) gradientForGamma;
@property (T@"<MTLBuffer>",R,N) gradientForBeta;
```

## Class methods

```
+[MPSCNNInstanceNormalizationGradientState temporaryStateWithCommandBuffer:numberOfFeatureChannels:instanceNormalization:];
```

## Instance methods

```
-[MPSCNNInstanceNormalizationGradientState gamma];
-[MPSCNNInstanceNormalizationGradientState debugDescription];
-[MPSCNNInstanceNormalizationGradientState dealloc];
-[MPSCNNInstanceNormalizationGradientState beta];
-[MPSCNNInstanceNormalizationGradientState gradientForBeta];
-[MPSCNNInstanceNormalizationGradientState gradientForGamma];
-[MPSCNNInstanceNormalizationGradientState initWithDevice:numberOfFeatureChannels:instanceNormalization:];
-[MPSCNNInstanceNormalizationGradientState instanceNormalization];
```
