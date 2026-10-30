# `BLSHWatchdogProvider`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 1 properties, 22 instance methods, 6 class methods

## Instance variables

```
@"BSAbsoluteMachTimer" _lock_fireRetryTimer;
@"BLSHWatchdogAbortParameters" _lock_waitingAbortParams;
B _lock_waitingForTailspin;
B _lock_startedTailspin;
B _lock_waitingForWatchdogCompletion;
@"<BSInvalidatable>" _lock_forceOverdueAbortTimer;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"<BLSHWatchdogProviderDelegate>" _providerDelegate;
B _watchdogEnabled;
```

## Properties

```
@property (TB,GisWatchdogEnabled,V_watchdogEnabled) watchdogEnabled;
```

## Class methods

```
+[BLSHWatchdogProvider checkForWatchdogDidFire:];
+[BLSHWatchdogProvider ignoreWatchdogAborts];
+[BLSHWatchdogProvider markWatchdogDidFire:abortReason:];
+[BLSHWatchdogProvider resetWatchdogDidFire];
+[BLSHWatchdogProvider setIgnoreWatchdogAborts:];
+[BLSHWatchdogProvider showWatchdogDidFireAlert:];
```

## Instance methods

```
-[BLSHWatchdogProvider isTesting];
-[BLSHWatchdogProvider registerHandlersForService:];
-[BLSHWatchdogProvider initWithDelegate:];
-[BLSHWatchdogProvider dealloc];
-[BLSHWatchdogProvider scheduleWatchdogWithDelegate:explanation:timeout:];
-[BLSHWatchdogProvider didDetectSignificantUserInteraction];
-[BLSHWatchdogProvider _abortForWatchdogFire:];
-[BLSHWatchdogProvider _checkForReadyToAbortAfterWaitingPastFire];
-[BLSHWatchdogProvider _clearIsWaitingForWatchdogCompletion];
-[BLSHWatchdogProvider _fireWatchdogWithTimer:delegate:timeout:elapsedTime:abortContext:explanation:remainingRetries:];
-[BLSHWatchdogProvider _giveUpWaitingForWatchdogCompletionAbortWhileWaitingPastFire:];
-[BLSHWatchdogProvider _startWritingTailspin];
-[BLSHWatchdogProvider clearWatchdogWithExplanation:reason:timeout:elapsedTime:];
-[BLSHWatchdogProvider fireWatchdogWithTimer:delegate:timeout:elapsedTime:];
-[BLSHWatchdogProvider isWaitingwaitingPastFireForCompletionAndTailspin];
-[BLSHWatchdogProvider isWatchdogEnabled];
-[BLSHWatchdogProvider listenForOSStartupComplete];
-[BLSHWatchdogProvider makeStartupCheck];
-[BLSHWatchdogProvider prepareForStartupCheck];
-[BLSHWatchdogProvider setWaitingwaitingPastFireForCompletionAndTailspin:waitForWatchdogCompletion:];
-[BLSHWatchdogProvider setWatchdogEnabled:];
-[BLSHWatchdogProvider waitingPastFireForCompletionAndTailspinAbortParams];
```
