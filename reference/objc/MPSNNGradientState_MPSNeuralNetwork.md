# `MPSNNGradientState`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSState`
- 20 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
{?="x"q"y"q"z"q} _offset;
{?="origin"{?="x"Q"y"Q"z"Q}"size"{?="width"Q"height"Q"depth"Q}} _clipRect;
{?="width"Q"height"Q"depth"Q} _destSize;
Q _destFeatureChannels;
Q _destinationFeatureChannelOffset;
Q _sourceFeatureChannelOffset;
Q _kernelWidth;
Q _kernelHeight;
Q _strideInPixelsX;
Q _strideInPixelsY;
Q _dilationRateX;
Q _dilationRateY;
@"<MPSNNPadding>" _padding;
Q _maxBatchSize;
B _isBackwards;
Q _edgeMode;
{?="width"Q"height"Q"depth"Q} _srcSize;
Q _sourceFeatureChannels;
B _initOnce;
I _provenance;
```

## Instance methods

```
-[MPSNNGradientState debugDescription];
-[MPSNNGradientState dealloc];
-[MPSNNGradientState destinationImageDescriptorForSourceImages:sourceStates:forKernel:suggestedDescriptor:];
```
