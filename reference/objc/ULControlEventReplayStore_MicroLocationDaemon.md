# `ULControlEventReplayStore`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULStore`
- Protocols: `_TtP19MicroLocationDaemon41ULControlEventReplayLoggerDatabaseService_`, `ULStoreProtocol`
- 0 instance variables, 8 properties, 10 instance methods, 3 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ULControlEventReplayStore MOClass];
+[ULControlEventReplayStore defaultSortProperty];
+[ULControlEventReplayStore maxEntriesInTable];
```

## Instance methods

```
-[ULControlEventReplayStore insertDataObjects:];
-[ULControlEventReplayStore _fetchControlEventsByAndPredicates:sortDescriptors:andLimit:];
-[ULControlEventReplayStore efficientlyFetchControlEventsByType:LOIGroupUUIDs:startDate:endDate:fetchLimit:newest:ascending:];
-[ULControlEventReplayStore fetchControlEventsByType:fromTime:toTime:limit:];
-[ULControlEventReplayStore fetchControlEventsFromTime:toTime:limit:];
-[ULControlEventReplayStore fetchMostRecentControlEventBeforeTime:];
-[ULControlEventReplayStore insertDataObjects:atLoiUUID:];
-[ULControlEventReplayStore insertEventType:timestamp:];
-[ULControlEventReplayStore insertEventType:timestamp:atLoiUUID:];
-[ULControlEventReplayStore isStoreReady];
```
