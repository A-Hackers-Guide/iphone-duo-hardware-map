# `PLTimeManager`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PLTimeReferenceManager`
- 4 instance variables, 8 properties, 24 instance methods, 1 class methods

## Instance variables

```
@"PLStorageOperator" _storageOperator;
@"PLSQLiteConnection" _connection;
@"NSDictionary" _timeReferences;
@"NSDictionary" _notificationsToTimeReferences;
```

## Properties

```
@property (T@"PLSQLiteConnection",W,V_connection) connection;
@property (T@"NSDictionary",&,V_timeReferences) timeReferences;
@property (T@"NSDictionary",&,V_notificationsToTimeReferences) notificationsToTimeReferences;
@property (T@"PLStorageOperator",W,V_storageOperator) storageOperator;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PLTimeManager sharedInstance];
```

## Instance methods

```
-[PLTimeManager storageQueue];
-[PLTimeManager init];
-[PLTimeManager connection];
-[PLTimeManager setConnection:];
-[PLTimeManager setStorageOperator:];
-[PLTimeManager storageOperator];
-[PLTimeManager getBootSessionUUID];
-[PLTimeManager bucketNSDate:withBucketInterval:];
-[PLTimeManager bucketTimeStampForDate:withTimeReference:withBucketInterval:];
-[PLTimeManager convertTime:fromTimeReference:toTimeReference:];
-[PLTimeManager currentTimeFromTimeReference:toTimeReference:];
-[PLTimeManager hourBucketBaseSnapOffsetWithMonotonicTime:];
-[PLTimeManager hourBucketBaseSnapOffsetWithMonotonicTimeNow:];
-[PLTimeManager initialMonotonicTime];
-[PLTimeManager initializeTimeOffsets];
-[PLTimeManager logTimeEntry];
-[PLTimeManager notificationsToTimeReferences];
-[PLTimeManager registerForTimeChangedCallbackWithIdentifier:forTimeReference:usingBlock:];
-[PLTimeManager setNotificationsToTimeReferences:];
-[PLTimeManager setTimeReferences:];
-[PLTimeManager timeOffsetForTimeReference:];
-[PLTimeManager timeReferences];
-[PLTimeManager timeZoneHourBucketShift:];
-[PLTimeManager unregisterForTimeChangedCallbackWithIdentifier:forTimeReference:];
```
