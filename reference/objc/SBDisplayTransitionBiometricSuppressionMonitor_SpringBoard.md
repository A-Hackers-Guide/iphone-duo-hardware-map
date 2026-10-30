# `SBDisplayTransitionBiometricSuppressionMonitor`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBDisplayContentModeTransitionObserver`
- 5 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"SBDisplayContentModeCoordinator" _displayContentModeCoordinator;
@"SBLockScreenCoordinator" _lockScreenCoordinator;
@"<BSInvalidatable>" _biometricAssertion;
@"NSTimer" _settlingTimer;
@"SBDisplayTransitionBiometricSuppressionSettings" _settings;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDisplayTransitionBiometricSuppressionMonitor displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBDisplayTransitionBiometricSuppressionMonitor dealloc];
-[SBDisplayTransitionBiometricSuppressionMonitor displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBDisplayTransitionBiometricSuppressionMonitor _acquireAssertion];
-[SBDisplayTransitionBiometricSuppressionMonitor _releaseAssertion];
-[SBDisplayTransitionBiometricSuppressionMonitor _startSettlingTimer];
-[SBDisplayTransitionBiometricSuppressionMonitor initWithDisplayContentModeCoordinator:lockScreenCoordinator:];
```
