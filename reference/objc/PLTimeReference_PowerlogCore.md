# `PLTimeReference`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 20 instance methods, 2 class methods

## Instance variables

```
d _offset;
@"<PLTimeReferenceManager>" _timeManager;
q _timeReferenceType;
@"NSString" _entryDefinitionKey;
d _hourBucketOffset;
```

## Properties

```
@property (Td,N,V_hourBucketOffset) hourBucketOffset;
@property (Td,N,V_offset) offset;
@property (T@"<PLTimeReferenceManager>",&,V_timeManager) timeManager;
@property (Tq,V_timeReferenceType) timeReferenceType;
@property (T@"NSString",&,V_entryDefinitionKey) entryDefinitionKey;
```

## Class methods

```
+[PLTimeReference defaultsKeyFromEntryDefinitionKey:];
+[PLTimeReference hourBucketOffsetKeyFromEntryDefinitionKey:];
```

## Instance methods

```
-[PLTimeReference registerForDayChangedNotification];
-[PLTimeReference currentTime];
-[PLTimeReference registerForTimeZoneChangedNotification];
-[PLTimeReference initWithTimeManager:entryDefinitionKey:timeReferenceType:];
-[PLTimeReference setOffset:];
-[PLTimeReference offset];
-[PLTimeReference setTimeManager:];
-[PLTimeReference addTimeOffsetToMonotonicTime:];
-[PLTimeReference computeHourBucketOffset];
-[PLTimeReference entryDefinitionKey];
-[PLTimeReference getHourBucketOffset];
-[PLTimeReference hourBucketOffset];
-[PLTimeReference initializeOffsetWithEntries:];
-[PLTimeReference removeTimeOffsetFromReferenceTime:];
-[PLTimeReference setEntryDefinitionKey:];
-[PLTimeReference setHourBucketOffset:];
-[PLTimeReference setTimeReferenceType:];
-[PLTimeReference timeManager];
-[PLTimeReference timeReferenceType];
-[PLTimeReference writeOffsetToDefaults];
```
