# `FBWorkspaceScene`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSSceneHandle`, `FBSSceneAgentProxy`, `BSDescriptionProviding`
- 27 instance variables, 9 properties, 35 instance methods, 1 class methods

## Instance variables

```
@"FBWorkspaceConnection" _lock_connection;
@"<FBSceneHost>" _host;
@"FBSSceneDefinition" _definition;
@"FBSSceneIdentity" _identity;
@"NSString" _logProem;
@"<FBSSceneHostAgent>" _hostAgent;
@"NSMutableArray" _agentSessions;
@"FBSSceneSettings" _lock_settings;
@"FBSSceneClientSettings" _lock_clientSettings;
@"NSMutableArray" _lock_sceneCreatedBlocks;
@"<BSInvalidatable>" _queue_workspaceAssertion;
@"NSMutableSet" _queue_allWatchdogs;
@"NSMutableArray" _queue_watchdogStack;
@"BSAtomicSignal" _queue_eventsCompleteSignal;
Q _queue_inFlightUpdateEvents;
Q _queue_inFlightDeactivationEvents;
Q _queue_inFlightUpdateAllowsThrottling;
Q _queue_inFlightUpdateDisallowsThrottling;
Q _queue_inFlightExternallyManagedEvents;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
{?="rawValue"I} _queue_workspaceState;
C _lock_lifecycleState;
B _reconnect;
B _lock_invalidated;
B _usesOutgoingConnection;
B _isUISubclass;
@"BSServiceDispatchQueue" _workspaceQueue;
```

## Properties

```
@property (TB,R,N,V_usesOutgoingConnection) usesOutgoingConnection;
@property (T@"<FBSceneHost>",R,W,N,V_host) host;
@property (T@"FBSSceneIdentity",R,C,N,V_identity) identity;
@property (T@"FBSSceneSettings",R,C,N) settings;
@property (T@"FBSSceneSpecification",R,C,N) specification;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBWorkspaceScene _sceneActionForLifecycleFromState:toState:];
```

## Instance methods

```
-[FBWorkspaceScene definition];
-[FBWorkspaceScene _workspaceQueue_sendSceneUpdateToClient:settingsDiff:transitionContext:completion:];
-[FBWorkspaceScene hostProcess];
-[FBWorkspaceScene parameters];
-[FBWorkspaceScene callOutQueue];
-[FBWorkspaceScene clientProcess];
-[FBWorkspaceScene _workspaceQueue_incrementInFlightUpdatesForAction:allowThrottling:externallyManaged:];
-[FBWorkspaceScene _workspaceQueue_invalidate];
-[FBWorkspaceScene _workspaceQueue_sendMessageToClient:];
-[FBWorkspaceScene _workspaceQueue_sendSceneCreateToClient:parameters:transitionContext:completion:];
-[FBWorkspaceScene debugDescription];
-[FBWorkspaceScene usesOutgoingConnection];
-[FBWorkspaceScene identifier];
-[FBWorkspaceScene succinctDescriptionBuilder];
-[FBWorkspaceScene counterpartAgent];
-[FBWorkspaceScene settings];
-[FBWorkspaceScene dealloc];
-[FBWorkspaceScene initWithConnection:host:settings:clientSettings:fromRemnant:];
-[FBWorkspaceScene openSessionWithName:executionPolicy:];
-[FBWorkspaceScene descriptionWithMultilinePrefix:];
-[FBWorkspaceScene agent:registerMessageHandler:];
-[FBWorkspaceScene closeSession:];
-[FBWorkspaceScene succinctDescription];
-[FBWorkspaceScene invalidate];
-[FBWorkspaceScene _workspaceQueue_invalidateSceneAgentWithEvent:];
-[FBWorkspaceScene identity];
-[FBWorkspaceScene description];
-[FBWorkspaceScene specification];
-[FBWorkspaceScene _workspaceQueue_cancelWatchdogTimer:];
-[FBWorkspaceScene _workspaceQueue_updateAssertion];
-[FBWorkspaceScene _workspaceQueue_decrementInFlightUpdatesForAction:allowThrottling:externallyManaged:];
-[FBWorkspaceScene agent:sendMessage:withResponse:];
-[FBWorkspaceScene _workspaceQueue_createWatchdogForProcess:sceneAction:settings:transitionContext:];
-[FBWorkspaceScene host];
-[FBWorkspaceScene descriptionBuilderWithMultilinePrefix:];
```
