# `PLDebugService`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLService`
- 24 instance variables, 24 properties, 137 instance methods, 14 class methods

## Instance variables

```
@"PLXPCListenerOperatorComposition" _xpcListenerPLLog;
@"PLXPCResponderOperatorComposition" _xpcResponderPLLog;
@"PLXPCResponderOperatorComposition" _xpcResponderPLAPITest;
@"PLXPCListenerOperatorComposition" _aggregateTestListener;
@"PLXPCResponderOperatorComposition" _aggregateTestResponder;
@"PLXPCListenerOperatorComposition" _schemaTestListener;
@"PLEntryNotificationOperatorComposition" _assertionListener;
@"PLEntryNotificationOperatorComposition" _assertionNewListener;
@"PLEntryNotificationOperatorComposition" _assertionUpdateListener;
@"PLEntryNotificationOperatorComposition" _canSleepNotification;
@"PLSemaphore" _canSleepSemaphore;
@"PLEntryNotificationOperatorComposition" _sleepNotification;
@"PLEntryNotificationOperatorComposition" _wakeNotification;
@"PLAccountingDebugService" _accDS;
@"PLXPCListenerOperatorComposition" _clientFrameworkTestListener;
@"PLXPCResponderOperatorComposition" _clientFrameworkTestResponder;
@"PLXPCListenerOperatorComposition" _clientFrameworkTestListenerNonAllowlisted;
@"PLXPCResponderOperatorComposition" _clientFrameworkTestResponderNonAllowlisted;
@"PLXPCListenerOperatorComposition" _clientFrameworkTestListenerBatch;
@"PLXPCResponderOperatorComposition" _clientFrameworkTestResponderBatch;
@"NSDictionary" _clientFrameworkTestData;
@"NSMutableArray" _clientFrameworkTestDataBatch;
@"PLXPCResponderOperatorComposition" _energyMonitorDebugResponder;
@"PLDiscretionaryEnergyMonitor" _energyMonitorDebugInstance;
```

## Properties

```
@property (T@"PLXPCListenerOperatorComposition",&,V_xpcListenerPLLog) xpcListenerPLLog;
@property (T@"PLXPCResponderOperatorComposition",&,V_xpcResponderPLLog) xpcResponderPLLog;
@property (T@"PLXPCResponderOperatorComposition",&,V_xpcResponderPLAPITest) xpcResponderPLAPITest;
@property (T@"PLXPCListenerOperatorComposition",&,V_aggregateTestListener) aggregateTestListener;
@property (T@"PLXPCResponderOperatorComposition",&,V_aggregateTestResponder) aggregateTestResponder;
@property (T@"PLXPCListenerOperatorComposition",&,V_schemaTestListener) schemaTestListener;
@property (T@"PLEntryNotificationOperatorComposition",&,V_assertionListener) assertionListener;
@property (T@"PLEntryNotificationOperatorComposition",&,V_assertionNewListener) assertionNewListener;
@property (T@"PLEntryNotificationOperatorComposition",&,V_assertionUpdateListener) assertionUpdateListener;
@property (T@"PLEntryNotificationOperatorComposition",&,V_canSleepNotification) canSleepNotification;
@property (T@"PLSemaphore",&,V_canSleepSemaphore) canSleepSemaphore;
@property (T@"PLEntryNotificationOperatorComposition",&,V_sleepNotification) sleepNotification;
@property (T@"PLEntryNotificationOperatorComposition",&,V_wakeNotification) wakeNotification;
@property (T@"PLAccountingDebugService",&,V_accDS) accDS;
@property (T@"PLXPCListenerOperatorComposition",&,V_clientFrameworkTestListener) clientFrameworkTestListener;
@property (T@"PLXPCResponderOperatorComposition",&,V_clientFrameworkTestResponder) clientFrameworkTestResponder;
@property (T@"PLXPCListenerOperatorComposition",&,V_clientFrameworkTestListenerNonAllowlisted) clientFrameworkTestListenerNonAllowlisted;
@property (T@"PLXPCResponderOperatorComposition",&,V_clientFrameworkTestResponderNonAllowlisted) clientFrameworkTestResponderNonAllowlisted;
@property (T@"PLXPCListenerOperatorComposition",&,V_clientFrameworkTestListenerBatch) clientFrameworkTestListenerBatch;
@property (T@"PLXPCResponderOperatorComposition",&,V_clientFrameworkTestResponderBatch) clientFrameworkTestResponderBatch;
@property (T@"NSDictionary",&,V_clientFrameworkTestData) clientFrameworkTestData;
@property (T@"NSMutableArray",&,V_clientFrameworkTestDataBatch) clientFrameworkTestDataBatch;
@property (T@"PLXPCResponderOperatorComposition",&,V_energyMonitorDebugResponder) energyMonitorDebugResponder;
@property (T@"PLDiscretionaryEnergyMonitor",&,V_energyMonitorDebugInstance) energyMonitorDebugInstance;
```

