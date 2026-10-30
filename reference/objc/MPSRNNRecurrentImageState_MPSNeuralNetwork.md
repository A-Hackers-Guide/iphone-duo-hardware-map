# `MPSRNNRecurrentImageState`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSState`
- 4 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
^@ recurrentImages;
^@ cellImages;
i nLayers;
B _isTemporary;
```

## Instance methods

```
-[MPSRNNRecurrentImageState dealloc];
-[MPSRNNRecurrentImageState isTemporary];
-[MPSRNNRecurrentImageState setReadCount:];
-[MPSRNNRecurrentImageState getMemoryCellImageForLayerIndex:];
-[MPSRNNRecurrentImageState getRecurrentOutputImageForLayerIndex:];
-[MPSRNNRecurrentImageState initWithCommandBuffer:recurrentImageDescriptors:cellImageDescriptors:isTemporary:layerCount:];
```
