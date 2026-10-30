# `CAFRange`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAFCacheableDescription`
- 2 instance variables, 19 properties, 23 instance methods, 3 class methods

## Instance variables

```
@"CAFCharacteristicMetadata" _metaData;
@"CAFCachedDescription" _cachedDescription;
```

## Properties

```
@property (T@"CAFFloatRange",R,N) floatRange;
@property (T@"CAFInt8Range",R,N) int8Range;
@property (T@"CAFInt16Range",R,N) int16Range;
@property (T@"CAFInt32Range",R,N) int32Range;
@property (T@"CAFInt64Range",R,N) int64Range;
@property (T@"CAFUInt8Range",R,N) uInt8Range;
@property (T@"CAFUInt16Range",R,N) uInt16Range;
@property (T@"CAFUInt32Range",R,N) uInt32Range;
@property (T@"CAFUInt64Range",R,N) uInt64Range;
@property (T@"CAFCharacteristicMetadata",R,N,V_metaData) metaData;
@property (T@"CAFCachedDescription",&,N,V_cachedDescription) cachedDescription;
@property (T@"NSNumber",R,N) minimum;
@property (T@"NSNumber",R,N) maximum;
@property (T@"NSNumber",R,N) step;
@property (T@"NSArray",R,N) validValues;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAFRange step];
+[CAFRange minimum];
+[CAFRange maximum];
```

## Instance methods

```
-[CAFRange step];
-[CAFRange cachedDescription];
-[CAFRange minimum];
-[CAFRange maximum];
-[CAFRange metaData];
-[CAFRange setCachedDescription:];
-[CAFRange description];
-[CAFRange validValues];
-[CAFRange valueRoundedToNearestStepValue:];
-[CAFRange floatRange];
-[CAFRange limitedToRange:];
-[CAFRange currentDescriptionForCache:];
-[CAFRange initWithMetaData:];
-[CAFRange int16Range];
-[CAFRange int32Range];
-[CAFRange int64Range];
-[CAFRange int8Range];
-[CAFRange isInRange:];
-[CAFRange measurementRangeWithUnit:];
-[CAFRange uInt16Range];
-[CAFRange uInt32Range];
-[CAFRange uInt64Range];
-[CAFRange uInt8Range];
```
