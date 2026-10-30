# `FBSPseudoSceneUpdater`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSSceneUpdater`
- 1 instance variables, 5 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"BSServiceQueue" _callOutQueue;
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
-[FBSPseudoSceneUpdater hostProcess];
-[FBSPseudoSceneUpdater callOutQueue];
-[FBSPseudoSceneUpdater sendActions:toWorkspaceID:completion:];
-[FBSPseudoSceneUpdater identifier];
-[FBSPseudoSceneUpdater scene:sendMessage:withResponse:];
-[FBSPseudoSceneUpdater scene:didReceiveActions:forExtension:];
-[FBSPseudoSceneUpdater scene:invalidateWithTransitionContext:];
-[FBSPseudoSceneUpdater requestSceneWithOptions:completion:];
-[FBSPseudoSceneUpdater createSceneFutureWithDefinition:];
-[FBSPseudoSceneUpdater sendBatchedMessages];
-[FBSPseudoSceneUpdater canHaveAgent];
-[FBSPseudoSceneUpdater scene:didUpdateClientSettings:withDiff:transitionContext:];
-[FBSPseudoSceneUpdater sceneWithIdentity:];
-[FBSPseudoSceneUpdater scene:sendInvocation:];
-[FBSPseudoSceneUpdater scenes];
-[FBSPseudoSceneUpdater activateSceneFuture:completion:];
-[FBSPseudoSceneUpdater _initWithCallOutQueue:];
```
