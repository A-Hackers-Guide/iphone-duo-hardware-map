# `PLSleepWakeAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 16 instance variables, 16 properties, 64 instance methods, 18 class methods

## Instance variables

```
I _rootDomainConnect;
I _pmNotifier;
^{IONotificationPort=} _systemPowerPortRef;
@"PLSemaphore" _canSleepSemaphore;
d _apSOCBasePower;
@"PLXPCListenerOperatorComposition" _wakeGestureXPCListener;
^{__IOPMConnection=} _pmConnection;
@"PLEventForwardPowerStateEntry" _lastSleepEntry;
@"PLEventForwardPowerStateEntry" _lastWakeEntry;
@"PLIOKitOperatorComposition" _iokitCoSocPower;
@"PLTimer" _CoSocPowerTimer;
@"NSDate" _lastEntryDate;
Q _prevIntervalsPos;
Q _prevPropertiesPos;
Q _kaIDMin;
Q _kaIDMax;
```

## Properties

```
@property (TI,V_rootDomainConnect) rootDomainConnect;
@property (TI,V_pmNotifier) pmNotifier;
@property (T^{IONotificationPort=},V_systemPowerPortRef) systemPowerPortRef;
@property (T@"PLSemaphore",&,V_canSleepSemaphore) canSleepSemaphore;
@property (Td,V_apSOCBasePower) apSOCBasePower;
@property (T@"PLXPCListenerOperatorComposition",&,V_wakeGestureXPCListener) wakeGestureXPCListener;
@property (T^{__IOPMConnection=},V_pmConnection) pmConnection;
@property (T@"PLEventForwardPowerStateEntry",&,V_lastSleepEntry) lastSleepEntry;
@property (T@"PLEventForwardPowerStateEntry",&,V_lastWakeEntry) lastWakeEntry;
@property (T@"PLIOKitOperatorComposition",R,V_iokitCoSocPower) iokitCoSocPower;
@property (T@"PLTimer",&,V_CoSocPowerTimer) CoSocPowerTimer;
@property (T@"NSDate",&,V_lastEntryDate) lastEntryDate;
@property (TQ,V_prevIntervalsPos) prevIntervalsPos;
@property (TQ,V_prevPropertiesPos) prevPropertiesPos;
@property (TQ,V_kaIDMin) kaIDMin;
@property (TQ,V_kaIDMax) kaIDMax;
```

## Class methods

```
+[PLSleepWakeAgent entryEventIntervalDefinitions];
+[PLSleepWakeAgent entryEventPointDefinitions];
+[PLSleepWakeAgent entryEventForwardDefinitions];
+[PLSleepWakeAgent entryEventBackwardDefinitions];
+[PLSleepWakeAgent entryEventNoneDefinitions];
+[PLSleepWakeAgent load];
+[PLSleepWakeAgent railDefinitions];
+[PLSleepWakeAgent entryEventForwardDefinitionPowerState];
+[PLSleepWakeAgent entryEventForwardDefinitionUserIdle];
+[PLSleepWakeAgent entryEventIntervalDefinitionKernelAssertions];
+[PLSleepWakeAgent entryEventNoneDefinitionKernelAssertionsLookup];
+[PLSleepWakeAgent entryEventNoneDefinitionPowerNapConfig];
+[PLSleepWakeAgent entryEventPointDefinitionCoSocPower];
+[PLSleepWakeAgent entryEventPointDefinitionCurrentKernelWakeTime];
+[PLSleepWakeAgent entryEventPointDefinitionCurrentMachWakeTime];
+[PLSleepWakeAgent entryEventPointDefinitionKernelState];
+[PLSleepWakeAgent entryEventPointDefinitionScheduledWake];
+[PLSleepWakeAgent entryEventPointDefinitionWakeGesture];
```

## Instance methods

