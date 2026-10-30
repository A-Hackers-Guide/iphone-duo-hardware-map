# `MPSNNPermuteGradient`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNGradientKernel`
- 1 instance variables, 0 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"MPSNNPermute" _revPermuteKernel;
```

## Class methods

```
+[MPSNNPermuteGradient libraryInfo:];
```

## Instance methods

```
-[MPSNNPermuteGradient initWithDevice:];
-[MPSNNPermuteGradient dealloc];
-[MPSNNPermuteGradient copyWithZone:device:];
-[MPSNNPermuteGradient initWithCoder:device:];
-[MPSNNPermuteGradient encodeWithCoder:];
-[MPSNNPermuteGradient encodeBatchToCommandBuffer:primaryImages:secondaryImages:inStates:destinationImages:];
-[MPSNNPermuteGradient encodeBatchToCommandEncoder:commandBuffer:primaryImages:secondaryImages:inStates:destinationImages:];
```
