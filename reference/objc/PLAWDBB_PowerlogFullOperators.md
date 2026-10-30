# `PLAWDBB`

- Image: [`/System/Library/PrivateFrameworks/PowerlogFullOperators.framework/PowerlogFullOperators`](../userland/System__Library__PrivateFrameworks__PowerlogFullOperators.framework__PowerlogFullOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAWDAuxMetrics`
- 13 instance variables, 13 properties, 66 instance methods, 5 class methods

## Instance variables

```
I _upBytes;
I _downBytes;
i _currQuality;
i _newQuality;
@"PLEntryNotificationOperatorComposition" _bbProtocolRailCallback;
@"PLEntryNotificationOperatorComposition" _bbEventCallback;
@"PLEntryNotificationOperatorComposition" _accountingGroupEventCallback;
@"PLEntryNotificationOperatorComposition" _iceStatsEventCallback;
@"PLEntryNotificationOperatorComposition" _connectedPowerRailCallback;
@"NSDate" _startTimeAppBB;
@"NSDate" _startTimeBBLqm;
@"PLEntryNotificationOperatorComposition" _bbLqmCellularActiveCallback;
@"PLEntryNotificationOperatorComposition" _bbLqmCumulativeNetworkCallback;
```

## Properties

```
@property (T@"PLEntryNotificationOperatorComposition",&,V_bbProtocolRailCallback) bbProtocolRailCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_bbEventCallback) bbEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_accountingGroupEventCallback) accountingGroupEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_iceStatsEventCallback) iceStatsEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_connectedPowerRailCallback) connectedPowerRailCallback;
@property (T@"NSDate",&,V_startTimeAppBB) startTimeAppBB;
@property (T@"NSDate",&,V_startTimeBBLqm) startTimeBBLqm;
@property (TI,V_upBytes) upBytes;
@property (TI,V_downBytes) downBytes;
@property (T@"PLEntryNotificationOperatorComposition",&,V_bbLqmCellularActiveCallback) bbLqmCellularActiveCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_bbLqmCumulativeNetworkCallback) bbLqmCumulativeNetworkCallback;
@property (Ti,V_currQuality) currQuality;
@property (Ti,V_newQuality) newQuality;
```

## Class methods

```
+[PLAWDBB entryAggregateDefinitions];
+[PLAWDBB entryAggregateDefinitionAwdBBQlm];
+[PLAWDBB entryAggregateDefinitionAwdBBQlmCounter];
+[PLAWDBB entryAggregateDefinitionAwdConnectedPower];
+[PLAWDBB getSharedObjWithOperator:];
```

## Instance methods

```
-[PLAWDBB handleBBRailCallbackBBProtocol:];
-[PLAWDBB resetBBLqmTable];
-[PLAWDBB setBbLqmCellularActiveCallback:];
-[PLAWDBB bbEventCallback];
-[PLAWDBB setCurrQuality:];
-[PLAWDBB upBytes];
-[PLAWDBB accountingGroupEventCallback];
-[PLAWDBB bbLqmCellularActiveCallback];
-[PLAWDBB bbLqmCumulativeNetworkCallback];
-[PLAWDBB bbProtocolRailCallback];
-[PLAWDBB connectedPowerRailCallback];
-[PLAWDBB convertQualityWithLinkQuality:];
-[PLAWDBB currQuality];
-[PLAWDBB downBytes];
-[PLAWDBB finalizeTableWithEntry:];
-[PLAWDBB getIntervalSinceLastUpdateWithEntryName:];
-[PLAWDBB handleAcountGroupCallback:];
-[PLAWDBB handleBBConnectedPowerRail:];
-[PLAWDBB handleBBLqmCellularActiveCallback:];
-[PLAWDBB handleBBLqmCumulativeNetworkCallback:];
-[PLAWDBB handleBBRailCallbackBBICE:];
-[PLAWDBB handleBBRailCallbackBBTx:];
-[PLAWDBB handleBBRailCallbackLTESleep:];
-[PLAWDBB handleBBRailCallbackOos:];
-[PLAWDBB handleBBRailCallbackTxCdma2K:];
-[PLAWDBB handleBBRailCallbackTxCdma:];
-[PLAWDBB handleBBRailCallbackTxEvdo:];
-[PLAWDBB handleBBRailCallbackTxGsm:];
-[PLAWDBB handleBBRailCallbackTxLte:];
-[PLAWDBB handleBBRailCallbackTxUtran:];
-[PLAWDBB handleBBRailCallbackWrapper:];
-[PLAWDBB handleIceStatsCallback:];
-[PLAWDBB iceStatsEventCallback];
-[PLAWDBB newQuality];
-[PLAWDBB resetAllBBLqmTables];
-[PLAWDBB resetBBLqmCounterTable];
-[PLAWDBB resetConnectedPowerTable];
-[PLAWDBB setAccountingGroupEventCallback:];
-[PLAWDBB setBbEventCallback:];
-[PLAWDBB setBbLqmCumulativeNetworkCallback:];
-[PLAWDBB setBbProtocolRailCallback:];
-[PLAWDBB setConnectedPowerRailCallback:];
-[PLAWDBB setDownBytes:];
-[PLAWDBB setIceStatsEventCallback:];
-[PLAWDBB setNewQuality:];
-[PLAWDBB setStartTimeAppBB:];
-[PLAWDBB setStartTimeBBLqm:];
-[PLAWDBB setUpBytes:];
-[PLAWDBB startAppBB];
-[PLAWDBB startBBLqm];
-[PLAWDBB startBBPower];
-[PLAWDBB startConnectedPower];
-[PLAWDBB startMetricCollection:];
-[PLAWDBB startTimeAppBB];
-[PLAWDBB startTimeBBLqm];
-[PLAWDBB stopAppBB];
-[PLAWDBB stopBBLqm];
-[PLAWDBB stopBBPower];
-[PLAWDBB stopConnectedPower];
-[PLAWDBB stopMetricCollection:];
-[PLAWDBB submitAppBB:withAwdConn:];
-[PLAWDBB submitBBLqm:withAwdConn:];
-[PLAWDBB submitConnectedPower:withAwdConn:];
-[PLAWDBB submitDataToAWDServer:withAwdConn:];
-[PLAWDBB updateCurrLqmState];
-[PLAWDBB updateLQMTableWithQuality:withTime:withRX:withTX:];
```
