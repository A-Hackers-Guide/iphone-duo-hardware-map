# `MPSCNNBatchNormalizationNode`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSNNFilterNode`
- Protocols: `MPSNNTrainableNode`
- 3 instance variables, 6 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"<MPSCNNBatchNormalizationDataSource>" _dataSource;
Q _flags;
Q _trainingStyle;
```

## Properties

```
@property (TQ,N,V_flags) flags;
@property (TQ,N,V_trainingStyle) trainingStyle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MPSCNNBatchNormalizationNode nodeWithSource:dataSource:];
```

## Instance methods

```
-[MPSCNNBatchNormalizationNode setFlags:];
-[MPSCNNBatchNormalizationNode flags];
-[MPSCNNBatchNormalizationNode dealloc];
-[MPSCNNBatchNormalizationNode calculateStatistics];
-[MPSCNNBatchNormalizationNode gradientClass];
-[MPSCNNBatchNormalizationNode initWithSource:dataSource:];
-[MPSCNNBatchNormalizationNode newFilterNode];
-[MPSCNNBatchNormalizationNode resultStates];
-[MPSCNNBatchNormalizationNode setTrainingStyle:];
-[MPSCNNBatchNormalizationNode sourceStates];
-[MPSCNNBatchNormalizationNode trainingStyle];
```
