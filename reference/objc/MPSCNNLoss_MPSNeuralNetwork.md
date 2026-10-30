# `MPSCNNLoss`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNKernel`
- 10 instance variables, 8 properties, 23 instance methods, 1 class methods

## Instance variables

```
I _lossType;
i _reductionType;
B _reduceAcrossBatch;
f _weight;
f _labelSmoothing;
Q _numberOfClasses;
f _epsilon;
f _delta;
@"MPSMatrix" _reductionBuffer;
@"MPSImage" _firstLossImage;
```

## Properties

```
@property (Tf,N,V_weight) weight;
@property (TI,R,N,V_lossType) lossType;
@property (Ti,R,N,V_reductionType) reductionType;
@property (Tf,R,N,V_labelSmoothing) labelSmoothing;
@property (TQ,R,N,V_numberOfClasses) numberOfClasses;
@property (Tf,R,N,V_epsilon) epsilon;
@property (Tf,R,N,V_delta) delta;
@property (TB,R,N,V_reduceAcrossBatch) reduceAcrossBatch;
```

## Class methods

```
+[MPSCNNLoss libraryInfo:];
```

## Instance methods

```
-[MPSCNNLoss initWithDevice:];
-[MPSCNNLoss debugDescription];
-[MPSCNNLoss maxBatchSize];
-[MPSCNNLoss dealloc];
-[MPSCNNLoss weight];
-[MPSCNNLoss setWeight:];
-[MPSCNNLoss copyWithZone:device:];
-[MPSCNNLoss initWithCoder:device:];
-[MPSCNNLoss encodeWithCoder:];
-[MPSCNNLoss epsilon];
-[MPSCNNLoss delta];
-[MPSCNNLoss numberOfClasses];
-[MPSCNNLoss lossType];
-[MPSCNNLoss encodeBatchToCommandBuffer:sourceImages:labels:];
-[MPSCNNLoss initWithDevice:lossDescriptor:];
-[MPSCNNLoss labelSmoothing];
-[MPSCNNLoss reductionType];
-[MPSCNNLoss encodeBatchToCommandBuffer:sourceImages:labels:destinationImages:];
-[MPSCNNLoss encodeToCommandBuffer:sourceImage:labels:];
-[MPSCNNLoss encodeToCommandBuffer:sourceImage:labels:destinationImage:];
-[MPSCNNLoss reduceAcrossBatch];
-[MPSCNNLoss resultStateForSourceImage:sourceStates:];
-[MPSCNNLoss temporaryResultStateForCommandBuffer:sourceImage:sourceStates:];
```
