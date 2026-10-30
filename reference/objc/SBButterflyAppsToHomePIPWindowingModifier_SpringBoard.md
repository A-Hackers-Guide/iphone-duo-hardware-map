# `SBButterflyAppsToHomePIPWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 8 instance variables, 2 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _appLayout;
B _shouldHide;
@"SBButterflyCoplanarWindowingModifier" _coplanarModifier;
@"NSUUID" _transitionID;
q _zoomingAppLayoutPreviousScreenRegion;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _zoomingAppLayoutBoundingBox;
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
-[SBButterflyAppsToHomePIPWindowingModifier clippingFrameForIndex:withBounds:];
-[SBButterflyAppsToHomePIPWindowingModifier rotationAngleForIndex:];
-[SBButterflyAppsToHomePIPWindowingModifier isSwitcherWindowUserInteractionEnabled];
-[SBButterflyAppsToHomePIPWindowingModifier clipsToBoundsAtIndex:];
-[SBButterflyAppsToHomePIPWindowingModifier isHomeScreenContentRequired];
-[SBButterflyAppsToHomePIPWindowingModifier shouldForceDefaultAnchorPointForTransition];
-[SBButterflyAppsToHomePIPWindowingModifier setShouldForceDefaultAnchorPointForTransition:];
-[SBButterflyAppsToHomePIPWindowingModifier clippingFrameForLayoutRole:inAppLayout:atIndex:withBounds:];
-[SBButterflyAppsToHomePIPWindowingModifier homeScreenBackdropBlurType];
-[SBButterflyAppsToHomePIPWindowingModifier initWithAppLayout:];
-[SBButterflyAppsToHomePIPWindowingModifier visibleHomeAffordanceLayoutElements];
-[SBButterflyAppsToHomePIPWindowingModifier isSwitcherWindowVisible];
-[SBButterflyAppsToHomePIPWindowingModifier isWallpaperRequiredForSwitcher];
-[SBButterflyAppsToHomePIPWindowingModifier wallpaperStyle];
-[SBButterflyAppsToHomePIPWindowingModifier transitionWillBegin:];
-[SBButterflyAppsToHomePIPWindowingModifier visibleItems];
-[SBButterflyAppsToHomePIPWindowingModifier shouldPerformCrossfadeForReduceMotion];
-[SBButterflyAppsToHomePIPWindowingModifier cornersForItem:];
-[SBButterflyAppsToHomePIPWindowingModifier shouldClippingTakeShadowIntoAccount];
-[SBButterflyAppsToHomePIPWindowingModifier animationAttributesForItem:];
-[SBButterflyAppsToHomePIPWindowingModifier opacityForItem:];
-[SBButterflyAppsToHomePIPWindowingModifier perspectiveAngleForItem:];
-[SBButterflyAppsToHomePIPWindowingModifier setShouldClippingTakeShadowIntoAccount:];
-[SBButterflyAppsToHomePIPWindowingModifier topMostItems];
-[SBButterflyAppsToHomePIPWindowingModifier visibleAppSpaces];
-[SBButterflyAppsToHomePIPWindowingModifier frameForItem:];
-[SBButterflyAppsToHomePIPWindowingModifier _isItemAppLayout:];
-[SBButterflyAppsToHomePIPWindowingModifier _shouldApplyMorphToPIPToItem:];
-[SBButterflyAppsToHomePIPWindowingModifier didHideMorphToPIPAppLayout:];
-[SBButterflyAppsToHomePIPWindowingModifier shouldInterruptForActivity:];
-[SBButterflyAppsToHomePIPWindowingModifier transitionDidComplete:];
```
