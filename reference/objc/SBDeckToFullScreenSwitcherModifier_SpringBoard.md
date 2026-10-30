# `SBDeckToFullScreenSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 4 instance variables, 0 properties, 20 instance methods, 0 class methods

## Instance variables

```
q _direction;
@"SBAppLayout" _fullScreenAppLayout;
@"SBSwitcherModifier" _deckModifier;
B _wantsMinificationFilter;
```

## Instance methods

```
-[SBDeckToFullScreenSwitcherModifier isSwitcherWindowUserInteractionEnabled];
-[SBDeckToFullScreenSwitcherModifier isHomeScreenContentRequired];
-[SBDeckToFullScreenSwitcherModifier cornerRadiiForIndex:];
-[SBDeckToFullScreenSwitcherModifier shouldAsyncRenderUntilDelay:];
-[SBDeckToFullScreenSwitcherModifier animationAttributesForLayoutElement:];
-[SBDeckToFullScreenSwitcherModifier homeScreenBackdropBlurType];
-[SBDeckToFullScreenSwitcherModifier _layoutSettings];
-[SBDeckToFullScreenSwitcherModifier topMostLayoutElements];
-[SBDeckToFullScreenSwitcherModifier isSwitcherWindowVisible];
-[SBDeckToFullScreenSwitcherModifier appLayoutsToCacheSnapshots];
-[SBDeckToFullScreenSwitcherModifier handleTransitionEvent:];
-[SBDeckToFullScreenSwitcherModifier isWallpaperRequiredForSwitcher];
-[SBDeckToFullScreenSwitcherModifier visibleAppLayouts];
-[SBDeckToFullScreenSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBDeckToFullScreenSwitcherModifier wallpaperStyle];
-[SBDeckToFullScreenSwitcherModifier transitionWillBegin];
-[SBDeckToFullScreenSwitcherModifier asyncRenderingAttributesForAppLayout:];
-[SBDeckToFullScreenSwitcherModifier appLayoutToScrollToBeforeTransitioning];
-[SBDeckToFullScreenSwitcherModifier _appLayoutToScrollToDuringTransition];
-[SBDeckToFullScreenSwitcherModifier initWithTransitionID:direction:fullScreenAppLayout:deckModifier:];
```
