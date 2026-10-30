# `LCFFeatureValue`

- Image: [`/System/Library/PrivateFrameworks/LighthouseCoreMLFeatureStore.framework/LighthouseCoreMLFeatureStore`](../userland/System__Library__PrivateFrameworks__LighthouseCoreMLFeatureStore.framework__LighthouseCoreMLFeatureStore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 8 properties, 17 instance methods, 0 class methods

## Instance variables

```
q _type;
@"NSNumber" _intValue;
@"NSNumber" _doubleValue;
@"NSString" _stringValue;
@"NSNumber" _boolValue;
@"NSNumber" _timeBucketValue;
@"NSArray" _doubleArray;
```

## Properties

```
@property (Tq,R,N,V_type) type;
@property (T@"NSString",R,N) valueInString;
@property (T@"NSNumber",R,N,V_intValue) intValue;
@property (T@"NSNumber",R,N,V_doubleValue) doubleValue;
@property (T@"NSString",R,N,V_stringValue) stringValue;
@property (T@"NSNumber",R,N,V_boolValue) boolValue;
@property (T@"NSNumber",R,N,V_timeBucketValue) timeBucketValue;
@property (T@"NSArray",R,N,V_doubleArray) doubleArray;
```

## Instance methods

```
-[LCFFeatureValue intValue];
-[LCFFeatureValue stringValue];
-[LCFFeatureValue boolValue];
-[LCFFeatureValue initEmpty];
-[LCFFeatureValue doubleValue];
-[LCFFeatureValue type];
-[LCFFeatureValue initWithBoolValue:];
-[LCFFeatureValue initWithIntValue:];
-[LCFFeatureValue initWithStringValue:];
-[LCFFeatureValue timeBucketValue];
-[LCFFeatureValue doubleArray];
-[LCFFeatureValue initWithDoubleArray:];
-[LCFFeatureValue initWithDoubleValue:];
-[LCFFeatureValue getTypeDBString];
-[LCFFeatureValue initWithTimeBucketValue:];
-[LCFFeatureValue isNullValue];
-[LCFFeatureValue valueInString];
```
