# `MPSCNNDropoutGradientState`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNGradientState`
- 6 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
{?="width"Q"height"Q"depth"Q} _maskStrideInPixels;
f _keepProbability;
Q _resourcePixelFormat;
{?="width"Q"height"Q"depth"Q} _resourceSize;
Q _commonBufferOffsetBytes;
@"<MTLBuffer>" _commonMaskBuffer;
```

## Instance methods

```
-[MPSCNNDropoutGradientState init];
-[MPSCNNDropoutGradientState dealloc];
-[MPSCNNDropoutGradientState synchronizeOnCommandBuffer:];
-[MPSCNNDropoutGradientState maskData];
```
