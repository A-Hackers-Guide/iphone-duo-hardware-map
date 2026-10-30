# `MPSRNNImageInferenceLayer`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNKernel`
- 14 instance variables, 6 properties, 17 instance methods, 1 class methods

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
B _recurrentOutputIsTemporary;
B _storeAllIntermediateStates;
Q _numberOfLayers;
Q _bidirectionalCombineMode;
Q _inputFeatureChannels;
Q _outputFeatureChannels;
```

## Properties

```
@property (TQ,R,N,V_inputFeatureChannels) inputFeatureChannels;
@property (TQ,R,N,V_outputFeatureChannels) outputFeatureChannels;
@property (TQ,R,N,V_numberOfLayers) numberOfLayers;
@property (TB,N,V_recurrentOutputIsTemporary) recurrentOutputIsTemporary;
@property (TB,N,V_storeAllIntermediateStates) storeAllIntermediateStates;
@property (TQ,N,V_bidirectionalCombineMode) bidirectionalCombineMode;
```

## Class methods

```
+[MPSRNNImageInferenceLayer libraryInfo:];
```

## Instance methods

```
-[MPSRNNImageInferenceLayer dealloc];
-[MPSRNNImageInferenceLayer copyWithZone:device:];
-[MPSRNNImageInferenceLayer initWithCoder:device:];
-[MPSRNNImageInferenceLayer encodeWithCoder:];
-[MPSRNNImageInferenceLayer numberOfLayers];
-[MPSRNNImageInferenceLayer inputFeatureChannels];
-[MPSRNNImageInferenceLayer outputFeatureChannels];
-[MPSRNNImageInferenceLayer setRecurrentOutputIsTemporary:];
-[MPSRNNImageInferenceLayer bidirectionalCombineMode];
-[MPSRNNImageInferenceLayer encodeBidirectionalSequenceToCommandBuffer:sourceSequence:destinationForwardImages:destinationBackwardImages:];
-[MPSRNNImageInferenceLayer encodeSequenceToCommandBuffer:sourceImages:destinationImages:recurrentInputState:recurrentOutputStates:];
-[MPSRNNImageInferenceLayer initWithDevice:rnnDescriptor:];
-[MPSRNNImageInferenceLayer initWithDevice:rnnDescriptors:];
-[MPSRNNImageInferenceLayer recurrentOutputIsTemporary];
-[MPSRNNImageInferenceLayer setBidirectionalCombineMode:];
-[MPSRNNImageInferenceLayer setStoreAllIntermediateStates:];
-[MPSRNNImageInferenceLayer storeAllIntermediateStates];
```
