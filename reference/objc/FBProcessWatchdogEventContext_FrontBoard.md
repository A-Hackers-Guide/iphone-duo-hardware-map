# `FBProcessWatchdogEventContext`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 4 instance variables, 8 properties, 9 instance methods, 1 class methods

## Instance variables

```
q _event;
@"FBSSceneSettings" _sceneSettings;
@"FBSSceneTransitionContext" _sceneTransitionContext;
@"FBSceneUpdateContext" _sceneUpdateContext;
```

## Properties

```
@property (Tq,R,N,V_event) event;
@property (T@"FBSceneUpdateContext",R,N,V_sceneUpdateContext) sceneUpdateContext;
@property (T@"FBSSceneSettings",R,N,V_sceneSettings) sceneSettings;
@property (T@"FBSSceneTransitionContext",R,W,N,V_sceneTransitionContext) sceneTransitionContext;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBProcessWatchdogEventContext contextForEvent:settings:transitionContext:];
```

## Instance methods

```
-[FBProcessWatchdogEventContext sceneSettings];
-[FBProcessWatchdogEventContext succinctDescriptionBuilder];
-[FBProcessWatchdogEventContext sceneTransitionContext];
-[FBProcessWatchdogEventContext event];
-[FBProcessWatchdogEventContext descriptionWithMultilinePrefix:];
-[FBProcessWatchdogEventContext succinctDescription];
-[FBProcessWatchdogEventContext description];
-[FBProcessWatchdogEventContext sceneUpdateContext];
-[FBProcessWatchdogEventContext descriptionBuilderWithMultilinePrefix:];
```
