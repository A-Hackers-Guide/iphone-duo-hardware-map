# `SBSceneLayoutWhitePointAdaptationController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 15 instance methods, 5 class methods

## Instance variables

```
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (T@"SBWindowScene",W,N,V_windowScene) windowScene;
```

## Class methods

```
+[SBSceneLayoutWhitePointAdaptationController sharedInstance];
+[SBSceneLayoutWhitePointAdaptationController _defaultAnimationDuration];
+[SBSceneLayoutWhitePointAdaptationController _defaultAnimationSettings];
+[SBSceneLayoutWhitePointAdaptationController _harmonySettings];
+[SBSceneLayoutWhitePointAdaptationController _isInteractiveUpdateEnabled];
```

## Instance methods

```
-[SBSceneLayoutWhitePointAdaptationController setWindowScene:];
-[SBSceneLayoutWhitePointAdaptationController init];
-[SBSceneLayoutWhitePointAdaptationController windowScene];
-[SBSceneLayoutWhitePointAdaptationController _applicationSceneHandleForLayoutElement:];
-[SBSceneLayoutWhitePointAdaptationController _deviceSceneHandlesFromEntities:];
-[SBSceneLayoutWhitePointAdaptationController _updateWhitePointAdaptationStrengthWithAnimationSettings:];
-[SBSceneLayoutWhitePointAdaptationController _updateWhitePointAdaptationStrengthWithFromApplicationScenes:toApplicationScenes:fromPercentage:toPercentage:animationSettings:interactive:];
-[SBSceneLayoutWhitePointAdaptationController _updateWhitePointAdaptationStrengthWithWorkspaceTransitionRequest:fromPercentage:toPercentage:animationSettings:cancelled:interactive:];
-[SBSceneLayoutWhitePointAdaptationController _whitePointAdaptivityStyleForLayoutElement:];
-[SBSceneLayoutWhitePointAdaptationController _whitePointAdaptivityStyleForSceneHandle:];
-[SBSceneLayoutWhitePointAdaptationController _whitePointAdaptivityStylesForLayoutState];
-[SBSceneLayoutWhitePointAdaptationController updateWhitePointAdaptationStrength];
-[SBSceneLayoutWhitePointAdaptationController updateWhitePointAdaptationStrengthWithAnimationSettings:];
-[SBSceneLayoutWhitePointAdaptationController updateWhitePointAdaptationStrengthWithFromApplicationSceneEntities:toApplicationSceneEntities:fromPercentage:toPercentage:animationSettings:interactive:];
-[SBSceneLayoutWhitePointAdaptationController updateWhitePointAdaptationStrengthWithWorkspaceTransitionRequest:animationTransitionContext:];
```
