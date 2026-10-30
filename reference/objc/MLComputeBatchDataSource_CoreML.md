# `MLComputeBatchDataSource`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLComputeDataProvider`
- 4 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _useForPrediction;
@"<MLBatchProvider>" _batchProvider;
@"MLNeuralNetworkEngine" _nnEngine;
Q _batchSize;
```

## Properties

```
@property (T@"<MLBatchProvider>",R,N,V_batchProvider) batchProvider;
@property (T@"MLNeuralNetworkEngine",R,N,V_nnEngine) nnEngine;
@property (TB,R,N,V_useForPrediction) useForPrediction;
@property (TQ,N,V_batchSize) batchSize;
```

## Instance methods

```
-[MLComputeBatchDataSource batchSize];
-[MLComputeBatchDataSource setBatchSize:];
-[MLComputeBatchDataSource numberOfBatches];
-[MLComputeBatchDataSource batchAtIndex:error:];
-[MLComputeBatchDataSource batchProvider];
-[MLComputeBatchDataSource initWithBatchProvider:batchSize:forPrediction:neuralNetworkEngine:error:];
-[MLComputeBatchDataSource mlcDataSourceAtIndex:error:];
-[MLComputeBatchDataSource nnEngine];
-[MLComputeBatchDataSource sizeOfBatchAtIndex:];
-[MLComputeBatchDataSource useForPrediction];
```
