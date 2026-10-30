# `_SBContinuitySessionStateMachineStateLaunching`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBContinuitySessionSystemEventMonitorObserver`, `SBContinuityDisplayAuthenticationStateObserver`, `_SBContinuitySessionStateMachineState`, `BSDescriptionStreaming`
- 9 instance variables, 8 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"SBContinuitySessionSystemEventMonitor" _systemEventMonitor;
@"SBContinuityDisplayAuthenticationCoordinator" _authenticationCoordinator;
@"NSMutableArray" _handlingLaunchEvents;
B _isCurrentState;
B _radar124642623;
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
-[_SBContinuitySessionStateMachineStateLaunching invalidate];
-[_SBContinuitySessionStateMachineStateLaunching description];
-[_SBContinuitySessionStateMachineStateLaunching appendDescriptionToStream:];
-[_SBContinuitySessionStateMachineStateLaunching stateTransitionHandler];
-[_SBContinuitySessionStateMachineStateLaunching _evaluateClientExternallyBlockedReasons];
-[_SBContinuitySessionStateMachineStateLaunching _evaluateLockState];
-[_SBContinuitySessionStateMachineStateLaunching _evaluateSystemEvents];
-[_SBContinuitySessionStateMachineStateLaunching _reevaluateStateForReason:];
-[_SBContinuitySessionStateMachineStateLaunching clientExternallyBlockedReasonsProvider];
-[_SBContinuitySessionStateMachineStateLaunching continuityDisplayAuthenticationCoordinatorDidUpdateLockState:];
-[_SBContinuitySessionStateMachineStateLaunching continuitySessionSystemEventMonitor:eventOccurred:];
-[_SBContinuitySessionStateMachineStateLaunching didHandleLaunchEvent:];
-[_SBContinuitySessionStateMachineStateLaunching didReceiveLaunchEvent:];
-[_SBContinuitySessionStateMachineStateLaunching enteredStateFrom:];
-[_SBContinuitySessionStateMachineStateLaunching exitedStateTo:];
-[_SBContinuitySessionStateMachineStateLaunching initWithSystemEventMonitor:continuityDisplayAuthenticationCoordinator:];
-[_SBContinuitySessionStateMachineStateLaunching invalidStateHandler];
-[_SBContinuitySessionStateMachineStateLaunching noteClientDidUpdateExternallyBlockedReasons];
-[_SBContinuitySessionStateMachineStateLaunching setClientExternallyBlockedReasonsProvider:];
-[_SBContinuitySessionStateMachineStateLaunching setInvalidStateHandler:];
-[_SBContinuitySessionStateMachineStateLaunching setStateTransitionHandler:];
-[_SBContinuitySessionStateMachineStateLaunching setStateUpdateHandler:];
-[_SBContinuitySessionStateMachineStateLaunching stateUpdateHandler];
```
