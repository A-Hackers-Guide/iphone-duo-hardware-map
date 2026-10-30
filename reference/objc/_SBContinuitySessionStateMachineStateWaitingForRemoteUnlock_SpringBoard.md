# `_SBContinuitySessionStateMachineStateWaitingForRemoteUnlock`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBContinuitySessionSystemEventMonitorObserver`, `SBContinuityDisplayAuthenticationStateObserver`, `_SBContinuitySessionStateMachineState`, `BSDescriptionStreaming`
- 8 instance variables, 8 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"SBContinuitySessionSystemEventMonitor" _systemEventMonitor;
@"SBContinuityDisplayAuthenticationCoordinator" _authenticationCoordinator;
B _remoteUnlocked;
B _isCurrentState;
@? _stateUpdateHandler;
@? _stateTransitionHandler;
@? _invalidStateHandler;
@"<_SBContinuitySessionStateMachineClientExternallyBlockedReasonsProvider>" _clientExternallyBlockedReasonsProvider;
```

## Properties

```
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
-[_SBContinuitySessionStateMachineStateWaitingForRemoteUnlock invalidate];
-[_SBContinuitySessionStateMachineStateWaitingForRemoteUnlock description];
-[_SBContinuitySessionStateMachineStateWaitingForRemoteUnlock appendDescriptionToStream:];
-[_SBContinuitySessionStateMachineStateWaitingForRemoteUnlock stateTransitionHandler];
-[_SBContinuitySessionStateMachineStateWaitingForRemoteUnlock _evaluateClientExternallyBlockedReasons];
-[_SBContinuitySessionStateMachineStateWaitingForRemoteUnlock _evaluateLockState];
-[_SBContinuitySessionStateMachineStateWaitingForRemoteUnlock _evaluateSystemEvents];
-[_SBContinuitySessionStateMachineStateWaitingForRemoteUnlock _reevaluateStateForReason:];
-[_SBContinuitySessionStateMachineStateWaitingForRemoteUnlock clientExternallyBlockedReasonsProvider];
-[_SBContinuitySessionStateMachineStateWaitingForRemoteUnlock continuityDisplayAuthenticationCoordinatorDidUpdateLockState:];
-[_SBContinuitySessionStateMachineStateWaitingForRemoteUnlock continuitySessionSystemEventMonitor:eventOccurred:];
-[_SBContinuitySessionStateMachineStateWaitingForRemoteUnlock enteredStateFrom:];
-[_SBContinuitySessionStateMachineStateWaitingForRemoteUnlock exitedStateTo:];
-[_SBContinuitySessionStateMachineStateWaitingForRemoteUnlock initWithSystemEventMonitor:continuityDisplayAuthenticationCoordinator:];
-[_SBContinuitySessionStateMachineStateWaitingForRemoteUnlock invalidStateHandler];
-[_SBContinuitySessionStateMachineStateWaitingForRemoteUnlock noteClientDidUpdateExternallyBlockedReasons];
-[_SBContinuitySessionStateMachineStateWaitingForRemoteUnlock setClientExternallyBlockedReasonsProvider:];
-[_SBContinuitySessionStateMachineStateWaitingForRemoteUnlock setInvalidStateHandler:];
-[_SBContinuitySessionStateMachineStateWaitingForRemoteUnlock setStateTransitionHandler:];
-[_SBContinuitySessionStateMachineStateWaitingForRemoteUnlock setStateUpdateHandler:];
-[_SBContinuitySessionStateMachineStateWaitingForRemoteUnlock stateUpdateHandler];
```
