# `MPSCNNInstanceNormalizationNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNFilterNode`
- Protocols: `MPSNNTrainableNode`
- 2 instance variables, 5 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"<MPSCNNInstanceNormalizationDataSource>" _dataSource;
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
+[MPSCNNInstanceNormalizationNode nodeWithSource:dataSource:];
```

## Instance methods

```
-[MPSCNNInstanceNormalizationNode dealloc];
-[MPSCNNInstanceNormalizationNode gradientClass];
-[MPSCNNInstanceNormalizationNode initWithSource:dataSource:];
-[MPSCNNInstanceNormalizationNode newFilterNode];
-[MPSCNNInstanceNormalizationNode setTrainingStyle:];
-[MPSCNNInstanceNormalizationNode trainingStyle];
```
