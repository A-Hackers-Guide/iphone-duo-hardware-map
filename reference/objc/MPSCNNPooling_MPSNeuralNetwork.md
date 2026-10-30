# `MPSCNNPooling`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNKernel`
- 0 instance variables, 0 properties, 13 instance methods, 1 class methods

## Class methods

```
+[MPSCNNPooling libraryInfo:];
```

## Instance methods

```
-[MPSCNNPooling initWithDevice:];
-[MPSCNNPooling debugDescription];
-[MPSCNNPooling newPlugin];
-[MPSCNNPooling copyWithZone:device:];
-[MPSCNNPooling initWithCoder:device:];
-[MPSCNNPooling initWithDevice:kernelWidth:kernelHeight:strideInPixelsX:strideInPixelsY:];
-[MPSCNNPooling encodeWithCoder:];
-[MPSCNNPooling encodeBatchToCommandBuffer:sourceImages:destinationImages:];
-[MPSCNNPooling encodeToCommandBuffer:sourceImage:destinationImage:];
-[MPSCNNPooling initWithDevice:kernelWidth:kernelHeight:];
-[MPSCNNPooling encodeBatchToCommandBuffer:sourceImages:];
-[MPSCNNPooling encodeToCommandBuffer:sourceImage:];
-[MPSCNNPooling setKernelWidth:kernelHeight:strideInPixelsX:strideInPixelsY:];
```
