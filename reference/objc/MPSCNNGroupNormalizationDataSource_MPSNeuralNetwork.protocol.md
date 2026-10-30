# `MPSCNNGroupNormalizationDataSource` (protocol)

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `NSCopying`
- 0 instance variables, 3 properties, 12 instance methods, 0 class methods

## Properties

```
@property (TQ,R,N) numberOfFeatureChannels;
@property (TQ,N) numberOfGroups;
@property (class, TB,?,R) supportsSecureCoding;
```

## Instance methods

```
-[MPSCNNGroupNormalizationDataSource gamma];
-[MPSCNNGroupNormalizationDataSource numberOfGroups];
-[MPSCNNGroupNormalizationDataSource label];
-[MPSCNNGroupNormalizationDataSource beta];
-[MPSCNNGroupNormalizationDataSource numberOfFeatureChannels];
-[MPSCNNGroupNormalizationDataSource setNumberOfGroups:];
-[MPSCNNGroupNormalizationDataSource copyWithZone:device:];
-[MPSCNNGroupNormalizationDataSource encodeWithCoder:];
-[MPSCNNGroupNormalizationDataSource initWithCoder:];
-[MPSCNNGroupNormalizationDataSource epsilon];
-[MPSCNNGroupNormalizationDataSource updateGammaAndBetaWithCommandBuffer:groupNormalizationStateBatch:];
-[MPSCNNGroupNormalizationDataSource updateGammaAndBetaWithGroupNormalizationStateBatch:];
```
