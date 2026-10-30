# `_MLDataSource`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ETDataProvider`
- 1 instance variables, 5 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" _dataTensorDictionary;
```

## Properties

```
@property (T@"NSDictionary",&,N,V_dataTensorDictionary) dataTensorDictionary;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MLDataSource numberOfDataPoints];
-[_MLDataSource dataPointAtIndex:error:];
-[_MLDataSource dataTensorDictionary];
-[_MLDataSource initWithMLFeatureProvider:forPrediction:neuralNetworkEngine:error:];
-[_MLDataSource setDataTensorDictionary:];
```
