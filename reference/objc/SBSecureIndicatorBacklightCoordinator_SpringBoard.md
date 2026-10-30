# `SBSecureIndicatorBacklightCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBBacklightControllerObserver`, `SBProximitySensorManagerObserver`, `SBSensorAccessSecureDisplayObserving`, `PTSettingsKeyObserver`, `SWSystemSleepObserver`, `BSInvalidatable`
- 20 instance variables, 20 properties, 55 instance methods, 0 class methods

## Instance variables

```
@"SBBacklightController" _backlightController;
@"SBWindowScene" _windowScene;
@"SBProximitySensorManager" _proximitySensorManager;
@"SBHIDUISensorModeController" _sensorModeController;
@"BSCompoundAssertion" _assertions;
B _isActive;
B _objectWithinCrudeProximity;
B _ignoresFeatureFlag;
I _preventSystemSleepAssertionID;
@"SBSecureIndicatorMinimumOnTimeCoordinator" _minimumOnTimeCoordinator;
@"NSString" _preventSystemSleepAssertionName;
@"BSContinuousMachTimer" _releasePreventSystemSleepAssertionTimer;
@"<SBSecureIndicatorMinimumOnTimeCoordinatedBlockRegistration>" _secureStateWantsWindowSceneActiveBlockRegistration;
@"BLSAssertion" _liveRenderingAssertion;
@"<BSInvalidatable>" _displayPowerAssertion;
@"<BSInvalidatable>" _disabledDigitizerModeAssertion;
@"<BSInvalidatable>" _proximityModeAssertion;
@"<SBSecureIndicatorMinimumOnTimeCoordinatedBlockRegistration>" _displayPowerAssertionCancellationBlockRegistration;
@"<SBRecordingIndicatorDisplayPowerManaging>" _indicatorDisplayPowerManaging;
@"SBRecordingIndicatorManager" _recordingIndicatorManager;
```

## Properties

