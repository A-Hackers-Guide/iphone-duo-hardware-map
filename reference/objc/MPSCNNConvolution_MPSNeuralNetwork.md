# `MPSCNNConvolution`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNKernel`
- 24 instance variables, 15 properties, 58 instance methods, 1 class methods

## Instance variables

```
Q _inputFeatureChannels;
Q _outputFeatureChannels;
Q _layout;
Q _groups;
@"MPSCNNNeuron" _neuron_deprecated;
@"<MTLBuffer>" _weights;
@"<MTLBuffer>" _bias;
Q _flags;
B _fullyConnected;
B _convolutionTranspose;
B _convertFloat32Weights;
@"<MTLBuffer>" _qWts;
i _qType;
Q _scaleFactor;
Q _channelMultiplier;
I _weightsDataType;
I _weightsLayout;
@"NSData" _biasOriginal;
@"<MTLBuffer>" _neuronABuffer;
Q _accumulatorPrecisionOption;
@"<MPSCNNConvolutionDataSource>" _dataSource;
@"NSData" _batchNormalizationData;
@"MPSNNNeuronDescriptor" _fusedNeuronDescriptor;
Q _featureChannelsLayout;
```

## Properties

```
@property (TQ,R,N,V_featureChannelsLayout) featureChannelsLayout;
@property (TQ,R,N) weightsBufferLength;
@property (TQ,R,N,V_inputFeatureChannels) inputFeatureChannels;
@property (TQ,R,N,V_outputFeatureChannels) outputFeatureChannels;
@property (TQ,R,N,V_groups) groups;
@property (T@"<MPSCNNConvolutionDataSource>",R,&,N,V_dataSource) dataSource;
@property (TQ,R,N,V_scaleFactor) subPixelScaleFactor;
@property (T@"MPSCNNNeuron",R,N,V_neuron_deprecated) neuron;
@property (Ti,R,N) neuronType;
@property (Tf,R,N) neuronParameterA;
@property (Tf,R,N) neuronParameterB;
@property (Tf,R,N) neuronParameterC;
@property (T@"MPSNNNeuronDescriptor",R,N,V_fusedNeuronDescriptor) fusedNeuronDescriptor;
@property (TQ,R,N,V_channelMultiplier) channelMultiplier;
@property (TQ,N) accumulatorPrecisionOption;
```

## Class methods

```
+[MPSCNNConvolution libraryInfo:];
```

## Instance methods

```
-[MPSCNNConvolution initWithDevice:];
-[MPSCNNConvolution debugDescription];
-[MPSCNNConvolution maxBatchSize];
-[MPSCNNConvolution dealloc];
-[MPSCNNConvolution resultStateForSourceImage:sourceStates:destinationImage:];
-[MPSCNNConvolution groups];
-[MPSCNNConvolution dataSource];
-[MPSCNNConvolution copyWithZone:device:];
-[MPSCNNConvolution initWithCoder:device:];
-[MPSCNNConvolution temporaryResultStateForCommandBuffer:sourceImage:sourceStates:destinationImage:];
-[MPSCNNConvolution encodeWithCoder:];
-[MPSCNNConvolution isResultStateReusedAcrossBatch];
-[MPSCNNConvolution weights];
-[MPSCNNConvolution initWithDevice:weights:];
-[MPSCNNConvolution reloadWeightsAndBiasesWithCommandBuffer:state:];
-[MPSCNNConvolution resultStateBatchForSourceImage:sourceStates:destinationImage:];
-[MPSCNNConvolution setAccumulatorPrecisionOption:];
-[MPSCNNConvolution setFusedNeuronDescriptor:];
-[MPSCNNConvolution weightsLayout];
-[MPSCNNConvolution biases];
-[MPSCNNConvolution inputFeatureChannels];
-[MPSCNNConvolution neuronType];
-[MPSCNNConvolution outputFeatureChannels];
-[MPSCNNConvolution fusedNeuronDescriptor];
-[MPSCNNConvolution channelMultiplier];
-[MPSCNNConvolution subPixelScaleFactor];
-[MPSCNNConvolution weightsDataType];
-[MPSCNNConvolution accumulatorPrecisionOption];
-[MPSCNNConvolution convolutionTranspose];
-[MPSCNNConvolution exportWeightsAndBiasesWithCommandBuffer:resultStateCanBeTemporary:];
-[MPSCNNConvolution reloadWeightsAndBiasesFromDataSource];
-[MPSCNNConvolution featureChannelsLayout];
-[MPSCNNConvolution PrepareAndLoadData:dataType:weightsLayout:weights:biases:quantizationType:ranges:lookUpTable:convertFloat32Weights:];
-[MPSCNNConvolution appendBatchBarrier];
-[MPSCNNConvolution batchEncodingStorageSizeForSourceImage:sourceStates:destinationImage:];
-[MPSCNNConvolution copyToGradientState:sourceImage:sourceStates:destinationImage:];
-[MPSCNNConvolution destinationImageDescriptorForSourceImages:sourceStates:paddingMethod:sourceOffset:];
-[MPSCNNConvolution destinationImageDescriptorForSourceImages:sourceStates:paddingMethod:sourceOffset:kernelOffset:];
-[MPSCNNConvolution encodeToCommandBuffer:sourceImage:destinationImage:state:];
-[MPSCNNConvolution encodingStorageSizeForSourceImage:sourceStates:destinationImage:];
-[MPSCNNConvolution initWithDevice:convolutionDescriptor:kernelWeights:biasTerms:flags:];
-[MPSCNNConvolution initWithDevice:convolutionDescriptor:kernelWeights:biasTerms:flags:fullyConnected:];
-[MPSCNNConvolution initWithDevice:convolutionDescriptor:kernelWeights:biasTerms:flags:fullyConnected:convolutionTranspose:];
-[MPSCNNConvolution initWithDevice:weights:fullyConnected:];
-[MPSCNNConvolution initWithDevice:weights:fullyConnected:convolutionTranspose:];
-[MPSCNNConvolution initialize:convolutionDescriptor:kernelWeights:dataType:weightsLayout:range:lookUpTable:qType:biasTerms:flags:fullyConnected:convolutionTranspose:preferredWeightsDataType:];
-[MPSCNNConvolution initializeWithDevice:weights:fullyConnected:convolutionTranspose:];
-[MPSCNNConvolution neuron];
-[MPSCNNConvolution neuronABuffer];
-[MPSCNNConvolution neuronParameterA];
-[MPSCNNConvolution neuronParameterB];
-[MPSCNNConvolution neuronParameterC];
-[MPSCNNConvolution quantizationBuffer];
-[MPSCNNConvolution quantizationType];
-[MPSCNNConvolution reloadWeightsAndBiasesWithDataSource:];
-[MPSCNNConvolution resourceListForSourceImages:destinationImages:];
-[MPSCNNConvolution temporaryResultStateBatchForCommandBuffer:sourceImage:sourceStates:destinationImage:];
-[MPSCNNConvolution weightsBufferLength];
```
