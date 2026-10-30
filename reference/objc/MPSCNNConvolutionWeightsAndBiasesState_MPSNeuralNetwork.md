# `MPSCNNConvolutionWeightsAndBiasesState`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSState`
- 6 instance variables, 8 properties, 17 instance methods, 3 class methods

## Instance variables

```
Q _numberOfWeights;
Q _numberOfBiases;
I _weightsDataType;
I _weightsLayout;
Q _weightsOffset;
Q _biasesOffset;
```

## Properties

```
@property (TQ,R,N) numberOfWeights;
@property (TQ,R,N) numberOfBiases;
@property (TI,R,N) weightsDataType;
@property (TI,R,N) weightsLayout;
@property (T@"<MTLBuffer>",R,N) weights;
@property (T@"<MTLBuffer>",R,N) biases;
@property (TQ,R,N) weightsOffset;
@property (TQ,R,N) biasesOffset;
```

## Class methods

```
+[MPSCNNConvolutionWeightsAndBiasesState temporaryCNNConvolutionWeightsAndBiasesStateWithCommandBuffer:cnnConvolutionDescriptor:];
+[MPSCNNConvolutionWeightsAndBiasesState temporaryCNNConvolutionWeightsAndBiasesStateWithCommandBuffer:cnnConvolutionDescriptor:weightsDataType:];
+[MPSCNNConvolutionWeightsAndBiasesState temporaryCNNConvolutionWeightsAndBiasesStateWithCommandBuffer:cnnConvolutionDescriptor:weightsDataType:weightsLayout:];
```

## Instance methods

```
-[MPSCNNConvolutionWeightsAndBiasesState weights];
-[MPSCNNConvolutionWeightsAndBiasesState initWithWeights:biases:];
-[MPSCNNConvolutionWeightsAndBiasesState initWithWeights:biases:weightsDataType:weightsLayout:];
-[MPSCNNConvolutionWeightsAndBiasesState weightsLayout];
-[MPSCNNConvolutionWeightsAndBiasesState biases];
-[MPSCNNConvolutionWeightsAndBiasesState weightsDataType];
-[MPSCNNConvolutionWeightsAndBiasesState numberOfWeights];
-[MPSCNNConvolutionWeightsAndBiasesState biasesOffset];
-[MPSCNNConvolutionWeightsAndBiasesState initWithDevice:cnnConvolutionDescriptor:];
-[MPSCNNConvolutionWeightsAndBiasesState initWithDevice:cnnConvolutionDescriptor:weightsDataType:];
-[MPSCNNConvolutionWeightsAndBiasesState initWithDevice:cnnConvolutionDescriptor:weightsDataType:weightsLayout:];
-[MPSCNNConvolutionWeightsAndBiasesState initWithWeights:biases:weightsDataType:];
-[MPSCNNConvolutionWeightsAndBiasesState initWithWeights:weightsOffset:biases:biasesOffset:cnnConvolutionDescriptor:];
-[MPSCNNConvolutionWeightsAndBiasesState initWithWeights:weightsOffset:weightsDataType:weightsLayout:biases:biasesOffset:cnnConvolutionDescriptor:];
-[MPSCNNConvolutionWeightsAndBiasesState initializeWithWeightsCount:weightsOffset:weightsDataType:weightsLayout:biasesCount:biasesOffset:];
-[MPSCNNConvolutionWeightsAndBiasesState numberOfBiases];
-[MPSCNNConvolutionWeightsAndBiasesState weightsOffset];
```
