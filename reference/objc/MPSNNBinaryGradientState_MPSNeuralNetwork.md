# `MPSNNBinaryGradientState`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSState`
- 33 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
{?="x"q"y"q"z"q} _primaryOffset;
{?="x"q"y"q"z"q} _secondaryOffset;
{?="origin"{?="x"Q"y"Q"z"Q}"size"{?="width"Q"height"Q"depth"Q}} _clipRect;
{?="width"Q"height"Q"depth"Q} _destSize;
Q _destFeatureChannels;
Q _destinationFeatureChannelOffset;
Q _primarySourceFeatureChannelOffset;
Q _secondarySourceFeatureChannelOffset;
Q _primarySourceFeatureChannelMaxCount;
Q _secondarySourceFeatureChannelMaxCount;
Q _primaryKernelWidth;
Q _primaryKernelHeight;
Q _secondaryKernelWidth;
Q _secondaryKernelHeight;
Q _primaryStrideInPixelsX;
Q _primaryStrideInPixelsY;
Q _secondaryStrideInPixelsX;
Q _secondaryStrideInPixelsY;
Q _primaryDilationRateX;
Q _primaryDilationRateY;
Q _secondaryDilationRateX;
Q _secondaryDilationRateY;
@"<MPSNNPadding>" _padding;
Q _maxBatchSize;
B _isBackwards;
Q _primaryEdgeMode;
Q _secondaryEdgeMode;
{?="width"Q"height"Q"depth"Q} _primarySrcSize;
Q _primarySourceFeatureChannels;
{?="width"Q"height"Q"depth"Q} _secondarySrcSize;
Q _secondarySourceFeatureChannels;
B _initOnce;
I _provenance;
```

## Instance methods

```
-[MPSNNBinaryGradientState dealloc];
-[MPSNNBinaryGradientState destinationImageDescriptorForSourceImages:sourceStates:forKernel:suggestedDescriptor:];
```