## Class methods

```
+[PLDebugService entryEventPointDefinitions];
+[PLDebugService entryEventNoneDefinitions];
+[PLDebugService load];
+[PLDebugService railDefinitions];
+[PLDebugService entryAggregateDefinitions];
+[PLDebugService entryAggregateDefinitionAggregateTest];
+[PLDebugService entryAggregateDefinitionAggregateTestSmall];
+[PLDebugService entryAggregateDefinitionAggregateTestSplitAndBucket];
+[PLDebugService entryAggregateDefinitionAggregateTestVerySmall];
+[PLDebugService entryEventNoneDefinitionArrayTest];
+[PLDebugService entryEventNoneDefinitionFastInsertTest];
+[PLDebugService entryEventNoneDefinitionPLAPITest];
+[PLDebugService entryEventNoneDefinitionSleepNotificationTest];
+[PLDebugService entryEventPointDefinitionTest];
```

## Instance methods

```
-[PLDebugService init];
-[PLDebugService canSleepNotification];
-[PLDebugService initOperatorDependancies];
-[PLDebugService setCanSleepSemaphore:];
-[PLDebugService setSleepNotification:];
-[PLDebugService sleepNotification];
-[PLDebugService setWakeNotification:];
-[PLDebugService canSleepSemaphore];
-[PLDebugService setCanSleepNotification:];
-[PLDebugService iterateServices];
-[PLDebugService wakeNotification];
-[PLDebugService iterateAgents];
-[PLDebugService populateIdentifiers:];
-[PLDebugService setClientFrameworkTestListener:];
-[PLDebugService setEnergyMonitorDebugResponder:];
-[PLDebugService testCompression];
-[PLDebugService testFastInserts];
-[PLDebugService testABM];
-[PLDebugService testEntryDelete];
-[PLDebugService testGenerateSafeguardSubmission];
-[PLDebugService testScheduleSafeguardSubmission];
-[PLDebugService accDS];
-[PLDebugService aggregateDataFromSignpost];
-[PLDebugService aggregateTestListener];
-[PLDebugService aggregateTestResponder];
-[PLDebugService assertionListener];
-[PLDebugService assertionNewListener];
-[PLDebugService assertionUpdateListener];
-[PLDebugService clientFrameworkTestData];
-[PLDebugService clientFrameworkTestDataBatch];
-[PLDebugService clientFrameworkTestListener];
-[PLDebugService clientFrameworkTestListenerBatch];
-[PLDebugService clientFrameworkTestListenerNonAllowlisted];
-[PLDebugService clientFrameworkTestResponder];
-[PLDebugService clientFrameworkTestResponderBatch];
-[PLDebugService clientFrameworkTestResponderNonAllowlisted];
-[PLDebugService constructAppIdentifierColumns];
-[PLDebugService constructAppIdentifierTables];
-[PLDebugService constructDMATables];
-[PLDebugService constructTrimQueries];
-[PLDebugService currentBasebandTime];
-[PLDebugService energyMonitorDebugInstance];
-[PLDebugService energyMonitorDebugResponder];
-[PLDebugService filledTestArrayEntry];
-[PLDebugService getValueForPropertyName:forEnergyMonitor:];
-[PLDebugService handleEnergyMonitorDebugQuery:];
-[PLDebugService printNullTestResultsForEntry:withDescription:];
-[PLDebugService rawRead:];
-[PLDebugService rawWrite:];
-[PLDebugService schemaTestListener];
-[PLDebugService setAccDS:];
-[PLDebugService setAggregateTestListener:];
-[PLDebugService setAggregateTestResponder:];
-[PLDebugService setAssertionListener:];
-[PLDebugService setAssertionNewListener:];
-[PLDebugService setAssertionUpdateListener:];
-[PLDebugService setClientFrameworkTestData:];
-[PLDebugService setClientFrameworkTestDataBatch:];
-[PLDebugService setClientFrameworkTestListenerBatch:];
-[PLDebugService setClientFrameworkTestListenerNonAllowlisted:];
-[PLDebugService setClientFrameworkTestResponder:];
-[PLDebugService setClientFrameworkTestResponderBatch:];
-[PLDebugService setClientFrameworkTestResponderNonAllowlisted:];
-[PLDebugService setEnergyMonitorDebugInstance:];
-[PLDebugService setSchemaTestListener:];
-[PLDebugService setXpcListenerPLLog:];
-[PLDebugService setXpcResponderPLAPITest:];
-[PLDebugService setXpcResponderPLLog:];
-[PLDebugService stressActivityScheduler];
-[PLDebugService stressAggregateSmall];
-[PLDebugService stressAggregateVerySmall];
-[PLDebugService stressCache];
-[PLDebugService stressCacheSmall];
-[PLDebugService stressMidnightCalculation];
-[PLDebugService stressMonotonicTimer];
-[PLDebugService stressMonotonicTimer2];
-[PLDebugService stressMonotonicTimer3];
-[PLDebugService stressObjectForKey];
-[PLDebugService stressPLEntry];
-[PLDebugService stressSetObjectForKey];
-[PLDebugService stressTaskingSubmission];
-[PLDebugService stressTimer];
-[PLDebugService testAllEntryKeyRequests];
-[PLDebugService testArray];
-[PLDebugService testBlockingFlushCaches];
-[PLDebugService testDailyTasks];
-[PLDebugService testEntryApplicationAgent];
-[PLDebugService testEntryLogRequestedForEntryKey:];
-[PLDebugService testEntryQueries];
-[PLDebugService testEntrySleep];
-[PLDebugService testEntryWake];
-[PLDebugService testExit];
-[PLDebugService testGenerateOTASubmission];
-[PLDebugService testMonotonicAggregateEntries];
-[PLDebugService testMonotonicAggregateEntriesExtendedTime];
-[PLDebugService testMonotonicTimerThroughSleep];
-[PLDebugService testPLAPIAccounting_AddPowerMeasurementEventInterval:];
-[PLDebugService testPLAPIAccounting_CreateDistributionEventForwardAdd:];
-[PLDebugService testPLAPIAccounting_CreateDistributionEventForwardChild:];
-[PLDebugService testPLAPIAccounting_CreateDistributionEventForwardRem:];
-[PLDebugService testPLAPIAccounting_CreateDistributionEventInterval:];
-[PLDebugService testPLAPIAccounting_CreateDistributionEventPoint:];
-[PLDebugService testPLAPIAccounting_CreatePowerEventBackward:];
-[PLDebugService testPLAPIAccounting_CreatePowerEventForward:];
-[PLDebugService testPLAPIAccounting_CreatePowerEventInterval:];
-[PLDebugService testPLAPIAccounting_CreateQualificationEventBackward:];
-[PLDebugService testPLAPIAccounting_CreateQualificationEventForwardAdd:];
-[PLDebugService testPLAPIAccounting_CreateQualificationEventForwardChild:];
-[PLDebugService testPLAPIAccounting_CreateQualificationEventForwardRem:];
-[PLDebugService testPLAPIAccounting_CreateQualificationEventInterval:];
-[PLDebugService testPLAPIAccounting_CreateQualificationEventPoint:];
-[PLDebugService testPLAPIAccounting_ExistingTest:];
-[PLDebugService testPLAPICore_DeleteAllEntriesForKey:];
-[PLDebugService testPLAPICore_DeleteAllEntriesForKeyBTWF:];
-[PLDebugService testPLAPICore_DeleteAllEntriesForKeyWF:];
-[PLDebugService testPLAPICore_DeleteEntry:];
-[PLDebugService testPLAPICore_DeleteEntryForKey:];
-[PLDebugService testPLAPICore_EntriesForKeyBeforeTICWF:];
-[PLDebugService testPLAPICore_EntriesForKeyInTimeRange:];
-[PLDebugService testPLAPICore_EntriesForKeyWithProperties:];
-[PLDebugService testPLAPICore_LastEntryForKeyWC:];
-[PLDebugService testPLAPICore_LastEntryForKeyWSEK:];
-[PLDebugService testPLAPICore_UpdateEntry:];
-[PLDebugService testPLAPICore_WriteEntries:];
-[PLDebugService testPLAPICore_WriteEntry:];
-[PLDebugService testProportionateAggregateEntries];
-[PLDebugService testQuarantineExit];
-[PLDebugService testTrimBGSQL];
-[PLDebugService testTrimCESQL];
-[PLDebugService testTrimEPSQL];
-[PLDebugService testTrimXCSQL];
-[PLDebugService testUTF8];
-[PLDebugService test_LogErr:str:];
-[PLDebugService test_LogPass:str:];
-[PLDebugService xpcListenerPLLog];
-[PLDebugService xpcResponderPLAPITest];
-[PLDebugService xpcResponderPLLog];
```
