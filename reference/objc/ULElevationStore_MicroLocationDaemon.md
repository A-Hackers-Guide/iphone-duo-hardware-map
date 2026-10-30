# `ULElevationStore`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULStore`
- Protocols: `ULStoreProtocol`
- 0 instance variables, 4 properties, 5 instance methods, 3 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ULElevationStore MOClass];
+[ULElevationStore defaultSortProperty];
+[ULElevationStore maxEntriesInTable];
```

## Instance methods

```
-[ULElevationStore insertDataObjects:];
-[ULElevationStore _fetchElevationEntriesByAndPredicates:sortDescriptors:andLimit:];
-[ULElevationStore deleteElevationEntriesBetweenStartTime:andEndTime:];
-[ULElevationStore fetchElevationEntriesFromTime:toTime:limit:];
-[ULElevationStore fetchMostRecentElevationEntriesBeforeTime:limit:];
```
