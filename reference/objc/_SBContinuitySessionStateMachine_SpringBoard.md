# `_SBContinuitySessionStateMachine`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `_SBContinuitySessionStateMachineClientExternallyBlockedReasonsProvider`
- 23 instance variables, 10 properties, 40 instance methods, 0 class methods

## Instance variables

```
@"SBContinuitySessionSystemEventMonitor" _systemEventMonitor;
@"SBContinuityDisplayAuthenticationCoordinator" _authenticationCoordinator;
@"_SBContinuitySessionStateMachineStateStoreDemoPrep" _storeDemoPrepState;
@"_SBContinuitySessionStateMachineStateBlocked" _blockedState;
@"_SBContinuitySessionStateMachineStatePreparingForRemoteUnlock" _preparingForRemoteUnlockState;
@"_SBContinuitySessionStateMachineStateWaitingForRemoteUnlock" _waitingForRemoteUnlockState;
@"_SBContinuitySessionStateMachineStateWaitingForScenes" _waitingForScenesState;
@"_SBContinuitySessionStateMachineStateWaitingForHIDServices" _waitingForHIDServicesState;
@"_SBContinuitySessionStateMachineStateActivating" _activatingState;
@"_SBContinuitySessionStateMachineStateUpdatingActiveDisplay" _updatingActiveDisplayState;
@"_SBContinuitySessionStateMachineStateLaunching" _launchingState;
@"_SBContinuitySessionStateMachineStateFlushing" _flushingState;
@"_SBContinuitySessionStateMachineStateActive" _activeState;
Q _internalState;
@"NSSet" _internalReasons;
Q _observerState;
@"NSSet" _observerReasons;
B _suppressReasonUpdateCallout;
B _invalidated;
B _automaticBiometricsDisabled;
@"<_SBContinuitySessionStateMachineDelegate>" _delegate;
@"<_SBContinuitySessionStateMachineClientExternallyBlockedReasonsProvider>" _clientExternallyBlockedReasonsProvider;
@"_SBContinuitySessionServiceClient" _client;
```

## Properties

```
@property (T@"_SBContinuitySessionServiceClient",&,N,V_client) client;
@property (TQ,R,N) state;
@property (T@"NSSet",R,N) reasons;
@property (T@"<_SBContinuitySessionStateMachineDelegate>",N,V_delegate) delegate;
@property (TB,N,GisAutomaticBiomtericsDisabled,V_automaticBiometricsDisabled) automaticBiometricsDisabled;
@property (T@"<_SBContinuitySessionStateMachineClientExternallyBlockedReasonsProvider>",W,N,V_clientExternallyBlockedReasonsProvider) clientExternallyBlockedReasonsProvider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_SBContinuitySessionStateMachine setClient:];
-[_SBContinuitySessionStateMachine reasons];
-[_SBContinuitySessionStateMachine succinctDescription];
-[_SBContinuitySessionStateMachine setDelegate:];
-[_SBContinuitySessionStateMachine delegate];
-[_SBContinuitySessionStateMachine description];
-[_SBContinuitySessionStateMachine appendDescriptionToStream:];
-[_SBContinuitySessionStateMachine client];
-[_SBContinuitySessionStateMachine state];
-[_SBContinuitySessionStateMachine _moveToState:];
-[_SBContinuitySessionStateMachine noteClientConfiguredHIDServices];
-[_SBContinuitySessionStateMachine setAutomaticBiometricsDisabled:];
-[_SBContinuitySessionStateMachine _initializeStates];
-[_SBContinuitySessionStateMachine _moveToInvalidStateForReasons:postToDelegate:];
-[_SBContinuitySessionStateMachine _stateMachineStateForState:];
-[_SBContinuitySessionStateMachine _updateCurrentStateReasons:];
-[_SBContinuitySessionStateMachine clientExternallyBlockedReasons];
-[_SBContinuitySessionStateMachine clientExternallyBlockedReasonsProvider];
-[_SBContinuitySessionStateMachine didHandleLaunchEvent:];
-[_SBContinuitySessionStateMachine didReceiveLaunchEvent:];
-[_SBContinuitySessionStateMachine initWithStoreDemoPrepState:blockedState:preparingForRemoteUnlockState:waitingForRemoteUnlockState:waitingForScenesState:waitingForHIDServicesState:activatingState:updatingActiveDisplayState:launchingState:flushingState:activeState:];
-[_SBContinuitySessionStateMachine initWithSystemEventMonitor:continuityDisplayAuthenticationCoordinator:inStoreDemoMode:];
-[_SBContinuitySessionStateMachine invalidateForReasons:];
-[_SBContinuitySessionStateMachine isAutomaticBiometricsDisabled];
-[_SBContinuitySessionStateMachine isAutomaticBiomtericsDisabled];
-[_SBContinuitySessionStateMachine noteActiveDisplayUpdated];
-[_SBContinuitySessionStateMachine noteAppHostingSceneConnected];
-[_SBContinuitySessionStateMachine noteClientConnectedWithInitialExternallyBlockedReasons:];
-[_SBContinuitySessionStateMachine noteClientDidUpdateExternallyBlockedReasons];
-[_SBContinuitySessionStateMachine noteMainSceneConnected];
-[_SBContinuitySessionStateMachine noteSceneConnected];
-[_SBContinuitySessionStateMachine noteSceneHasValidDisplayUUID];
-[_SBContinuitySessionStateMachine noteStoreDemoLockFailed];
-[_SBContinuitySessionStateMachine noteSystemApertureCurtainSceneConnected];
-[_SBContinuitySessionStateMachine noteSystemApertureCurtainUIIsReady];
-[_SBContinuitySessionStateMachine noteSystemApertureSceneConnected];
-[_SBContinuitySessionStateMachine noteSystemApertureUIIsReady];
-[_SBContinuitySessionStateMachine noteUIFlushed];
-[_SBContinuitySessionStateMachine noteUIIsReady];
-[_SBContinuitySessionStateMachine setClientExternallyBlockedReasonsProvider:];
```
