# `_SBContinuitySessionStateMachineStateWaitingForScenes`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBContinuitySessionSystemEventMonitorObserver`, `SBContinuityDisplayAuthenticationStateObserver`, `_SBContinuitySessionStateMachineState`, `BSDescriptionStreaming`
- 12 instance variables, 8 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"SBContinuitySessionSystemEventMonitor" _systemEventMonitor;
@"SBContinuityDisplayAuthenticationCoordinator" _authenticationCoordinator;
B _mainSceneConnected;
B _systemApertureSceneConnected;
B _systemApertureCurtainSceneConnected;
B _appHostingSceneConnected;
B _validDisplayUUID;
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
-[_SBContinuitySessionStateMachineStateWaitingForScenes invalidate];
-[_SBContinuitySessionStateMachineStateWaitingForScenes description];
-[_SBContinuitySessionStateMachineStateWaitingForScenes appendDescriptionToStream:];
-[_SBContinuitySessionStateMachineStateWaitingForScenes stateTransitionHandler];
-[_SBContinuitySessionStateMachineStateWaitingForScenes _evaluateClientExternallyBlockedReasons];
-[_SBContinuitySessionStateMachineStateWaitingForScenes _evaluateLockState];
-[_SBContinuitySessionStateMachineStateWaitingForScenes _evaluateSystemEvents];
-[_SBContinuitySessionStateMachineStateWaitingForScenes _reevaluateStateForReason:];
-[_SBContinuitySessionStateMachineStateWaitingForScenes clientExternallyBlockedReasonsProvider];
-[_SBContinuitySessionStateMachineStateWaitingForScenes continuityDisplayAuthenticationCoordinatorDidUpdateLockState:];
-[_SBContinuitySessionStateMachineStateWaitingForScenes continuitySessionSystemEventMonitor:eventOccurred:];
-[_SBContinuitySessionStateMachineStateWaitingForScenes enteredStateFrom:];
-[_SBContinuitySessionStateMachineStateWaitingForScenes exitedStateTo:];
-[_SBContinuitySessionStateMachineStateWaitingForScenes initWithSystemEventMonitor:continuityDisplayAuthenticationCoordinator:];
-[_SBContinuitySessionStateMachineStateWaitingForScenes invalidStateHandler];
-[_SBContinuitySessionStateMachineStateWaitingForScenes isMainSceneConnected];
-[_SBContinuitySessionStateMachineStateWaitingForScenes noteAppHostingSceneConnected];
-[_SBContinuitySessionStateMachineStateWaitingForScenes noteClientDidUpdateExternallyBlockedReasons];
-[_SBContinuitySessionStateMachineStateWaitingForScenes noteMainSceneConnected];
-[_SBContinuitySessionStateMachineStateWaitingForScenes noteSceneHasValidDisplayUUID];
-[_SBContinuitySessionStateMachineStateWaitingForScenes noteSystemApertureCurtainSceneConnected];
-[_SBContinuitySessionStateMachineStateWaitingForScenes noteSystemApertureSceneConnected];
-[_SBContinuitySessionStateMachineStateWaitingForScenes setClientExternallyBlockedReasonsProvider:];
-[_SBContinuitySessionStateMachineStateWaitingForScenes setInvalidStateHandler:];
-[_SBContinuitySessionStateMachineStateWaitingForScenes setStateTransitionHandler:];
-[_SBContinuitySessionStateMachineStateWaitingForScenes setStateUpdateHandler:];
-[_SBContinuitySessionStateMachineStateWaitingForScenes stateUpdateHandler];
```