```
@property (T@"SBSecureIndicatorMinimumOnTimeCoordinator",R,N,V_minimumOnTimeCoordinator) minimumOnTimeCoordinator;
@property (T@"NSString",C,N,V_preventSystemSleepAssertionName) preventSystemSleepAssertionName;
@property (TI,N,V_preventSystemSleepAssertionID) preventSystemSleepAssertionID;
@property (T@"BSContinuousMachTimer",&,N,V_releasePreventSystemSleepAssertionTimer) releasePreventSystemSleepAssertionTimer;
@property (T@"<SBSecureIndicatorMinimumOnTimeCoordinatedBlockRegistration>",&,N,V_secureStateWantsWindowSceneActiveBlockRegistration) secureStateWantsWindowSceneActiveBlockRegistration;
@property (T@"BLSAssertion",R,N,V_liveRenderingAssertion) liveRenderingAssertion;
@property (T@"<BSInvalidatable>",R,N,V_displayPowerAssertion) displayPowerAssertion;
@property (T@"<BSInvalidatable>",R,N,V_disabledDigitizerModeAssertion) disabledDigitizerModeAssertion;
@property (T@"<BSInvalidatable>",R,N,V_proximityModeAssertion) proximityModeAssertion;
@property (T@"<SBSecureIndicatorMinimumOnTimeCoordinatedBlockRegistration>",R,N,V_displayPowerAssertionCancellationBlockRegistration) displayPowerAssertionCancellationBlockRegistration;
@property (T@"<SBRecordingIndicatorDisplayPowerManaging>",&,N,G_indicatorDisplayPowerManaging,S_setIndicatorDisplayPowerManaging:,V_indicatorDisplayPowerManaging) indicatorDisplayPowerManaging;
@property (TB,N,G_isObjectWithinCrudeProximity,S_setObjectWithinCrudeProximity:,V_objectWithinCrudeProximity) objectWithinCrudeProximity;
@property (TB,N,G_ignoresFeatureFlag,S_setIgnoresFeatureFlag:,V_ignoresFeatureFlag) ignoresFeatureFlag;
@property (T@"SBRecordingIndicatorManager",&,N,S_setRecordingIndicatorManager:,V_recordingIndicatorManager) recordingIndicatorManager;
@property (TB,R,N) isSuppressingFlipbookRendering;
@property (TB,R,N) allowsBacklightChanges;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSecureIndicatorBacklightCoordinator minimumOnTimeCoordinator];
-[SBSecureIndicatorBacklightCoordinator backlightController:didTransitionToBacklightState:source:];
-[SBSecureIndicatorBacklightCoordinator recordingIndicatorManager];
-[SBSecureIndicatorBacklightCoordinator liveRenderingAssertion];
-[SBSecureIndicatorBacklightCoordinator _updateState];
-[SBSecureIndicatorBacklightCoordinator _acquirePreventSystemSleepAssertionIfNecessary];
-[SBSecureIndicatorBacklightCoordinator _secureStateWantsWindowSceneActive];
-[SBSecureIndicatorBacklightCoordinator backlightController:willTransitionToBacklightState:source:];
-[SBSecureIndicatorBacklightCoordinator proximityModeAssertion];
-[SBSecureIndicatorBacklightCoordinator _setIndicatorDisplayPowerManaging:];
-[SBSecureIndicatorBacklightCoordinator _handleObjectWithinCrudeProximityChanged];
-[SBSecureIndicatorBacklightCoordinator _updateLiveRenderingAssertionIfNeeded];
-[SBSecureIndicatorBacklightCoordinator preventSystemSleepAssertionID];
-[SBSecureIndicatorBacklightCoordinator dealloc];
-[SBSecureIndicatorBacklightCoordinator _setIgnoresFeatureFlag:];
-[SBSecureIndicatorBacklightCoordinator _setRecordingIndicatorManager:];
-[SBSecureIndicatorBacklightCoordinator setSecureStateWantsWindowSceneActiveBlockRegistration:];
-[SBSecureIndicatorBacklightCoordinator secureStateWantsWindowSceneActiveBlockRegistration];
-[SBSecureIndicatorBacklightCoordinator _schedulePowerAssertionCancellationIfStillApplies:reason:];
-[SBSecureIndicatorBacklightCoordinator _createOrResetPreventSystemSleepAssertion];
-[SBSecureIndicatorBacklightCoordinator settings:changedValueForKey:];
-[SBSecureIndicatorBacklightCoordinator systemSleepMonitorWillWakeFromSleep:];
-[SBSecureIndicatorBacklightCoordinator _indicatorDisplayPowerManaging];
-[SBSecureIndicatorBacklightCoordinator _requiredSecureSurface];
-[SBSecureIndicatorBacklightCoordinator invalidate];
-[SBSecureIndicatorBacklightCoordinator _thisDisplayIsRequired];
-[SBSecureIndicatorBacklightCoordinator _updateDisplayPowerAssertionIfNeeded];
-[SBSecureIndicatorBacklightCoordinator allowsBacklightChanges];
-[SBSecureIndicatorBacklightCoordinator _ignoresFeatureFlag];
-[SBSecureIndicatorBacklightCoordinator displayPowerAssertion];
-[SBSecureIndicatorBacklightCoordinator _releasePreventSystemSleepAssertion];
-[SBSecureIndicatorBacklightCoordinator _updateHIDSensorModeForBacklightState:source:];
-[SBSecureIndicatorBacklightCoordinator _schedulePowerAssertionCancellation];
-[SBSecureIndicatorBacklightCoordinator _updateAssertions];
-[SBSecureIndicatorBacklightCoordinator _pushSecureStateWantsWindowSceneActive];
-[SBSecureIndicatorBacklightCoordinator isSuppressingFlipbookRendering];
-[SBSecureIndicatorBacklightCoordinator preventSystemSleepAssertionName];
-[SBSecureIndicatorBacklightCoordinator setPreventSystemSleepAssertionName:];
-[SBSecureIndicatorBacklightCoordinator _evaluateSecureStateWantsWindowSceneActive];
-[SBSecureIndicatorBacklightCoordinator setReleasePreventSystemSleepAssertionTimer:];
-[SBSecureIndicatorBacklightCoordinator releasePreventSystemSleepAssertionTimer];
-[SBSecureIndicatorBacklightCoordinator secureDisplayProvider:didUpdateRequiredSurface:];
-[SBSecureIndicatorBacklightCoordinator acquireBacklightCoordinatorAssertionForReason:];
-[SBSecureIndicatorBacklightCoordinator _cancelPowerAssertionCancellation];
-[SBSecureIndicatorBacklightCoordinator displayPowerAssertionCancellationBlockRegistration];
-[SBSecureIndicatorBacklightCoordinator initWithBacklightController:sensorModeController:proximitySensorManager:minimumOnTimeCoordinator:indicatorDisplayPowerManaging:windowScene:];
-[SBSecureIndicatorBacklightCoordinator _isObjectWithinCrudeProximity];
-[SBSecureIndicatorBacklightCoordinator _scheduleReleaseOfPreventSystemSleepAssertion];
-[SBSecureIndicatorBacklightCoordinator setPreventSystemSleepAssertionID:];
-[SBSecureIndicatorBacklightCoordinator _applySecureStateWantsWindowSceneActive:];
-[SBSecureIndicatorBacklightCoordinator systemSleepMonitorSleepRequestAborted:];
-[SBSecureIndicatorBacklightCoordinator _updateHIDSensorMode];
-[SBSecureIndicatorBacklightCoordinator _setObjectWithinCrudeProximity:];
-[SBSecureIndicatorBacklightCoordinator disabledDigitizerModeAssertion];
-[SBSecureIndicatorBacklightCoordinator proximitySensorManager:crudeProximityDidChange:];
```
