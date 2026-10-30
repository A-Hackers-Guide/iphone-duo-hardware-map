# `PLProcessNetworkAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 15 instance variables, 15 properties, 56 instance methods, 14 class methods

## Instance variables

```
^{__NStatManager=} _statManagerRef;
@"UsageFeed" _usageFeed;
@"PLEntryNotificationOperatorComposition" _batteryLevelChanged;
@"PLEntryNotificationOperatorComposition" _batteryLevelChangedListenerForNetworkBitmap;
@"PLMonotonicTimer" _logUsageTimer;
@"NSDictionary" _lastProcessNameToNetworkUsageEntry;
@"NSDate" _lastEntryDate;
@"NSMutableSet" _processes;
Q _lastNetworkBitmapTimestamp;
Q _curNetworkBitmapTimestampForSysdiagnoseTrigger;
@"PLCFNotificationOperatorComposition" _flushNetworkBitmapsListener;
@"PLNSNotificationOperatorComposition" _sysdiagnoseListener;
@"PLXPCListenerOperatorComposition" _highBWStartListener;
@"PLXPCListenerOperatorComposition" _highBWEndlistener;
@"NSObject<OS_os_transaction>" _transaction;
```

## Properties

```
@property (T^{__NStatManager=},V_statManagerRef) statManagerRef;
@property (T@"UsageFeed",&,V_usageFeed) usageFeed;
@property (T@"PLEntryNotificationOperatorComposition",&,V_batteryLevelChanged) batteryLevelChanged;
@property (T@"PLEntryNotificationOperatorComposition",&,V_batteryLevelChangedListenerForNetworkBitmap) batteryLevelChangedListenerForNetworkBitmap;
@property (T@"PLMonotonicTimer",&,V_logUsageTimer) logUsageTimer;
@property (T@"NSDictionary",&,V_lastProcessNameToNetworkUsageEntry) lastProcessNameToNetworkUsageEntry;
@property (T@"NSDate",&,V_lastEntryDate) lastEntryDate;
@property (T@"NSMutableSet",&,V_processes) processes;
@property (TQ,V_lastNetworkBitmapTimestamp) lastNetworkBitmapTimestamp;
@property (TQ,V_curNetworkBitmapTimestampForSysdiagnoseTrigger) curNetworkBitmapTimestampForSysdiagnoseTrigger;
@property (T@"PLCFNotificationOperatorComposition",&,V_flushNetworkBitmapsListener) flushNetworkBitmapsListener;
@property (T@"PLNSNotificationOperatorComposition",&,V_sysdiagnoseListener) sysdiagnoseListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_highBWStartListener) highBWStartListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_highBWEndlistener) highBWEndlistener;
@property (T@"NSObject<OS_os_transaction>",&,V_transaction) transaction;
```

## Class methods

```
+[PLProcessNetworkAgent entryEventIntervalDefinitions];
+[PLProcessNetworkAgent entryEventPointDefinitions];
+[PLProcessNetworkAgent entryEventForwardDefinitions];
+[PLProcessNetworkAgent entryEventBackwardDefinitions];
+[PLProcessNetworkAgent entryEventNoneDefinitions];
+[PLProcessNetworkAgent load];
+[PLProcessNetworkAgent isEnabled];
+[PLProcessNetworkAgent entryEventBackwardDefinitionNetworkBitmap];
+[PLProcessNetworkAgent entryEventBackwardDefinitionUsage];
+[PLProcessNetworkAgent entryEventForwardDefinitionHighCellularBWTransactions];
+[PLProcessNetworkAgent entryEventForwardDefinitionHighCellularBWTransactionsDetail];
+[PLProcessNetworkAgent entryEventForwardDefinitionLowInternet];
+[PLProcessNetworkAgent entryEventIntervalDefinitionUsage];
+[PLProcessNetworkAgent entryEventPointDefinitionConnection];
```

## Instance methods

