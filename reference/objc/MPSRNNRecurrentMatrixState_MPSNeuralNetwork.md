# `MPSRNNRecurrentMatrixState`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSState`
- 4 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
^@ recurrentMatrices;
^@ cellMatrices;
i nLayers;
B _isTemporary;
```

## Instance methods

```
-[MPSRNNRecurrentMatrixState dealloc];
-[MPSRNNRecurrentMatrixState isTemporary];
-[MPSRNNRecurrentMatrixState setReadCount:];
-[MPSRNNRecurrentMatrixState getMemoryCellMatrixForLayerIndex:];
-[MPSRNNRecurrentMatrixState getRecurrentOutputMatrixForLayerIndex:];
-[MPSRNNRecurrentMatrixState initWithCommandBuffer:recurrentMatrixDescriptors:cellMatrixDescriptors:isTemporary:layerCount:];
-[MPSRNNRecurrentMatrixState initWithDevice:commandBuffer:recurrentMatrixDescriptors:cellMatrixDescriptors:isTemporary:layerCount:];
```
