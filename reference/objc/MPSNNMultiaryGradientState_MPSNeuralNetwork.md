# `MPSNNMultiaryGradientState`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSState`
- 12 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
Q _srcCount;
^{NNKernelSourceParams={?=qqq}QQQQQQQQQ} _srcInfo;
^{?=QQQ} _srcSizes;
{?="origin"{?="x"Q"y"Q"z"Q}"size"{?="width"Q"height"Q"depth"Q}} _clipRect;
{?="width"Q"height"Q"depth"Q} _destSize;
Q _destFeatureChannels;
Q _destinationFeatureChannelOffset;
@"<MPSNNPadding>" _padding;
Q _maxBatchSize;
B _isBackwards;
B _initOnce;
I _provenance;
```

## Instance methods

```
-[MPSNNMultiaryGradientState dealloc];
-[MPSNNMultiaryGradientState initWithSourceCount:];
```
