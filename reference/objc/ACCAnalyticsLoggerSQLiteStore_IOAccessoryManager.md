# `ACCAnalyticsLoggerSQLiteStore`

- Image: [`/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager`](../userland/System__Library__CoreAccessories__PlugIns__Transports__IOAccessoryManager.transport__IOAccessoryManager.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ACCSQLite`
- 0 instance variables, 2 properties, 12 instance methods, 1 class methods

## Properties

```
@property (T@"NSArray",R) allEvents;
@property (T@"NSDate",&) uploadDate;
```

## Class methods

```
+[ACCAnalyticsLoggerSQLiteStore storeWithPath:schema:];
```

## Instance methods

```
-[ACCAnalyticsLoggerSQLiteStore summaryCounts];
-[ACCAnalyticsLoggerSQLiteStore successCount];
-[ACCAnalyticsLoggerSQLiteStore dealloc];
-[ACCAnalyticsLoggerSQLiteStore allEvents];
-[ACCAnalyticsLoggerSQLiteStore tryToOpenDatabase];
-[ACCAnalyticsLoggerSQLiteStore clearAllData];
-[ACCAnalyticsLoggerSQLiteStore uploadDate];
-[ACCAnalyticsLoggerSQLiteStore setUploadDate:];
-[ACCAnalyticsLoggerSQLiteStore addEventDict:toTable:];
-[ACCAnalyticsLoggerSQLiteStore incrementSuccessCount];
-[ACCAnalyticsLoggerSQLiteStore incrementWrapFailureCount];
-[ACCAnalyticsLoggerSQLiteStore wrapFailureCount];
```
