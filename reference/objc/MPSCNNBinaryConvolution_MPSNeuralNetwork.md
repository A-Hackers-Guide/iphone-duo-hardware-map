# `MPSCNNBinaryConvolution`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNKernel`
- 14 instance variables, 2 properties, 15 instance methods, 1 class methods

## Instance variables

```
Q _inputFeatureChannels;
Q _outputFeatureChannels;
{NeuronInfo="type"i"a"f"b"f"c"f"aData"@"NSData"} _neuronInfo;
Q _filterStride;
@"<MTLBuffer>" _weights;
@"<MTLBuffer>" _outputbias;
@"<MTLBuffer>" _outputScale;
@"<MTLBuffer>" _inputbias;
@"<MTLBuffer>" _inputScale;
Q _flags;
Q _convType;
@"MPSCNNPoolingAverage" _poolingFilter;
B _fullyConnected;
f _outputScaleValue;
```

## Properties

```
@property (TQ,R,N,V_inputFeatureChannels) inputFeatureChannels;
@property (TQ,R,N,V_outputFeatureChannels) outputFeatureChannels;
```

## Class methods

```
+[MPSCNNBinaryConvolution libraryInfo:];
```

## Instance methods

```
-[MPSCNNBinaryConvolution initWithDevice:];
-[MPSCNNBinaryConvolution debugDescription];
-[MPSCNNBinaryConvolution dealloc];
-[MPSCNNBinaryConvolution copyWithZone:device:];
-[MPSCNNBinaryConvolution initWithCoder:device:];
-[MPSCNNBinaryConvolution encodeWithCoder:];
-[MPSCNNBinaryConvolution inputFeatureChannels];
-[MPSCNNBinaryConvolution outputFeatureChannels];
-[MPSCNNBinaryConvolution initWithDevice:convolutionData:outputBiasTerms:outputScaleTerms:inputBiasTerms:inputScaleTerms:type:flags:];
-[MPSCNNBinaryConvolution copyBuffer:device:];
-[MPSCNNBinaryConvolution createBuffersFromkernelWeights:inputBiasTerms:inputScaleTerms:outputBiasTerms:outputScaleTerms:useHalfPrecision:];
-[MPSCNNBinaryConvolution destinationImageDescriptorForSourceImages:sourceStates:paddingMethod:sourceOffset:];
-[MPSCNNBinaryConvolution initWithDevice:convolutionData:scaleValue:type:flags:];
-[MPSCNNBinaryConvolution initWithDeviceImpl:convolutionDescriptor:kernelWeights:biasTerms:scaleValue:type:flags:];
-[MPSCNNBinaryConvolution initWithDeviceImpl:convolutionDescriptor:kernelWeights:outputBiasTerms:outputScaleTerms:inputBiasTerms:inputScaleTerms:type:flags:];
```
