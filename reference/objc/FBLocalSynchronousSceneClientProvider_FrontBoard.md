# `FBLocalSynchronousSceneClientProvider`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSSceneUpdater`, `FBSceneClient`, `FBSWorkspaceServiceTarget`, `FBSceneClientProvider`
- 11 instance variables, 5 properties, 26 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _pendingSceneCreatesBeforeFBSWorkspaceInitialization;
@"NSMutableDictionary" _localSceneInfoByIdentity;
@"NSMutableDictionary" _hostsByIdentity;
@"NSMutableSet" _pendingScenes;
@"<FBSProcess>" _currentProcess;
@"FBSWorkspaceCoupler" _coupler;
@"FBSWorkspace" _callOutQueue_workspace;
@"FBWorkspaceEventDispatcher" _eventDispatcher;
@"NSMutableSet" _clientFutureHostsBeingSynchronized;
@"NSMutableSet" _clientFutureScenesBeingSynchronized;
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

## Class methods

```
+[FBLocalSynchronousSceneClientProvider sharedInstance];
```

## Instance methods

```
-[FBLocalSynchronousSceneClientProvider hostProcess];
-[FBLocalSynchronousSceneClientProvider host:didInvalidateWithTransitionContext:completion:];
-[FBLocalSynchronousSceneClientProvider callOutQueue];
-[FBLocalSynchronousSceneClientProvider sendActions:toWorkspaceID:completion:];
-[FBLocalSynchronousSceneClientProvider identifier];
-[FBLocalSynchronousSceneClientProvider init];
-[FBLocalSynchronousSceneClientProvider scene:sendMessage:withResponse:];
-[FBLocalSynchronousSceneClientProvider scene:didReceiveActions:forExtension:];
-[FBLocalSynchronousSceneClientProvider dealloc];
-[FBLocalSynchronousSceneClientProvider scene:invalidateWithTransitionContext:];
-[FBLocalSynchronousSceneClientProvider host:didReceiveActions:forExtension:];
-[FBLocalSynchronousSceneClientProvider registerHost:settings:initialClientSettings:fromRemnant:error:];
-[FBLocalSynchronousSceneClientProvider host:sendInvocation:withReply:];
-[FBLocalSynchronousSceneClientProvider requestSceneWithOptions:completion:];
-[FBLocalSynchronousSceneClientProvider createSceneFutureWithDefinition:];
-[FBLocalSynchronousSceneClientProvider sendBatchedMessages];
-[FBLocalSynchronousSceneClientProvider host:didUpdateSettings:withDiff:transitionContext:completion:];
-[FBLocalSynchronousSceneClientProvider canHaveAgent];
-[FBLocalSynchronousSceneClientProvider scene:didUpdateClientSettings:withDiff:transitionContext:];
-[FBLocalSynchronousSceneClientProvider sceneWithIdentity:];
-[FBLocalSynchronousSceneClientProvider scene:sendInvocation:];
-[FBLocalSynchronousSceneClientProvider scenes];
-[FBLocalSynchronousSceneClientProvider unregisterHost:];
-[FBLocalSynchronousSceneClientProvider activateSceneFuture:completion:];
-[FBLocalSynchronousSceneClientProvider fbsSceneForScene:];
-[FBLocalSynchronousSceneClientProvider fbsSceneWithIdentifier:];
```
