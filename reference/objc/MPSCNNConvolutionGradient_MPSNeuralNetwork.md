# `MPSCNNConvolutionGradient`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNGradientKernel`
- 14 instance variables, 7 properties, 35 instance methods, 1 class methods

## Instance variables

```
Q _inputFeatureChannels;
Q _outputFeatureChannels;
Q _groups;
Q _channelMultiplier;
Q _gradientOption;
@"<MTLBuffer>" _weights;
B _fullyConnected;
B _convolutionTranspose;
I _weightsDataType;
I _preferredWeightsDataType;
I _weightsLayout;
@"<MPSCNNConvolutionDataSource>" _dataSource;
{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]} _lock;
B _serializeWeightsAndBiases;
```

## Properties

```
@property (TQ,R,N,V_inputFeatureChannels) sourceGradientFeatureChannels;
@property (TQ,R,N,V_outputFeatureChannels) sourceImageFeatureChannels;
@property (TQ,R,N,V_groups) groups;
@property (TQ,R,N,V_channelMultiplier) channelMultiplier;
@property (T@"<MPSCNNConvolutionDataSource>",R,&,N,V_dataSource) dataSource;
@property (TQ,N,V_gradientOption) gradientOption;
@property (TB,N,V_serializeWeightsAndBiases) serializeWeightsAndBiases;
```

## Class methods

```
+[MPSCNNConvolutionGradient libraryInfo:];
```

## Instance methods

```
-[MPSCNNConvolutionGradient initWithDevice:];
-[MPSCNNConvolutionGradient maxBatchSize];
-[MPSCNNConvolutionGradient dealloc];
-[MPSCNNConvolutionGradient groups];
-[MPSCNNConvolutionGradient dataSource];
-[MPSCNNConvolutionGradient copyWithZone:device:];
-[MPSCNNConvolutionGradient initWithCoder:device:];
-[MPSCNNConvolutionGradient encodeWithCoder:];
-[MPSCNNConvolutionGradient isResultStateReusedAcrossBatch];
-[MPSCNNConvolutionGradient weights];
-[MPSCNNConvolutionGradient initWithDevice:weights:];
-[MPSCNNConvolutionGradient reloadWeightsAndBiasesWithCommandBuffer:state:];
-[MPSCNNConvolutionGradient setGradientOption:];
-[MPSCNNConvolutionGradient weightsLayout];
-[MPSCNNConvolutionGradient biases];
-[MPSCNNConvolutionGradient channelMultiplier];
-[MPSCNNConvolutionGradient weightsDataType];
-[MPSCNNConvolutionGradient convolutionTranspose];
-[MPSCNNConvolutionGradient reloadWeightsAndBiasesFromDataSource];
-[MPSCNNConvolutionGradient PeakAtWeightsWithConvolutionGradientState:];
-[MPSCNNConvolutionGradient PeakAtWeightsWithConvolutionTransposeGradientState:];
-[MPSCNNConvolutionGradient batchEncodingStorageSizeForSourceImage:sourceStates:destinationImage:];
-[MPSCNNConvolutionGradient destinationImageDescriptorForSourceImages:sourceStates:paddingMethod:primaryOffset:secondaryOffset:kernelOffset:];
-[MPSCNNConvolutionGradient encodingStorageSizeForSourceImage:sourceStates:destinationImage:];
-[MPSCNNConvolutionGradient filterHandlesPlugin];
-[MPSCNNConvolutionGradient gradientOption];
-[MPSCNNConvolutionGradient initWithDevice:weights:convolutionTranspose:];
-[MPSCNNConvolutionGradient initWithDevice:weights:fullyConnected:];
-[MPSCNNConvolutionGradient initialize:convDesc:weights:dataType:weightsLayout:fullyConnected:convolutionTranspose:preferredWeightsDataType:];
-[MPSCNNConvolutionGradient initialize:weights:fullyConnected:convolutionTranspose:];
-[MPSCNNConvolutionGradient preferredWeightsDataType];
-[MPSCNNConvolutionGradient serializeWeightsAndBiases];
-[MPSCNNConvolutionGradient setSerializeWeightsAndBiases:];
-[MPSCNNConvolutionGradient sourceGradientFeatureChannels];
-[MPSCNNConvolutionGradient sourceImageFeatureChannels];
```
