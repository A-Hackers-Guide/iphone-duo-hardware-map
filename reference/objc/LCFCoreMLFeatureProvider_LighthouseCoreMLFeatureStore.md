# `LCFCoreMLFeatureProvider`

- Image: [`/System/Library/PrivateFrameworks/LighthouseCoreMLFeatureStore.framework/LighthouseCoreMLFeatureStore`](../userland/System__Library__PrivateFrameworks__LighthouseCoreMLFeatureStore.framework__LighthouseCoreMLFeatureStore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLFeatureProvider`
- 4 instance variables, 4 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSString" _featureStoreKey;
@"NSDate" _timestamp;
@"NSDictionary" _featureValues;
@"NSSet" _featureNames;
```

## Properties

```
@property (T@"NSString",R,N,V_featureStoreKey) featureStoreKey;
@property (T@"NSDate",R,N,V_timestamp) timestamp;
@property (T@"NSDictionary",R,N,V_featureValues) featureValues;
@property (T@"NSSet",R,N,V_featureNames) featureNames;
```

## Class methods

```
+[LCFCoreMLFeatureProvider fromMLProvider:];
```

## Instance methods

```
-[LCFCoreMLFeatureProvider timestamp];
-[LCFCoreMLFeatureProvider featureNames];
-[LCFCoreMLFeatureProvider featureValueForName:];
-[LCFCoreMLFeatureProvider featureValues];
-[LCFCoreMLFeatureProvider featureStoreKey];
-[LCFCoreMLFeatureProvider init:timestamp:featureValues:];
```
