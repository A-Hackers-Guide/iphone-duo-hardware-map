# `PLProximityAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 12 instance variables, 12 properties, 34 instance methods, 15 class methods

## Instance variables

```
@"PLXPCListenerOperatorComposition" _radioStateListener;
@"PLXPCListenerOperatorComposition" _clientStateListener;
@"PLXPCListenerOperatorComposition" _radioPowerListener;
@"PLXPCListenerOperatorComposition" _timerStateListener;
@"PLXPCListenerOperatorComposition" _maintenanceListener;
@"PLXPCListenerOperatorComposition" _deviceConnectionListener;
@"PLTimer" _runTimeAggregatorTimer;
Q _numBTLines;
Q _numConnects;
Q _numDisconnects;
@"PLEntryNotificationOperatorComposition" _batteryLevelChanged;
@"NSDate" _lastSBCTimestamp;
```

## Properties

```
@property (T@"PLXPCListenerOperatorComposition",&,V_radioStateListener) radioStateListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_clientStateListener) clientStateListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_radioPowerListener) radioPowerListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_timerStateListener) timerStateListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_maintenanceListener) maintenanceListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_deviceConnectionListener) deviceConnectionListener;
@property (T@"PLTimer",&,V_runTimeAggregatorTimer) runTimeAggregatorTimer;
@property (TQ,V_numBTLines) numBTLines;
@property (TQ,V_numConnects) numConnects;
@property (TQ,V_numDisconnects) numDisconnects;
@property (T@"PLEntryNotificationOperatorComposition",&,V_batteryLevelChanged) batteryLevelChanged;
@property (T@"NSDate",&,V_lastSBCTimestamp) lastSBCTimestamp;
```

## Class methods

```
+[PLProximityAgent entryEventIntervalDefinitions];
+[PLProximityAgent entryEventPointDefinitions];
+[PLProximityAgent entryEventForwardDefinitions];
+[PLProximityAgent entryEventBackwardDefinitions];
+[PLProximityAgent entryEventNoneDefinitions];
+[PLProximityAgent load];
+[PLProximityAgent defaults];
+[PLProximityAgent entryEventForwardDefinitionRadioState];
+[PLProximityAgent entryEventIntervalDefinitionBinnedDeviceConnection];
+[PLProximityAgent entryEventPointDefinitionDeviceConnection];
+[PLProximityAgent entryEventForwardDefinitionClientState];
+[PLProximityAgent isProximityLiteSupported];
+[PLProximityAgent entryEventBackwardDefinitionRadioPower];
+[PLProximityAgent entryEventPointDefinitionMaintainedDevices];
+[PLProximityAgent entryEventPointDefinitionTimerState];
```

## Instance methods

```
-[PLProximityAgent logEventPointDeviceConnection:];
-[PLProximityAgent logEventForwardClientState:];
-[PLProximityAgent setNumConnects:];
-[PLProximityAgent setNumDisconnects:];
-[PLProximityAgent radioPowerListener];
-[PLProximityAgent init];
-[PLProximityAgent initOperatorDependancies];
-[PLProximityAgent setRunTimeAggregatorTimer:];
-[PLProximityAgent setRadioStateListener:];
-[PLProximityAgent maintenanceListener];
-[PLProximityAgent setTimerStateListener:];
-[PLProximityAgent logEventForwardRadioState:];
-[PLProximityAgent logEventBackwardPowerStats:];
-[PLProximityAgent clientStateListener];
-[PLProximityAgent setLastSBCTimestamp:];
-[PLProximityAgent setMaintenanceListener:];
-[PLProximityAgent numBTLines];
-[PLProximityAgent lastSBCTimestamp];
-[PLProximityAgent numConnects];
-[PLProximityAgent deviceConnectionListener];
-[PLProximityAgent timerStateListener];
-[PLProximityAgent radioStateListener];
-[PLProximityAgent logEventIntervalBinnedDeviceConnection];
-[PLProximityAgent setRadioPowerListener:];
-[PLProximityAgent setClientStateListener:];
-[PLProximityAgent numDisconnects];
-[PLProximityAgent setDeviceConnectionListener:];
-[PLProximityAgent setNumBTLines:];
-[PLProximityAgent setBatteryLevelChanged:];
-[PLProximityAgent log];
-[PLProximityAgent batteryLevelChanged];
-[PLProximityAgent logEventPointTimerState:];
-[PLProximityAgent logEventPointMaintenance:];
-[PLProximityAgent runTimeAggregatorTimer];
```
