# `PLHomeKitAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 23 instance variables, 23 properties, 58 instance methods, 14 class methods

## Instance variables

```
B _enablelog;
@"PLXPCListenerOperatorComposition" _homeKitEventsListener;
@"PLXPCListenerOperatorComposition" _homeConfigurationListener;
@"PLXPCListenerOperatorComposition" _cameraConfigurationListener;
@"PLXPCListenerOperatorComposition" _homeKitRegistrationListener;
Q _numBTPushes;
Q _numConnections;
Q _numPrevBTPushes;
Q _numPrevConnections;
Q _numBTConnections;
Q _numIPConnections;
Q _numBonjour;
Q _numIPEvents;
Q _numIDSPushes;
Q _numCloudPushes;
Q _numBTWakeAdvt;
Q _numBTWakes;
d _lastapwake;
@"PLEntryNotificationOperatorComposition" _sbcLevelChanged;
@"PLEntryNotificationOperatorComposition" _deviceWake;
@"PLTimer" _runTimeAggregatorTimer;
Q _numaggregatelines;
Q _numBTlines;
```

## Properties

```
@property (T@"PLXPCListenerOperatorComposition",&,V_homeKitEventsListener) homeKitEventsListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_homeConfigurationListener) homeConfigurationListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_cameraConfigurationListener) cameraConfigurationListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_homeKitRegistrationListener) homeKitRegistrationListener;
@property (TQ,V_numBTPushes) numBTPushes;
@property (TQ,V_numConnections) numConnections;
@property (TQ,V_numPrevBTPushes) numPrevBTPushes;
@property (TQ,V_numPrevConnections) numPrevConnections;
@property (TQ,V_numBTConnections) numBTConnections;
@property (TQ,V_numIPConnections) numIPConnections;
@property (TQ,V_numBonjour) numBonjour;
@property (TQ,V_numIPEvents) numIPEvents;
@property (TQ,V_numIDSPushes) numIDSPushes;
@property (TQ,V_numCloudPushes) numCloudPushes;
@property (TQ,V_numBTWakeAdvt) numBTWakeAdvt;
@property (TQ,V_numBTWakes) numBTWakes;
@property (Td,V_lastapwake) lastapwake;
@property (TB,V_enablelog) enablelog;
@property (T@"PLEntryNotificationOperatorComposition",&,V_sbcLevelChanged) sbcLevelChanged;
@property (T@"PLEntryNotificationOperatorComposition",&,V_deviceWake) deviceWake;
@property (T@"PLTimer",&,V_runTimeAggregatorTimer) runTimeAggregatorTimer;
@property (TQ,V_numaggregatelines) numaggregatelines;
@property (TQ,V_numBTlines) numBTlines;
```

## Class methods

```
+[PLHomeKitAgent entryEventPointDefinitions];
+[PLHomeKitAgent entryEventForwardDefinitions];
+[PLHomeKitAgent entryEventBackwardDefinitions];
+[PLHomeKitAgent entryEventNoneDefinitions];
+[PLHomeKitAgent load];
+[PLHomeKitAgent defaults];
+[PLHomeKitAgent entryEventForwardDefinitionHomeConfiguration];
+[PLHomeKitAgent entryEventPointDefinitionHomeKitSummary];
+[PLHomeKitAgent entryEventPointDefinitionHomeKitRegistration];
+[PLHomeKitAgent entryEventPointDefinitionHomeKitAdvt];
+[PLHomeKitAgent entryAggregateDefinitionIDSPushMessageTypes];
+[PLHomeKitAgent entryEventPointDefinitionHomeKitEvents];
+[PLHomeKitAgent entryAggregateDefinitions];
+[PLHomeKitAgent entryEventForwardDefinitionCameraConfiguration];
```

## Instance methods

```
-[PLHomeKitAgent cameraConfigurationListener];
-[PLHomeKitAgent numBTWakes];
-[PLHomeKitAgent setNumConnections:];
-[PLHomeKitAgent logEventPointHomeKitRegistration:];
-[PLHomeKitAgent numBTlines];
-[PLHomeKitAgent homeKitRegistrationListener];
-[PLHomeKitAgent init];
-[PLHomeKitAgent numBTPushes];
-[PLHomeKitAgent setHomeConfigurationListener:];
-[PLHomeKitAgent initOperatorDependancies];
-[PLHomeKitAgent setRunTimeAggregatorTimer:];
-[PLHomeKitAgent logEventPointHomeKitEvents:];
-[PLHomeKitAgent setCameraConfigurationListener:];
-[PLHomeKitAgent logEventForwardHomeConfiguration:];
-[PLHomeKitAgent sbcLevelChanged];
-[PLHomeKitAgent setNumBTPushes:];
-[PLHomeKitAgent setNumIDSPushes:];
-[PLHomeKitAgent registrationTypeStringToEnum:];
-[PLHomeKitAgent numBonjour];
-[PLHomeKitAgent numIDSPushes];
-[PLHomeKitAgent setNumCloudPushes:];
-[PLHomeKitAgent setSbcLevelChanged:];
-[PLHomeKitAgent setNumBonjour:];
-[PLHomeKitAgent setNumPrevConnections:];
-[PLHomeKitAgent numPrevConnections];
-[PLHomeKitAgent setNumBTWakeAdvt:];
-[PLHomeKitAgent writeAggregateCounters:];
-[PLHomeKitAgent numBTWakeAdvt];
-[PLHomeKitAgent numaggregatelines];
-[PLHomeKitAgent setDeviceWake:];
-[PLHomeKitAgent setLastapwake:];
-[PLHomeKitAgent homeKitEventsListener];
-[PLHomeKitAgent numPrevBTPushes];
-[PLHomeKitAgent eventTypeStringToEnum:];
-[PLHomeKitAgent numCloudPushes];
-[PLHomeKitAgent setNumIPEvents:];
-[PLHomeKitAgent logEventForwardCameraConfiguration:];
-[PLHomeKitAgent setHomeKitEventsListener:];
-[PLHomeKitAgent setEnablelog:];
-[PLHomeKitAgent setNumBTConnections:];
-[PLHomeKitAgent setNumPrevBTPushes:];
-[PLHomeKitAgent setNumBTlines:];
-[PLHomeKitAgent log];
-[PLHomeKitAgent isAllowedMessageType:];
-[PLHomeKitAgent setHomeKitRegistrationListener:];
-[PLHomeKitAgent setNumIPConnections:];
-[PLHomeKitAgent numIPConnections];
-[PLHomeKitAgent logAggregateIDSPushMessageTypes:];
-[PLHomeKitAgent homeConfigurationListener];
-[PLHomeKitAgent setNumaggregatelines:];
-[PLHomeKitAgent numIPEvents];
-[PLHomeKitAgent setNumBTWakes:];
-[PLHomeKitAgent lastapwake];
-[PLHomeKitAgent enablelog];
-[PLHomeKitAgent numBTConnections];
-[PLHomeKitAgent deviceWake];
-[PLHomeKitAgent runTimeAggregatorTimer];
-[PLHomeKitAgent numConnections];
```
