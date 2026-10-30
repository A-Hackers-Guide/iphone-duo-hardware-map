# `LCFELBatchProviderInfo`

- Image: [`/System/Library/PrivateFrameworks/LighthouseCoreMLFeatureStore.framework/LighthouseCoreMLFeatureStore`](../userland/System__Library__PrivateFrameworks__LighthouseCoreMLFeatureStore.framework__LighthouseCoreMLFeatureStore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 9 instance methods, 2 class methods

## Instance variables

```
@"NSUUID" _contextId;
@"NSUUID" _eventId;
@"NSString" _featureStoreKey;
@"NSNumber" _timeRange;
@"NSNumber" _featureCount;
@"NSDictionary" _totalFeatureStatistics;
@"NSArray" _positiveFeatureStatistics;
@"NSArray" _negativeFeatureStatistics;
```

## Properties

```
@property (T@"NSUUID",R,N,V_contextId) contextId;
@property (T@"NSUUID",R,N,V_eventId) eventId;
@property (T@"NSString",R,N,V_featureStoreKey) featureStoreKey;
@property (T@"NSNumber",R,N,V_timeRange) timeRange;
@property (T@"NSNumber",R,N,V_featureCount) featureCount;
@property (T@"NSDictionary",R,N,V_totalFeatureStatistics) totalFeatureStatistics;
@property (T@"NSArray",R,N,V_positiveFeatureStatistics) positiveFeatureStatistics;
@property (T@"NSArray",R,N,V_negativeFeatureStatistics) negativeFeatureStatistics;
```

## Class methods

```
+[LCFELBatchProviderInfo meanOf:];
+[LCFELBatchProviderInfo standardDeviationOf:];
```

## Instance methods

```
-[LCFELBatchProviderInfo contextId];
-[LCFELBatchProviderInfo timeRange];
-[LCFELBatchProviderInfo eventId];
-[LCFELBatchProviderInfo featureCount];
-[LCFELBatchProviderInfo featureStoreKey];
-[LCFELBatchProviderInfo init:labelFeatureName:];
-[LCFELBatchProviderInfo negativeFeatureStatistics];
-[LCFELBatchProviderInfo positiveFeatureStatistics];
-[LCFELBatchProviderInfo totalFeatureStatistics];
```
