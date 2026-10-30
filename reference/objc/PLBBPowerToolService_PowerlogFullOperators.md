# `PLBBPowerToolService`

- Image: [`/System/Library/PrivateFrameworks/PowerlogFullOperators.framework/PowerlogFullOperators`](../userland/System__Library__PrivateFrameworks__PowerlogFullOperators.framework__PowerlogFullOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLService`
- 13 instance variables, 13 properties, 40 instance methods, 6 class methods

## Instance variables

```
C _exclusionMask;
@"PLEntryNotificationOperatorComposition" _audioEventCallback;
@"PLEntryNotificationOperatorComposition" _displayEventCallback;
@"PLEntryNotificationOperatorComposition" _hotspotEventCallback;
@"PLEntryNotificationOperatorComposition" _msgLiteCallback;
@"PLEntryNotificationOperatorComposition" _wcdmaRRCCallback;
@"PLEntryNotificationOperatorComposition" _lteRRCCallback;
@"PLEntryNotificationOperatorComposition" _telActivityCallback;
@"PLNSNotificationOperatorComposition" _dailyTaskNotification;
@"NSMutableArray" _startExclusionPeriods;
@"NSMutableArray" _endExclusionPeriods;
@"PLTelephonyConnection" _connection;
@"NSDate" _notToRemoveDate;
```

## Properties

```
@property (TC,V_exclusionMask) exclusionMask;
@property (T@"PLEntryNotificationOperatorComposition",&,V_audioEventCallback) audioEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_displayEventCallback) displayEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_hotspotEventCallback) hotspotEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_msgLiteCallback) msgLiteCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_wcdmaRRCCallback) wcdmaRRCCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_lteRRCCallback) lteRRCCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_telActivityCallback) telActivityCallback;
@property (T@"PLNSNotificationOperatorComposition",&,V_dailyTaskNotification) dailyTaskNotification;
@property (T@"NSMutableArray",&,V_startExclusionPeriods) startExclusionPeriods;
@property (T@"NSMutableArray",&,V_endExclusionPeriods) endExclusionPeriods;
@property (T@"PLTelephonyConnection",W,V_connection) connection;
@property (T@"NSDate",&,V_notToRemoveDate) notToRemoveDate;
```

## Class methods

```
+[PLBBPowerToolService entryEventPointDefinitions];
+[PLBBPowerToolService load];
+[PLBBPowerToolService entryAggregateDefinitions];
+[PLBBPowerToolService entryArmUtil];
+[PLBBPowerToolService entryCauseDefinition];
+[PLBBPowerToolService entryCauseHelperDefinition];
```

## Instance methods

```
-[PLBBPowerToolService init];
-[PLBBPowerToolService initOperatorDependancies];
-[PLBBPowerToolService connection];
-[PLBBPowerToolService setDailyTaskNotification:];
-[PLBBPowerToolService setConnection:];
-[PLBBPowerToolService dailyTaskNotification];
-[PLBBPowerToolService setExclusionMask:];
-[PLBBPowerToolService exclusionMask];
-[PLBBPowerToolService handleAudioCallback:];
-[PLBBPowerToolService handleDisplayCallback:];
-[PLBBPowerToolService notToRemoveDate];
-[PLBBPowerToolService lteRRCCallback:];
-[PLBBPowerToolService msgLiteCallback];
-[PLBBPowerToolService audioEventCallback];
-[PLBBPowerToolService displayEventCallback];
-[PLBBPowerToolService endExclusionPeriods];
-[PLBBPowerToolService handleExclusionWithState:withExclusion:];
-[PLBBPowerToolService handleHotspotCallback:];
-[PLBBPowerToolService hotspotEventCallback];
-[PLBBPowerToolService lteRRCCallback];
-[PLBBPowerToolService msgLiteCallback:];
-[PLBBPowerToolService percentageHistogramFromArray:];
-[PLBBPowerToolService setAudioEventCallback:];
-[PLBBPowerToolService setDisplayEventCallback:];
-[PLBBPowerToolService setEndExclusionPeriods:];
-[PLBBPowerToolService setHotspotEventCallback:];
-[PLBBPowerToolService setLteRRCCallback:];
-[PLBBPowerToolService setMsgLiteCallback:];
-[PLBBPowerToolService setNotToRemoveDate:];
-[PLBBPowerToolService setStartExclusionPeriods:];
-[PLBBPowerToolService setTelActivityCallback:];
-[PLBBPowerToolService setWcdmaRRCCallback:];
-[PLBBPowerToolService setupInitExclusions];
-[PLBBPowerToolService startExclusionPeriods];
-[PLBBPowerToolService submitAWD];
-[PLBBPowerToolService telActivityCallback];
-[PLBBPowerToolService telActivityCallback:];
-[PLBBPowerToolService wcdmaRRCCallback];
-[PLBBPowerToolService wcdmaRRCCallback:];
-[PLBBPowerToolService writeToHelperTable:WithValue:withDate:];
```
