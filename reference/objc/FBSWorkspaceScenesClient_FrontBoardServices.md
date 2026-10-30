# `FBSWorkspaceScenesClient`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSSceneUpdater`, `FBSWorkspaceServiceTarget`, `FBSWorkspaceServiceServerInterface`
- 19 instance variables, 5 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"FBSWorkspace" _workspace;
@"<FBSWorkspaceDelegate>" _workspaceDelegate;
@"BSServiceDispatchQueue" _queue;
@"BSServiceQueue" _callOutQueue;
@"BSServiceConnection" _connection;
@"FBSWorkspaceScenesClientIdentifier" _identifier;
@"NSMutableDictionary" _scenesByIdentity;
@"NSMutableDictionary" _clientSettingsByIdentity;
@"NSHashTable" _reconnectingScenes;
@"NSMutableArray" _pendedSendBlocks;
@"NSMutableArray" _hostEvent_pendingEvents;
@"FBSSceneHostHandle" _hostHandle;
@"<FBSWorkspaceServiceClientInterface>" _handshakeLock_remoteTarget;
@"NSMutableDictionary" _reportingLock_scenesByIdentity;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _handshakeLock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _reportingLock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _hostEventLock;
B _activated;
B _invalidated;
```

## Properties

```
@property (T@"NSObject<NSCopying>",R,N) identifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBSWorkspaceScenesClient sceneID:destroyWithTransitionContext:completion:];
-[FBSWorkspaceScenesClient hostProcess];
-[FBSWorkspaceScenesClient callOutQueue];
-[FBSWorkspaceScenesClient sceneID:handleInvocation:completion:];
-[FBSWorkspaceScenesClient sendActions:toWorkspaceID:completion:];
-[FBSWorkspaceScenesClient sendActions:completion:];
-[FBSWorkspaceScenesClient identifier];
-[FBSWorkspaceScenesClient init];
-[FBSWorkspaceScenesClient scene:sendMessage:withResponse:];
-[FBSWorkspaceScenesClient createSceneWithIdentity:parameters:transitionContext:completion:];
-[FBSWorkspaceScenesClient scene:didReceiveActions:forExtension:];
-[FBSWorkspaceScenesClient sceneID:updateWithSettingsDiff:transitionContext:completion:];
-[FBSWorkspaceScenesClient scene:invalidateWithTransitionContext:];
-[FBSWorkspaceScenesClient reconnectSceneWithIdentity:parameters:transitionContext:completion:];
-[FBSWorkspaceScenesClient sceneID:sendActions:toExtension:completion:];
-[FBSWorkspaceScenesClient willTerminateWithTransitionContext:];
-[FBSWorkspaceScenesClient requestSceneWithOptions:completion:];
-[FBSWorkspaceScenesClient createSceneFutureWithDefinition:];
-[FBSWorkspaceScenesClient sendBatchedMessages];
-[FBSWorkspaceScenesClient canHaveAgent];
-[FBSWorkspaceScenesClient scene:didUpdateClientSettings:withDiff:transitionContext:];
-[FBSWorkspaceScenesClient sceneWithIdentity:];
-[FBSWorkspaceScenesClient sceneID:sendMessage:completion:];
-[FBSWorkspaceScenesClient scene:sendInvocation:];
-[FBSWorkspaceScenesClient scenes];
-[FBSWorkspaceScenesClient activateSceneFuture:completion:];
```
