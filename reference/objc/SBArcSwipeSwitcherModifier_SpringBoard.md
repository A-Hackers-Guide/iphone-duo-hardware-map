# `SBArcSwipeSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 4 instance variables, 0 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _toAppLayout;
@"SBAppLayout" _fromAppLayout;
B _pinSpaceCornerRadiiToDisplayCornerRadii;
@"NSUUID" _systemApertureSuppressionIdentifier;
```

## Instance methods

```
-[SBArcSwipeSwitcherModifier isSwitcherWindowUserInteractionEnabled];
-[SBArcSwipeSwitcherModifier isHomeScreenContentRequired];
-[SBArcSwipeSwitcherModifier cornerRadiiForIndex:];
-[SBArcSwipeSwitcherModifier shouldAsyncRenderUntilDelay:];
-[SBArcSwipeSwitcherModifier animationAttributesForLayoutElement:];
-[SBArcSwipeSwitcherModifier homeScreenBackdropBlurType];
-[SBArcSwipeSwitcherModifier _layoutSettings];
-[SBArcSwipeSwitcherModifier isSwitcherWindowVisible];
-[SBArcSwipeSwitcherModifier appLayoutsToCacheSnapshots];
-[SBArcSwipeSwitcherModifier isWallpaperRequiredForSwitcher];
-[SBArcSwipeSwitcherModifier visibleAppLayouts];
-[SBArcSwipeSwitcherModifier isContentStatusBarVisibleForIndex:];
-[SBArcSwipeSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBArcSwipeSwitcherModifier transitionDidEnd];
-[SBArcSwipeSwitcherModifier wallpaperStyle];
-[SBArcSwipeSwitcherModifier transitionWillBegin];
-[SBArcSwipeSwitcherModifier keyboardSuppressionMode];
-[SBArcSwipeSwitcherModifier shouldPerformCrossfadeForReduceMotion];
-[SBArcSwipeSwitcherModifier appLayoutsToResignActive];
-[SBArcSwipeSwitcherModifier asyncRenderingAttributesForAppLayout:];
-[SBArcSwipeSwitcherModifier appLayoutsToCacheFullsizeSnapshots];
-[SBArcSwipeSwitcherModifier initWithTransitionID:fromAppLayout:toAppLayout:pinSpaceCornerRadiiToDisplayCornerRadii:];
```
