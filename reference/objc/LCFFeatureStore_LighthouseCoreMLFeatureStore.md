# `LCFFeatureStore`

- Image: [`/System/Library/PrivateFrameworks/LighthouseCoreMLFeatureStore.framework/LighthouseCoreMLFeatureStore`](../userland/System__Library__PrivateFrameworks__LighthouseCoreMLFeatureStore.framework__LighthouseCoreMLFeatureStore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _useSqlite;
@"NSString" _featureStoreKey;
@"LCFBiomeManager" _biomeManagerLabeledDataStore;
@"LCFDatabaseConnection" _dbFeatureStore;
```

## Properties

```
@property (T@"LCFBiomeManager",R,N,V_biomeManagerLabeledDataStore) biomeManagerLabeledDataStore;
@property (T@"LCFDatabaseConnection",R,N,V_dbFeatureStore) dbFeatureStore;
@property (TB,R,N,V_useSqlite) useSqlite;
@property (T@"NSString",R,N,V_featureStoreKey) featureStoreKey;
```

## Instance methods

```
-[LCFFeatureStore init:url:useSqlite:];
-[LCFFeatureStore featureStoreKey];
-[LCFFeatureStore getFeatureVector:atTime:option:];
-[LCFFeatureStore biomeManagerLabeledDataStore];
-[LCFFeatureStore dbFeatureStore];
-[LCFFeatureStore featureProviderFromfeatureSet:featureNames:];
-[LCFFeatureStore getFeatureSets:startDate:endDate:option:];
-[LCFFeatureStore getFeatureVector:option:];
-[LCFFeatureStore getFeatureVectorTimestamps];
-[LCFFeatureStore getFeatureVectorWithStoreEvents:storeEventsInReversedOrder:option:];
-[LCFFeatureStore getFeatureVectors:option:];
-[LCFFeatureStore getFeatureVectors:startDate:endDate:option:];
-[LCFFeatureStore getMultiArrayFeatureVectors:vectorName:srcLabelName:destLabelName:option:];
-[LCFFeatureStore getMultiArrayFeatureVectors:vectorName:srcLabelName:destLabelName:startDate:endDate:option:];
-[LCFFeatureStore pruneFrom:endDate:option:];
-[LCFFeatureStore updateFeatureSet:];
-[LCFFeatureStore updateFeatureSet:featureVestion:featureValues:];
-[LCFFeatureStore useSqlite];
```
