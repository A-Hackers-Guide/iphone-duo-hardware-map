# `SBAccidentalActivationMitigationHostSession`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBIdleTimerObserving`, `SBSAccidentalActivationMitigationSession`
- 11 instance variables, 10 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"SBCaptureButtonSuppressionManager" _suppressionManager;
@"SBLiftToWakeController" _liftToWakeController;
@"<SBSAccidentalActivationMitigationSessionCancellationPolicy>" _cancellationPolicy;
@"NSHashTable" _observers;
@"<SBIdleTimer>" _idleTimer;
B _mitigatedEarly;
q _state;
@"<SBAccidentalActivationMitigationHostSessionDelegate>" _delegate;
@"NSString" _bundleIdentifier;
d _duration;
@"NSString" _cancellationPolicyClassName;
```

## Properties

```
@property (Tq,N,V_state) state;
@property (T@"<SBAccidentalActivationMitigationHostSessionDelegate>",&,N,V_delegate) delegate;
@property (T@"NSString",R,C,N,V_bundleIdentifier) bundleIdentifier;
@property (Td,R,N,V_duration) duration;
@property (T@"NSString",R,N,V_cancellationPolicyClassName) cancellationPolicyClassName;
@property (TB,R,N,V_mitigatedEarly) mitigatedEarly;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAccidentalActivationMitigationHostSession setState:];
-[SBAccidentalActivationMitigationHostSession removeObserver:];
-[SBAccidentalActivationMitigationHostSession bundleIdentifier];
-[SBAccidentalActivationMitigationHostSession duration];
-[SBAccidentalActivationMitigationHostSession idleTimerDidExpire:];
-[SBAccidentalActivationMitigationHostSession addObserver:];
-[SBAccidentalActivationMitigationHostSession setDelegate:];
-[SBAccidentalActivationMitigationHostSession delegate];
-[SBAccidentalActivationMitigationHostSession state];
-[SBAccidentalActivationMitigationHostSession activateSessionForBundleIdentifier:duration:accidentalActivationMitigationSessionCancellationPolicyClassName:];
-[SBAccidentalActivationMitigationHostSession requestSessionCancellation];
-[SBAccidentalActivationMitigationHostSession cancellationPolicyClassName];
-[SBAccidentalActivationMitigationHostSession initWithSuppressionManager:liftToWakeController:];
-[SBAccidentalActivationMitigationHostSession mitigatedEarly];
-[SBAccidentalActivationMitigationHostSession requestSessionMitigateEarly];
```
