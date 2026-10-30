# `MPSNNForwardLossNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNFilterNode`
- 10 instance variables, 9 properties, 20 instance methods, 3 class methods

## Instance variables

```
I _lossType;
i _reductionType;
f _weight;
f _labelSmoothing;
Q _numberOfClasses;
f _epsilon;
f _delta;
@"MPSCNNLossDescriptor" _descriptor;
@"<MPSNNLossCallback>" _propertyCallBack;
B _reduceAcrossBatch;
```

## Properties

```
@property (TI,R,N,V_lossType) lossType;
@property (Ti,R,N,V_reductionType) reductionType;
@property (TQ,R,N,V_numberOfClasses) numberOfClasses;
@property (TB,R,N,V_reduceAcrossBatch) reduceAcrossBatch;
@property (Tf,R,N,V_weight) weight;
@property (Tf,R,N,V_labelSmoothing) labelSmoothing;
@property (Tf,R,N,V_epsilon) epsilon;
@property (Tf,R,N,V_delta) delta;
@property (T@"<MPSNNLossCallback>",&,N,V_propertyCallBack) propertyCallBack;
```

## Class methods

```
+[MPSNNForwardLossNode nodeWithSources:lossDescriptor:];
+[MPSNNForwardLossNode nodeWithSource:labels:lossDescriptor:];
+[MPSNNForwardLossNode nodeWithSource:labels:weights:lossDescriptor:];
```

## Instance methods

```
-[MPSNNForwardLossNode dealloc];
-[MPSNNForwardLossNode weight];
-[MPSNNForwardLossNode epsilon];
-[MPSNNForwardLossNode delta];
-[MPSNNForwardLossNode numberOfClasses];
-[MPSNNForwardLossNode lossType];
-[MPSNNForwardLossNode labelSmoothing];
-[MPSNNForwardLossNode reductionType];
-[MPSNNForwardLossNode initWithSources:lossDescriptor:];
-[MPSNNForwardLossNode gradientClass];
-[MPSNNForwardLossNode gradientFilterWithSource:];
-[MPSNNForwardLossNode gradientFilterWithSources:];
-[MPSNNForwardLossNode gradientFiltersWithSource:];
-[MPSNNForwardLossNode gradientFiltersWithSources:];
-[MPSNNForwardLossNode initWithSource:labels:lossDescriptor:];
-[MPSNNForwardLossNode initWithSource:labels:weights:lossDescriptor:];
-[MPSNNForwardLossNode newFilterNode];
-[MPSNNForwardLossNode propertyCallBack];
-[MPSNNForwardLossNode reduceAcrossBatch];
-[MPSNNForwardLossNode setPropertyCallBack:];
```
