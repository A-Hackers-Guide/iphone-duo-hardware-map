# `_SBContinuitySessionStateMachineStateBlocked`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBContinuitySessionSystemEventMonitorObserver`, `_SBContinuitySessionStateMachineState`, `BSDescriptionStreaming`
- 16 instance variables, 8 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"SBContinuitySessionSystemEventMonitor" _systemEventMonitor;
@"NSSet" _blockedReasons_client;
B _clientConnected;
B _uiLocked;
B _uiBlocked;
B _inCall;
B _sosActive;
B _lockScreenSearchPresented;
B _usingSecureApp;
B _isAirplayMirroring;
B _isUserInitiatedRemoteTransientOverlayPresented;
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
-[_SBContinuitySessionStateMachineStateBlocked invalidate];
-[_SBContinuitySessionStateMachineStateBlocked description];
-[_SBContinuitySessionStateMachineStateBlocked appendDescriptionToStream:];
-[_SBContinuitySessionStateMachineStateBlocked stateTransitionHandler];
-[_SBContinuitySessionStateMachineStateBlocked isClientConnected];
-[_SBContinuitySessionStateMachineStateBlocked _evaluateClientExternallyBlockedReasons];
-[_SBContinuitySessionStateMachineStateBlocked _evaluateSystemEvents];
-[_SBContinuitySessionStateMachineStateBlocked _reevaluateStateForReason:];
-[_SBContinuitySessionStateMachineStateBlocked clientExternallyBlockedReasonsProvider];
-[_SBContinuitySessionStateMachineStateBlocked continuitySessionSystemEventMonitor:eventOccurred:];
-[_SBContinuitySessionStateMachineStateBlocked enteredStateFrom:];
-[_SBContinuitySessionStateMachineStateBlocked exitedStateTo:];
-[_SBContinuitySessionStateMachineStateBlocked initWithSystemEventMonitor:];
-[_SBContinuitySessionStateMachineStateBlocked invalidStateHandler];
-[_SBContinuitySessionStateMachineStateBlocked noteClientConnectedWithInitialExternallyBlockedReasons:];
-[_SBContinuitySessionStateMachineStateBlocked noteClientDidUpdateExternallyBlockedReasons];
-[_SBContinuitySessionStateMachineStateBlocked setClientExternallyBlockedReasonsProvider:];
-[_SBContinuitySessionStateMachineStateBlocked setInvalidStateHandler:];
-[_SBContinuitySessionStateMachineStateBlocked setStateTransitionHandler:];
-[_SBContinuitySessionStateMachineStateBlocked setStateUpdateHandler:];
-[_SBContinuitySessionStateMachineStateBlocked stateUpdateHandler];
```
