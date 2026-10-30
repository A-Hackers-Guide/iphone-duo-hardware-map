# `SBButterflyHomeGestureToZoomDownWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 7 instance variables, 0 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _appLayout;
@"SBChainableModifier" _nonGestureInitiatedZoomModifier;
q _startingEnvironmentMode;
@"SBButterflyGestureInitiatedIconZoomAnimationAttributesWindowingModifier" _animationAttributesModifier;
B _showingOrAnimatingCardsForFlyIn;
B _allowsLayoutBeforeTransitionBegins;
@"NSUUID" _transitionID;
```

## Instance methods

```
-[SBButterflyHomeGestureToZoomDownWindowingModifier isSwitcherWindowUserInteractionEnabled];
-[SBButterflyHomeGestureToZoomDownWindowingModifier isHomeScreenContentRequired];
-[SBButterflyHomeGestureToZoomDownWindowingModifier homeScreenBackdropBlurType];
-[SBButterflyHomeGestureToZoomDownWindowingModifier isSwitcherWindowVisible];
-[SBButterflyHomeGestureToZoomDownWindowingModifier appLayoutsToCacheSnapshots];
-[SBButterflyHomeGestureToZoomDownWindowingModifier isWallpaperRequiredForSwitcher];
-[SBButterflyHomeGestureToZoomDownWindowingModifier didUpdate];
-[SBButterflyHomeGestureToZoomDownWindowingModifier wallpaperStyle];
-[SBButterflyHomeGestureToZoomDownWindowingModifier transitionWillBegin:];
-[SBButterflyHomeGestureToZoomDownWindowingModifier completesWhenChildrenComplete];
-[SBButterflyHomeGestureToZoomDownWindowingModifier shouldPerformCrossfadeForReduceMotion];
-[SBButterflyHomeGestureToZoomDownWindowingModifier initWithAppLayout:nonGestureInitiatedZoomModifier:effectiveStartingEnvironmentMode:liftOffVelocity:adjustAnimationAttributes:showingOrAnimatingCardsForFlyIn:];
-[SBButterflyHomeGestureToZoomDownWindowingModifier shouldInterruptForActivity:];
```
