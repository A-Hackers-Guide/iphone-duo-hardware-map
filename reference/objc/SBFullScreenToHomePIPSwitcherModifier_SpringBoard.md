# `SBFullScreenToHomePIPSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 6 instance variables, 2 properties, 37 instance methods, 0 class methods

## Instance variables

```
q _layoutRole;
@"SBAppLayout" _appLayout;
B _shouldHide;
@"SBCoplanarSwitcherModifier" _coplanarModifier;
B _shouldForceDefaultAnchorPointForTransition;
B _shouldClippingTakeShadowIntoAccount;
```

## Properties

```
@property (TB,N,V_shouldForceDefaultAnchorPointForTransition) shouldForceDefaultAnchorPointForTransition;
@property (TB,N,V_shouldClippingTakeShadowIntoAccount) shouldClippingTakeShadowIntoAccount;
```

## Instance methods

```
-[SBFullScreenToHomePIPSwitcherModifier scaleForIndex:];
-[SBFullScreenToHomePIPSwitcherModifier anchorPointForIndex:];
-[SBFullScreenToHomePIPSwitcherModifier clippingFrameForIndex:withBounds:];
-[SBFullScreenToHomePIPSwitcherModifier rotationAngleForIndex:];
-[SBFullScreenToHomePIPSwitcherModifier isSwitcherWindowUserInteractionEnabled];
-[SBFullScreenToHomePIPSwitcherModifier shouldUseAnchorPointToPinLayoutRolesToSpace:];
-[SBFullScreenToHomePIPSwitcherModifier clipsToBoundsAtIndex:];
-[SBFullScreenToHomePIPSwitcherModifier isHomeScreenContentRequired];
-[SBFullScreenToHomePIPSwitcherModifier didMoveToParentModifier:];
-[SBFullScreenToHomePIPSwitcherModifier shouldForceDefaultAnchorPointForTransition];
-[SBFullScreenToHomePIPSwitcherModifier cornerRadiiForIndex:];
-[SBFullScreenToHomePIPSwitcherModifier adjustedSpaceAccessoryViewAnchorPoint:forAppLayout:];
-[SBFullScreenToHomePIPSwitcherModifier animationAttributesForLayoutElement:];
-[SBFullScreenToHomePIPSwitcherModifier setShouldForceDefaultAnchorPointForTransition:];
-[SBFullScreenToHomePIPSwitcherModifier clippingFrameForLayoutRole:inAppLayout:atIndex:withBounds:];
-[SBFullScreenToHomePIPSwitcherModifier homeScreenBackdropBlurType];
-[SBFullScreenToHomePIPSwitcherModifier adjustedSpaceAccessoryViewFrame:forAppLayout:];
-[SBFullScreenToHomePIPSwitcherModifier visibleHomeAffordanceLayoutElements];
-[SBFullScreenToHomePIPSwitcherModifier topMostLayoutElements];
-[SBFullScreenToHomePIPSwitcherModifier isSwitcherWindowVisible];
-[SBFullScreenToHomePIPSwitcherModifier appLayoutsToCacheSnapshots];
-[SBFullScreenToHomePIPSwitcherModifier shouldPinLayoutRolesToSpace:];
-[SBFullScreenToHomePIPSwitcherModifier transitionWillUpdate];
-[SBFullScreenToHomePIPSwitcherModifier isWallpaperRequiredForSwitcher];
-[SBFullScreenToHomePIPSwitcherModifier visibleAppLayouts];
-[SBFullScreenToHomePIPSwitcherModifier perspectiveAngleForIndex:];
-[SBFullScreenToHomePIPSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBFullScreenToHomePIPSwitcherModifier wallpaperStyle];
-[SBFullScreenToHomePIPSwitcherModifier frameForIndex:];
-[SBFullScreenToHomePIPSwitcherModifier transitionWillBegin];
-[SBFullScreenToHomePIPSwitcherModifier shouldClippingTakeShadowIntoAccount];
-[SBFullScreenToHomePIPSwitcherModifier _insetFrameForDiffuseShadowRadius:];
-[SBFullScreenToHomePIPSwitcherModifier setShouldClippingTakeShadowIntoAccount:];
-[SBFullScreenToHomePIPSwitcherModifier _isIndexSelectedAppLayout:];
-[SBFullScreenToHomePIPSwitcherModifier _shouldApplyMorphToPIPToIndex:];
-[SBFullScreenToHomePIPSwitcherModifier handleHideMorphToPIPAppLayoutEvent:];
-[SBFullScreenToHomePIPSwitcherModifier initWithTransitionID:appLayout:layoutRole:];
```
