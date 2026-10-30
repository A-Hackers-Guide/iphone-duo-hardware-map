# `SBLockScreenSessionAnalyticsCollector`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 1 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"<SBLockScreenSessionAnalyticsEnvironment>" _environment;
@"<SBLockScreenSessionAnalyticsReporting>" _reporter;
@? _timeProvider;
@"SBLockScreenSessionAnalyticsEvent" _activeEvent;
d _activeSessionWakeTime;
d _lastLockScreenExitTime;
d _lastMatchSuccessTime;
d _lastMatchFailureTime;
d _lastMatchAttemptTime;
d _matchAttemptIntervalSum;
q _currentSecureApp;
@"NSMutableArray" _pendingMatchAttempts;
q _pendingUnlockMethod;
d _pendingUnlockTime;
```

## Properties

```
@property (TB,R,N,GisSessionActive) sessionActive;
```

## Instance methods

```
-[SBLockScreenSessionAnalyticsCollector isSessionActive];
-[SBLockScreenSessionAnalyticsCollector _applyPendingNotes];
-[SBLockScreenSessionAnalyticsCollector _endActiveSession];
-[SBLockScreenSessionAnalyticsCollector _expirePendingNotesAtTime:];
-[SBLockScreenSessionAnalyticsCollector _recordMatchAttemptWithSuccess:reachedLockout:atTime:];
-[SBLockScreenSessionAnalyticsCollector _recordMatchTimeWithSuccess:atTime:];
-[SBLockScreenSessionAnalyticsCollector _setEnvironmentMonitoringActive:];
-[SBLockScreenSessionAnalyticsCollector _startSessionWithWakeReason:tapToWakeLocation:];
-[SBLockScreenSessionAnalyticsCollector initWithEnvironment:reporter:];
-[SBLockScreenSessionAnalyticsCollector initWithEnvironment:reporter:timeProvider:];
-[SBLockScreenSessionAnalyticsCollector noteBiometricLockout];
-[SBLockScreenSessionAnalyticsCollector noteBiometricMatchAttemptWithSuccess:];
-[SBLockScreenSessionAnalyticsCollector noteBiometricMatchAttemptWithSuccess:reachedLockout:];
-[SBLockScreenSessionAnalyticsCollector noteDeviceDidLockAndSleepWithReason:];
-[SBLockScreenSessionAnalyticsCollector noteDeviceDidWakeWithReason:tapToWakeLocation:];
-[SBLockScreenSessionAnalyticsCollector noteDidLeaveLockScreenToDestination:launchOrigin:dismissalMethod:];
-[SBLockScreenSessionAnalyticsCollector noteDidReturnToLockScreenFromDestination:];
-[SBLockScreenSessionAnalyticsCollector noteNotificationCenterShown];
-[SBLockScreenSessionAnalyticsCollector noteNotificationPreviewShown];
-[SBLockScreenSessionAnalyticsCollector noteRestToOpen];
-[SBLockScreenSessionAnalyticsCollector noteSecureAppDidChange:];
-[SBLockScreenSessionAnalyticsCollector noteUnlockWithMethod:];
-[SBLockScreenSessionAnalyticsCollector noteUserInteraction];
```
