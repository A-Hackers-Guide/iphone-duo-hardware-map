# `SBLockScreenSessionAnalyticsEvent`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 46 instance variables, 46 properties, 94 instance methods, 0 class methods

## Instance variables

```
B _didInteract;
B _didRestToOpen;
B _didUnlock;
B _didLock;
B _didLockout;
B _didEnterLockout;
B _didShowNotificationPreview;
B _didShowNotificationCenter;
B _hadNotifications;
B _pauEnabled;
B _inPocketAtWake;
B _inPocketAtFirstAttempt;
B _inPocketAtUnlock;
B _faceDownAtWake;
B _faceDownAtFirstAttempt;
B _faceDownAtUnlock;
q _wakeReason;
q _tapToWakeLocation;
q _destination;
q _launchOrigin;
q _secureApp;
q _dismissalMethod;
q _lockReason;
Q _authenticationFailureCount;
q _unlockMethod;
d _displayAwakeDuration;
d _timeSinceLastLockScreenExit;
q _poseAtWake;
q _poseAtUnlock;
q _orientationAtWake;
q _orientationAtUnlock;
q _notificationPreviewSetting;
Q _authenticationAttemptCount;
d _firstAuthenticationAttemptDelay;
d _authenticationAttemptIntervalMin;
d _authenticationAttemptIntervalMean;
d _authenticationAttemptIntervalMax;
d _timeSinceLastMatchSuccess;
d _timeSinceLastMatchFailure;
q _motionActivityAtFirstAttempt;
q _motionActivityAtUnlock;
q _poseAtFirstAttempt;
q _orientationAtFirstAttempt;
q _deviceOrientationAtWake;
q _deviceOrientationAtFirstAttempt;
q _deviceOrientationAtUnlock;
```

## Properties

```
@property (Tq,N,V_wakeReason) wakeReason;
@property (Tq,N,V_tapToWakeLocation) tapToWakeLocation;
@property (TB,N,V_didInteract) didInteract;
@property (Tq,N,V_destination) destination;
@property (Tq,N,V_launchOrigin) launchOrigin;
@property (Tq,N,V_secureApp) secureApp;
@property (Tq,N,V_dismissalMethod) dismissalMethod;
@property (TB,N,V_didRestToOpen) didRestToOpen;
@property (TB,N,V_didUnlock) didUnlock;
@property (TB,N,V_didLock) didLock;
@property (Tq,N,V_lockReason) lockReason;
@property (TB,N,V_didLockout) didLockout;
@property (TB,N,V_didEnterLockout) didEnterLockout;
@property (TB,N,V_didShowNotificationPreview) didShowNotificationPreview;
@property (TB,N,V_didShowNotificationCenter) didShowNotificationCenter;
@property (TQ,N,V_authenticationFailureCount) authenticationFailureCount;
@property (Tq,N,V_unlockMethod) unlockMethod;
@property (Td,N,V_displayAwakeDuration) displayAwakeDuration;
@property (Td,N,V_timeSinceLastLockScreenExit) timeSinceLastLockScreenExit;
@property (TB,N,V_hadNotifications) hadNotifications;
@property (Tq,N,V_poseAtWake) poseAtWake;
@property (Tq,N,V_poseAtUnlock) poseAtUnlock;
@property (Tq,N,V_orientationAtWake) orientationAtWake;
@property (Tq,N,V_orientationAtUnlock) orientationAtUnlock;
@property (TB,N,GisPAUEnabled,V_pauEnabled) pauEnabled;
@property (Tq,N,V_notificationPreviewSetting) notificationPreviewSetting;
@property (TQ,N,V_authenticationAttemptCount) authenticationAttemptCount;
@property (Td,N,V_firstAuthenticationAttemptDelay) firstAuthenticationAttemptDelay;
@property (Td,N,V_authenticationAttemptIntervalMin) authenticationAttemptIntervalMin;
@property (Td,N,V_authenticationAttemptIntervalMean) authenticationAttemptIntervalMean;
@property (Td,N,V_authenticationAttemptIntervalMax) authenticationAttemptIntervalMax;
@property (TB,N,V_inPocketAtWake) inPocketAtWake;
@property (TB,N,V_inPocketAtFirstAttempt) inPocketAtFirstAttempt;
@property (TB,N,V_inPocketAtUnlock) inPocketAtUnlock;
@property (TB,N,V_faceDownAtWake) faceDownAtWake;
@property (TB,N,V_faceDownAtFirstAttempt) faceDownAtFirstAttempt;
@property (TB,N,V_faceDownAtUnlock) faceDownAtUnlock;
@property (Tq,N,V_motionActivityAtFirstAttempt) motionActivityAtFirstAttempt;
@property (Tq,N,V_motionActivityAtUnlock) motionActivityAtUnlock;
@property (Tq,N,V_poseAtFirstAttempt) poseAtFirstAttempt;
@property (Tq,N,V_orientationAtFirstAttempt) orientationAtFirstAttempt;
@property (Tq,N,V_deviceOrientationAtWake) deviceOrientationAtWake;
@property (Tq,N,V_deviceOrientationAtFirstAttempt) deviceOrientationAtFirstAttempt;
@property (Tq,N,V_deviceOrientationAtUnlock) deviceOrientationAtUnlock;
@property (Td,N,V_timeSinceLastMatchSuccess) timeSinceLastMatchSuccess;
@property (Td,N,V_timeSinceLastMatchFailure) timeSinceLastMatchFailure;
```

