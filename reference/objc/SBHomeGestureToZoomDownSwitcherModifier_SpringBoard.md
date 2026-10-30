# `SBHomeGestureToZoomDownSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 6 instance variables, 0 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _appLayout;
@"SBSwitcherModifier" _nonGestureInitiatedZoomModifier;
q _startingEnvironmentMode;
@"SBGestureInitiatedIconZoomAnimationAttributesSwitcherModifier" _animationAttributesModifier;
B _showingOrAnimatingCardsForFlyIn;
B _allowsLayoutBeforeTransitionBegins;
```

## Instance methods

```
-[SBHomeGestureToZoomDownSwitcherModifier isSwitcherWindowUserInteractionEnabled];
-[SBHomeGestureToZoomDownSwitcherModifier handleEvent:];
-[SBHomeGestureToZoomDownSwitcherModifier isHomeScreenContentRequired];
-[SBHomeGestureToZoomDownSwitcherModifier homeScreenBackdropBlurType];
-[SBHomeGestureToZoomDownSwitcherModifier isSwitcherWindowVisible];
-[SBHomeGestureToZoomDownSwitcherModifier appLayoutsToCacheSnapshots];
-[SBHomeGestureToZoomDownSwitcherModifier isWallpaperRequiredForSwitcher];
-[SBHomeGestureToZoomDownSwitcherModifier wallpaperStyle];
-[SBHomeGestureToZoomDownSwitcherModifier completesWhenChildrenComplete];
-[SBHomeGestureToZoomDownSwitcherModifier appLayoutsToCacheFullsizeSnapshots];
-[SBHomeGestureToZoomDownSwitcherModifier initWithTransitionID:appLayout:nonGestureInitiatedZoomModifier:effectiveStartingEnvironmentMode:liftOffVelocity:adjustAnimationAttributes:showingOrAnimatingCardsForFlyIn:];
-[SBHomeGestureToZoomDownSwitcherModifier responseForProposedChildResponse:childModifier:event:];
```
