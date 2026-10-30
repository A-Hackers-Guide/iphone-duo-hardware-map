# `MPSNNPermute`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNKernel`
- 1 instance variables, 1 properties, 14 instance methods, 1 class methods

## Instance variables

```
{MPSNNDimensionOrder="dimensions"[4Q]} _dimensionOrder;
```

## Properties

```
@property (T{MPSNNDimensionOrder=[4Q]},N,V_dimensionOrder) dimensionOrder;
```

## Class methods

```
+[MPSNNPermute libraryInfo:];
```

## Instance methods

```
-[MPSNNPermute initWithDevice:];
-[MPSNNPermute resultStateForSourceImage:sourceStates:destinationImage:];
-[MPSNNPermute copyWithZone:device:];
-[MPSNNPermute initWithCoder:device:];
-[MPSNNPermute temporaryResultStateForCommandBuffer:sourceImage:sourceStates:destinationImage:];
-[MPSNNPermute encodeWithCoder:];
-[MPSNNPermute isResultStateReusedAcrossBatch];
-[MPSNNPermute dimensionOrder];
-[MPSNNPermute appendBatchBarrier];
-[MPSNNPermute destinationImageDescriptorForSourceImages:sourceStates:paddingMethod:sourceOffset:];
-[MPSNNPermute encodeBatchInternalToCommandEncoder:commandBuffer:sourceImages:inStates:destinationImages:srcSize:destSize:testClipRect:testMaxClipRect:];
-[MPSNNPermute encodeBatchToCommandBuffer:sourceImages:inStates:destinationImages:];
-[MPSNNPermute encodeBatchToCommandEncoder:commandBuffer:sourceImages:inStates:destinationImages:];
-[MPSNNPermute setDimensionOrder:];
```
