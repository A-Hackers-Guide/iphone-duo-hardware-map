# `ULHomeSlamLearningHistoryStore`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULStore`
- Protocols: `ULStoreProtocol`
- 0 instance variables, 4 properties, 8 instance methods, 3 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ULHomeSlamLearningHistoryStore MOClass];
+[ULHomeSlamLearningHistoryStore defaultSortProperty];
+[ULHomeSlamLearningHistoryStore maxEntriesInTable];
```

## Instance methods

```
-[ULHomeSlamLearningHistoryStore _fetchWithPredicates:sortDescriptors:andLimit:];
-[ULHomeSlamLearningHistoryStore _predicateForLoiGroupId:];
-[ULHomeSlamLearningHistoryStore deleteRowsOlderThan:];
-[ULHomeSlamLearningHistoryStore fetchRowsAtLoiGroupId:fromTimestamp:excludingTimestamp:];
-[ULHomeSlamLearningHistoryStore fetchTwoMostRecentSuccessfulAtLoiGroupId:excludingTimestamp:];
-[ULHomeSlamLearningHistoryStore insertDataObject:atLoiUUID:];
-[ULHomeSlamLearningHistoryStore mostRecentSuccessfulTimestampAtLoiGroupId:excludingTimestamp:];
-[ULHomeSlamLearningHistoryStore oldestTimestampAtLoiGroupId:];
```
