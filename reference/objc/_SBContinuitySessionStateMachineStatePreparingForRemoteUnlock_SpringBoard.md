# `_SBContinuitySessionStateMachineStatePreparingForRemoteUnlock`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBContinuitySessionSystemEventMonitorObserver`, `SBContinuityDisplayAuthenticationStateObserver`, `_SBContinuitySessionStateMachineState`, `BSDescriptionStreaming`
- 10 instance variables, 9 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"SBContinuitySessionSystemEventMonitor" _systemEventMonitor;
@"SBContinuityDisplayAuthenticationCoordinator" _authenticationCoordinator;
B _keybagLocked;
B _disabledAutomaticBiometrics;
B _isCurrentState;
B _automaticBiometricsDisabled;
@? _stateUpdateHandler;
@? _stateTransitionHandler;
@? _invalidStateHandler;
@"<_SBContinuitySessionStateMachineClientExternallyBlockedReasonsProvider>" _clientExternallyBlockedReasonsProvider;
```

## Properties

```
@property (TB,N,GisAutomaticBiomtericsDisabled,V_automaticBiometricsDisabled) automaticBiometricsDisabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@?,C,N,V_stateUpdateHandler) stateUpdateHandler;
@property (T@?,C,N,V_stateTransitionHandler) stateTransitionHandler;
@property (T@?,C,N,V_invalidStateHandler) invalidStateHandler;
@property (T@"<_SBContinuitySessionStateMachineClientExternallyBlockedReasonsProvider>",W,N,V_clientExternallyBlockedReasonsProvider) clientExternallyBlockedReasonsProvider;
```

## Instance methods

```
-[_SBContinuitySessionStateMachineStatePreparingForRemoteUnlock invalidate];
-[_SBContinuitySessionStateMachineStatePreparingForRemoteUnlock description];
-[_SBContinuitySessionStateMachineStatePreparingForRemoteUnlock appendDescriptionToStream:];
-[_SBContinuitySessionStateMachineStatePreparingForRemoteUnlock stateTransitionHandler];
-[_SBContinuitySessionStateMachineStatePreparingForRemoteUnlock setAutomaticBiometricsDisabled:];
-[_SBContinuitySessionStateMachineStatePreparingForRemoteUnlock _evaluateClientExternallyBlockedReasons];
-[_SBContinuitySessionStateMachineStatePreparingForRemoteUnlock _evaluateLockState];
-[_SBContinuitySessionStateMachineStatePreparingForRemoteUnlock _evaluateSystemEvents];
-[_SBContinuitySessionStateMachineStatePreparingForRemoteUnlock _reevaluateStateForReason:];
-[_SBContinuitySessionStateMachineStatePreparingForRemoteUnlock clientExternallyBlockedReasonsProvider];
-[_SBContinuitySessionStateMachineStatePreparingForRemoteUnlock continuityDisplayAuthenticationCoordinatorDidUpdateLockState:];
-[_SBContinuitySessionStateMachineStatePreparingForRemoteUnlock continuitySessionSystemEventMonitor:eventOccurred:];
-[_SBContinuitySessionStateMachineStatePreparingForRemoteUnlock enteredStateFrom:];
-[_SBContinuitySessionStateMachineStatePreparingForRemoteUnlock exitedStateTo:];
-[_SBContinuitySessionStateMachineStatePreparingForRemoteUnlock initWithSystemEventMonitor:continuityDisplayAuthenticationCoordinator:];
-[_SBContinuitySessionStateMachineStatePreparingForRemoteUnlock invalidStateHandler];
-[_SBContinuitySessionStateMachineStatePreparingForRemoteUnlock isAutomaticBiomtericsDisabled];
-[_SBContinuitySessionStateMachineStatePreparingForRemoteUnlock noteClientDidUpdateExternallyBlockedReasons];
-[_SBContinuitySessionStateMachineStatePreparingForRemoteUnlock setClientExternallyBlockedReasonsProvider:];
-[_SBContinuitySessionStateMachineStatePreparingForRemoteUnlock setInvalidStateHandler:];
-[_SBContinuitySessionStateMachineStatePreparingForRemoteUnlock setStateTransitionHandler:];
-[_SBContinuitySessionStateMachineStatePreparingForRemoteUnlock setStateUpdateHandler:];
-[_SBContinuitySessionStateMachineStatePreparingForRemoteUnlock stateUpdateHandler];
```
