# `MPSCNNGroupNormalization`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNKernel`
- 6 instance variables, 2 properties, 16 instance methods, 1 class methods

## Instance variables

```
^v _gamma;
^v _beta;
@"<MPSCNNGroupNormalizationDataSource>" _dataSource;
Q _numberOfFeatureChannels;
Q _numberOfGroups;
f _epsilon;
```

## Properties

```
@property (Tf,N,V_epsilon) epsilon;
@property (T@"<MPSCNNGroupNormalizationDataSource>",R,&,N,V_dataSource) dataSource;
```

## Class methods

```
+[MPSCNNGroupNormalization libraryInfo:];
```

## Instance methods

```
-[MPSCNNGroupNormalization debugDescription];
-[MPSCNNGroupNormalization maxBatchSize];
-[MPSCNNGroupNormalization dealloc];
-[MPSCNNGroupNormalization resultStateForSourceImage:sourceStates:destinationImage:];
-[MPSCNNGroupNormalization dataSource];
-[MPSCNNGroupNormalization copyWithZone:device:];
-[MPSCNNGroupNormalization initWithCoder:device:];
-[MPSCNNGroupNormalization temporaryResultStateForCommandBuffer:sourceImage:sourceStates:destinationImage:];
-[MPSCNNGroupNormalization encodeWithCoder:];
-[MPSCNNGroupNormalization setEpsilon:];
-[MPSCNNGroupNormalization epsilon];
-[MPSCNNGroupNormalization initWithDevice:dataSource:];
-[MPSCNNGroupNormalization reloadDataSource:];
-[MPSCNNGroupNormalization reloadDataSourceDeprecated:];
-[MPSCNNGroupNormalization reloadGammaAndBetaFromDataSource];
-[MPSCNNGroupNormalization reloadGammaAndBetaWithCommandBuffer:gammaAndBetaState:];
```
