# `WAAnalyticsAccess`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 3 properties, 18 instance methods, 2 class methods

## Instance variables

```
B readOnly;
@"NSPersistentContainer" _persistentContainer;
@"NSManagedObjectContext" _backgroundMOC;
Q _options;
```

## Properties

```
@property (T@"NSPersistentContainer",&,N,V_persistentContainer) persistentContainer;
@property (T@"NSManagedObjectContext",&,N,V_backgroundMOC) backgroundMOC;
@property (TQ,N,V_options) options;
```

## Class methods

```
+[WAAnalyticsAccess initialize];
+[WAAnalyticsAccess accessWithPersistentContainer:];
```

## Instance methods

```
-[WAAnalyticsAccess setOptions:];
-[WAAnalyticsAccess setPersistentContainer:];
-[WAAnalyticsAccess persistentStoreCoordinator];
-[WAAnalyticsAccess persistentContainer];
-[WAAnalyticsAccess backgroundMOC];
-[WAAnalyticsAccess setBackgroundMOC:];
-[WAAnalyticsAccess options];
-[WAAnalyticsAccess canWrite];
-[WAAnalyticsAccess mainObjectContext];
-[WAAnalyticsAccess _countForFetchRequest:error:onMoc:];
-[WAAnalyticsAccess _countForFetchRequestWithBlockAndWait:error:onMoc:];
-[WAAnalyticsAccess _performFetch:error:onMoc:];
-[WAAnalyticsAccess _performFetchWithBlockAndWait:error:onMoc:];
-[WAAnalyticsAccess countForFetchRequestWithBlockAndWait:error:];
-[WAAnalyticsAccess countForFetchRequestWithBlockAndWaitOnBbMoc:error:];
-[WAAnalyticsAccess initWithOptions:andContainer:];
-[WAAnalyticsAccess performFetchWithBlockAndWait:error:];
-[WAAnalyticsAccess performFetchWithBlockAndWaitOnBbMoc:error:];
```
