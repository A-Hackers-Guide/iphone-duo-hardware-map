# `MPSCNNBatchNormalizationStatisticsGradient`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNGradientKernel`
- 2 instance variables, 0 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"MPSNNNeuronDescriptor" _fusedNeuronDescriptor;
@"<MTLBuffer>" _preluBuffer;
```

## Class methods

```
+[MPSCNNBatchNormalizationStatisticsGradient libraryInfo:];
```

## Instance methods

```
-[MPSCNNBatchNormalizationStatisticsGradient initWithDevice:];
-[MPSCNNBatchNormalizationStatisticsGradient maxBatchSize];
-[MPSCNNBatchNormalizationStatisticsGradient dealloc];
-[MPSCNNBatchNormalizationStatisticsGradient copyWithZone:device:];
-[MPSCNNBatchNormalizationStatisticsGradient initWithCoder:device:];
-[MPSCNNBatchNormalizationStatisticsGradient encodeWithCoder:];
-[MPSCNNBatchNormalizationStatisticsGradient isResultStateReusedAcrossBatch];
-[MPSCNNBatchNormalizationStatisticsGradient encodeToCommandBuffer:sourceGradient:sourceImage:gradientState:];
-[MPSCNNBatchNormalizationStatisticsGradient encodeBatchToCommandBuffer:sourceGradients:sourceImages:gradientStates:];
-[MPSCNNBatchNormalizationStatisticsGradient encodeBatchToCommandBuffer:sourceGradients:sourceImages:gradientStates:destinationGradients:];
-[MPSCNNBatchNormalizationStatisticsGradient encodeToCommandBuffer:sourceGradient:sourceImage:gradientState:destinationGradient:];
-[MPSCNNBatchNormalizationStatisticsGradient accumulatesOverBatch];
-[MPSCNNBatchNormalizationStatisticsGradient encodeBatchToCommandBuffer:sourceGradients:sourceImages:batchNormalizationState:];
-[MPSCNNBatchNormalizationStatisticsGradient initWithDevice:fusedNeuronDescriptor:];
```
