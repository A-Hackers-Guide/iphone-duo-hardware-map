# `MPSNNConcatenation`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNKernel`
- 0 instance variables, 0 properties, 17 instance methods, 1 class methods

## Class methods

```
+[MPSNNConcatenation libraryInfo:];
```

## Instance methods

```
-[MPSNNConcatenation initWithDevice:];
-[MPSNNConcatenation resultStateForSourceImage:sourceStates:destinationImage:];
-[MPSNNConcatenation initWithCoder:device:];
-[MPSNNConcatenation temporaryResultStateForCommandBuffer:sourceImage:sourceStates:destinationImage:];
-[MPSNNConcatenation encodeWithCoder:];
-[MPSNNConcatenation isResultStateReusedAcrossBatch];
-[MPSNNConcatenation resultStateBatchForSourceImage:sourceStates:destinationImage:];
-[MPSNNConcatenation copyToGradientState:sourceImages:sourceStates:destinationImage:];
-[MPSNNConcatenation copyToGradientState:sourceImage:sourceStates:destinationImage:];
-[MPSNNConcatenation destinationImageDescriptorForSourceImages:sourceStates:paddingMethod:sourceOffset:];
-[MPSNNConcatenation encodeBatchToCommandBuffer:sourceImages:destinationImage:];
-[MPSNNConcatenation encodeToCommandBuffer:sourceImages:destinationImage:];
-[MPSNNConcatenation resultStateBatchForSourceImages:sourceStates:destinationImage:];
-[MPSNNConcatenation resultStateForSourceImages:sourceStates:destinationImage:];
-[MPSNNConcatenation temporaryResultStateBatchForCommandBuffer:sourceImage:sourceStates:destinationImage:];
-[MPSNNConcatenation temporaryResultStateBatchForCommandBuffer:sourceImages:sourceStates:destinationImage:];
-[MPSNNConcatenation temporaryResultStateForCommandBuffer:sourceImages:sourceStates:destinationImage:];
```
