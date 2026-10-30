# `_SBContinuitySessionStateMachineStateActivating`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBContinuitySessionSystemEventMonitorObserver`, `SBContinuityDisplayAuthenticationStateObserver`, `_SBContinuitySessionStateMachineState`, `BSDescriptionStreaming`
- 10 instance variables, 8 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"SBContinuitySessionSystemEventMonitor" _systemEventMonitor;
@"SBContinuityDisplayAuthenticationCoordinator" _authenticationCoordinator;
B _uiReady;
B _systemApertureReady;
B _systemApertureCurtainReady;
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
-[_SBContinuitySessionStateMachineStateActivating invalidate];
-[_SBContinuitySessionStateMachineStateActivating description];
-[_SBContinuitySessionStateMachineStateActivating appendDescriptionToStream:];
-[_SBContinuitySessionStateMachineStateActivating stateTransitionHandler];
-[_SBContinuitySessionStateMachineStateActivating _evaluateClientExternallyBlockedReasons];
-[_SBContinuitySessionStateMachineStateActivating _evaluateLockState];
-[_SBContinuitySessionStateMachineStateActivating _evaluateSystemEvents];
-[_SBContinuitySessionStateMachineStateActivating _reevaluateStateForReason:];
-[_SBContinuitySessionStateMachineStateActivating clientExternallyBlockedReasonsProvider];
-[_SBContinuitySessionStateMachineStateActivating continuityDisplayAuthenticationCoordinatorDidUpdateLockState:];
-[_SBContinuitySessionStateMachineStateActivating continuitySessionSystemEventMonitor:eventOccurred:];
-[_SBContinuitySessionStateMachineStateActivating enteredStateFrom:];
-[_SBContinuitySessionStateMachineStateActivating exitedStateTo:];
-[_SBContinuitySessionStateMachineStateActivating initWithSystemEventMonitor:continuityDisplayAuthenticationCoordinator:];
-[_SBContinuitySessionStateMachineStateActivating invalidStateHandler];
-[_SBContinuitySessionStateMachineStateActivating noteClientDidUpdateExternallyBlockedReasons];
-[_SBContinuitySessionStateMachineStateActivating noteSystemApertureCurtainUIIsReady];
-[_SBContinuitySessionStateMachineStateActivating noteSystemApertureUIIsReady];
-[_SBContinuitySessionStateMachineStateActivating noteUIIsReady];
-[_SBContinuitySessionStateMachineStateActivating setClientExternallyBlockedReasonsProvider:];
-[_SBContinuitySessionStateMachineStateActivating setInvalidStateHandler:];
-[_SBContinuitySessionStateMachineStateActivating setStateTransitionHandler:];
-[_SBContinuitySessionStateMachineStateActivating setStateUpdateHandler:];
-[_SBContinuitySessionStateMachineStateActivating stateUpdateHandler];
```
