# `FBSSceneTransitionContext`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSettings`
- Protocols: `FBSSceneTransitionContext`, `NSCopying`, `NSMutableCopying`, `FBSMutableSettings`
- 0 instance variables, 17 properties, 7 instance methods, 7 class methods

## Properties

```
@property (T@"BSAnimationSettings",C,D,N) animationSettings;
@property (T@"BKSAnimationFenceHandle",&,D,N) animationFence;
@property (T@"NSSet",C,D,N) actions;
@property (T@"BSProcessHandle",&,D,N) originatingProcess;
@property (T@"NSError",&,D,N) error;
@property (TB,D,N,GisBarrier) barrier;
@property (T@"FBSSceneUpdate",?,&,D,N) parentUpdate;
@property (T@"FBProcessExecutionContext",?,&,D,N) executionContext;
@property (T@"RBSProcessHandle",?,&,D,N) clientProcessHandle;
@property (T@"FBSceneUpdateContext",?,&,D,N) updateContext;
@property (T@"FBWatchdogTransitionContext",?,&,D,N) watchdogTransitionContext;
@property (TB,?,D,N) allowCPUThrottling;
@property (TB,?,D,N,GisRunningBoardAssertionDisabled) runningBoardAssertionDisabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSSceneTransitionContext _baseClass];
+[FBSSceneTransitionContext transitionContext];
+[FBSSceneTransitionContext subclassExtension];
+[FBSSceneTransitionContext mutableSubclass];
+[FBSSceneTransitionContext _settingsExtensionsForSceneExtension:];
+[FBSSceneTransitionContext immutableSubclass];
+[FBSSceneTransitionContext _mutableClass];
```

## Instance methods

```
-[FBSSceneTransitionContext addAction:];
-[FBSSceneTransitionContext copyWithZone:];
-[FBSSceneTransitionContext initWithSettings:];
-[FBSSceneTransitionContext addActions:];
-[FBSSceneTransitionContext removeAction:];
-[FBSSceneTransitionContext removeActions:];
-[FBSSceneTransitionContext transientLocalClientSettings];
```
