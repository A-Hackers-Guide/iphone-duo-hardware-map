# `MPSCNNConvolutionTranspose`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNKernel`
- 8 instance variables, 9 properties, 44 instance methods, 2 class methods

## Instance variables

```
Q _inputFeatureChannels;
Q _outputFeatureChannels;
Q _featureChannelsLayout;
q _kernelOffsetX;
q _kernelOffsetY;
Q _groups;
@"MPSCNNConvolution" _convolution;
@"MPSNNNeuronDescriptor" _fusedNeuronDescriptor;
```

## Properties

```
@property (TQ,R,N,V_featureChannelsLayout) featureChannelsLayout;
@property (TQ,R,N) weightsBufferLength;
@property (TQ,R,N,V_inputFeatureChannels) inputFeatureChannels;
@property (TQ,R,N,V_outputFeatureChannels) outputFeatureChannels;
@property (Tq,N,V_kernelOffsetX) kernelOffsetX;
@property (Tq,N,V_kernelOffsetY) kernelOffsetY;
@property (TQ,R,N,V_groups) groups;
@property (TQ,N) accumulatorPrecisionOption;
@property (T@"<MPSCNNConvolutionDataSource>",R,&,N) dataSource;
```

## Class methods

```
+[MPSCNNConvolutionTranspose supportsSecureCoding];
+[MPSCNNConvolutionTranspose libraryInfo:];
```

## Instance methods

```
-[MPSCNNConvolutionTranspose debugDescription];
-[MPSCNNConvolutionTranspose dealloc];
-[MPSCNNConvolutionTranspose resultStateForSourceImage:sourceStates:destinationImage:];
-[MPSCNNConvolutionTranspose groups];
-[MPSCNNConvolutionTranspose dataSource];
-[MPSCNNConvolutionTranspose copyWithZone:device:];
-[MPSCNNConvolutionTranspose initWithCoder:device:];
-[MPSCNNConvolutionTranspose temporaryResultStateForCommandBuffer:sourceImage:sourceStates:destinationImage:];
-[MPSCNNConvolutionTranspose encodeWithCoder:];
-[MPSCNNConvolutionTranspose isResultStateReusedAcrossBatch];
-[MPSCNNConvolutionTranspose encodeBatchToCommandBuffer:sourceImages:convolutionGradientStates:destinationImages:];
-[MPSCNNConvolutionTranspose encodeBatchToCommandBuffer:sourceImages:destinationStates:destinationImages:];
-[MPSCNNConvolutionTranspose encodeToCommandBuffer:sourceImage:destinationState:destinationImage:];
-[MPSCNNConvolutionTranspose initWithDevice:weights:];
-[MPSCNNConvolutionTranspose kernelOffsetX];
-[MPSCNNConvolutionTranspose kernelOffsetY];
-[MPSCNNConvolutionTranspose reloadWeightsAndBiasesWithCommandBuffer:state:];
-[MPSCNNConvolutionTranspose resultStateBatchForSourceImage:sourceStates:destinationImage:];
-[MPSCNNConvolutionTranspose setAccumulatorPrecisionOption:];
-[MPSCNNConvolutionTranspose setKernelOffsetX:];
-[MPSCNNConvolutionTranspose setKernelOffsetY:];
-[MPSCNNConvolutionTranspose encodeBatchToCommandBuffer:sourceImages:destinationStates:destinationStateIsTemporary:];
-[MPSCNNConvolutionTranspose inputFeatureChannels];
-[MPSCNNConvolutionTranspose outputFeatureChannels];
-[MPSCNNConvolutionTranspose accumulatorPrecisionOption];
-[MPSCNNConvolutionTranspose encodeBatchToCommandBuffer:sourceImages:convolutionGradientStates:destinationStates:destinationStateIsTemporary:];
-[MPSCNNConvolutionTranspose exportWeightsAndBiasesWithCommandBuffer:resultStateCanBeTemporary:];
-[MPSCNNConvolutionTranspose reloadWeightsAndBiasesFromDataSource];
-[MPSCNNConvolutionTranspose featureChannelsLayout];
-[MPSCNNConvolutionTranspose appendBatchBarrier];
-[MPSCNNConvolutionTranspose copyToGradientState:sourceImage:sourceStates:destinationImage:];
-[MPSCNNConvolutionTranspose destinationImageDescriptorForSourceImages:sourceStates:paddingMethod:sourceOffset:];
-[MPSCNNConvolutionTranspose encodeBatchToCommandBuffer:sourceImages:convolutionGradientStates:];
-[MPSCNNConvolutionTranspose encodeToCommandBuffer:sourceImage:convolutionGradientState:];
-[MPSCNNConvolutionTranspose encodeToCommandBuffer:sourceImage:convolutionGradientState:destinationImage:];
-[MPSCNNConvolutionTranspose encodeToCommandBuffer:sourceImage:convolutionGradientState:destinationState:destinationStateIsTemporary:];
-[MPSCNNConvolutionTranspose encodeToCommandBuffer:sourceImage:convolutionState:];
-[MPSCNNConvolutionTranspose encodeToCommandBuffer:sourceImage:destinationState:destinationStateIsTemporary:];
-[MPSCNNConvolutionTranspose initWithDevice:convolutionDescriptor:kernelWeights:biasTerms:flags:];
-[MPSCNNConvolutionTranspose initialize:convolutionDescriptor:kernelWeights:biasTerms:flags:fullyConnected:];
-[MPSCNNConvolutionTranspose initialize:weights:fullyConnected:];
-[MPSCNNConvolutionTranspose reloadWeightsAndBiasesWithDataSource:];
-[MPSCNNConvolutionTranspose temporaryResultStateBatchForCommandBuffer:sourceImage:sourceStates:destinationImage:];
-[MPSCNNConvolutionTranspose weightsBufferLength];
```
