# `ULAnalyticEventStore`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULStore`
- Protocols: `ULStoreProtocol`
- 0 instance variables, 4 properties, 10 instance methods, 3 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ULAnalyticEventStore MOClass];
+[ULAnalyticEventStore defaultSortProperty];
+[ULAnalyticEventStore maxEntriesInTable];
```

## Instance methods

```
-[ULAnalyticEventStore fetchAllRecordsWithLimit:];
-[ULAnalyticEventStore insertDataObjects:];
-[ULAnalyticEventStore fetchFirstEvent];
-[ULAnalyticEventStore _fetchAnalyticEventsByAndPredicates:sortDescriptors:andLimit:];
-[ULAnalyticEventStore countEventsOfType:forLoiGroupUUID:fromTimestamp:toTimestamp:];
-[ULAnalyticEventStore fetchAnalyticEventsASCFromTime:toTime:];
-[ULAnalyticEventStore fetchEventsOfTypes:forLoiGroupUUID:fromTimestamp:toTimestamp:];
-[ULAnalyticEventStore fetchLatestAnalyticEventType:beforeTime:];
-[ULAnalyticEventStore hasAnyEventsOfTypes:];
-[ULAnalyticEventStore insertDataObjects:atLoiUUID:];
```
