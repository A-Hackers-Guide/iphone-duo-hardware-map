# `_MLBatchDataSource`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ETDataProvider`
- 3 instance variables, 7 properties, 6 instance methods, 0 class methods

## Instance variables

```
B _useForPrediction;
@"<MLBatchProvider>" _batchProvider;
@"MLNeuralNetworkEngine" _nnEngine;
```

## Properties

```
@property (T@"<MLBatchProvider>",R,N,V_batchProvider) batchProvider;
@property (T@"MLNeuralNetworkEngine",R,N,V_nnEngine) nnEngine;
@property (TB,R,N,V_useForPrediction) useForPrediction;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MLBatchDataSource numberOfDataPoints];
-[_MLBatchDataSource dataPointAtIndex:error:];
-[_MLBatchDataSource batchProvider];
-[_MLBatchDataSource initWithMLBatchProvider:forPrediction:neuralNetworkEngine:error:];
-[_MLBatchDataSource nnEngine];
-[_MLBatchDataSource useForPrediction];
```
