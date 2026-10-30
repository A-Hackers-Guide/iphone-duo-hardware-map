# `MPSNNForwardLoss`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNKernel`
- 11 instance variables, 8 properties, 26 instance methods, 1 class methods

## Instance variables

```
B _reduceAcrossBatch;
@"<MPSNNLossCallback>" _propertyCallback;
@"MPSMatrix" _reductionBuffer;
@"MPSImage" _firstLossImage;
I _lossType;
i _reductionType;
f _weight;
f _labelSmoothing;
f _epsilon;
f _delta;
Q _numberOfClasses;
```

## Properties

```
@property (TI,R,N,V_lossType) lossType;
@property (Ti,R,N,V_reductionType) reductionType;
@property (TB,R,N,V_reduceAcrossBatch) reduceAcrossBatch;
@property (TQ,R,N,V_numberOfClasses) numberOfClasses;
@property (Tf,N,V_weight) weight;
@property (Tf,N,V_labelSmoothing) labelSmoothing;
@property (Tf,N,V_epsilon) epsilon;
@property (Tf,N,V_delta) delta;
```

## Class methods

```
+[MPSNNForwardLoss libraryInfo:];
```

## Instance methods

```
-[MPSNNForwardLoss initWithDevice:];
-[MPSNNForwardLoss debugDescription];
-[MPSNNForwardLoss maxBatchSize];
-[MPSNNForwardLoss dealloc];
-[MPSNNForwardLoss weight];
-[MPSNNForwardLoss resultStateForSourceImage:sourceStates:destinationImage:];
-[MPSNNForwardLoss setWeight:];
-[MPSNNForwardLoss copyWithZone:device:];
-[MPSNNForwardLoss initWithCoder:device:];
-[MPSNNForwardLoss temporaryResultStateForCommandBuffer:sourceImage:sourceStates:destinationImage:];
-[MPSNNForwardLoss encodeWithCoder:];
-[MPSNNForwardLoss setEpsilon:];
-[MPSNNForwardLoss epsilon];
-[MPSNNForwardLoss isResultStateReusedAcrossBatch];
-[MPSNNForwardLoss delta];
-[MPSNNForwardLoss setDelta:];
-[MPSNNForwardLoss numberOfClasses];
-[MPSNNForwardLoss lossType];
-[MPSNNForwardLoss initWithDevice:lossDescriptor:];
-[MPSNNForwardLoss encodeBatchToCommandBuffer:sourceImages:labels:weights:destinationStates:destinationStateIsTemporary:];
-[MPSNNForwardLoss labelSmoothing];
-[MPSNNForwardLoss reductionType];
-[MPSNNForwardLoss setLabelSmoothing:];
-[MPSNNForwardLoss destinationImageDescriptorForSourceImages:sourceStates:];
-[MPSNNForwardLoss encodeBatchToCommandBuffer:sourceImages:labels:weights:destinationStates:destinationImages:];
-[MPSNNForwardLoss reduceAcrossBatch];
```
