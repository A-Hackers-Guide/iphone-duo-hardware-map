# `CAMLibrarySelectionSession`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 14 properties, 28 instance methods, 0 class methods

## Instance variables

```
B _restoredFromPreferences;
B _canResetToDefaultMode;
B _overriddenByUser;
B _userWasPreviouslyOnTrip;
@"<CAMLibrarySelectionDelegate>" _delegate;
q _initialMode;
q _currentMode;
q _userInteractionsCount;
d _timeToDetectDevicesInProximity;
d _timeToAcquireFirstLocation;
d _timeToAcquireFirstPreciseLocation;
d _timeForSmartSharingAutoDecision;
d _timeForUserManualOverride;
@"NSDate" _launchDate;
```

## Properties

```
@property (T@"NSDate",&,N,V_launchDate) launchDate;
@property (T@"<CAMLibrarySelectionDelegate>",W,N,V_delegate) delegate;
@property (Tq,R,N,V_initialMode) initialMode;
@property (Tq,R,N,V_currentMode) currentMode;
@property (Tq,R,N,V_userInteractionsCount) userInteractionsCount;
@property (TB,R,N,V_restoredFromPreferences) restoredFromPreferences;
@property (TB,R,N,V_canResetToDefaultMode) canResetToDefaultMode;
@property (TB,R,N,V_overriddenByUser) overriddenByUser;
@property (TB,R,N,V_userWasPreviouslyOnTrip) userWasPreviouslyOnTrip;
@property (Td,R,N,V_timeToDetectDevicesInProximity) timeToDetectDevicesInProximity;
@property (Td,R,N,V_timeToAcquireFirstLocation) timeToAcquireFirstLocation;
@property (Td,R,N,V_timeToAcquireFirstPreciseLocation) timeToAcquireFirstPreciseLocation;
@property (Td,R,N,V_timeForSmartSharingAutoDecision) timeForSmartSharingAutoDecision;
@property (Td,R,N,V_timeForUserManualOverride) timeForUserManualOverride;
```

## Instance methods

```
-[CAMLibrarySelectionSession currentMode];
-[CAMLibrarySelectionSession initWithMode:];
-[CAMLibrarySelectionSession setDelegate:];
-[CAMLibrarySelectionSession delegate];
-[CAMLibrarySelectionSession updateWithResult:];
-[CAMLibrarySelectionSession launchDate];
-[CAMLibrarySelectionSession setLaunchDate:];
-[CAMLibrarySelectionSession timeForSmartSharingAutoDecision];
-[CAMLibrarySelectionSession updateWithMode:];
-[CAMLibrarySelectionSession _applyAutoResetModeAndNotify:];
-[CAMLibrarySelectionSession _autoResetMode];
-[CAMLibrarySelectionSession _canResetDuringSessionWithResult:];
-[CAMLibrarySelectionSession _canTransitionToAutoOn];
-[CAMLibrarySelectionSession _defaultMode];
-[CAMLibrarySelectionSession _shouldResetDuringSessionWithResult:];
-[CAMLibrarySelectionSession _shouldResetSessionBasedOnTimeoutDuringTrip:atSameLocation:];
-[CAMLibrarySelectionSession _userWasPreviouslyOnTrip];
-[CAMLibrarySelectionSession canResetToDefaultMode];
-[CAMLibrarySelectionSession initialMode];
-[CAMLibrarySelectionSession notifyResetIfNeeded];
-[CAMLibrarySelectionSession overriddenByUser];
-[CAMLibrarySelectionSession restoredFromPreferences];
-[CAMLibrarySelectionSession timeForUserManualOverride];
-[CAMLibrarySelectionSession timeToAcquireFirstLocation];
-[CAMLibrarySelectionSession timeToAcquireFirstPreciseLocation];
-[CAMLibrarySelectionSession timeToDetectDevicesInProximity];
-[CAMLibrarySelectionSession userInteractionsCount];
-[CAMLibrarySelectionSession userWasPreviouslyOnTrip];
```
