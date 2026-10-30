# `MPSRNNMatrixTrainingLayer`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSKernel`
- 16 instance variables, 7 properties, 27 instance methods, 1 class methods

## Instance variables

```
i layerType;
^v layer;
@"MPSMatrixMultiplication" gemmKernel;
@"MPSMatrixMultiplication" gemmKernel_noAccumulate;
@"MPSMatrixMultiplication" gemmKernelNonTranspose;
@"MPSMatrixMultiplication" gemmKernelNonTranspose_noAccumulate;
@"MPSMatrixMultiplication" gemmKernelTN;
@"MPSMatrixMultiplication" gemmKernelTN_accumulate;
@"NSMutableArray" weightDescriptors;
B _recurrentOutputIsTemporary;
B _trainingStateIsTemporary;
B _storeAllIntermediateStates;
B _accumulateWeightGradients;
B _propagateFullRecurrentRows;
Q _inputFeatureChannels;
Q _outputFeatureChannels;
```

## Properties

```
@property (TB,N,V_propagateFullRecurrentRows) propagateFullRecurrentRows;
@property (TQ,R,N,V_inputFeatureChannels) inputFeatureChannels;
@property (TQ,R,N,V_outputFeatureChannels) outputFeatureChannels;
@property (TB,N,V_storeAllIntermediateStates) storeAllIntermediateStates;
@property (TB,N,V_recurrentOutputIsTemporary) recurrentOutputIsTemporary;
@property (TB,N,V_trainingStateIsTemporary) trainingStateIsTemporary;
@property (TB,N,V_accumulateWeightGradients) accumulateWeightGradients;
```

## Class methods

```
+[MPSRNNMatrixTrainingLayer libraryInfo:];
```

## Instance methods

```
-[MPSRNNMatrixTrainingLayer dealloc];
-[MPSRNNMatrixTrainingLayer copyWithZone:device:];
-[MPSRNNMatrixTrainingLayer initWithCoder:device:];
-[MPSRNNMatrixTrainingLayer encodeWithCoder:];
-[MPSRNNMatrixTrainingLayer createWeightGradientMatrices:dataType:];
-[MPSRNNMatrixTrainingLayer createWeightMatrices:];
-[MPSRNNMatrixTrainingLayer encodeCopyWeightsToCommandBuffer:weights:matrixId:matrix:copyFromWeightsToMatrix:matrixOffset:];
-[MPSRNNMatrixTrainingLayer encodeForwardSequenceToCommandBuffer:sourceMatrices:destinationMatrices:trainingStates:weights:];
-[MPSRNNMatrixTrainingLayer encodeForwardSequenceToCommandBuffer:sourceMatrices:sourceOffsets:destinationMatrices:destinationOffsets:trainingStates:recurrentInputState:recurrentOutputStates:weights:];
-[MPSRNNMatrixTrainingLayer encodeGradientSequenceToCommandBuffer:forwardSources:forwardSourceOffsets:sourceGradients:sourceGradientOffsets:destinationGradients:destinationOffsets:weightGradients:trainingStates:recurrentInputState:recurrentOutputStates:weights:];
-[MPSRNNMatrixTrainingLayer encodeGradientSequenceToCommandBuffer:forwardSources:sourceGradients:destinationGradients:weightGradients:trainingStates:weights:];
-[MPSRNNMatrixTrainingLayer initWithDevice:rnnDescriptor:trainableWeights:];
-[MPSRNNMatrixTrainingLayer inputFeatureChannels];
-[MPSRNNMatrixTrainingLayer outputFeatureChannels];
-[MPSRNNMatrixTrainingLayer setPropagateFullRecurrentRows:];
-[MPSRNNMatrixTrainingLayer setRecurrentOutputIsTemporary:];
-[MPSRNNMatrixTrainingLayer temporaryRecurrentStateForCommandBuffer:batchSize:forGradientPass:];
-[MPSRNNMatrixTrainingLayer accumulateWeightGradients];
-[MPSRNNMatrixTrainingLayer createTemporaryWeightGradientMatrices:dataType:commandBuffer:];
-[MPSRNNMatrixTrainingLayer propagateFullRecurrentRows];
-[MPSRNNMatrixTrainingLayer recurrentOutputIsTemporary];
-[MPSRNNMatrixTrainingLayer recurrentStateForBatchSize:forGradientPass:];
-[MPSRNNMatrixTrainingLayer setAccumulateWeightGradients:];
-[MPSRNNMatrixTrainingLayer setStoreAllIntermediateStates:];
-[MPSRNNMatrixTrainingLayer setTrainingStateIsTemporary:];
-[MPSRNNMatrixTrainingLayer storeAllIntermediateStates];
-[MPSRNNMatrixTrainingLayer trainingStateIsTemporary];
```
