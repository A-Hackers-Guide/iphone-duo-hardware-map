# `MPSNNLossGradient`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNBinaryKernel`
- 12 instance variables, 9 properties, 25 instance methods, 1 class methods

## Instance variables

```
B _reduceAcrossBatch;
@"<MPSNNLossCallback>" _propertyCallback;
@"MPSMatrix" _reductionBuffer;
@"<MTLTexture>" _firstLossGradientImage;
B _computeLabelGradients;
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
@property (TB,N,V_computeLabelGradients) computeLabelGradients;
```

## Class methods

```
+[MPSNNLossGradient libraryInfo:];
```

## Instance methods

```
-[MPSNNLossGradient initWithDevice:];
-[MPSNNLossGradient debugDescription];
-[MPSNNLossGradient maxBatchSize];
-[MPSNNLossGradient dealloc];
-[MPSNNLossGradient weight];
-[MPSNNLossGradient setWeight:];
-[MPSNNLossGradient copyWithZone:device:];
-[MPSNNLossGradient initWithCoder:device:];
-[MPSNNLossGradient encodeWithCoder:];
-[MPSNNLossGradient setEpsilon:];
-[MPSNNLossGradient epsilon];
-[MPSNNLossGradient delta];
-[MPSNNLossGradient setDelta:];
-[MPSNNLossGradient numberOfClasses];
-[MPSNNLossGradient lossType];
-[MPSNNLossGradient initWithDevice:lossDescriptor:];
-[MPSNNLossGradient encodeBatchToCommandBuffer:sourceGradients:sourceImages:labels:weights:sourceStates:];
-[MPSNNLossGradient labelSmoothing];
-[MPSNNLossGradient reductionType];
-[MPSNNLossGradient setLabelSmoothing:];
-[MPSNNLossGradient computeLabelGradients];
-[MPSNNLossGradient destinationImageDescriptorForSourceImages:sourceStates:];
-[MPSNNLossGradient encodeBatchToCommandBuffer:sourceGradients:sourceImages:labels:weights:sourceStates:destinationGradients:];
-[MPSNNLossGradient reduceAcrossBatch];
-[MPSNNLossGradient setComputeLabelGradients:];
```
