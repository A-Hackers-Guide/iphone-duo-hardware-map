# `SBHIDUISensorModeController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `SBBacklightCoordinatorObserver`, `SBProximitySensorControlling`, `SBAVSystemControllerCacheObserver`, `BSInvalidatable`
- 21 instance variables, 7 properties, 35 instance methods, 0 class methods

## Instance variables

```
@"BKSHIDUISensorService" _sensorService;
@"BKSHIDUISensorService" _mirrorSensorService;
@"NSString" _surfaceDescription;
@"SBBacklightCoordinator" _backlightCoordinator;
@"BKSHIDUISensorMode" _sensorMode;
@"<BSInvalidatable>" _sensorModeAssertion;
@"<BSInvalidatable>" _mirrorSensorModeAssertion;
@"<BSInvalidatable>" _proximityDetectionModeAssertion;
@"<BSInvalidatable>" _mirrorProximityDetectionModeAssertion;
@"BSCompoundAssertion" _digitizerModeBaselineAssertion;
@"BSCompoundAssertion" _proximityModeAssertion;
@"BSCompoundAssertion" _secureIndicatorDisabledDigitizerAssertion;
@"BSCompoundAssertion" _secureIndicatorProximityModeAssertion;
@"BSCompoundAssertion" _digitizerActiveDuringSecureIndicatorAssertion;
@"NSMutableArray" _assertions;
@"SBHIDUISensorModeAssertion" _pocketTouchesAssertion;
q _sensorModeTransactionCount;
B _proximityDetectionEnabled;
B _activeAudioRouteIsReceiver;
@"SBAVSystemControllerCache" _avCache;
B _shouldUseLowPowerActiveProxDetectionMode;
```

## Properties

```
@property (TB,N) pocketTouchesExpected;
@property (TB,R,N,V_shouldUseLowPowerActiveProxDetectionMode) shouldUseLowPowerActiveProxDetectionMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,N,GisProximityDetectionEnabled) proximityDetectionEnabled;
```

## Instance methods

```
-[SBHIDUISensorModeController setPocketTouchesExpected:];
-[SBHIDUISensorModeController init];
-[SBHIDUISensorModeController cache:didUpdateActiveAudioRoute:];
-[SBHIDUISensorModeController initWithWindowScene:];
-[SBHIDUISensorModeController invalidate];
-[SBHIDUISensorModeController requestProximityMode:forReason:];
-[SBHIDUISensorModeController description];
-[SBHIDUISensorModeController backlightCoordinator:didUpdateAggregateBacklightState:fromSource:];
-[SBHIDUISensorModeController appendDescriptionToStream:];
-[SBHIDUISensorModeController pocketTouchesExpected];
-[SBHIDUISensorModeController backlightCoordinator:willUpdateAggregateBacklightState:fromSource:];
-[SBHIDUISensorModeController initWithSensorService:mirrorSensorService:backlightCoordinator:];
-[SBHIDUISensorModeController _hasModeAssertions];
-[SBHIDUISensorModeController _isInCallOnReceiverRoute];
-[SBHIDUISensorModeController _reevaluateLockStateForSource:];
-[SBHIDUISensorModeController _removeHIDUISensorModeAssertion:];
-[SBHIDUISensorModeController _requestSensorModeAssertionForReason:source:builder:];
-[SBHIDUISensorModeController addStartupHIDLockAssertion];
-[SBHIDUISensorModeController assertBaselineDisabledDigitizerMode:source:reason:];
-[SBHIDUISensorModeController assertDigitizerActiveDuringSecureIndicatorDisplayOffForReason:];
-[SBHIDUISensorModeController assertDisplayState:source:reason:];
-[SBHIDUISensorModeController assertSecureIndicatorEnabledDisabledDigitizerModeForReason:];
-[SBHIDUISensorModeController assertSecureIndicatorEnabledProximityModeForReason:];
-[SBHIDUISensorModeController initWithSensorService:];
-[SBHIDUISensorModeController initWithSensorService:backlightCoordinator:];
-[SBHIDUISensorModeController isProximityDetectionEnabled];
-[SBHIDUISensorModeController resetProximityCalibration];
-[SBHIDUISensorModeController sensorModeTransactionForBacklightChangeSource:];
-[SBHIDUISensorModeController setProximityDetectionEnabled:];
-[SBHIDUISensorModeController setProximityDetectionEnabled:changeSource:];
-[SBHIDUISensorModeController shouldUseLowPowerActiveProxDetectionMode];
-[SBHIDUISensorModeController suspendProximityDetection:disableDigitizer:source:reason:];
-[SBHIDUISensorModeController suspendProximityDetection:disableDigitizer:wakeSwipeEdges:source:reason:];
-[SBHIDUISensorModeController suspendProximityDetectionAndDisableDigitizer:source:reason:];
-[SBHIDUISensorModeController suspendProximityDetectionForSource:reason:];
```
