# `MPSNNLossGradientNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNGradientFilterNode`
- 11 instance variables, 10 properties, 17 instance methods, 3 class methods

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
B _isLabelsGradientFilter;
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
@property (TB,R,N,V_isLabelsGradientFilter) isLabelsGradientFilter;
@property (T@"<MPSNNLossCallback>",&,N,V_propertyCallBack) propertyCallBack;
```

## Class methods

```
+[MPSNNLossGradientNode nodeWithSourceGradient:sourceImage:labels:gradientState:lossDescriptor:isLabelsGradientFilter:];
+[MPSNNLossGradientNode nodeWithSourceGradient:sourceImage:labels:weights:gradientState:lossDescriptor:isLabelsGradientFilter:];
+[MPSNNLossGradientNode nodeWithSources:gradientState:lossDescriptor:isLabelsGradientFilter:];
```

## Instance methods

```
-[MPSNNLossGradientNode dealloc];
-[MPSNNLossGradientNode weight];
-[MPSNNLossGradientNode epsilon];
-[MPSNNLossGradientNode delta];
-[MPSNNLossGradientNode numberOfClasses];
-[MPSNNLossGradientNode lossType];
-[MPSNNLossGradientNode labelSmoothing];
-[MPSNNLossGradientNode reductionType];
-[MPSNNLossGradientNode gradientFilterWithSources:];
-[MPSNNLossGradientNode initWithSourceGradient:sourceImage:labels:gradientState:lossDescriptor:isLabelsGradientFilter:];
-[MPSNNLossGradientNode initWithSourceGradient:sourceImage:labels:weights:gradientState:lossDescriptor:isLabelsGradientFilter:];
-[MPSNNLossGradientNode initWithSources:gradientState:lossDescriptor:isLabelsGradientFilter:];
-[MPSNNLossGradientNode isLabelsGradientFilter];
-[MPSNNLossGradientNode newFilterNode];
-[MPSNNLossGradientNode propertyCallBack];
-[MPSNNLossGradientNode reduceAcrossBatch];
-[MPSNNLossGradientNode setPropertyCallBack:];
```
