# `MPSCNNInstanceNormalization`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNKernel`
- 5 instance variables, 2 properties, 16 instance methods, 1 class methods

## Instance variables

```
^v _gamma;
^v _beta;
@"<MPSCNNInstanceNormalizationDataSource>" _dataSource;
Q _numberOfFeatureChannels;
f _epsilon;
```

## Properties

```
@property (Tf,N,V_epsilon) epsilon;
@property (T@"<MPSCNNInstanceNormalizationDataSource>",R,&,N,V_dataSource) dataSource;
```

## Class methods

```
+[MPSCNNInstanceNormalization libraryInfo:];
```

## Instance methods

```
-[MPSCNNInstanceNormalization debugDescription];
-[MPSCNNInstanceNormalization maxBatchSize];
-[MPSCNNInstanceNormalization dealloc];
-[MPSCNNInstanceNormalization resultStateForSourceImage:sourceStates:destinationImage:];
-[MPSCNNInstanceNormalization dataSource];
-[MPSCNNInstanceNormalization copyWithZone:device:];
-[MPSCNNInstanceNormalization initWithCoder:device:];
-[MPSCNNInstanceNormalization temporaryResultStateForCommandBuffer:sourceImage:sourceStates:destinationImage:];
-[MPSCNNInstanceNormalization encodeWithCoder:];
-[MPSCNNInstanceNormalization setEpsilon:];
-[MPSCNNInstanceNormalization epsilon];
-[MPSCNNInstanceNormalization initWithDevice:dataSource:];
-[MPSCNNInstanceNormalization reloadDataSource:];
-[MPSCNNInstanceNormalization reloadDataSourceDeprecated:];
-[MPSCNNInstanceNormalization reloadGammaAndBetaFromDataSource];
-[MPSCNNInstanceNormalization reloadGammaAndBetaWithCommandBuffer:gammaAndBetaState:];
```
