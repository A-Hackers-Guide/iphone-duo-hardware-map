# `AVDateRangeMetadataGroup`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetadataGroup`
- Protocols: `NSCopying`, `NSMutableCopying`
- 1 instance variables, 7 properties, 22 instance methods, 2 class methods

## Instance variables

```
@"AVDateRangeMetadataGroupInternal" _priv;
```

## Properties

```
@property (T@"NSString",R,N) cueingOptions;
@property (T@"NSDate",R,N) discoveryTimestamp;
@property (T@"NSDate",R,N) modificationTimestamp;
@property (T@"AVDateRangeMetadataGroupInternal",R,N,G_dateRangeMetadataGroupInternal) dateRangeMetadataGroupInternal;
@property (T@"NSDate",R,C,N) startDate;
@property (T@"NSDate",R,C,N) endDate;
@property (T@"NSArray",R,C,N) items;
```

## Class methods

```
+[AVDateRangeMetadataGroup _figMetadataArrayForMetadataItems:];
+[AVDateRangeMetadataGroup _metadataItemsForFigMetadataArray:];
```

## Instance methods

```
-[AVDateRangeMetadataGroup initWithPropertyList:];
-[AVDateRangeMetadataGroup startDate];
-[AVDateRangeMetadataGroup mutableCopyWithZone:];
-[AVDateRangeMetadataGroup propertyList];
-[AVDateRangeMetadataGroup init];
-[AVDateRangeMetadataGroup dealloc];
-[AVDateRangeMetadataGroup endDate];
-[AVDateRangeMetadataGroup items];
-[AVDateRangeMetadataGroup uniqueID];
-[AVDateRangeMetadataGroup modificationTimestamp];
-[AVDateRangeMetadataGroup hash];
-[AVDateRangeMetadataGroup description];
-[AVDateRangeMetadataGroup copyWithZone:];
-[AVDateRangeMetadataGroup isEqual:];
-[AVDateRangeMetadataGroup _dateRangeMetadataGroupInternal];
-[AVDateRangeMetadataGroup _extractPropertiesFromTaggedRangeMetadataDictionary:];
-[AVDateRangeMetadataGroup _initWithTaggedRangeMetadataDictionary:items:];
-[AVDateRangeMetadataGroup _taggedRangeMetadataDictionary];
-[AVDateRangeMetadataGroup classifyingLabel];
-[AVDateRangeMetadataGroup cueingOptions];
-[AVDateRangeMetadataGroup discoveryTimestamp];
-[AVDateRangeMetadataGroup initWithItems:startDate:endDate:];
```
