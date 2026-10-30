# `SBFullScreenToHomeSlideOverSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 6 instance variables, 3 properties, 33 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _appLayout;
Q _direction;
@"SBFullScreenAppLayoutSwitcherModifier" _fullScreenModifier;
B _shouldBlurUnreadyScenes;
B _shouldForceDefaultAnchorPointForTransition;
q _startingScreenEdge;
```

## Properties

```
@property (Tq,N,V_startingScreenEdge) startingScreenEdge;
@property (TB,N,V_shouldBlurUnreadyScenes) shouldBlurUnreadyScenes;
@property (TB,N,V_shouldForceDefaultAnchorPointForTransition) shouldForceDefaultAnchorPointForTransition;
```

## Instance methods

```
-[SBFullScreenToHomeSlideOverSwitcherModifier scaleForIndex:];
-[SBFullScreenToHomeSlideOverSwitcherModifier anchorPointForIndex:];
-[SBFullScreenToHomeSlideOverSwitcherModifier isSwitcherWindowUserInteractionEnabled];
-[SBFullScreenToHomeSlideOverSwitcherModifier shouldUseAnchorPointToPinLayoutRolesToSpace:];
-[SBFullScreenToHomeSlideOverSwitcherModifier homeScreenAlpha];
-[SBFullScreenToHomeSlideOverSwitcherModifier isHomeScreenContentRequired];
-[SBFullScreenToHomeSlideOverSwitcherModifier shouldForceDefaultAnchorPointForTransition];
-[SBFullScreenToHomeSlideOverSwitcherModifier adjustedSpaceAccessoryViewAnchorPoint:forAppLayout:];
-[SBFullScreenToHomeSlideOverSwitcherModifier animationAttributesForLayoutElement:];
-[SBFullScreenToHomeSlideOverSwitcherModifier setShouldForceDefaultAnchorPointForTransition:];
-[SBFullScreenToHomeSlideOverSwitcherModifier homeScreenBackdropBlurType];
-[SBFullScreenToHomeSlideOverSwitcherModifier adjustedSpaceAccessoryViewFrame:forAppLayout:];
-[SBFullScreenToHomeSlideOverSwitcherModifier isSwitcherWindowVisible];
-[SBFullScreenToHomeSlideOverSwitcherModifier appLayoutsToCacheSnapshots];
-[SBFullScreenToHomeSlideOverSwitcherModifier shouldPinLayoutRolesToSpace:];
-[SBFullScreenToHomeSlideOverSwitcherModifier isWallpaperRequiredForSwitcher];
-[SBFullScreenToHomeSlideOverSwitcherModifier visibleAppLayouts];
-[SBFullScreenToHomeSlideOverSwitcherModifier perspectiveAngleForIndex:];
-[SBFullScreenToHomeSlideOverSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBFullScreenToHomeSlideOverSwitcherModifier wallpaperStyle];
-[SBFullScreenToHomeSlideOverSwitcherModifier frameForIndex:];
-[SBFullScreenToHomeSlideOverSwitcherModifier transitionWillBegin];
-[SBFullScreenToHomeSlideOverSwitcherModifier blurDelayForLayoutRole:inAppLayout:];
-[SBFullScreenToHomeSlideOverSwitcherModifier initWithTransitionID:appLayout:direction:];
-[SBFullScreenToHomeSlideOverSwitcherModifier isLayoutRoleMatchMovedToScene:inAppLayout:];
-[SBFullScreenToHomeSlideOverSwitcherModifier isLayoutRoleBlurred:inAppLayout:];
-[SBFullScreenToHomeSlideOverSwitcherModifier _isIndexSlideOverAppLayout:];
-[SBFullScreenToHomeSlideOverSwitcherModifier _shouldApplySlideOverLayoutToIndex:];
-[SBFullScreenToHomeSlideOverSwitcherModifier handleSceneReadyEvent:];
-[SBFullScreenToHomeSlideOverSwitcherModifier setShouldBlurUnreadyScenes:];
-[SBFullScreenToHomeSlideOverSwitcherModifier setStartingScreenEdge:];
-[SBFullScreenToHomeSlideOverSwitcherModifier shouldBlurUnreadyScenes];
-[SBFullScreenToHomeSlideOverSwitcherModifier startingScreenEdge];
```
