# `SBButterflyAppsToHomeCenterZoomDownWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 6 instance variables, 0 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _appLayout;
d _offsetYPercentOfScreenHeight;
@"NSUUID" _transitionID;
@"SBButterflyCoplanarWindowingModifier" _coplanarModifier;
q _coplanarSpacingType;
@"SBAppsRegionModel" _initialAppsRegionModel;
```

## Instance methods

```
-[SBButterflyAppsToHomeCenterZoomDownWindowingModifier isSwitcherWindowUserInteractionEnabled];
-[SBButterflyAppsToHomeCenterZoomDownWindowingModifier isHomeScreenContentRequired];
-[SBButterflyAppsToHomeCenterZoomDownWindowingModifier _opacitySettings];
-[SBButterflyAppsToHomeCenterZoomDownWindowingModifier clipsToUnobscuredMarginAtIndex:];
-[SBButterflyAppsToHomeCenterZoomDownWindowingModifier shouldFireTransitionCompletionInDefaultRunLoopMode];
-[SBButterflyAppsToHomeCenterZoomDownWindowingModifier homeScreenBackdropBlurType];
-[SBButterflyAppsToHomeCenterZoomDownWindowingModifier _layoutSettings];
-[SBButterflyAppsToHomeCenterZoomDownWindowingModifier isSwitcherWindowVisible];
-[SBButterflyAppsToHomeCenterZoomDownWindowingModifier appLayoutsToCacheSnapshots];
-[SBButterflyAppsToHomeCenterZoomDownWindowingModifier isWallpaperRequiredForSwitcher];
-[SBButterflyAppsToHomeCenterZoomDownWindowingModifier fadeInDelayForSplitViewHandles];
-[SBButterflyAppsToHomeCenterZoomDownWindowingModifier wallpaperStyle];
-[SBButterflyAppsToHomeCenterZoomDownWindowingModifier transitionWillBegin:];
-[SBButterflyAppsToHomeCenterZoomDownWindowingModifier visibleItems];
-[SBButterflyAppsToHomeCenterZoomDownWindowingModifier shouldPerformCrossfadeForReduceMotion];
-[SBButterflyAppsToHomeCenterZoomDownWindowingModifier cornersForItem:];
-[SBButterflyAppsToHomeCenterZoomDownWindowingModifier animationAttributesForItem:];
-[SBButterflyAppsToHomeCenterZoomDownWindowingModifier opacityForItem:];
-[SBButterflyAppsToHomeCenterZoomDownWindowingModifier topMostItems];
-[SBButterflyAppsToHomeCenterZoomDownWindowingModifier visibleAppSpaces];
-[SBButterflyAppsToHomeCenterZoomDownWindowingModifier frameForItem:];
-[SBButterflyAppsToHomeCenterZoomDownWindowingModifier _isZoomingItem:];
-[SBButterflyAppsToHomeCenterZoomDownWindowingModifier initWithZoomingAppLayout:offsetYPercentOfScreenHeight:];
-[SBButterflyAppsToHomeCenterZoomDownWindowingModifier initWithZoomingAppLayout:offsetYPercentOfScreenHeight:initialAppsRegionModel:coplanarSpacingType:];
-[SBButterflyAppsToHomeCenterZoomDownWindowingModifier shouldInterruptForActivity:];
-[SBButterflyAppsToHomeCenterZoomDownWindowingModifier transitionDidComplete:];
```
