# `MLStreamingInputDataSource`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLComputeDataProvider`
- 2 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
Q _batchSize;
@"NSMutableArray" _dataSources;
```

## Properties

```
@property (TQ,N,V_batchSize) batchSize;
@property (T@"NSMutableArray",&,N,V_dataSources) dataSources;
```

## Instance methods

```
-[MLStreamingInputDataSource batchSize];
-[MLStreamingInputDataSource setBatchSize:];
-[MLStreamingInputDataSource dataSources];
-[MLStreamingInputDataSource setDataSources:];
-[MLStreamingInputDataSource numberOfBatches];
-[MLStreamingInputDataSource appendBatchedTensors:numberOfTensors:];
-[MLStreamingInputDataSource batchAtIndex:error:];
-[MLStreamingInputDataSource initWithBatchSize:];
-[MLStreamingInputDataSource sizeOfBatchAtIndex:];
```
