# `MPSCNNBatchNormalizationState`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNGradientState`
- 4 instance variables, 1 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"MPSCNNBatchNormalization" _batchNormalization;
Q _accumulationCount;
Q _numberOfFeatureChannels;
f _epsilon;
```

## Properties

```
@property (T@"MPSCNNBatchNormalization",R,&,N,V_batchNormalization) batchNormalization;
```

## Class methods

```
+[MPSCNNBatchNormalizationState temporaryStateWithCommandBuffer:numberOfFeatureChannels:epsilon:batchNormalization:];
```

## Instance methods

```
-[MPSCNNBatchNormalizationState gamma];
-[MPSCNNBatchNormalizationState dealloc];
-[MPSCNNBatchNormalizationState reset];
-[MPSCNNBatchNormalizationState beta];
-[MPSCNNBatchNormalizationState mean];
-[MPSCNNBatchNormalizationState variance];
-[MPSCNNBatchNormalizationState gradientForBeta];
-[MPSCNNBatchNormalizationState batchNormalization];
-[MPSCNNBatchNormalizationState gradientForGamma];
-[MPSCNNBatchNormalizationState initDeferredWithDevice:numberOfFeatureChannels:epsilon:batchNormalization:];
```
