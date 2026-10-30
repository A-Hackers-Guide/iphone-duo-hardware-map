# `_SBContinuitySessionStateMachineStateUpdatingActiveDisplay`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBContinuitySessionSystemEventMonitorObserver`, `SBContinuityDisplayAuthenticationStateObserver`, `_SBContinuitySessionStateMachineState`, `BSDescriptionStreaming`
- 8 instance variables, 8 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"SBContinuitySessionSystemEventMonitor" _systemEventMonitor;
@"SBContinuityDisplayAuthenticationCoordinator" _authenticationCoordinator;
B _updatedActiveDisplay;
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
-[_SBContinuitySessionStateMachineStateUpdatingActiveDisplay invalidate];
-[_SBContinuitySessionStateMachineStateUpdatingActiveDisplay description];
-[_SBContinuitySessionStateMachineStateUpdatingActiveDisplay appendDescriptionToStream:];
-[_SBContinuitySessionStateMachineStateUpdatingActiveDisplay stateTransitionHandler];
-[_SBContinuitySessionStateMachineStateUpdatingActiveDisplay _evaluateClientExternallyBlockedReasons];
-[_SBContinuitySessionStateMachineStateUpdatingActiveDisplay _evaluateLockState];
-[_SBContinuitySessionStateMachineStateUpdatingActiveDisplay _evaluateSystemEvents];
-[_SBContinuitySessionStateMachineStateUpdatingActiveDisplay _reevaluateStateForReason:];
-[_SBContinuitySessionStateMachineStateUpdatingActiveDisplay clientExternallyBlockedReasonsProvider];
-[_SBContinuitySessionStateMachineStateUpdatingActiveDisplay continuityDisplayAuthenticationCoordinatorDidUpdateLockState:];
-[_SBContinuitySessionStateMachineStateUpdatingActiveDisplay continuitySessionSystemEventMonitor:eventOccurred:];
-[_SBContinuitySessionStateMachineStateUpdatingActiveDisplay enteredStateFrom:];
-[_SBContinuitySessionStateMachineStateUpdatingActiveDisplay exitedStateTo:];
-[_SBContinuitySessionStateMachineStateUpdatingActiveDisplay initWithSystemEventMonitor:continuityDisplayAuthenticationCoordinator:];
-[_SBContinuitySessionStateMachineStateUpdatingActiveDisplay invalidStateHandler];
-[_SBContinuitySessionStateMachineStateUpdatingActiveDisplay noteActiveDisplayUpdated];
-[_SBContinuitySessionStateMachineStateUpdatingActiveDisplay noteClientDidUpdateExternallyBlockedReasons];
-[_SBContinuitySessionStateMachineStateUpdatingActiveDisplay setClientExternallyBlockedReasonsProvider:];
-[_SBContinuitySessionStateMachineStateUpdatingActiveDisplay setInvalidStateHandler:];
-[_SBContinuitySessionStateMachineStateUpdatingActiveDisplay setStateTransitionHandler:];
-[_SBContinuitySessionStateMachineStateUpdatingActiveDisplay setStateUpdateHandler:];
-[_SBContinuitySessionStateMachineStateUpdatingActiveDisplay stateUpdateHandler];
```