```
-[PLSleepWakeAgent init];
-[PLSleepWakeAgent initOperatorDependancies];
-[PLSleepWakeAgent setCanSleepSemaphore:];
-[PLSleepWakeAgent lastEntryDate];
-[PLSleepWakeAgent canSleepSemaphore];
-[PLSleepWakeAgent wakeReasons];
-[PLSleepWakeAgent log];
-[PLSleepWakeAgent setLastEntryDate:];
-[PLSleepWakeAgent getSleepState];
-[PLSleepWakeAgent wakeType];
-[PLSleepWakeAgent kaIDMin];
-[PLSleepWakeAgent registerForUserIdleNotification];
-[PLSleepWakeAgent CoSocPowerTimer];
-[PLSleepWakeAgent iokitCoSocPower];
-[PLSleepWakeAgent kaIDMax];
-[PLSleepWakeAgent logWakeEntries:withCurrentTime:];
-[PLSleepWakeAgent systemPoweredOn];
-[PLSleepWakeAgent apSOCBasePower];
-[PLSleepWakeAgent capabilitiesChanged:];
-[PLSleepWakeAgent driverWakeReasons];
-[PLSleepWakeAgent getCurrentWakeTime];
-[PLSleepWakeAgent getCurrentWakeTimeKey];
-[PLSleepWakeAgent getIOPMKernelAssertionsData:];
-[PLSleepWakeAgent getIOPMRootDomain];
-[PLSleepWakeAgent getLastSleepEntry];
-[PLSleepWakeAgent getLastWakeEntry];
-[PLSleepWakeAgent getPostWakeEntry:];
-[PLSleepWakeAgent getSleepStatisticsApps];
-[PLSleepWakeAgent getSleepSubclassKey];
-[PLSleepWakeAgent getThisWakeEntry:withCurrentWakeTime:withIsDarkwake:withDidSleep:];
-[PLSleepWakeAgent lastSleepEntry];
-[PLSleepWakeAgent lastWakeEntry];
-[PLSleepWakeAgent logEventForwardUserIdle:];
-[PLSleepWakeAgent logEventIntervalKernelAssertions:];
-[PLSleepWakeAgent logEventNoneKernelAssertionsLookup];
-[PLSleepWakeAgent logEventNonePowerNapConfig];
-[PLSleepWakeAgent logEventPointCurrentScheduledWake];
-[PLSleepWakeAgent logEventPointKernelState];
-[PLSleepWakeAgent logEventPointWakeGesture:];
-[PLSleepWakeAgent logSleepEntries:];
-[PLSleepWakeAgent pmConnection];
-[PLSleepWakeAgent pmNotifier];
-[PLSleepWakeAgent prevIntervalsPos];
-[PLSleepWakeAgent prevPropertiesPos];
-[PLSleepWakeAgent registerForCapabilitiesChange];
-[PLSleepWakeAgent rootDomainConnect];
-[PLSleepWakeAgent setApSOCBasePower:];
-[PLSleepWakeAgent setCoSocPowerTimer:];
-[PLSleepWakeAgent setKaIDMax:];
-[PLSleepWakeAgent setKaIDMin:];
-[PLSleepWakeAgent setLastSleepEntry:];
-[PLSleepWakeAgent setLastWakeEntry:];
-[PLSleepWakeAgent setPmConnection:];
-[PLSleepWakeAgent setPmNotifier:];
-[PLSleepWakeAgent setPrevIntervalsPos:];
-[PLSleepWakeAgent setPrevPropertiesPos:];
-[PLSleepWakeAgent setRootDomainConnect:];
-[PLSleepWakeAgent setSystemPowerPortRef:];
-[PLSleepWakeAgent setWakeGestureXPCListener:];
-[PLSleepWakeAgent sleepTriggers];
-[PLSleepWakeAgent systemPowerPortRef];
-[PLSleepWakeAgent wakeGestureXPCListener];
-[PLSleepWakeAgent wakeReasonFromIORegistry];
-[PLSleepWakeAgent wakeReasonsAsNSString];
```
