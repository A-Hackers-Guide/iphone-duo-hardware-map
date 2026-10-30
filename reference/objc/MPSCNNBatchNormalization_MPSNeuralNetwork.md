# `MPSCNNBatchNormalization`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNKernel`
- 10 instance variables, 3 properties, 28 instance methods, 1 class methods

## Instance variables

```
^v _gamma;
^v _beta;
^v _meanDS;
^v _varDS;
@"<MPSCNNBatchNormalizationDataSource>" _dataSource;
B _stateNeedsToLoad;
@"MPSNNNeuronDescriptor" _fusedNeuronDescriptor;
@"<MTLBuffer>" _preluBuffer;
f _epsilon;
Q _numberOfFeatureChannels;
```

## Properties

```
@property (TQ,R,N,V_numberOfFeatureChannels) numberOfFeatureChannels;
@property (Tf,N,V_epsilon) epsilon;
@property (T@"<MPSCNNBatchNormalizationDataSource>",R,&,N,V_dataSource) dataSource;
```

## Class methods

```
+[MPSCNNBatchNormalization libraryInfo:];
```

## Instance methods

```
-[MPSCNNBatchNormalization debugDescription];
-[MPSCNNBatchNormalization dealloc];
-[MPSCNNBatchNormalization resultStateForSourceImage:sourceStates:destinationImage:];
-[MPSCNNBatchNormalization dataSource];
-[MPSCNNBatchNormalization copyWithZone:device:];
-[MPSCNNBatchNormalization initWithCoder:device:];
-[MPSCNNBatchNormalization temporaryResultStateForCommandBuffer:sourceImage:sourceStates:destinationImage:];
-[MPSCNNBatchNormalization encodeWithCoder:];
-[MPSCNNBatchNormalization setEpsilon:];
-[MPSCNNBatchNormalization epsilon];
-[MPSCNNBatchNormalization isResultStateReusedAcrossBatch];
-[MPSCNNBatchNormalization encodeBatchToCommandBuffer:sourceImages:destinationStates:destinationImages:];
-[MPSCNNBatchNormalization encodeToCommandBuffer:sourceImage:destinationState:destinationImage:];
-[MPSCNNBatchNormalization encodeBatchToCommandBuffer:sourceImages:destinationStates:destinationStateIsTemporary:];
-[MPSCNNBatchNormalization encodeBatchToCommandBuffer:sourceImages:batchNormalizationState:];
-[MPSCNNBatchNormalization encodeBatchToCommandBuffer:sourceImages:batchNormalizationState:destinationImages:];
-[MPSCNNBatchNormalization encodeToCommandBuffer:sourceImage:batchNormalizationState:];
-[MPSCNNBatchNormalization encodeToCommandBuffer:sourceImage:batchNormalizationState:destinationImage:];
-[MPSCNNBatchNormalization encodeToCommandBuffer:sourceImage:destinationState:destinationStateIsTemporary:];
-[MPSCNNBatchNormalization initWithDevice:dataSource:];
-[MPSCNNBatchNormalization initWithDevice:dataSource:fusedNeuronDescriptor:];
-[MPSCNNBatchNormalization numberOfFeatureChannels];
-[MPSCNNBatchNormalization reloadDataSource:];
-[MPSCNNBatchNormalization reloadDataSourceDeprecated:doReloadWeights:doReloadStats:];
-[MPSCNNBatchNormalization reloadGammaAndBetaFromDataSource];
-[MPSCNNBatchNormalization reloadGammaAndBetaWithCommandBuffer:gammaAndBetaState:];
-[MPSCNNBatchNormalization reloadMeanAndVarianceFromDataSource];
-[MPSCNNBatchNormalization reloadMeanAndVarianceWithCommandBuffer:meanAndVarianceState:];
```
