# `SBLayoutStateTransitionCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBWorkspaceApplicationSceneTransitionContextDelegate`
- 5 instance variables, 8 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSPointerArray" _observerPointerArray;
@"_SBDefaultSceneEntityFrameProvider" _defaultSceneEntityFrameProvider;
@"SBLayoutStateTransitionContext" _transitionContext;
@"SBWindowScene" _windowScene;
@"<SBLayoutStateTransitionSceneEntityFrameProvider>" _sceneEntityFrameProvider;
```

## Properties

```
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (T@"<SBLayoutStateTransitionSceneEntityFrameProvider>",W,N,V_sceneEntityFrameProvider) sceneEntityFrameProvider;
@property (TB,R,N,GisTransitioning) transitioning;
@property (T@"SBLayoutStateTransitionContext",R,N,V_transitionContext) transitionContext;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBLayoutStateTransitionCoordinator transitionContext];
-[SBLayoutStateTransitionCoordinator removeObserver:];
-[SBLayoutStateTransitionCoordinator isTransitioning];
-[SBLayoutStateTransitionCoordinator applicationTransitionContext:frameForApplicationSceneEntity:];
-[SBLayoutStateTransitionCoordinator layoutStateForApplicationTransitionContext:];
-[SBLayoutStateTransitionCoordinator initWithWindowScene:];
-[SBLayoutStateTransitionCoordinator addObserver:];
-[SBLayoutStateTransitionCoordinator previousLayoutStateForApplicationTransitionContext:];
-[SBLayoutStateTransitionCoordinator windowScene];
-[SBLayoutStateTransitionCoordinator beginTransitionForWorkspaceTransaction:];
-[SBLayoutStateTransitionCoordinator endTransitionWithError:];
-[SBLayoutStateTransitionCoordinator sceneEntityFrameProvider];
-[SBLayoutStateTransitionCoordinator setSceneEntityFrameProvider:];
-[SBLayoutStateTransitionCoordinator willEndTransition];
```
