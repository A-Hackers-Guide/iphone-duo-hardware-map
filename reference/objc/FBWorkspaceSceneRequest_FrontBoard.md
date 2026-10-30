# `FBWorkspaceSceneRequest`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSceneObserver`
- 7 instance variables, 8 properties, 17 instance methods, 0 class methods

## Instance variables

```
@? _lock_completion;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _lock_responded;
@"FBSSceneClientIdentity" _clientIdentity;
@"NSString" _targetIdentifier;
@"FBSWorkspaceSceneRequestOptions" _options;
@"NSSet" _actions;
```

## Properties

```
@property (T@"FBSSceneClientIdentity",R,C,N,V_clientIdentity) clientIdentity;
@property (T@"NSString",R,C,N,V_targetIdentifier) targetIdentifier;
@property (T@"FBSWorkspaceSceneRequestOptions",R,N,V_options) options;
@property (T@"NSSet",R,N,V_actions) actions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBWorkspaceSceneRequest _respondWithScene:error:];
-[FBWorkspaceSceneRequest observeScene:];
-[FBWorkspaceSceneRequest init];
-[FBWorkspaceSceneRequest sceneDidActivate:];
-[FBWorkspaceSceneRequest dealloc];
-[FBWorkspaceSceneRequest invalidateWithError:];
-[FBWorkspaceSceneRequest initWithClientIdentity:targetIdentifier:options:completion:];
-[FBWorkspaceSceneRequest targetIdentifier];
-[FBWorkspaceSceneRequest requiresTargetPreregistration];
-[FBWorkspaceSceneRequest requiresModernDispatcher];
-[FBWorkspaceSceneRequest actions];
-[FBWorkspaceSceneRequest sceneDidInvalidate:];
-[FBWorkspaceSceneRequest initWithTargetIdentifier:];
-[FBWorkspaceSceneRequest respondWithScene:];
-[FBWorkspaceSceneRequest options];
-[FBWorkspaceSceneRequest initWithTargetIdentifier:actions:completion:];
-[FBWorkspaceSceneRequest clientIdentity];
```
