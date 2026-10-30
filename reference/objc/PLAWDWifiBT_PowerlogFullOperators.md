# `PLAWDWifiBT`

- Image: [`/System/Library/PrivateFrameworks/PowerlogFullOperators.framework/PowerlogFullOperators`](../userland/System__Library__PrivateFrameworks__PowerlogFullOperators.framework__PowerlogFullOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAWDAuxMetrics`
- 11 instance variables, 11 properties, 38 instance methods, 4 class methods

## Instance variables

```
B _isWiFiStart;
B _isWiFiRailStart;
B _isBTStart;
B _isBTRailStart;
@"PLEntryNotificationOperatorComposition" _wifiEventCallback;
@"PLEntryNotificationOperatorComposition" _btEventCallback;
@"PLEntryNotificationOperatorComposition" _btPowerCallback;
@"PLEntryNotificationOperatorComposition" _wifiRailCallback;
@"PLEntryNotificationOperatorComposition" _btRailCallback;
q _wifiSubmitCnt;
q _btSubmitCnt;
```

## Properties

```
@property (T@"PLEntryNotificationOperatorComposition",&,V_wifiEventCallback) wifiEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_btEventCallback) btEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_btPowerCallback) btPowerCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_wifiRailCallback) wifiRailCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_btRailCallback) btRailCallback;
@property (TB,V_isWiFiStart) isWiFiStart;
@property (TB,V_isWiFiRailStart) isWiFiRailStart;
@property (TB,V_isBTStart) isBTStart;
@property (TB,V_isBTRailStart) isBTRailStart;
@property (Tq,V_wifiSubmitCnt) wifiSubmitCnt;
@property (Tq,V_btSubmitCnt) btSubmitCnt;
```

## Class methods

```
+[PLAWDWifiBT entryAggregateDefinitions];
+[PLAWDWifiBT entryAggregateDefinitionAwdWifi];
+[PLAWDWifiBT entryAggregateDefinitionAwdBT];
+[PLAWDWifiBT getSharedObjWithOperator:];
```

## Instance methods

```
-[PLAWDWifiBT btEventCallback];
-[PLAWDWifiBT setIsWiFiStart:];
-[PLAWDWifiBT btPowerCallback];
-[PLAWDWifiBT isWiFiRailStart];
-[PLAWDWifiBT setBtSubmitCnt:];
-[PLAWDWifiBT addEntryToBTTable:withValue:];
-[PLAWDWifiBT addEntryToWiFiTable:withValue:andBand:];
-[PLAWDWifiBT btRailCallback];
-[PLAWDWifiBT btSubmitCnt];
-[PLAWDWifiBT handleBTCallback:];
-[PLAWDWifiBT handleBTPowerCallback:];
-[PLAWDWifiBT handleBTRailCallback:];
-[PLAWDWifiBT handleWifiCallback:];
-[PLAWDWifiBT handleWifiRailCallback:];
-[PLAWDWifiBT isBTRailStart];
-[PLAWDWifiBT isBTStart];
-[PLAWDWifiBT isWiFiStart];
-[PLAWDWifiBT resetBTTable];
-[PLAWDWifiBT resetWifiTable];
-[PLAWDWifiBT setBtEventCallback:];
-[PLAWDWifiBT setBtPowerCallback:];
-[PLAWDWifiBT setBtRailCallback:];
-[PLAWDWifiBT setIsBTRailStart:];
-[PLAWDWifiBT setIsBTStart:];
-[PLAWDWifiBT setIsWiFiRailStart:];
-[PLAWDWifiBT setWifiEventCallback:];
-[PLAWDWifiBT setWifiRailCallback:];
-[PLAWDWifiBT setWifiSubmitCnt:];
-[PLAWDWifiBT startBtMetricCollection];
-[PLAWDWifiBT startMetricCollection:];
-[PLAWDWifiBT startWifiMetricCollection];
-[PLAWDWifiBT stopMetricCollection:];
-[PLAWDWifiBT submitBtDataToAWDServer:withAwdConn:];
-[PLAWDWifiBT submitDataToAWDServer:withAwdConn:];
-[PLAWDWifiBT submitWiFiDataToAWDServer:withAwdConn:];
-[PLAWDWifiBT wifiEventCallback];
-[PLAWDWifiBT wifiRailCallback];
-[PLAWDWifiBT wifiSubmitCnt];
```
