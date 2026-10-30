# `MPSRNNMatrixInferenceLayer`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSKernel`
- 17 instance variables, 7 properties, 22 instance methods, 1 class methods

## Instance variables

```
^i layerTypes;
^^v layers;
^^v forwardLayers;
^i forwardLayerTypes;
Q nForwardLayers;
^^v backwardLayers;
^i backwardLayerTypes;
Q nBackwardLayers;
@"MPSMatrixMultiplication" gemmKernel;
@"MPSMatrixMultiplication" gemmKernelNonTranspose;
B _recurrentOutputIsTemporary;
B _storeAllIntermediateStates;
B _propagateFullRecurrentRows;
Q _numberOfLayers;
Q _bidirectionalCombineMode;
Q _inputFeatureChannels;
Q _outputFeatureChannels;
```

## Properties

```
@property (TB,N,V_propagateFullRecurrentRows) propagateFullRecurrentRows;
@property (TQ,R,N,V_inputFeatureChannels) inputFeatureChannels;
@property (TQ,R,N,V_outputFeatureChannels) outputFeatureChannels;
@property (TQ,R,N,V_numberOfLayers) numberOfLayers;
@property (TB,N,V_recurrentOutputIsTemporary) recurrentOutputIsTemporary;
@property (TB,N,V_storeAllIntermediateStates) storeAllIntermediateStates;
@property (TQ,N,V_bidirectionalCombineMode) bidirectionalCombineMode;
```

## Class methods

```
+[MPSRNNMatrixInferenceLayer libraryInfo:];
```

## Instance methods

```
-[MPSRNNMatrixInferenceLayer dealloc];
-[MPSRNNMatrixInferenceLayer copyWithZone:device:];
-[MPSRNNMatrixInferenceLayer initWithCoder:device:];
-[MPSRNNMatrixInferenceLayer encodeWithCoder:];
-[MPSRNNMatrixInferenceLayer numberOfLayers];
-[MPSRNNMatrixInferenceLayer inputFeatureChannels];
-[MPSRNNMatrixInferenceLayer outputFeatureChannels];
-[MPSRNNMatrixInferenceLayer setPropagateFullRecurrentRows:];
-[MPSRNNMatrixInferenceLayer setRecurrentOutputIsTemporary:];
-[MPSRNNMatrixInferenceLayer bidirectionalCombineMode];
-[MPSRNNMatrixInferenceLayer encodeBidirectionalSequenceToCommandBuffer:sourceSequence:destinationForwardMatrices:destinationBackwardMatrices:];
-[MPSRNNMatrixInferenceLayer encodeSequenceToCommandBuffer:sourceMatrices:destinationMatrices:recurrentInputState:recurrentOutputStates:];
-[MPSRNNMatrixInferenceLayer encodeSequenceToCommandBuffer:sourceMatrices:sourceOffsets:destinationMatrices:destinationOffsets:recurrentInputState:recurrentOutputStates:];
-[MPSRNNMatrixInferenceLayer initWithDevice:rnnDescriptor:];
-[MPSRNNMatrixInferenceLayer initWithDevice:rnnDescriptors:];
-[MPSRNNMatrixInferenceLayer propagateFullRecurrentRows];
-[MPSRNNMatrixInferenceLayer recurrentOutputIsTemporary];
-[MPSRNNMatrixInferenceLayer recurrentStateForBatchSize:];
-[MPSRNNMatrixInferenceLayer setBidirectionalCombineMode:];
-[MPSRNNMatrixInferenceLayer setStoreAllIntermediateStates:];
-[MPSRNNMatrixInferenceLayer storeAllIntermediateStates];
-[MPSRNNMatrixInferenceLayer temporaryRecurrentStateForCommandBuffer:batchSize:];
```
