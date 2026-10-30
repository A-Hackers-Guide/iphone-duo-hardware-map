# `HalogenWrapper`

- Image: [`/System/Library/PrivateFrameworks/IOAccessoryManager.framework/IOAccessoryManager`](../userland/System__Library__PrivateFrameworks__IOAccessoryManager.framework__IOAccessoryManager.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 45 instance variables, 45 properties, 92 instance methods, 0 class methods

## Instance variables

```
B _attachDelayTimerRunning;
B _isWet;
B _wasTapToRadarShown;
B _isTapToRadarPending;
B _isReceptacleEmpty;
B _isTimestampValid;
B _isMeasurementEnabled;
B _isMeasurementActive;
B _didNotify;
B _didConfidentNotify;
B _didHighConfidentNotify;
B _didWetDuration;
B _accessoryConnectedWhileWet;
B _didWetTooLong;
B _isHeadsetConnected;
B _isDebugAccessoryConnected;
B _isBlacklistedAccessoryConnected;
B _justDetached;
B _justAttachedCase;
B _isPowerAssertionHeld;
I _service;
i _portID;
i _eventBasedOrientation;
i _connectedAccessoryOrientation;
i _pinID;
I _sleepAssertionID;
@"NSObject<OS_dispatch_queue>" _halogenMeasurementDispatchQueue;
@"NSObject<OS_dispatch_queue>" _halogenTtrDispatchQueue;
@"NSObject<OS_dispatch_source>" _timer;
Q _wetPollingIntervalNs;
Q _dryPollingIntervalNs;
Q _ldcmArbiterRetryNs;
Q _ldcmStartMeasurementsDelayNs;
Q _ldcmStartMeasurementsRetryNs;
Q _minDryReadings;
Q _dryCnt;
Q _firstDryTimestamp;
Q _wetDryTransitionTimestamp;
@"NSCondition" _cond;
@"HalogenMeasurement" _halogenMeasurement;
@"NSData" _eventBasedPDigitalID;
Q _eventBasedDigitalID;
@"NSData" _connectedAccessoryPDigitalID;
Q _connectedAccessoryDigitalID;
Q _wetAccessoryAttachTimestamp;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",N,V_halogenMeasurementDispatchQueue) halogenMeasurementDispatchQueue;
@property (T@"NSObject<OS_dispatch_queue>",N,V_halogenTtrDispatchQueue) halogenTtrDispatchQueue;
@property (T@"NSObject<OS_dispatch_source>",N,V_timer) timer;
@property (TB,N,V_attachDelayTimerRunning) attachDelayTimerRunning;
@property (TQ,N,V_wetPollingIntervalNs) wetPollingIntervalNs;
@property (TQ,N,V_dryPollingIntervalNs) dryPollingIntervalNs;
@property (TQ,N,V_ldcmArbiterRetryNs) ldcmArbiterRetryNs;
@property (TQ,N,V_ldcmStartMeasurementsDelayNs) ldcmStartMeasurementsDelayNs;
@property (TQ,N,V_ldcmStartMeasurementsRetryNs) ldcmStartMeasurementsRetryNs;
@property (TQ,N,V_minDryReadings) minDryReadings;
@property (TQ,N,V_dryCnt) dryCnt;
@property (TQ,N,V_firstDryTimestamp) firstDryTimestamp;
@property (TB,N,V_isWet) isWet;
@property (TB,N,V_wasTapToRadarShown) wasTapToRadarShown;
@property (TB,N,V_isTapToRadarPending) isTapToRadarPending;
@property (TB,N,V_isReceptacleEmpty) isReceptacleEmpty;
@property (TQ,N,V_wetDryTransitionTimestamp) wetDryTransitionTimestamp;
@property (TB,N,V_isTimestampValid) isTimestampValid;
@property (T@"NSCondition",N,V_cond) cond;
@property (TB,N,V_isMeasurementEnabled) isMeasurementEnabled;
@property (TB,N,V_isMeasurementActive) isMeasurementActive;
@property (T@"HalogenMeasurement",N,V_halogenMeasurement) halogenMeasurement;
@property (TI,N,V_service) service;
@property (Ti,N,V_portID) portID;
@property (T@"NSData",N,V_eventBasedPDigitalID) eventBasedPDigitalID;
@property (TQ,N,V_eventBasedDigitalID) eventBasedDigitalID;
@property (Ti,N,V_eventBasedOrientation) eventBasedOrientation;
@property (T@"NSData",N,V_connectedAccessoryPDigitalID) connectedAccessoryPDigitalID;
@property (TQ,N,V_connectedAccessoryDigitalID) connectedAccessoryDigitalID;
@property (Ti,N,V_connectedAccessoryOrientation) connectedAccessoryOrientation;
@property (Ti,N,V_pinID) pinID;
@property (TB,N,V_didNotify) didNotify;
@property (TB,N,V_didConfidentNotify) didConfidentNotify;
@property (TB,N,V_didHighConfidentNotify) didHighConfidentNotify;
@property (TB,N,V_didWetDuration) didWetDuration;
@property (TB,N,V_accessoryConnectedWhileWet) accessoryConnectedWhileWet;
@property (TQ,N,V_wetAccessoryAttachTimestamp) wetAccessoryAttachTimestamp;
@property (TB,N,V_didWetTooLong) didWetTooLong;
@property (TB,N,V_isHeadsetConnected) isHeadsetConnected;
@property (TB,N,V_isDebugAccessoryConnected) isDebugAccessoryConnected;
@property (TB,N,V_isBlacklistedAccessoryConnected) isBlacklistedAccessoryConnected;
@property (TB,N,V_justDetached) justDetached;
@property (TB,N,V_justAttachedCase) justAttachedCase;
@property (TB,N,V_isPowerAssertionHeld) isPowerAssertionHeld;
@property (TI,N,V_sleepAssertionID) sleepAssertionID;
```

## Instance methods

```
-[HalogenWrapper setTimer:];
-[HalogenWrapper setService:];
-[HalogenWrapper init];
-[HalogenWrapper timer];
-[HalogenWrapper dealloc];
-[HalogenWrapper service];
-[HalogenWrapper portID];
-[HalogenWrapper isMeasurementEnabled];
-[HalogenWrapper cond];
-[HalogenWrapper setCond:];
-[HalogenWrapper halogenMeasurementDispatchQueue];
-[HalogenWrapper isBlacklistedAccessoryConnected];
-[HalogenWrapper setConnectedAccessoryDigitalID:];
-[HalogenWrapper setWetAccessoryAttachTimestamp:];
-[HalogenWrapper accessoryConnectedWhileWet];
-[HalogenWrapper attachDelayTimerRunning];
-[HalogenWrapper connectedAccessoryDigitalID];
-[HalogenWrapper connectedAccessoryOrientation];
-[HalogenWrapper connectedAccessoryPDigitalID];
-[HalogenWrapper didConfidentNotify];
-[HalogenWrapper didHighConfidentNotify];
-[HalogenWrapper didNotify];
-[HalogenWrapper didWetDuration];
-[HalogenWrapper didWetTooLong];
-[HalogenWrapper dryCnt];
-[HalogenWrapper dryPollingIntervalNs];
-[HalogenWrapper eventBasedDigitalID];
-[HalogenWrapper eventBasedOrientation];
-[HalogenWrapper eventBasedPDigitalID];
-[HalogenWrapper firstDryTimestamp];
-[HalogenWrapper halogenMeasurement];
-[HalogenWrapper halogenTtrDispatchQueue];
-[HalogenWrapper isDebugAccessoryConnected];
-[HalogenWrapper isHeadsetConnected];
-[HalogenWrapper isMeasurementActive];
-[HalogenWrapper isPowerAssertionHeld];
-[HalogenWrapper isReceptacleEmpty];
-[HalogenWrapper isTapToRadarPending];
-[HalogenWrapper isTimestampValid];
-[HalogenWrapper isWet];
-[HalogenWrapper justAttachedCase];
-[HalogenWrapper justDetached];
-[HalogenWrapper ldcmArbiterRetryNs];
-[HalogenWrapper ldcmStartMeasurementsDelayNs];
-[HalogenWrapper ldcmStartMeasurementsRetryNs];
-[HalogenWrapper minDryReadings];
-[HalogenWrapper pinID];
-[HalogenWrapper setAccessoryConnectedWhileWet:];
-[HalogenWrapper setAttachDelayTimerRunning:];
-[HalogenWrapper setConnectedAccessoryOrientation:];
-[HalogenWrapper setConnectedAccessoryPDigitalID:];
-[HalogenWrapper setDidConfidentNotify:];
-[HalogenWrapper setDidHighConfidentNotify:];
-[HalogenWrapper setDidNotify:];
-[HalogenWrapper setDidWetDuration:];
-[HalogenWrapper setDidWetTooLong:];
-[HalogenWrapper setDryCnt:];
-[HalogenWrapper setDryPollingIntervalNs:];
-[HalogenWrapper setEventBasedDigitalID:];
-[HalogenWrapper setEventBasedOrientation:];
-[HalogenWrapper setEventBasedPDigitalID:];
-[HalogenWrapper setFirstDryTimestamp:];
-[HalogenWrapper setHalogenMeasurement:];
-[HalogenWrapper setHalogenMeasurementDispatchQueue:];
-[HalogenWrapper setHalogenTtrDispatchQueue:];
-[HalogenWrapper setIsBlacklistedAccessoryConnected:];
-[HalogenWrapper setIsDebugAccessoryConnected:];
-[HalogenWrapper setIsHeadsetConnected:];
-[HalogenWrapper setIsMeasurementActive:];
-[HalogenWrapper setIsMeasurementEnabled:];
-[HalogenWrapper setIsPowerAssertionHeld:];
-[HalogenWrapper setIsReceptacleEmpty:];
-[HalogenWrapper setIsTapToRadarPending:];
-[HalogenWrapper setIsTimestampValid:];
-[HalogenWrapper setIsWet:];
-[HalogenWrapper setJustAttachedCase:];
-[HalogenWrapper setJustDetached:];
-[HalogenWrapper setLdcmArbiterRetryNs:];
-[HalogenWrapper setLdcmStartMeasurementsDelayNs:];
-[HalogenWrapper setLdcmStartMeasurementsRetryNs:];
-[HalogenWrapper setMinDryReadings:];
-[HalogenWrapper setPinID:];
-[HalogenWrapper setPortID:];
-[HalogenWrapper setSleepAssertionID:];
-[HalogenWrapper setWasTapToRadarShown:];
-[HalogenWrapper setWetDryTransitionTimestamp:];
-[HalogenWrapper setWetPollingIntervalNs:];
-[HalogenWrapper sleepAssertionID];
-[HalogenWrapper wasTapToRadarShown];
-[HalogenWrapper wetAccessoryAttachTimestamp];
-[HalogenWrapper wetDryTransitionTimestamp];
-[HalogenWrapper wetPollingIntervalNs];
```
