# `FBSScene`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSSceneSnapshotRequestDelegate`, `FBSSceneHandle`, `FBSSceneAgentProxy`, `FBSSceneUpdaterDelegate`, `FBSComponentSceneSupport`, `FBSInvocationReceiving`, `BSDescriptionProviding`, `FBSSceneExtensible`
- 22 instance variables, 17 properties, 86 instance methods, 1 class methods

## Instance variables

```
@"BSServiceQueue" _callOutQueue;
@"<FBSSceneClientAgent>" _callOutQueue_agent;
@"NSMutableArray" _callOutQueue_agentSessions;
@? _callOutQueue_agentMessageHandler;
@"BKSAnimationFenceHandle" _calloutQueue_animationFence;
@"FBSSceneUpdate" _callout_sceneUpdate;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"FBSSceneSettings" _lock_settings;
@"FBSSceneClientSettings" _lock_clientSettings;
@"<FBSSceneDelegate>" _lock_delegate;
@"NSMutableArray" _lock_sceneObservers;
@"NSMapTable" _lock_components;
@"FBSSceneHostHandle" _lock_hostHandle;
C _callout_updateDepth;
B _hasAgent;
B _callOutQueue_mutationLocked;
B _callout_coalesceUpdates;
B _everActivated;
@"FBSSceneIdentity" _identity;
@"FBSSceneIdentityToken" _identityToken;
@"FBSSceneDefinition" _definition;
@"<FBSSceneUpdater>" _lock_updater;
```

## Properties

```
@property (T@"FBSSceneDefinition",R,N,V_definition) definition;
@property (T@"<FBSSceneUpdater>",R,N,V_lock_updater) updater;
@property (TB,R,N,V_everActivated) everActivated;
@property (T@"BSAuditToken",R,N) hostAuditToken;
@property (T@"NSString",R,C,N) identifier;
@property (T@"FBSSceneIdentity",R,N,V_identity) identity;
@property (T@"FBSSceneIdentityToken",R,N,V_identityToken) identityToken;
@property (T@"FBSSceneSpecification",R,N) specification;
@property (T@"<FBSSceneDelegate>",W,N) delegate;
@property (T@"FBSSceneSettings",R,N) settings;
@property (T@"FBSSceneClientSettings",R,N) clientSettings;
@property (T@"FBSSceneHostHandle",R,N) hostHandle;
@property (T@"FBSWorkspaceService",R,N) workspaceService;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSScene pseudoSceneWithIdentifier:specification:];
```

## Instance methods

```
-[FBSScene invalidate:];
-[FBSScene updater];
-[FBSScene snapshotRequest:performWithContext:];
-[FBSScene definition];
-[FBSScene hostProcess];
-[FBSScene parameters];
-[FBSScene layers];
-[FBSScene callOutQueue];
-[FBSScene clientProcess];
-[FBSScene activateWithCompletion:];
-[FBSScene sendActions:];
-[FBSScene loggingIdentifier];
-[FBSScene identifier];
-[FBSScene succinctDescriptionBuilder];
-[FBSScene removeObserver:];
-[FBSScene init];
-[FBSScene counterpartAgent];
-[FBSScene settings];
-[FBSScene add:];
-[FBSScene remove:];
-[FBSScene openSessionWithName:executionPolicy:];
-[FBSScene descriptionWithMultilinePrefix:];
-[FBSScene _observers];
-[FBSScene _createTransitionContext];
-[FBSScene _callOutQueue];
-[FBSScene agent:registerMessageHandler:];
-[FBSScene closeSession:];
-[FBSScene succinctDescription];
-[FBSScene identityToken];
-[FBSScene addObserver:];
-[FBSScene invalidate];
-[FBSScene attachContext:];
-[FBSScene performSnapshotWithContext:];
-[FBSScene snapshotRequestAllowSnapshot:];
-[FBSScene setDelegate:];
-[FBSScene hostAuditToken];
-[FBSScene conformsToExtension:];
-[FBSScene delegate];
-[FBSScene identity];
-[FBSScene detachContext:];
-[FBSScene description];
-[FBSScene specification];
-[FBSScene updateClientSettings:];
-[FBSScene sendBatchedMessages];
-[FBSScene clientSettings];
-[FBSScene isEqual:];
-[FBSScene agent:sendMessage:withResponse:];
-[FBSScene updateClientSettingsWithBlock:];
-[FBSScene descriptionBuilderWithMultilinePrefix:];
-[FBSScene updateSettings:];
-[FBSScene addLocalExtensions:];
-[FBSScene attachLayer:];
-[FBSScene componentForExtension:ofClass:];
-[FBSScene configureParameters:];
-[FBSScene detachLayer:];
-[FBSScene hostHandle];
-[FBSScene invalidateSnapshotWithContext:];
-[FBSScene updateClientSettingsWithTransitionBlock:];
-[FBSScene _beginUpdate];
-[FBSScene _callOutQueue_updateExtensionsFromSettings:toSettings:withDiff:];
-[FBSScene snapshotRequest];
-[FBSScene sendInvocation:];
-[FBSScene _callOutQueue_addExtensions:removeExtensions:fromHost:];
-[FBSScene _callOutQueue_didCreateWithTransitionContext:alternativeCreationCallout:completion:];
-[FBSScene _callOutQueue_didUpdateHostHandle:];
-[FBSScene _callOutQueue_ensureCoalesceClientSettingsUpdates:];
-[FBSScene _callOutQueue_invalidate];
-[FBSScene _callOutQueue_maybeCoalesceClientSettingsUpdates:];
-[FBSScene _callOutQueue_willDestroyWithTransitionContext:completion:];
-[FBSScene _configureParameters:];
-[FBSScene _initWithUpdater:identityToken:identity:parameters:hostHandle:];
-[FBSScene _lock_allComponents];
-[FBSScene _sendUpdate:];
-[FBSScene _updateClientSettings:];
-[FBSScene addObserver:withConfiguration:];
-[FBSScene attachSceneContext:];
-[FBSScene detachSceneContext:];
-[FBSScene everActivated];
-[FBSScene removeLocalExtensions:];
-[FBSScene sendActions:toExtension:];
-[FBSScene targetForInvocation:];
-[FBSScene updateClientSettings:withTransitionContext:];
-[FBSScene updater:didReceiveActions:forExtension:];
-[FBSScene updater:didReceiveMessage:withResponse:];
-[FBSScene updater:didUpdateSettings:withDiff:transitionContext:completion:];
-[FBSScene workspaceService];
```
