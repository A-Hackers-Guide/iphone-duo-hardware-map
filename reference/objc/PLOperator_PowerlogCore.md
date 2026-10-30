# `PLOperator`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 10 properties, 49 instance methods, 26 class methods

## Instance variables

```
@"NSMutableDictionary" _filterDefinitions;
@"NSMutableDictionary" _filterDeltaLastEntryIDs;
@"NSMutableArray" _bufferedEntries;
@"PLTimer" _triggerBufferFlush;
@"NSMutableDictionary" _lastLogDateForEntryKey;
```

## Properties

```
@property (T@"NSMutableDictionary",&,V_filterDefinitions) filterDefinitions;
@property (T@"NSMutableDictionary",&,V_filterDeltaLastEntryIDs) filterDeltaLastEntryIDs;
@property (T@"NSMutableArray",&,V_bufferedEntries) bufferedEntries;
@property (T@"PLTimer",&,V_triggerBufferFlush) triggerBufferFlush;
@property (T@"NSMutableDictionary",&,V_lastLogDateForEntryKey) lastLogDateForEntryKey;
@property (T@"NSObject<OS_dispatch_queue>",R,W) workQueue;
@property (T@"NSObject<OS_dispatch_queue>",R,W) storageQueue;
@property (T@"PLCoreStorage",R,W) storage;
@property (T@"NSString",R,W) className;
@property (T@"NSString",R,W) storageQueueName;
```

## Class methods

```
+[PLOperator entryEventIntervalDefinitions];
+[PLOperator entryEventPointDefinitions];
+[PLOperator entryEventForwardDefinitions];
+[PLOperator entryEventBackwardDefinitions];
+[PLOperator entryEventNoneDefinitions];
+[PLOperator load];
+[PLOperator defaults];
+[PLOperator className];
+[PLOperator accountingGroupDefinitions];
+[PLOperator railDefinitions];
+[PLOperator isEnabled];
+[PLOperator fullMode];
+[PLOperator operator];
+[PLOperator setEnabled:];
+[PLOperator entryAggregateDefinitions];
+[PLOperator entryKeys];
+[PLOperator isDebugEnabled];
+[PLOperator createEntriesForMetrics:withData:withDate:];
+[PLOperator dddOverrideDateInPayload:subsystem:category:];
+[PLOperator entryDefinitions];
+[PLOperator entryKeyForType:andName:];
+[PLOperator entryKeyForType:andName:isDynamic:];
+[PLOperator isDebugEnabledForKey:];
+[PLOperator storageQueueName];
+[PLOperator trimConditionsWithEntryKey:withTrimDate:withCount:withStartDateKey:];
+[PLOperator trimConditionsWithEntryKey:withTrimDate:withDuration:withStartDateKey:];
```

## Instance methods

```
-[PLOperator className];
-[PLOperator storageQueue];
-[PLOperator init];
-[PLOperator workQueue];
-[PLOperator dealloc];
-[PLOperator initOperatorDependancies];
-[PLOperator storage];
-[PLOperator logEntries:withGroupID:];
-[PLOperator flushBuffer];
-[PLOperator initTaskOperatorDependancies];
-[PLOperator logEntry:];
-[PLOperator log];
-[PLOperator updateEntry:withBlock:];
-[PLOperator trimConditionsForEntryKey:forTrimDate:];
-[PLOperator entryKeys];
-[PLOperator isDebugEnabled];
-[PLOperator initForTest];
-[PLOperator bufferedEntries];
-[PLOperator defaultBoolForKey:];
-[PLOperator defaultDoubleForKey:];
-[PLOperator defaultLongForKey:];
-[PLOperator defaultObjectForKey:];
-[PLOperator enableBufferFlushTimer:];
-[PLOperator entryDefinitions];
-[PLOperator filterDefinitions];
-[PLOperator filterDeltaLastEntryIDs];
-[PLOperator isDebugEnabledForKey:];
-[PLOperator lastLogDateForEntryKey];
-[PLOperator logDMAEntry:];
-[PLOperator logForSubsystem:category:data:];
-[PLOperator logForSubsystem:category:data:date:];
-[PLOperator logFromCFCallback:];
-[PLOperator logProportionateAggregateEntry:withStartDate:withEndDate:];
-[PLOperator logRequestNotification:];
-[PLOperator postEntries:];
-[PLOperator postEntries:withGroupID:];
-[PLOperator postFilteredNotificationForEntry:withFilteredDefition:withNotificationName:];
-[PLOperator setBufferedEntries:];
-[PLOperator setFilterDefinitions:];
-[PLOperator setFilterDeltaLastEntryIDs:];
-[PLOperator setLastLogDateForEntryKey:];
-[PLOperator setTriggerBufferFlush:];
-[PLOperator setupFilterRequest:];
-[PLOperator shouldWriteEntry:withDebug:];
-[PLOperator storageQueueName];
-[PLOperator subscribeNotificationsForEntries];
-[PLOperator tablesToTrimConditionsForTrimDate:];
-[PLOperator timeIntervalSinceLastLogForEntryKey:];
-[PLOperator triggerBufferFlush];
```
