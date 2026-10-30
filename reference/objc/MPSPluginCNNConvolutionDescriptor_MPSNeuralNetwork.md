# `MPSPluginCNNConvolutionDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 14 properties, 16 instance methods, 0 class methods

## Instance variables

```
Q _kernelWidth;
Q _kernelHeight;
Q _inputFeatureChannels;
Q _outputFeatureChannels;
Q _strideInPixelsX;
Q _strideInPixelsY;
Q _groups;
Q _dilationRateX;
Q _dilationRateY;
@"MPSNNNeuronDescriptor" _fusedNeuronDescriptor;
Q _channelMultiplier;
Q _subPixelScaleFactor;
B _isFullyConnected;
B _isConvolutionTranspose;
```

## Properties

```
@property (TQ,R,N,V_kernelWidth) kernelWidth;
@property (TQ,R,N,V_kernelHeight) kernelHeight;
@property (TQ,R,N,V_inputFeatureChannels) inputFeatureChannels;
@property (TQ,R,N,V_outputFeatureChannels) outputFeatureChannels;
@property (TQ,R,N,V_strideInPixelsX) strideInPixelsX;
@property (TQ,R,N,V_strideInPixelsY) strideInPixelsY;
@property (TQ,R,N,V_groups) groups;
@property (TQ,R,N,V_dilationRateX) dilationRateX;
@property (TQ,R,N,V_dilationRateY) dilationRateY;
@property (T@"MPSNNNeuronDescriptor",R,N,V_fusedNeuronDescriptor) fusedNeuronDescriptor;
@property (TQ,R,N,V_channelMultiplier) channelMultiplier;
@property (TQ,R,N,V_subPixelScaleFactor) subPixelScaleFactor;
@property (TB,R,N,V_isFullyConnected) isFullyConnected;
@property (TB,R,N,V_isConvolutionTranspose) isConvolutionTranspose;
```

## Instance methods

```
-[MPSPluginCNNConvolutionDescriptor dealloc];
-[MPSPluginCNNConvolutionDescriptor groups];
-[MPSPluginCNNConvolutionDescriptor kernelHeight];
-[MPSPluginCNNConvolutionDescriptor kernelWidth];
-[MPSPluginCNNConvolutionDescriptor inputFeatureChannels];
-[MPSPluginCNNConvolutionDescriptor outputFeatureChannels];
-[MPSPluginCNNConvolutionDescriptor isFullyConnected];
-[MPSPluginCNNConvolutionDescriptor fusedNeuronDescriptor];
-[MPSPluginCNNConvolutionDescriptor strideInPixelsX];
-[MPSPluginCNNConvolutionDescriptor strideInPixelsY];
-[MPSPluginCNNConvolutionDescriptor channelMultiplier];
-[MPSPluginCNNConvolutionDescriptor subPixelScaleFactor];
-[MPSPluginCNNConvolutionDescriptor dilationRateX];
-[MPSPluginCNNConvolutionDescriptor dilationRateY];
-[MPSPluginCNNConvolutionDescriptor isConvolutionTranspose];
-[MPSPluginCNNConvolutionDescriptor initWithKernelWidth:kernelHeight:inputFeatureChannels:outputFeatureChannels:strideInPixelsX:strideInPixelsY:groups:dilationRateX:dilationRateY:channelMultiplier:subPixelScaleFactor:isFullyConnected:isConvolutionTranspose:fusedNeuronDescriptor:];
```