```
-[PLProcessNetworkAgent setTransaction:];
-[PLProcessNetworkAgent processes];
-[PLProcessNetworkAgent transaction];
-[PLProcessNetworkAgent init];
-[PLProcessNetworkAgent initOperatorDependancies];
-[PLProcessNetworkAgent lastEntryDate];
-[PLProcessNetworkAgent setBatteryLevelChanged:];
-[PLProcessNetworkAgent log];
-[PLProcessNetworkAgent setProcesses:];
-[PLProcessNetworkAgent batteryLevelChanged];
-[PLProcessNetworkAgent setLastEntryDate:];
-[PLProcessNetworkAgent setFlushNetworkBitmapsListener:];
-[PLProcessNetworkAgent accountWithNetworkUsageDiffEntries:withStartDate:withEndDate:];
-[PLProcessNetworkAgent addSource:toPID:];
-[PLProcessNetworkAgent aggregateAndLogNetworkBitmaps:withStartTime:andEndTime:];
-[PLProcessNetworkAgent batteryLevelChangedListenerForNetworkBitmap];
-[PLProcessNetworkAgent compressNetworkBitmap:];
-[PLProcessNetworkAgent curNetworkBitmapTimestampForSysdiagnoseTrigger];
-[PLProcessNetworkAgent didAddNewSource:];
-[PLProcessNetworkAgent didRemoveSource:];
-[PLProcessNetworkAgent didSetCountsBlock:withCounts:];
-[PLProcessNetworkAgent didSetDescriptionBlock:withDescription:];
-[PLProcessNetworkAgent flushNetworkBitmapsListener];
-[PLProcessNetworkAgent getNetWorkBitmapForEndTime:andSysdiagnoseTrigger:];
-[PLProcessNetworkAgent handleHighBWEndCallback:];
-[PLProcessNetworkAgent handleHighBWStartCallback:];
-[PLProcessNetworkAgent hasSymptomsLogging];
-[PLProcessNetworkAgent highBWEndlistener];
-[PLProcessNetworkAgent highBWStartListener];
-[PLProcessNetworkAgent lastNetworkBitmapTimestamp];
-[PLProcessNetworkAgent lastProcessNameToNetworkUsageEntry];
-[PLProcessNetworkAgent logEventBackwardNetworkBitmaps];
-[PLProcessNetworkAgent logEventBackwardNetworkBitmapsSysdiagnoseTrigger];
-[PLProcessNetworkAgent logEventBackwardUsage];
-[PLProcessNetworkAgent logEventBackwardUsageWithOutcome:];
-[PLProcessNetworkAgent logEventForwardLowInternet];
-[PLProcessNetworkAgent logEventPointConnectionEvent:forSource:];
-[PLProcessNetworkAgent logUsageTimer];
-[PLProcessNetworkAgent outcomeHasDataUsage:];
-[PLProcessNetworkAgent processesOfInterest:];
-[PLProcessNetworkAgent setBatteryLevelChangedListenerForNetworkBitmap:];
-[PLProcessNetworkAgent setCurNetworkBitmapTimestampForSysdiagnoseTrigger:];
-[PLProcessNetworkAgent setHighBWEndlistener:];
-[PLProcessNetworkAgent setHighBWStartListener:];
-[PLProcessNetworkAgent setLastNetworkBitmapTimestamp:];
-[PLProcessNetworkAgent setLastNetworkBitmapTimestampFor:];
-[PLProcessNetworkAgent setLastProcessNameToNetworkUsageEntry:];
-[PLProcessNetworkAgent setLogUsageTimer:];
-[PLProcessNetworkAgent setStatManagerRef:];
-[PLProcessNetworkAgent setSysdiagnoseListener:];
-[PLProcessNetworkAgent setUsageFeed:];
-[PLProcessNetworkAgent statManagerRef];
-[PLProcessNetworkAgent sysdiagnoseListener];
-[PLProcessNetworkAgent timestampNetConnectEntry:withEventType:withSource:];
-[PLProcessNetworkAgent transferSource:fromPID:toPID:];
-[PLProcessNetworkAgent usageFeed];
```
