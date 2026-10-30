# `MPSCNNConvolutionDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 16 instance variables, 12 properties, 47 instance methods, 4 class methods

## Instance variables

```
Q _kernelWidth;
Q _kernelHeight;
Q _inputFeatureChannels;
Q _outputFeatureChannels;
Q _featureChannelsLayout;
Q _strideInPixelsX;
Q _strideInPixelsY;
Q _groups;
@"NSData" _batchNormalizationData;
@"MPSCNNNeuron" _deprecated_neuron;
Q _subPixelScaleFactor;
Q _dilationRateX;
Q _dilationRateY;
B _depthWiseConvolution;
@"MPSNNNeuronDescriptor" _fusedNeuronDescriptor;
@"MPSCNNNeuron" _neuron_deprecated;
```

## Properties

```
@property (TQ,N,V_featureChannelsLayout) featureChannelsLayout;
@property (TQ,N,V_kernelWidth) kernelWidth;
@property (TQ,N,V_kernelHeight) kernelHeight;
@property (TQ,N,V_inputFeatureChannels) inputFeatureChannels;
@property (TQ,N,V_outputFeatureChannels) outputFeatureChannels;
@property (TQ,N,V_strideInPixelsX) strideInPixelsX;
@property (TQ,N,V_strideInPixelsY) strideInPixelsY;
@property (TQ,N,V_groups) groups;
@property (TQ,N,V_dilationRateX) dilationRateX;
@property (TQ,N,V_dilationRateY) dilationRateY;
@property (T@"MPSNNNeuronDescriptor",&,N,V_fusedNeuronDescriptor) fusedNeuronDescriptor;
@property (T@"MPSCNNNeuron",&,N,V_neuron_deprecated) neuron;
```

## Class methods

```
+[MPSCNNConvolutionDescriptor supportsSecureCoding];
+[MPSCNNConvolutionDescriptor cnnConvolutionDescriptorWithKernelWidth:kernelHeight:inputFeatureChannels:outputFeatureChannels:];
+[MPSCNNConvolutionDescriptor cnnConvolutionDescriptorWithKernelWidth:kernelHeight:inputFeatureChannels:outputFeatureChannels:neuronFilter:];
+[MPSCNNConvolutionDescriptor cnnConvolutionDescriptorWithKernelWidth:kernelHeight:inputFeatureChannels:outputFeatureChannels:postFilters:];
```

## Instance methods

```
-[MPSCNNConvolutionDescriptor debugDescription];
-[MPSCNNConvolutionDescriptor init];
-[MPSCNNConvolutionDescriptor dealloc];
-[MPSCNNConvolutionDescriptor setGroups:];
-[MPSCNNConvolutionDescriptor groups];
-[MPSCNNConvolutionDescriptor encodeWithCoder:];
-[MPSCNNConvolutionDescriptor initWithCoder:];
-[MPSCNNConvolutionDescriptor copyWithZone:];
-[MPSCNNConvolutionDescriptor kernelHeight];
-[MPSCNNConvolutionDescriptor kernelWidth];
-[MPSCNNConvolutionDescriptor setDilationRateX:];
-[MPSCNNConvolutionDescriptor setDilationRateY:];
-[MPSCNNConvolutionDescriptor setFusedNeuronDescriptor:];
-[MPSCNNConvolutionDescriptor setNeuronType:parameterA:parameterB:];
-[MPSCNNConvolutionDescriptor setNeuronType:parameterA:parameterB:parameterC:];
-[MPSCNNConvolutionDescriptor setStrideInPixelsX:];
-[MPSCNNConvolutionDescriptor setStrideInPixelsY:];
-[MPSCNNConvolutionDescriptor setKernelWidth:];
-[MPSCNNConvolutionDescriptor inputFeatureChannels];
-[MPSCNNConvolutionDescriptor neuronType];
-[MPSCNNConvolutionDescriptor outputFeatureChannels];
-[MPSCNNConvolutionDescriptor setKernelHeight:];
-[MPSCNNConvolutionDescriptor fusedNeuronDescriptor];
-[MPSCNNConvolutionDescriptor setBatchNormalizationParametersForInferenceWithMean:variance:gamma:beta:epsilon:];
-[MPSCNNConvolutionDescriptor setFeatureChannelsLayout:];
-[MPSCNNConvolutionDescriptor setNeuronType:];
-[MPSCNNConvolutionDescriptor strideInPixelsX];
-[MPSCNNConvolutionDescriptor strideInPixelsY];
-[MPSCNNConvolutionDescriptor setInputFeatureChannels:];
-[MPSCNNConvolutionDescriptor setOutputFeatureChannels:];
-[MPSCNNConvolutionDescriptor dilationRateX];
-[MPSCNNConvolutionDescriptor dilationRateY];
-[MPSCNNConvolutionDescriptor featureChannelsLayout];
-[MPSCNNConvolutionDescriptor hasBatchNormData];
-[MPSCNNConvolutionDescriptor initWithKernelWidth:kernelHeight:inputFeatureChannels:outputFeatureChannels:];
-[MPSCNNConvolutionDescriptor initWithKernelWidth:kernelHeight:inputFeatureChannels:outputFeatureChannels:neuronFilter:];
-[MPSCNNConvolutionDescriptor neuron];
-[MPSCNNConvolutionDescriptor neuronInfo];
-[MPSCNNConvolutionDescriptor neuronParameterA];
-[MPSCNNConvolutionDescriptor neuronParameterB];
-[MPSCNNConvolutionDescriptor neuronParameterC];
-[MPSCNNConvolutionDescriptor newDescriptorWithNeuronInfo:];
-[MPSCNNConvolutionDescriptor setNeuron:];
-[MPSCNNConvolutionDescriptor setNeuronParameterA:];
-[MPSCNNConvolutionDescriptor setNeuronParameterB:];
-[MPSCNNConvolutionDescriptor setNeuronParameterC:];
-[MPSCNNConvolutionDescriptor setNeuronToPReLUWithParametersA:];
```
