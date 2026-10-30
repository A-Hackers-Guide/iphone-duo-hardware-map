# `MPSCNNBatchNormalizationGradientNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNGradientFilterNode`
- Protocols: `MPSNNTrainableNode`
- 1 instance variables, 5 properties, 5 instance methods, 1 class methods

## Instance variables

```
Q _trainingStyle;
```

## Properties

```
@property (TQ,N,V_trainingStyle) trainingStyle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MPSCNNBatchNormalizationGradientNode nodeWithSourceGradient:sourceImage:gradientState:];
```

## Instance methods

```
-[MPSCNNBatchNormalizationGradientNode initWithGradientImages:forwardFilter:];
-[MPSCNNBatchNormalizationGradientNode initWithSourceGradient:sourceImage:gradientState:];
-[MPSCNNBatchNormalizationGradientNode newFilterNode];
-[MPSCNNBatchNormalizationGradientNode setTrainingStyle:];
-[MPSCNNBatchNormalizationGradientNode trainingStyle];
```
