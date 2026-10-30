# `_SBContinuitySessionStateMachineStateWaitingForHIDServices`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBContinuitySessionSystemEventMonitorObserver`, `SBContinuityDisplayAuthenticationStateObserver`, `_SBContinuitySessionStateMachineState`, `BSDescriptionStreaming`
- 8 instance variables, 8 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"SBContinuitySessionSystemEventMonitor" _systemEventMonitor;
@"SBContinuityDisplayAuthenticationCoordinator" _authenticationCoordinator;
B _configuredHIDServices;
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
-[_SBContinuitySessionStateMachineStateWaitingForHIDServices invalidate];
-[_SBContinuitySessionStateMachineStateWaitingForHIDServices description];
-[_SBContinuitySessionStateMachineStateWaitingForHIDServices appendDescriptionToStream:];
-[_SBContinuitySessionStateMachineStateWaitingForHIDServices stateTransitionHandler];
-[_SBContinuitySessionStateMachineStateWaitingForHIDServices noteClientConfiguredHIDServices];
-[_SBContinuitySessionStateMachineStateWaitingForHIDServices _evaluateClientExternallyBlockedReasons];
-[_SBContinuitySessionStateMachineStateWaitingForHIDServices _evaluateLockState];
-[_SBContinuitySessionStateMachineStateWaitingForHIDServices _evaluateSystemEvents];
-[_SBContinuitySessionStateMachineStateWaitingForHIDServices _reevaluateStateForReason:];
-[_SBContinuitySessionStateMachineStateWaitingForHIDServices clientExternallyBlockedReasonsProvider];
-[_SBContinuitySessionStateMachineStateWaitingForHIDServices continuityDisplayAuthenticationCoordinatorDidUpdateLockState:];
-[_SBContinuitySessionStateMachineStateWaitingForHIDServices continuitySessionSystemEventMonitor:eventOccurred:];
-[_SBContinuitySessionStateMachineStateWaitingForHIDServices enteredStateFrom:];
-[_SBContinuitySessionStateMachineStateWaitingForHIDServices exitedStateTo:];
-[_SBContinuitySessionStateMachineStateWaitingForHIDServices initWithSystemEventMonitor:continuityDisplayAuthenticationCoordinator:];
-[_SBContinuitySessionStateMachineStateWaitingForHIDServices invalidStateHandler];
-[_SBContinuitySessionStateMachineStateWaitingForHIDServices noteClientDidUpdateExternallyBlockedReasons];
-[_SBContinuitySessionStateMachineStateWaitingForHIDServices setClientExternallyBlockedReasonsProvider:];
-[_SBContinuitySessionStateMachineStateWaitingForHIDServices setInvalidStateHandler:];
-[_SBContinuitySessionStateMachineStateWaitingForHIDServices setStateTransitionHandler:];
-[_SBContinuitySessionStateMachineStateWaitingForHIDServices setStateUpdateHandler:];
-[_SBContinuitySessionStateMachineStateWaitingForHIDServices stateUpdateHandler];
```
