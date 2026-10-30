# `_SBContinuitySessionStateMachineStateActive`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBContinuitySessionSystemEventMonitorObserver`, `SBContinuityDisplayAuthenticationStateObserver`, `_SBContinuitySessionStateMachineState`, `BSDescriptionStreaming`
- 7 instance variables, 8 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"SBContinuitySessionSystemEventMonitor" _systemEventMonitor;
@"SBContinuityDisplayAuthenticationCoordinator" _authenticationCoordinator;
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
-[_SBContinuitySessionStateMachineStateActive invalidate];
-[_SBContinuitySessionStateMachineStateActive description];
-[_SBContinuitySessionStateMachineStateActive appendDescriptionToStream:];
-[_SBContinuitySessionStateMachineStateActive stateTransitionHandler];
-[_SBContinuitySessionStateMachineStateActive _evaluateClientExternallyBlockedReasons];
-[_SBContinuitySessionStateMachineStateActive _evaluateLockState];
-[_SBContinuitySessionStateMachineStateActive _evaluateSystemEvents];
-[_SBContinuitySessionStateMachineStateActive clientExternallyBlockedReasonsProvider];
-[_SBContinuitySessionStateMachineStateActive continuityDisplayAuthenticationCoordinatorDidUpdateLockState:];
-[_SBContinuitySessionStateMachineStateActive continuitySessionSystemEventMonitor:eventOccurred:];
-[_SBContinuitySessionStateMachineStateActive enteredStateFrom:];
-[_SBContinuitySessionStateMachineStateActive exitedStateTo:];
-[_SBContinuitySessionStateMachineStateActive initWithSystemEventMonitor:continuityDisplayAuthenticationCoordinator:];
-[_SBContinuitySessionStateMachineStateActive invalidStateHandler];
-[_SBContinuitySessionStateMachineStateActive noteClientDidUpdateExternallyBlockedReasons];
-[_SBContinuitySessionStateMachineStateActive setClientExternallyBlockedReasonsProvider:];
-[_SBContinuitySessionStateMachineStateActive setInvalidStateHandler:];
-[_SBContinuitySessionStateMachineStateActive setStateTransitionHandler:];
-[_SBContinuitySessionStateMachineStateActive setStateUpdateHandler:];
-[_SBContinuitySessionStateMachineStateActive stateUpdateHandler];
```
