# `FBSSceneTransitionContext` (protocol)

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 13 properties, 26 instance methods, 0 class methods

## Properties

```
@property (T@"BSAnimationSettings",C,N) animationSettings;
@property (T@"BKSAnimationFenceHandle",&,N) animationFence;
@property (T@"NSSet",C,N) actions;
@property (T@"BSProcessHandle",&,N) originatingProcess;
@property (TB,N,GisBarrier) barrier;
@property (T@"FBSSceneUpdate",?,&,N) parentUpdate;
@property (T@"FBProcessExecutionContext",?,&,N) executionContext;
@property (T@"RBSProcessHandle",?,&,N) clientProcessHandle;
@property (T@"FBSceneUpdateContext",?,&,N) updateContext;
@property (T@"FBWatchdogTransitionContext",?,&,N) watchdogTransitionContext;
@property (TB,?,N) allowCPUThrottling;
@property (TB,?,N,GisRunningBoardAssertionDisabled) runningBoardAssertionDisabled;
@property (T@"NSError",?,&,N) error;
```

## Instance methods

```
-[FBSSceneTransitionContext setAnimationSettings:];
-[FBSSceneTransitionContext animationFence];
-[FBSSceneTransitionContext animationSettings];
-[FBSSceneTransitionContext isBarrier];
-[FBSSceneTransitionContext setActions:];
-[FBSSceneTransitionContext originatingProcess];
-[FBSSceneTransitionContext actions];
-[FBSSceneTransitionContext setBarrier:];
-[FBSSceneTransitionContext setAnimationFence:];
-[FBSSceneTransitionContext setOriginatingProcess:];
-[FBSSceneTransitionContext clientProcessHandle];
-[FBSSceneTransitionContext setError:];
-[FBSSceneTransitionContext setExecutionContext:];
-[FBSSceneTransitionContext setAllowCPUThrottling:];
-[FBSSceneTransitionContext setUpdateContext:];
-[FBSSceneTransitionContext updateContext];
-[FBSSceneTransitionContext setRunningBoardAssertionDisabled:];
-[FBSSceneTransitionContext watchdogTransitionContext];
-[FBSSceneTransitionContext error];
-[FBSSceneTransitionContext executionContext];
-[FBSSceneTransitionContext setClientProcessHandle:];
-[FBSSceneTransitionContext isRunningBoardAssertionDisabled];
-[FBSSceneTransitionContext allowCPUThrottling];
-[FBSSceneTransitionContext setWatchdogTransitionContext:];
-[FBSSceneTransitionContext parentUpdate];
-[FBSSceneTransitionContext setParentUpdate:];
```
