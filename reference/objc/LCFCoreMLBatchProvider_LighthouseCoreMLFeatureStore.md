# `LCFCoreMLBatchProvider`

- Image: [`/System/Library/PrivateFrameworks/LighthouseCoreMLFeatureStore.framework/LighthouseCoreMLFeatureStore`](../userland/System__Library__PrivateFrameworks__LighthouseCoreMLFeatureStore.framework__LighthouseCoreMLFeatureStore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLBatchProvider`
- 5 instance variables, 5 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSString" _featureStoreKey;
@"NSDate" _timeFirst;
@"NSDate" _timeLast;
q _count;
@"NSArray" _featureProviders;
```

## Properties

```
@property (T@"NSString",R,N,V_featureStoreKey) featureStoreKey;
@property (T@"NSDate",R,N,V_timeFirst) timeFirst;
@property (T@"NSDate",R,N,V_timeLast) timeLast;
@property (Tq,R,N,V_count) count;
@property (T@"NSArray",R,N,V_featureProviders) featureProviders;
```

## Class methods

```
+[LCFCoreMLBatchProvider fromMLProvider:];
```

## Instance methods

```
-[LCFCoreMLBatchProvider count];
-[LCFCoreMLBatchProvider featureProviders];
-[LCFCoreMLBatchProvider featuresAtIndex:];
-[LCFCoreMLBatchProvider featureStoreKey];
-[LCFCoreMLBatchProvider init:featureProviders:];
-[LCFCoreMLBatchProvider timeFirst];
-[LCFCoreMLBatchProvider timeLast];
```
