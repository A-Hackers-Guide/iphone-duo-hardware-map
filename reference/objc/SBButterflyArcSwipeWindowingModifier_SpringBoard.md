# `SBButterflyArcSwipeWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 13 instance variables, 0 properties, 33 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _transitionID;
@"SBButterflyRegionDividerAnimationWindowingModifier" _regionDividerAnimationModifier;
@"SBAppLayout" _toAppLayout;
@"SBAppLayout" _fromAppLayout;
@"SBAppLayout" _selectedAppLayout;
@"SBAppLayout" _steadyAppLayout;
@"SBDeckRegionModel" _deckRegionModel;
@"SBSwitcherKeyboardSuppressionMode" _keyboardSuppressionMode;
@"NSUUID" _systemApertureSuppressionIdentifier;
@"SBUnlockedEnvironmentState" _fromUnlockedEnvironmentState;
@"SBUnlockedEnvironmentState" _toUnlockedEnvironmentState;
B _isHidingHomeScreenContent;
@"NSString" _timerReason;
```

## Instance methods

```
-[SBButterflyArcSwipeWindowingModifier homeScreenScale];
-[SBButterflyArcSwipeWindowingModifier isSwitcherWindowUserInteractionEnabled];
-[SBButterflyArcSwipeWindowingModifier homeScreenAlpha];
-[SBButterflyArcSwipeWindowingModifier isHomeScreenContentRequired];
-[SBButterflyArcSwipeWindowingModifier shouldAsyncRenderUntilDelay:];
-[SBButterflyArcSwipeWindowingModifier homeScreenBackdropBlurType];
-[SBButterflyArcSwipeWindowingModifier _layoutSettings];
-[SBButterflyArcSwipeWindowingModifier isSwitcherWindowVisible];
-[SBButterflyArcSwipeWindowingModifier appLayoutsToCacheSnapshots];
-[SBButterflyArcSwipeWindowingModifier isWallpaperRequiredForSwitcher];
-[SBButterflyArcSwipeWindowingModifier isContentStatusBarVisibleForIndex:];
-[SBButterflyArcSwipeWindowingModifier fadeInDelayForSplitViewHandles];
-[SBButterflyArcSwipeWindowingModifier wallpaperStyle];
-[SBButterflyArcSwipeWindowingModifier keyboardSuppressionMode];
-[SBButterflyArcSwipeWindowingModifier transitionWillBegin:];
-[SBButterflyArcSwipeWindowingModifier wantsSceneResizesHostedContextForAppLayout:];
-[SBButterflyArcSwipeWindowingModifier visibleItems];
-[SBButterflyArcSwipeWindowingModifier shouldPerformCrossfadeForReduceMotion];
-[SBButterflyArcSwipeWindowingModifier cornersForItem:];
-[SBButterflyArcSwipeWindowingModifier appLayoutsToResignActive];
-[SBButterflyArcSwipeWindowingModifier animationAttributesForItem:];
-[SBButterflyArcSwipeWindowingModifier opacityForItem:];
-[SBButterflyArcSwipeWindowingModifier asyncRenderingAttributesForAppLayout:];
-[SBButterflyArcSwipeWindowingModifier isLayoutRoleMatchMovedToScene:inAppLayout:];
-[SBButterflyArcSwipeWindowingModifier timerFired:];
-[SBButterflyArcSwipeWindowingModifier topMostItems];
-[SBButterflyArcSwipeWindowingModifier willBegin];
-[SBButterflyArcSwipeWindowingModifier didComplete];
-[SBButterflyArcSwipeWindowingModifier deckRegionModel];
-[SBButterflyArcSwipeWindowingModifier _isSteadyItem:];
-[SBButterflyArcSwipeWindowingModifier initWithFromAppLayout:toAppLayout:selectedAppLayout:steadyAppLayout:deckRegionModel:keyboardSuppressionMode:];
-[SBButterflyArcSwipeWindowingModifier shouldInterruptForActivity:];
-[SBButterflyArcSwipeWindowingModifier transitionDidComplete:];
```
