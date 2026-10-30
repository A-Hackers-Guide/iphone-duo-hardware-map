# `MPSCNNInstanceNormalizationDataSource` (protocol)

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `NSCopying`
- 0 instance variables, 2 properties, 12 instance methods, 0 class methods

## Properties

```
@property (TQ,R,N) numberOfFeatureChannels;
@property (class, TB,?,R) supportsSecureCoding;
```

## Instance methods

```
-[MPSCNNInstanceNormalizationDataSource gamma];
-[MPSCNNInstanceNormalizationDataSource label];
-[MPSCNNInstanceNormalizationDataSource beta];
-[MPSCNNInstanceNormalizationDataSource numberOfFeatureChannels];
-[MPSCNNInstanceNormalizationDataSource load];
-[MPSCNNInstanceNormalizationDataSource copyWithZone:device:];
-[MPSCNNInstanceNormalizationDataSource encodeWithCoder:];
-[MPSCNNInstanceNormalizationDataSource purge];
-[MPSCNNInstanceNormalizationDataSource initWithCoder:];
-[MPSCNNInstanceNormalizationDataSource epsilon];
-[MPSCNNInstanceNormalizationDataSource updateGammaAndBetaWithCommandBuffer:instanceNormalizationStateBatch:];
-[MPSCNNInstanceNormalizationDataSource updateGammaAndBetaWithInstanceNormalizationStateBatch:];
```
