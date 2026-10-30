# `FBSSceneTransitionContextCore`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSCoreSettingsExtension`
- Protocols: `FBSSceneTransitionContext`
- 0 instance variables, 13 properties, 22 instance methods, 1 class methods

## Properties

```
@property (T@"BSAnimationSettings",C,N) animationSettings;
@property (T@"BKSAnimationFenceHandle",&,N) animationFence;
@property (T@"NSSet",C,D,N) actions;
@property (T@"BSProcessHandle",&,N) originatingProcess;
@property (TB,N,GisBarrier) barrier;
@property (T@"FBSSceneUpdate",?,&,D,N) parentUpdate;
@property (T@"FBProcessExecutionContext",?,&,N) executionContext;
@property (T@"RBSProcessHandle",?,&,N) clientProcessHandle;
@property (T@"FBSceneUpdateContext",?,&,N) updateContext;
@property (T@"FBWatchdogTransitionContext",?,&,N) watchdogTransitionContext;
@property (TB,?,N) allowCPUThrottling;
@property (TB,?,N,GisRunningBoardAssertionDisabled) runningBoardAssertionDisabled;
@property (T@"NSError",?,&,N) error;
```

## Class methods

```
+[FBSSceneTransitionContextCore protocol];
```

## Instance methods

```
-[FBSSceneTransitionContextCore setAnimationSettings:];
-[FBSSceneTransitionContextCore animationFence];
-[FBSSceneTransitionContextCore clientProcessHandle];
-[FBSSceneTransitionContextCore animationSettings];
-[FBSSceneTransitionContextCore isBarrier];
-[FBSSceneTransitionContextCore setError:];
-[FBSSceneTransitionContextCore setExecutionContext:];
-[FBSSceneTransitionContextCore setAllowCPUThrottling:];
-[FBSSceneTransitionContextCore setUpdateContext:];
-[FBSSceneTransitionContextCore updateContext];
-[FBSSceneTransitionContextCore setRunningBoardAssertionDisabled:];
-[FBSSceneTransitionContextCore originatingProcess];
-[FBSSceneTransitionContextCore watchdogTransitionContext];
-[FBSSceneTransitionContextCore error];
-[FBSSceneTransitionContextCore executionContext];
-[FBSSceneTransitionContextCore setBarrier:];
-[FBSSceneTransitionContextCore setAnimationFence:];
-[FBSSceneTransitionContextCore setClientProcessHandle:];
-[FBSSceneTransitionContextCore isRunningBoardAssertionDisabled];
-[FBSSceneTransitionContextCore allowCPUThrottling];
-[FBSSceneTransitionContextCore setWatchdogTransitionContext:];
-[FBSSceneTransitionContextCore setOriginatingProcess:];
```
