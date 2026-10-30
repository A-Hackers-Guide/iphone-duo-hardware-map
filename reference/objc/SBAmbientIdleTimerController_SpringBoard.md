# `SBAmbientIdleTimerController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFIdleTimerBehaviorProviding`, `PTSettingsKeyObserver`, `SBBacklightControllerObserver`, `SBAmbientMotionDetectionWakeAttributeMonitorObserver`, `SBMotionDetectionWakeControllerDelegate`
- 26 instance variables, 17 properties, 59 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _observers;
@"SBAmbientSettings" _ambientSettings;
@"SBBacklightController" _backlightController;
B _suppressionEnabled;
B _suppressionServiceStarted;
Q _monitoredSuppressionReasons;
@"CMSuppressionManager" _suppressionManager;
B _onAC;
@"SBLockScreenManager" _lockScreenManager;
@"AMAmbientDefaults" _ambientDefaults;
B _alwaysOnInactivityTimeoutActive;
B _alwaysOnSuppressed;
@"SWWakingTimer" _alwaysOnInactivityTimer;
@"BLSAssertion" _motionDetectionWakeAssertion;
@"SBAmbientMotionDetectionWakeAttributeMonitor" _motionDetectionWakeAttributeMonitor;
@"SBMotionDetectionWakeController" _presenceDetectionController;
@"<BSInvalidatable>" _presenceDetectionWakeAssertion;
@"<BSInvalidatable>" _motionDetectionIdleTimerAssertion;
B _motionDetected;
B _suppressForSleep;
B _userSleepPredicted;
B _ambientSuppressed;
B _idleTimerAllowedForAssertions;
B _idleTimerAllowedForAssertionsForSleepFocus;
B _idleTimerAllowedForSuppression;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (T@"SBWindowScene",W,N,G_windowScene,S_setWindowScene:,V_windowScene) windowScene;
@property (TB,N,GisAmbientSuppressed,S_setAmbientSuppressed:,V_ambientSuppressed) ambientSuppressed;
@property (TB,N,G_isIdleTimerAllowedForAssertions,S_setIdleTimerAllowedForAssertions:,V_idleTimerAllowedForAssertions) idleTimerAllowedForAssertions;
@property (TB,N,G_isIdleTimerAllowedForAssertionsForSleepFocus,S_setIdleTimerAllowedForAssertionsForSleepFocus:,V_idleTimerAllowedForAssertionsForSleepFocus) idleTimerAllowedForAssertionsForSleepFocus;
@property (TB,N,G_isIdleTimerAllowedForSuppression,S_setIdleTimerAllowedForSuppression:,V_idleTimerAllowedForSuppression) idleTimerAllowedForSuppression;
@property (TB,N,GisUserSleepPredicted,S_setUserSleepPredicted:,V_userSleepPredicted) userSleepPredicted;
@property (T@"<SBFIdleTimerBehaviorProviding>",R,N) idleTimerBehaviorProvider;
@property (TB,N,V_suppressForSleep) suppressForSleep;
@property (Tq,R,N) idleTimerDuration;
@property (Tq,R,N) idleTimerMode;
@property (Tq,R,N) idleWarnMode;
@property (Td,?,R,N) customIdleExpirationTimeout;
@property (Td,?,R,N) customIdleWarningTimeout;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAmbientIdleTimerController backlightController:didTransitionToBacklightState:source:];
-[SBAmbientIdleTimerController _windowScene];
-[SBAmbientIdleTimerController removeObserver:];
-[SBAmbientIdleTimerController dealloc];
-[SBAmbientIdleTimerController releaseInactivityTimerSuppressionIfSuppressed];
-[SBAmbientIdleTimerController idleTimerDuration];
-[SBAmbientIdleTimerController settings:changedValueForKey:];
-[SBAmbientIdleTimerController initWithWindowScene:];
-[SBAmbientIdleTimerController addObserver:];
-[SBAmbientIdleTimerController idleTimerMode];
-[SBAmbientIdleTimerController idleWarnMode];
-[SBAmbientIdleTimerController isUserSleepPredicted];
-[SBAmbientIdleTimerController _restoreAlwaysOnFromSuppression];
-[SBAmbientIdleTimerController _updateMotionDetectionListening];
-[SBAmbientIdleTimerController _startAlwaysOnInactivityTimeout];
-[SBAmbientIdleTimerController _alwaysOnInactivityTimerFired:];
-[SBAmbientIdleTimerController _canPerformMotionWake];
-[SBAmbientIdleTimerController _cancelAlwaysOnInactivityTimer];
-[SBAmbientIdleTimerController _handlePresenceMotion];
-[SBAmbientIdleTimerController _isAlwaysOnPreventedBySuppression];
-[SBAmbientIdleTimerController _isIdleTimerAllowedForAssertions];
-[SBAmbientIdleTimerController _isIdleTimerAllowedForAssertionsForSleepFocus];
-[SBAmbientIdleTimerController _isIdleTimerAllowedForSuppression];
-[SBAmbientIdleTimerController _isMotionDetectionCapable];
-[SBAmbientIdleTimerController _isMotionToWakePermitted];
-[SBAmbientIdleTimerController _isSuppressionActive];
-[SBAmbientIdleTimerController _notifyObserversIdleTimerBehaviorDidChange];
-[SBAmbientIdleTimerController _notifyObserversShouldRestoreAlwaysOn];
-[SBAmbientIdleTimerController _notifyObserversShouldSuppressAlwaysOn];
-[SBAmbientIdleTimerController _notifyObserversSuppressionDidEnd];
-[SBAmbientIdleTimerController _notifyObserversUserSleepPredictedDidChange];
-[SBAmbientIdleTimerController _resetAlwaysOnInactivityTimer];
-[SBAmbientIdleTimerController _setActiveSuppressionReasons:];
-[SBAmbientIdleTimerController _setAmbientSuppressed:];
-[SBAmbientIdleTimerController _setIdleTimerAllowedForAssertions:];
-[SBAmbientIdleTimerController _setIdleTimerAllowedForAssertions:forSleepFocus:];
-[SBAmbientIdleTimerController _setIdleTimerAllowedForAssertionsForSleepFocus:];
-[SBAmbientIdleTimerController _setIdleTimerAllowedForSuppression:];
-[SBAmbientIdleTimerController _setSuppressionEnabled:];
-[SBAmbientIdleTimerController _setUserSleepPredicted:];
-[SBAmbientIdleTimerController _setWindowScene:];
-[SBAmbientIdleTimerController _shouldStartAlwaysOnInactivityTimeout];
-[SBAmbientIdleTimerController _sourcesForMonitoredEvents];
-[SBAmbientIdleTimerController _stopAlwaysOnInactivityTimeout];
-[SBAmbientIdleTimerController _updateAlwaysOnInactivityTimeout];
-[SBAmbientIdleTimerController _updateAmbientSuppressed];
-[SBAmbientIdleTimerController _updateMotionDetectionCapability];
-[SBAmbientIdleTimerController _updateMotionDetectionIdleTimerAssertion];
-[SBAmbientIdleTimerController _updateMotionDetectionWake];
-[SBAmbientIdleTimerController _updateSuppressionManager];
-[SBAmbientIdleTimerController _updateUserSleepPredicted];
-[SBAmbientIdleTimerController idleTimerBehaviorProvider];
-[SBAmbientIdleTimerController isAmbientSuppressed];
-[SBAmbientIdleTimerController motionDetectionWakeAttributeMonitor:didUpdateShouldEnableMotionDetectionWake:];
-[SBAmbientIdleTimerController motionDetectionWakeController:motionDetectStateChanged:];
-[SBAmbientIdleTimerController refreshMotionDetectionWake];
-[SBAmbientIdleTimerController setOnAC:];
-[SBAmbientIdleTimerController setSuppressForSleep:];
-[SBAmbientIdleTimerController suppressForSleep];
```
