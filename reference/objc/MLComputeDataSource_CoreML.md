# `MLComputeDataSource`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" _dataDictionary;
```

## Properties

```
@property (T@"NSDictionary",R,N,V_dataDictionary) dataDictionary;
```

## Instance methods

```
-[MLComputeDataSource dataCHWFromChanneledPixelType:channelOrderIsBGR:error:];
-[MLComputeDataSource dataCHWFromPixelBuffer:channelOrderIsBGR:error:];
-[MLComputeDataSource dataCHWFromPixelTypeGray8:error:];
-[MLComputeDataSource dataDictionary];
-[MLComputeDataSource initWithFeatureProvider:forPrediction:neuralNetworkEngine:error:];
-[MLComputeDataSource oneHotEncodedDataFromFeatureValue:withNNEngine:error:];
```
