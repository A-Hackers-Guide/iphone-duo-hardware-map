# `SFAnalyticsSQLiteStore`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SFSQLite`
- 0 instance variables, 8 properties, 29 instance methods, 1 class methods

## Properties

```
@property (T@"NSArray",R) hardFailures;
@property (T@"NSArray",R) softFailures;
@property (T@"NSArray",R) rockwells;
@property (T@"NSArray",R) allEvents;
@property (T@"NSArray",R) samples;
@property (T@"NSString",R) databaseBasename;
@property (T@"NSDate",&) uploadDate;
@property (T@"NSString",&) metricsAccountID;
```

## Class methods

```
+[SFAnalyticsSQLiteStore storeWithPath:schema:];
```

## Instance methods

```
-[SFAnalyticsSQLiteStore samples];
-[SFAnalyticsSQLiteStore enumerateEventsWithLimit:usingBlock:];
-[SFAnalyticsSQLiteStore addSample:forName:];
-[SFAnalyticsSQLiteStore summaryCounts];
-[SFAnalyticsSQLiteStore dealloc];
-[SFAnalyticsSQLiteStore allEvents];
-[SFAnalyticsSQLiteStore databaseBasename];
-[SFAnalyticsSQLiteStore addEventDict:toTable:timestampBucket:];
-[SFAnalyticsSQLiteStore tryToOpenDatabase];
-[SFAnalyticsSQLiteStore clearAllData];
-[SFAnalyticsSQLiteStore removeAllSamplesForName:];
-[SFAnalyticsSQLiteStore dataPropertyForKey:];
-[SFAnalyticsSQLiteStore uploadDate];
-[SFAnalyticsSQLiteStore softFailureCountForEventType:];
-[SFAnalyticsSQLiteStore rockwells];
-[SFAnalyticsSQLiteStore setUploadDate:];
-[SFAnalyticsSQLiteStore streamEventsWithLimit:fromTable:eventHandler:];
-[SFAnalyticsSQLiteStore softFailures];
-[SFAnalyticsSQLiteStore metricsAccountID];
-[SFAnalyticsSQLiteStore incrementSoftFailureCountForEventType:];
-[SFAnalyticsSQLiteStore addRockwellDict:userinfo:toTable:timestampBucket:];
-[SFAnalyticsSQLiteStore hardFailureCountForEventType:];
-[SFAnalyticsSQLiteStore incrementSuccessCountForEventType:];
-[SFAnalyticsSQLiteStore setDataProperty:forKey:];
-[SFAnalyticsSQLiteStore incrementHardFailureCountForEventType:];
-[SFAnalyticsSQLiteStore hardFailures];
-[SFAnalyticsSQLiteStore addEventDict:toTable:];
-[SFAnalyticsSQLiteStore setMetricsAccountID:];
-[SFAnalyticsSQLiteStore successCountForEventType:];
```
