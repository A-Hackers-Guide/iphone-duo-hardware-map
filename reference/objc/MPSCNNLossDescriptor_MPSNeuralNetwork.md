# `MPSCNNLossDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 8 instance variables, 8 properties, 19 instance methods, 1 class methods

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
```

## Properties

```
@property (TI,N,V_lossType) lossType;
@property (Ti,N,V_reductionType) reductionType;
@property (TB,N,V_reduceAcrossBatch) reduceAcrossBatch;
@property (Tf,N,V_weight) weight;
@property (Tf,N,V_labelSmoothing) labelSmoothing;
@property (TQ,N,V_numberOfClasses) numberOfClasses;
@property (Tf,N,V_epsilon) epsilon;
@property (Tf,N,V_delta) delta;
```

## Class methods

```
+[MPSCNNLossDescriptor cnnLossDescriptorWithType:reductionType:];
```

## Instance methods

```
-[MPSCNNLossDescriptor debugDescription];
-[MPSCNNLossDescriptor dealloc];
-[MPSCNNLossDescriptor weight];
-[MPSCNNLossDescriptor setWeight:];
-[MPSCNNLossDescriptor setEpsilon:];
-[MPSCNNLossDescriptor epsilon];
-[MPSCNNLossDescriptor copyWithZone:];
-[MPSCNNLossDescriptor delta];
-[MPSCNNLossDescriptor setDelta:];
-[MPSCNNLossDescriptor numberOfClasses];
-[MPSCNNLossDescriptor setNumberOfClasses:];
-[MPSCNNLossDescriptor lossType];
-[MPSCNNLossDescriptor setLossType:];
-[MPSCNNLossDescriptor labelSmoothing];
-[MPSCNNLossDescriptor reductionType];
-[MPSCNNLossDescriptor setLabelSmoothing:];
-[MPSCNNLossDescriptor setReduceAcrossBatch:];
-[MPSCNNLossDescriptor reduceAcrossBatch];
-[MPSCNNLossDescriptor setReductionType:];
```
