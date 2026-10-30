# `PLNfcAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 11 instance variables, 11 properties, 33 instance methods, 13 class methods

## Instance variables

```
i _nfcConnectionRetryCount;
@"PLXPCListenerOperatorComposition" _cardNotification;
@"PLXPCListenerOperatorComposition" _fieldNotification;
@"PLXPCListenerOperatorComposition" _transactionNotification;
@"PLXPCListenerOperatorComposition" _tsmCommunicationNotification;
@"PLEntryNotificationOperatorComposition" _nfcPowerCountersNotification;
@"PLEntryNotificationOperatorComposition" _nfcAccessoryPowerCounterNotification;
d _onPower;
@"NSDate" _lastPowerCountersLogTime;
@"NSDate" _lastAccessoryPowerCountersLogTime;
@"PLTimer" _nfcConnectionRetryTimer;
```

## Properties

```
@property (T@"PLXPCListenerOperatorComposition",&,V_cardNotification) cardNotification;
@property (T@"PLXPCListenerOperatorComposition",&,V_fieldNotification) fieldNotification;
@property (T@"PLXPCListenerOperatorComposition",&,V_transactionNotification) transactionNotification;
@property (T@"PLXPCListenerOperatorComposition",&,V_tsmCommunicationNotification) tsmCommunicationNotification;
@property (T@"PLEntryNotificationOperatorComposition",&,V_nfcPowerCountersNotification) nfcPowerCountersNotification;
@property (T@"PLEntryNotificationOperatorComposition",&,V_nfcAccessoryPowerCounterNotification) nfcAccessoryPowerCounterNotification;
@property (Td,V_onPower) onPower;
@property (T@"NSDate",&,V_lastPowerCountersLogTime) lastPowerCountersLogTime;
@property (T@"NSDate",&,V_lastAccessoryPowerCountersLogTime) lastAccessoryPowerCountersLogTime;
@property (T@"PLTimer",&,V_nfcConnectionRetryTimer) nfcConnectionRetryTimer;
@property (Ti,V_nfcConnectionRetryCount) nfcConnectionRetryCount;
```

## Class methods

```
+[PLNfcAgent entryEventIntervalDefinitions];
+[PLNfcAgent entryEventForwardDefinitions];
+[PLNfcAgent load];
+[PLNfcAgent defaults];
+[PLNfcAgent isEnabled];
+[PLNfcAgent entryEventForwardDefinitionLPEM];
+[PLNfcAgent entryEventForwardDefinitionCard];
+[PLNfcAgent entryEventForwardDefinitionField];
+[PLNfcAgent entryEventForwardDefinitionTSMCommunication];
+[PLNfcAgent entryEventForwardDefinitionTransaction];
+[PLNfcAgent entryEventIntervalDefinitionAccessoryPower];
+[PLNfcAgent entryEventIntervalDefinitionPower];
+[PLNfcAgent parseLPEMFromData:];
```

## Instance methods

```
-[PLNfcAgent setNfcAccessoryPowerCounterNotification:];
-[PLNfcAgent nfcAccessoryPowerCounterNotification];
-[PLNfcAgent setupLPEMCounter];
-[PLNfcAgent init];
-[PLNfcAgent lastAccessoryPowerCountersLogTime];
-[PLNfcAgent setNfcConnectionRetryCount:];
-[PLNfcAgent retrieveAndLogNfcAccessoryPowerCountersWithRetry:];
-[PLNfcAgent initOperatorDependancies];
-[PLNfcAgent setNfcConnectionRetryTimer:];
-[PLNfcAgent tsmCommunicationNotification];
-[PLNfcAgent nfcPowerCountersNotification];
-[PLNfcAgent fieldNotification];
-[PLNfcAgent nfcConnectionRetryCount];
-[PLNfcAgent retrieveAndLogNfcPowerCountersWithRetry:];
-[PLNfcAgent setTransactionNotification:];
-[PLNfcAgent setCardNotification:];
-[PLNfcAgent setOnPower:];
-[PLNfcAgent getNFCHarwareState];
-[PLNfcAgent transactionNotification];
-[PLNfcAgent initTaskOperatorDependancies];
-[PLNfcAgent setLastPowerCountersLogTime:];
-[PLNfcAgent setFieldNotification:];
-[PLNfcAgent lastPowerCountersLogTime];
-[PLNfcAgent onPower];
-[PLNfcAgent nfcConnectionRetryTimer];
-[PLNfcAgent cardNotification];
-[PLNfcAgent setNfcPowerCountersNotification:];
-[PLNfcAgent setUpNfcPowerCounterRetrieval];
-[PLNfcAgent setLastAccessoryPowerCountersLogTime:];
-[PLNfcAgent fieldChangedWithEntry:];
-[PLNfcAgent setupNfcAccessoryPowerCounterRetrieval];
-[PLNfcAgent setTsmCommunicationNotification:];
-[PLNfcAgent logEventForwardLPEM];
```