## Instance methods

```
-[SBLockScreenSessionAnalyticsEvent destination];
-[SBLockScreenSessionAnalyticsEvent init];
-[SBLockScreenSessionAnalyticsEvent setDestination:];
-[SBLockScreenSessionAnalyticsEvent description];
-[SBLockScreenSessionAnalyticsEvent lockReason];
-[SBLockScreenSessionAnalyticsEvent setLockReason:];
-[SBLockScreenSessionAnalyticsEvent didLock];
-[SBLockScreenSessionAnalyticsEvent didUnlock];
-[SBLockScreenSessionAnalyticsEvent setDidInteract:];
-[SBLockScreenSessionAnalyticsEvent didInteract];
-[SBLockScreenSessionAnalyticsEvent launchOrigin];
-[SBLockScreenSessionAnalyticsEvent setLaunchOrigin:];
-[SBLockScreenSessionAnalyticsEvent setTimeSinceLastLockScreenExit:];
-[SBLockScreenSessionAnalyticsEvent deviceOrientationAtFirstAttempt];
-[SBLockScreenSessionAnalyticsEvent didEnterLockout];
-[SBLockScreenSessionAnalyticsEvent dismissalMethod];
-[SBLockScreenSessionAnalyticsEvent firstAuthenticationAttemptDelay];
-[SBLockScreenSessionAnalyticsEvent authenticationAttemptCount];
-[SBLockScreenSessionAnalyticsEvent authenticationAttemptIntervalMax];
-[SBLockScreenSessionAnalyticsEvent authenticationAttemptIntervalMean];
-[SBLockScreenSessionAnalyticsEvent authenticationAttemptIntervalMin];
-[SBLockScreenSessionAnalyticsEvent authenticationFailureCount];
-[SBLockScreenSessionAnalyticsEvent deviceOrientationAtUnlock];
-[SBLockScreenSessionAnalyticsEvent deviceOrientationAtWake];
-[SBLockScreenSessionAnalyticsEvent didLockout];
-[SBLockScreenSessionAnalyticsEvent didRestToOpen];
-[SBLockScreenSessionAnalyticsEvent didShowNotificationCenter];
-[SBLockScreenSessionAnalyticsEvent didShowNotificationPreview];
-[SBLockScreenSessionAnalyticsEvent displayAwakeDuration];
-[SBLockScreenSessionAnalyticsEvent faceDownAtFirstAttempt];
-[SBLockScreenSessionAnalyticsEvent faceDownAtUnlock];
-[SBLockScreenSessionAnalyticsEvent faceDownAtWake];
-[SBLockScreenSessionAnalyticsEvent hadNotifications];
-[SBLockScreenSessionAnalyticsEvent inPocketAtFirstAttempt];
-[SBLockScreenSessionAnalyticsEvent inPocketAtUnlock];
-[SBLockScreenSessionAnalyticsEvent inPocketAtWake];
-[SBLockScreenSessionAnalyticsEvent isPAUEnabled];
-[SBLockScreenSessionAnalyticsEvent motionActivityAtFirstAttempt];
-[SBLockScreenSessionAnalyticsEvent motionActivityAtUnlock];
-[SBLockScreenSessionAnalyticsEvent notificationPreviewSetting];
-[SBLockScreenSessionAnalyticsEvent orientationAtFirstAttempt];
-[SBLockScreenSessionAnalyticsEvent orientationAtUnlock];
-[SBLockScreenSessionAnalyticsEvent orientationAtWake];
-[SBLockScreenSessionAnalyticsEvent poseAtFirstAttempt];
-[SBLockScreenSessionAnalyticsEvent poseAtUnlock];
-[SBLockScreenSessionAnalyticsEvent poseAtWake];
-[SBLockScreenSessionAnalyticsEvent secureApp];
-[SBLockScreenSessionAnalyticsEvent setAuthenticationAttemptCount:];
-[SBLockScreenSessionAnalyticsEvent setAuthenticationAttemptIntervalMax:];
-[SBLockScreenSessionAnalyticsEvent setAuthenticationAttemptIntervalMean:];
-[SBLockScreenSessionAnalyticsEvent setAuthenticationAttemptIntervalMin:];
-[SBLockScreenSessionAnalyticsEvent setAuthenticationFailureCount:];
-[SBLockScreenSessionAnalyticsEvent setDeviceOrientationAtFirstAttempt:];
-[SBLockScreenSessionAnalyticsEvent setDeviceOrientationAtUnlock:];
-[SBLockScreenSessionAnalyticsEvent setDeviceOrientationAtWake:];
-[SBLockScreenSessionAnalyticsEvent setDidEnterLockout:];
-[SBLockScreenSessionAnalyticsEvent setDidLock:];
-[SBLockScreenSessionAnalyticsEvent setDidLockout:];
-[SBLockScreenSessionAnalyticsEvent setDidRestToOpen:];
-[SBLockScreenSessionAnalyticsEvent setDidShowNotificationCenter:];
-[SBLockScreenSessionAnalyticsEvent setDidShowNotificationPreview:];
-[SBLockScreenSessionAnalyticsEvent setDidUnlock:];
-[SBLockScreenSessionAnalyticsEvent setDismissalMethod:];
-[SBLockScreenSessionAnalyticsEvent setDisplayAwakeDuration:];
-[SBLockScreenSessionAnalyticsEvent setFaceDownAtFirstAttempt:];
-[SBLockScreenSessionAnalyticsEvent setFaceDownAtUnlock:];
-[SBLockScreenSessionAnalyticsEvent setFaceDownAtWake:];
-[SBLockScreenSessionAnalyticsEvent setFirstAuthenticationAttemptDelay:];
-[SBLockScreenSessionAnalyticsEvent setHadNotifications:];
-[SBLockScreenSessionAnalyticsEvent setInPocketAtFirstAttempt:];
-[SBLockScreenSessionAnalyticsEvent setInPocketAtUnlock:];
-[SBLockScreenSessionAnalyticsEvent setInPocketAtWake:];
-[SBLockScreenSessionAnalyticsEvent setMotionActivityAtFirstAttempt:];
-[SBLockScreenSessionAnalyticsEvent setMotionActivityAtUnlock:];
-[SBLockScreenSessionAnalyticsEvent setNotificationPreviewSetting:];
-[SBLockScreenSessionAnalyticsEvent setOrientationAtFirstAttempt:];
-[SBLockScreenSessionAnalyticsEvent setOrientationAtUnlock:];
-[SBLockScreenSessionAnalyticsEvent setOrientationAtWake:];
-[SBLockScreenSessionAnalyticsEvent setPauEnabled:];
-[SBLockScreenSessionAnalyticsEvent setPoseAtFirstAttempt:];
-[SBLockScreenSessionAnalyticsEvent setPoseAtUnlock:];
-[SBLockScreenSessionAnalyticsEvent setPoseAtWake:];
-[SBLockScreenSessionAnalyticsEvent setSecureApp:];
-[SBLockScreenSessionAnalyticsEvent setTapToWakeLocation:];
-[SBLockScreenSessionAnalyticsEvent setTimeSinceLastMatchFailure:];
-[SBLockScreenSessionAnalyticsEvent setTimeSinceLastMatchSuccess:];
-[SBLockScreenSessionAnalyticsEvent setUnlockMethod:];
-[SBLockScreenSessionAnalyticsEvent setWakeReason:];
-[SBLockScreenSessionAnalyticsEvent tapToWakeLocation];
-[SBLockScreenSessionAnalyticsEvent timeSinceLastLockScreenExit];
-[SBLockScreenSessionAnalyticsEvent timeSinceLastMatchFailure];
-[SBLockScreenSessionAnalyticsEvent timeSinceLastMatchSuccess];
-[SBLockScreenSessionAnalyticsEvent unlockMethod];
-[SBLockScreenSessionAnalyticsEvent wakeReason];
```
