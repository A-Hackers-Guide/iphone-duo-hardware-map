# `PLAWDDisplay`

- Image: [`/System/Library/PrivateFrameworks/PowerlogFullOperators.framework/PowerlogFullOperators`](../userland/System__Library__PrivateFrameworks__PowerlogFullOperators.framework__PowerlogFullOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAWDAuxMetrics`
- 21 instance variables, 21 properties, 65 instance methods, 3 class methods

## Instance variables

```
B _prevDisplayOn;
B _prevDeviceCharging;
B _prevMieOn;
B _prevAlsOn;
@"PLEntryNotificationOperatorComposition" _displayEventCallback;
@"PLEntryNotificationOperatorComposition" _backlightEventCallback;
@"PLEntryNotificationOperatorComposition" _alsUserPreferencesEventCallback;
@"PLEntryNotificationOperatorComposition" _batteryEventCallback;
@"PLEntryNotificationOperatorComposition" _backlightRailCallback;
@"PLEntryNotificationOperatorComposition" _touchEventCallback;
@"PLEntryNotificationOperatorComposition" _alsEnabledEventCallback;
d _displayOnTimeStamp;
d _mieOnTimeStamp;
d _bklTimeStamp;
q _prevBklBucketIdx;
d _prevBklChgTimeStamp;
q _startTouchEntryId;
d _bklPowerRailTimeStamp;
q _dispSubmitCnt;
q _touchSubmitCnt;
d _prevBklPower;
```

## Properties

```
@property (T@"PLEntryNotificationOperatorComposition",&,V_displayEventCallback) displayEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_backlightEventCallback) backlightEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_alsUserPreferencesEventCallback) alsUserPreferencesEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_batteryEventCallback) batteryEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_backlightRailCallback) backlightRailCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_touchEventCallback) touchEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_alsEnabledEventCallback) alsEnabledEventCallback;
@property (TB,V_prevDisplayOn) prevDisplayOn;
@property (Td,V_displayOnTimeStamp) displayOnTimeStamp;
@property (TB,V_prevDeviceCharging) prevDeviceCharging;
@property (TB,V_prevMieOn) prevMieOn;
@property (Td,V_mieOnTimeStamp) mieOnTimeStamp;
@property (Td,V_bklTimeStamp) bklTimeStamp;
@property (Tq,V_prevBklBucketIdx) prevBklBucketIdx;
@property (Td,V_prevBklChgTimeStamp) prevBklChgTimeStamp;
@property (Tq,V_startTouchEntryId) startTouchEntryId;
@property (Td,V_bklPowerRailTimeStamp) bklPowerRailTimeStamp;
@property (Tq,V_dispSubmitCnt) dispSubmitCnt;
@property (Tq,V_touchSubmitCnt) touchSubmitCnt;
@property (TB,V_prevAlsOn) prevAlsOn;
@property (Td,V_prevBklPower) prevBklPower;
```

## Class methods

```
+[PLAWDDisplay entryAggregateDefinitions];
+[PLAWDDisplay entryAggregateDefinitionAwdDisplayAndAls];
+[PLAWDDisplay getSharedObjWithOperator:];
```

## Instance methods

```
-[PLAWDDisplay handleBatteryCallback:];
-[PLAWDDisplay handleDisplayCallback:];
-[PLAWDDisplay alsUserPreferencesEventCallback];
-[PLAWDDisplay updateDisplayMetrics:withState:];
-[PLAWDDisplay getUAmpsBucket:];
-[PLAWDDisplay addEntryToDisplayAlsTable:withValue:];
-[PLAWDDisplay alsEnabledEventCallback];
-[PLAWDDisplay backlightEventCallback];
-[PLAWDDisplay backlightRailCallback];
-[PLAWDDisplay batteryEventCallback];
-[PLAWDDisplay bklPowerRailTimeStamp];
-[PLAWDDisplay bklTimeStamp];
-[PLAWDDisplay dispSubmitCnt];
-[PLAWDDisplay displayEventCallback];
-[PLAWDDisplay displayOnTimeStamp];
-[PLAWDDisplay finalizeDisplayAlsTable];
-[PLAWDDisplay getBklbucketIdx:withLux:];
-[PLAWDDisplay getLuxBucket:];
-[PLAWDDisplay handleAlsEnabledCallback:];
-[PLAWDDisplay handleAlsUserPreferencesCallback:];
-[PLAWDDisplay handleBacklightCallback:];
-[PLAWDDisplay handleBacklightRailCallback:];
-[PLAWDDisplay handleTouchCallback:];
-[PLAWDDisplay initDisplayBacklightAlsStats];
-[PLAWDDisplay initTouchStats];
-[PLAWDDisplay mieOnTimeStamp];
-[PLAWDDisplay prevAlsOn];
-[PLAWDDisplay prevBklBucketIdx];
-[PLAWDDisplay prevBklChgTimeStamp];
-[PLAWDDisplay prevBklPower];
-[PLAWDDisplay prevDeviceCharging];
-[PLAWDDisplay prevDisplayOn];
-[PLAWDDisplay prevMieOn];
-[PLAWDDisplay reInitDisplayBacklightAlsStats];
-[PLAWDDisplay registerForDisplayAgentNotifications];
-[PLAWDDisplay registerForTouchNotifications];
-[PLAWDDisplay resetDisplayAlsTable];
-[PLAWDDisplay setAlsEnabledEventCallback:];
-[PLAWDDisplay setAlsUserPreferencesEventCallback:];
-[PLAWDDisplay setBacklightEventCallback:];
-[PLAWDDisplay setBacklightRailCallback:];
-[PLAWDDisplay setBatteryEventCallback:];
-[PLAWDDisplay setBklPowerRailTimeStamp:];
-[PLAWDDisplay setBklTimeStamp:];
-[PLAWDDisplay setDispSubmitCnt:];
-[PLAWDDisplay setDisplayEventCallback:];
-[PLAWDDisplay setDisplayOnTimeStamp:];
-[PLAWDDisplay setMieOnTimeStamp:];
-[PLAWDDisplay setPrevAlsOn:];
-[PLAWDDisplay setPrevBklBucketIdx:];
-[PLAWDDisplay setPrevBklChgTimeStamp:];
-[PLAWDDisplay setPrevBklPower:];
-[PLAWDDisplay setPrevDeviceCharging:];
-[PLAWDDisplay setPrevDisplayOn:];
-[PLAWDDisplay setPrevMieOn:];
-[PLAWDDisplay setStartTouchEntryId:];
-[PLAWDDisplay setTouchEventCallback:];
-[PLAWDDisplay setTouchSubmitCnt:];
-[PLAWDDisplay startMetricCollection:];
-[PLAWDDisplay startTouchEntryId];
-[PLAWDDisplay stopMetricCollection:];
-[PLAWDDisplay submitDataToAWDServer:withAwdConn:];
-[PLAWDDisplay touchEventCallback];
-[PLAWDDisplay touchSubmitCnt];
-[PLAWDDisplay updateMieMetrics:];
```
