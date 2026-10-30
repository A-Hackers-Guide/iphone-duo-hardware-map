# `MPSCNNGradientKernel`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNBinaryKernel`
- 2 instance variables, 2 properties, 22 instance methods, 0 class methods

## Instance variables

```
q _kernelOffsetX;
q _kernelOffsetY;
```

## Properties

```
@property (Tq,N,V_kernelOffsetX) kernelOffsetX;
@property (Tq,N,V_kernelOffsetY) kernelOffsetY;
```

## Instance methods

```
-[MPSCNNGradientKernel initWithDevice:];
-[MPSCNNGradientKernel copyWithZone:device:];
-[MPSCNNGradientKernel initWithCoder:device:];
-[MPSCNNGradientKernel encodeWithCoder:];
-[MPSCNNGradientKernel encodeToCommandBuffer:sourceGradient:sourceImage:gradientState:];
-[MPSCNNGradientKernel encodeBatchToCommandBuffer:sourceGradients:sourceImages:gradientStates:];
-[MPSCNNGradientKernel encodeBatchToCommandBuffer:sourceGradients:sourceImages:gradientStates:destinationGradients:];
-[MPSCNNGradientKernel encodeToCommandBuffer:sourceGradient:sourceImage:gradientState:destinationGradient:];
-[MPSCNNGradientKernel kernelOffsetX];
-[MPSCNNGradientKernel kernelOffsetY];
-[MPSCNNGradientKernel setKernelOffsetX:];
-[MPSCNNGradientKernel setKernelOffsetY:];
-[MPSCNNGradientKernel isStateModified];
-[MPSCNNGradientKernel destinationImageDescriptorForSourceImages:sourceStates:];
-[MPSCNNGradientKernel encodeBatchToCommandEncoder:commandBuffer:sourceGradients:sourceImages:gradientStates:];
-[MPSCNNGradientKernel encodeBatchToCommandEncoder:commandBuffer:sourceGradients:sourceImages:gradientStates:destinationGradients:];
-[MPSCNNGradientKernel encodeToCommandEncoder:commandBuffer:sourceGradient:sourceImage:gradientState:];
-[MPSCNNGradientKernel encodeToCommandEncoder:commandBuffer:sourceGradient:sourceImage:gradientState:destinationGradient:];
-[MPSCNNGradientKernel readBinaryGradientState:isSecondarySourceFilter:];
-[MPSCNNGradientKernel readGradientState:];
-[MPSCNNGradientKernel resultStateForPrimaryImage:secondaryImage:sourceStates:];
-[MPSCNNGradientKernel temporaryResultStateForCommandBuffer:primaryImage:secondaryImage:sourceStates:];
```
