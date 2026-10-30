# `MPSNNReshape`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNKernel`
- 3 instance variables, 0 properties, 10 instance methods, 1 class methods

## Instance variables

```
Q _reshapedWidth;
Q _reshapedHeight;
Q _reshapedFeatureChannels;
```

## Class methods

```
+[MPSNNReshape libraryInfo:];
```

## Instance methods

```
-[MPSNNReshape initWithDevice:];
-[MPSNNReshape debugDescription];
-[MPSNNReshape copyWithZone:device:];
-[MPSNNReshape initWithCoder:device:];
-[MPSNNReshape encodeWithCoder:];
-[MPSNNReshape destinationImageDescriptorForSourceImages:sourceStates:paddingMethod:sourceOffset:];
-[MPSNNReshape encodeBatchToCommandBuffer:sourceImages:destinationStates:destinationStateIsTemporary:reshapedWidth:reshapedHeight:reshapedFeatureChannels:];
-[MPSNNReshape encodeBatchToCommandBuffer:sourceImages:reshapedWidth:reshapedHeight:reshapedFeatureChannels:];
-[MPSNNReshape encodeToCommandBuffer:sourceImage:destinationState:destinationStateIsTemporary:reshapedWidth:reshapedHeight:reshapedFeatureChannels:];
-[MPSNNReshape encodeToCommandBuffer:sourceImage:reshapedWidth:reshapedHeight:reshapedFeatureChannels:];
```
