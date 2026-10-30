# `MPSCNNConvolutionDataSource` (protocol)

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSCopying`, `NSObject`
- 0 instance variables, 0 properties, 15 instance methods, 0 class methods

## Instance methods

```
-[MPSCNNConvolutionDataSource load];
-[MPSCNNConvolutionDataSource descriptor];
-[MPSCNNConvolutionDataSource label];
-[MPSCNNConvolutionDataSource purge];
-[MPSCNNConvolutionDataSource dataType];
-[MPSCNNConvolutionDataSource weights];
-[MPSCNNConvolutionDataSource biasTerms];
-[MPSCNNConvolutionDataSource copyWithZone:device:];
-[MPSCNNConvolutionDataSource kernelWeightsDataType];
-[MPSCNNConvolutionDataSource lookupTableForUInt8Kernel];
-[MPSCNNConvolutionDataSource rangesForUInt8Kernel];
-[MPSCNNConvolutionDataSource updateWithCommandBuffer:gradientState:sourceState:];
-[MPSCNNConvolutionDataSource updateWithGradientState:sourceState:];
-[MPSCNNConvolutionDataSource weightsLayout];
-[MPSCNNConvolutionDataSource weightsQuantizationType];
```
