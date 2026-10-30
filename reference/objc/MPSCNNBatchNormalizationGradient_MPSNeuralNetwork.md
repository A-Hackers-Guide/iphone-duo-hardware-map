# `MPSCNNBatchNormalizationGradient`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNGradientKernel`
- 2 instance variables, 0 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"MPSNNNeuronDescriptor" _fusedNeuronDescriptor;
@"<MTLBuffer>" _preluBuffer;
```

## Class methods

```
+[MPSCNNBatchNormalizationGradient libraryInfo:];
```

## Instance methods

```
-[MPSCNNBatchNormalizationGradient initWithDevice:];
-[MPSCNNBatchNormalizationGradient dealloc];
-[MPSCNNBatchNormalizationGradient copyWithZone:device:];
-[MPSCNNBatchNormalizationGradient initWithCoder:device:];
-[MPSCNNBatchNormalizationGradient encodeWithCoder:];
-[MPSCNNBatchNormalizationGradient encodeBatchToCommandBuffer:sourceGradients:sourceImages:batchNormalizationState:];
-[MPSCNNBatchNormalizationGradient encodeBatchToCommandBuffer:sourceGradients:sourceImages:batchNormalizationState:destinationGradients:];
-[MPSCNNBatchNormalizationGradient encodeToCommandBuffer:sourceGradient:sourceImage:batchNormalizationState:];
-[MPSCNNBatchNormalizationGradient encodeToCommandBuffer:sourceGradient:sourceImage:batchNormalizationState:destinationGradient:];
-[MPSCNNBatchNormalizationGradient initWithDevice:fusedNeuronDescriptor:];
```
