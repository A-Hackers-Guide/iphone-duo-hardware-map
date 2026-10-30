# `MPSCNNBatchNormalizationDataSource` (protocol)

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `NSCopying`
- 0 instance variables, 1 properties, 16 instance methods, 0 class methods

## Properties

```
@property (class, TB,?,R) supportsSecureCoding;
```

## Instance methods

```
-[MPSCNNBatchNormalizationDataSource load];
-[MPSCNNBatchNormalizationDataSource gamma];
-[MPSCNNBatchNormalizationDataSource label];
-[MPSCNNBatchNormalizationDataSource purge];
-[MPSCNNBatchNormalizationDataSource beta];
-[MPSCNNBatchNormalizationDataSource mean];
-[MPSCNNBatchNormalizationDataSource variance];
-[MPSCNNBatchNormalizationDataSource numberOfFeatureChannels];
-[MPSCNNBatchNormalizationDataSource copyWithZone:device:];
-[MPSCNNBatchNormalizationDataSource encodeWithCoder:];
-[MPSCNNBatchNormalizationDataSource initWithCoder:];
-[MPSCNNBatchNormalizationDataSource epsilon];
-[MPSCNNBatchNormalizationDataSource updateMeanAndVarianceWithCommandBuffer:batchNormalizationState:];
-[MPSCNNBatchNormalizationDataSource updateGammaAndBetaWithBatchNormalizationState:];
-[MPSCNNBatchNormalizationDataSource updateGammaAndBetaWithCommandBuffer:batchNormalizationState:];
-[MPSCNNBatchNormalizationDataSource updateMeanAndVarianceWithBatchNormalizationState:];
```
