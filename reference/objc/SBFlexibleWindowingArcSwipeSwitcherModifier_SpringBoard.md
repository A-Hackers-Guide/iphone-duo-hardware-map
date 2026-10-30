# `SBFlexibleWindowingArcSwipeSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 6 instance variables, 0 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _toAppLayout;
@"SBAppLayout" _fromAppLayout;
B _pinSpaceCornerRadiiToDisplayCornerRadii;
@"NSUUID" _systemApertureSuppressionIdentifier;
B _hideSplitViewHandles;
@"NSString" _uniqueTimerReason;
```

## Instance methods

```
-[SBFlexibleWindowingArcSwipeSwitcherModifier isSwitcherWindowUserInteractionEnabled];
-[SBFlexibleWindowingArcSwipeSwitcherModifier appLayoutsToEnsureExistForMainTransitionEvent:];
-[SBFlexibleWindowingArcSwipeSwitcherModifier isHomeScreenContentRequired];
-[SBFlexibleWindowingArcSwipeSwitcherModifier cornerRadiiForIndex:];
-[SBFlexibleWindowingArcSwipeSwitcherModifier shouldAsyncRenderUntilDelay:];
-[SBFlexibleWindowingArcSwipeSwitcherModifier animationAttributesForLayoutElement:];
-[SBFlexibleWindowingArcSwipeSwitcherModifier adjustedAppLayoutsForAppLayouts:];
-[SBFlexibleWindowingArcSwipeSwitcherModifier visibleSplitViewHandleNubViews];
-[SBFlexibleWindowingArcSwipeSwitcherModifier homeScreenBackdropBlurType];
-[SBFlexibleWindowingArcSwipeSwitcherModifier _layoutSettings];
-[SBFlexibleWindowingArcSwipeSwitcherModifier visibleSplitViewHandleDimmingViews];
-[SBFlexibleWindowingArcSwipeSwitcherModifier isSwitcherWindowVisible];
-[SBFlexibleWindowingArcSwipeSwitcherModifier appLayoutsToCacheSnapshots];
-[SBFlexibleWindowingArcSwipeSwitcherModifier transitionWillUpdate];
-[SBFlexibleWindowingArcSwipeSwitcherModifier isWallpaperRequiredForSwitcher];
-[SBFlexibleWindowingArcSwipeSwitcherModifier visibleAppLayouts];
-[SBFlexibleWindowingArcSwipeSwitcherModifier isContentStatusBarVisibleForIndex:];
-[SBFlexibleWindowingArcSwipeSwitcherModifier fadeInDelayForSplitViewHandles];
-[SBFlexibleWindowingArcSwipeSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBFlexibleWindowingArcSwipeSwitcherModifier transitionDidEnd];
-[SBFlexibleWindowingArcSwipeSwitcherModifier handleTimerEvent:];
-[SBFlexibleWindowingArcSwipeSwitcherModifier wallpaperStyle];
-[SBFlexibleWindowingArcSwipeSwitcherModifier transitionWillBegin];
-[SBFlexibleWindowingArcSwipeSwitcherModifier keyboardSuppressionMode];
-[SBFlexibleWindowingArcSwipeSwitcherModifier shouldPerformCrossfadeForReduceMotion];
-[SBFlexibleWindowingArcSwipeSwitcherModifier appLayoutsToResignActive];
-[SBFlexibleWindowingArcSwipeSwitcherModifier asyncRenderingAttributesForAppLayout:];
-[SBFlexibleWindowingArcSwipeSwitcherModifier appLayoutsToCacheFullsizeSnapshots];
-[SBFlexibleWindowingArcSwipeSwitcherModifier initWithTransitionID:fromAppLayout:toAppLayout:pinSpaceCornerRadiiToDisplayCornerRadii:];
```
