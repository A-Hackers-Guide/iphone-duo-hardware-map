# `_SBContinuitySessionStateMachineStateFlushing`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBContinuitySessionSystemEventMonitorObserver`, `SBContinuityDisplayAuthenticationStateObserver`, `_SBContinuitySessionStateMachineState`, `BSDescriptionStreaming`
- 8 instance variables, 8 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"SBContinuitySessionSystemEventMonitor" _systemEventMonitor;
@"SBContinuityDisplayAuthenticationCoordinator" _authenticationCoordinator;
B _uiFlushed;
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
-[_SBContinuitySessionStateMachineStateFlushing invalidate];
-[_SBContinuitySessionStateMachineStateFlushing description];
-[_SBContinuitySessionStateMachineStateFlushing appendDescriptionToStream:];
-[_SBContinuitySessionStateMachineStateFlushing stateTransitionHandler];
-[_SBContinuitySessionStateMachineStateFlushing _evaluateClientExternallyBlockedReasons];
-[_SBContinuitySessionStateMachineStateFlushing _evaluateLockState];
-[_SBContinuitySessionStateMachineStateFlushing _evaluateSystemEvents];
-[_SBContinuitySessionStateMachineStateFlushing _reevaluateStateForReason:];
-[_SBContinuitySessionStateMachineStateFlushing clientExternallyBlockedReasonsProvider];
-[_SBContinuitySessionStateMachineStateFlushing continuityDisplayAuthenticationCoordinatorDidUpdateLockState:];
-[_SBContinuitySessionStateMachineStateFlushing continuitySessionSystemEventMonitor:eventOccurred:];
-[_SBContinuitySessionStateMachineStateFlushing enteredStateFrom:];
-[_SBContinuitySessionStateMachineStateFlushing exitedStateTo:];
-[_SBContinuitySessionStateMachineStateFlushing initWithSystemEventMonitor:continuityDisplayAuthenticationCoordinator:];
-[_SBContinuitySessionStateMachineStateFlushing invalidStateHandler];
-[_SBContinuitySessionStateMachineStateFlushing noteClientDidUpdateExternallyBlockedReasons];
-[_SBContinuitySessionStateMachineStateFlushing noteUIFlushed];
-[_SBContinuitySessionStateMachineStateFlushing setClientExternallyBlockedReasonsProvider:];
-[_SBContinuitySessionStateMachineStateFlushing setInvalidStateHandler:];
-[_SBContinuitySessionStateMachineStateFlushing setStateTransitionHandler:];
-[_SBContinuitySessionStateMachineStateFlushing setStateUpdateHandler:];
-[_SBContinuitySessionStateMachineStateFlushing stateUpdateHandler];
```
