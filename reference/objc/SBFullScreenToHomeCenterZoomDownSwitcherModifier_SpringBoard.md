# `SBFullScreenToHomeCenterZoomDownSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 5 instance variables, 1 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _appLayout;
{CGPoint="x"d"y"d} _liftOffVelocity;
d _offsetYPercentOfScreenHeight;
@"SBSwitcherModifier" _coplanarModifier;
B _shouldForceDefaultAnchorPointForTransition;
```

## Properties

```
@property (TB,N,V_shouldForceDefaultAnchorPointForTransition) shouldForceDefaultAnchorPointForTransition;
```

## Instance methods

```
-[SBFullScreenToHomeCenterZoomDownSwitcherModifier scaleForIndex:];
-[SBFullScreenToHomeCenterZoomDownSwitcherModifier anchorPointForIndex:];
-[SBFullScreenToHomeCenterZoomDownSwitcherModifier isSwitcherWindowUserInteractionEnabled];
-[SBFullScreenToHomeCenterZoomDownSwitcherModifier shouldUseAnchorPointToPinLayoutRolesToSpace:];
-[SBFullScreenToHomeCenterZoomDownSwitcherModifier isHomeScreenContentRequired];
-[SBFullScreenToHomeCenterZoomDownSwitcherModifier didMoveToParentModifier:];
-[SBFullScreenToHomeCenterZoomDownSwitcherModifier shouldForceDefaultAnchorPointForTransition];
-[SBFullScreenToHomeCenterZoomDownSwitcherModifier cornerRadiiForIndex:];
-[SBFullScreenToHomeCenterZoomDownSwitcherModifier _opacitySettings];
-[SBFullScreenToHomeCenterZoomDownSwitcherModifier adjustedSpaceAccessoryViewAnchorPoint:forAppLayout:];
-[SBFullScreenToHomeCenterZoomDownSwitcherModifier shouldFireTransitionCompletionInDefaultRunLoopMode];
-[SBFullScreenToHomeCenterZoomDownSwitcherModifier animationAttributesForLayoutElement:];
-[SBFullScreenToHomeCenterZoomDownSwitcherModifier setShouldForceDefaultAnchorPointForTransition:];
-[SBFullScreenToHomeCenterZoomDownSwitcherModifier homeScreenBackdropBlurType];
-[SBFullScreenToHomeCenterZoomDownSwitcherModifier _layoutSettings];
-[SBFullScreenToHomeCenterZoomDownSwitcherModifier adjustedSpaceAccessoryViewFrame:forAppLayout:];
-[SBFullScreenToHomeCenterZoomDownSwitcherModifier topMostLayoutElements];
-[SBFullScreenToHomeCenterZoomDownSwitcherModifier isSwitcherWindowVisible];
-[SBFullScreenToHomeCenterZoomDownSwitcherModifier appLayoutsToCacheSnapshots];
-[SBFullScreenToHomeCenterZoomDownSwitcherModifier shouldPinLayoutRolesToSpace:];
-[SBFullScreenToHomeCenterZoomDownSwitcherModifier isWallpaperRequiredForSwitcher];
-[SBFullScreenToHomeCenterZoomDownSwitcherModifier visibleAppLayouts];
-[SBFullScreenToHomeCenterZoomDownSwitcherModifier fadeInDelayForSplitViewHandles];
-[SBFullScreenToHomeCenterZoomDownSwitcherModifier perspectiveAngleForIndex:];
-[SBFullScreenToHomeCenterZoomDownSwitcherModifier wallpaperStyle];
-[SBFullScreenToHomeCenterZoomDownSwitcherModifier frameForIndex:];
-[SBFullScreenToHomeCenterZoomDownSwitcherModifier transitionWillBegin];
-[SBFullScreenToHomeCenterZoomDownSwitcherModifier initWithTransitionID:appLayout:offsetYPercentOfScreenHeight:];
-[SBFullScreenToHomeCenterZoomDownSwitcherModifier _isIndexCenterZoomAppLayout:];
```
