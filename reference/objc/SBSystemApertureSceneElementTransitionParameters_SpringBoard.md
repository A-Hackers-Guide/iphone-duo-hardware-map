# `SBSystemApertureSceneElementTransitionParameters`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _shouldSetForeground;
B _wantsForeground;
@"UIApplicationSceneTransitionContext" _transitionContext;
@"BSSettings" _otherSystemApertureSceneSettingsToApply;
{CGSize="width"d"height"d} _sceneSize;
```

## Properties

```
@property (TB,N,V_shouldSetForeground) shouldSetForeground;
@property (T{CGSize=dd},N,V_sceneSize) sceneSize;
@property (TB,N,V_wantsForeground) wantsForeground;
@property (T@"UIApplicationSceneTransitionContext",&,N,V_transitionContext) transitionContext;
@property (T@"BSSettings",C,N,V_otherSystemApertureSceneSettingsToApply) otherSystemApertureSceneSettingsToApply;
```

## Instance methods

```
-[SBSystemApertureSceneElementTransitionParameters transitionContext];
-[SBSystemApertureSceneElementTransitionParameters setTransitionContext:];
-[SBSystemApertureSceneElementTransitionParameters sceneSize];
-[SBSystemApertureSceneElementTransitionParameters wantsForeground];
-[SBSystemApertureSceneElementTransitionParameters otherSystemApertureSceneSettingsToApply];
-[SBSystemApertureSceneElementTransitionParameters setOtherSystemApertureSceneSettingsToApply:];
-[SBSystemApertureSceneElementTransitionParameters setSceneSize:];
-[SBSystemApertureSceneElementTransitionParameters setShouldSetForeground:];
-[SBSystemApertureSceneElementTransitionParameters setWantsForeground:];
-[SBSystemApertureSceneElementTransitionParameters shouldSetForeground];
```
