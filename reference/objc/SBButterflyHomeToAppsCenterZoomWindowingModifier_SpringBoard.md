# `SBButterflyHomeToAppsCenterZoomWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 4 instance variables, 1 properties, 33 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _appLayout;
@"NSUUID" _transitionID;
@"SBAppsRegionModel" _toAppsRegionModel;
B _shouldForceDefaultAnchorPointForTransition;
```

## Properties

```
@property (TB,N,V_shouldForceDefaultAnchorPointForTransition) shouldForceDefaultAnchorPointForTransition;
```

## Instance methods

```
-[SBButterflyHomeToAppsCenterZoomWindowingModifier homeScreenScale];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier homeScreenBackdropBlurProgress];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier isSwitcherWindowUserInteractionEnabled];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier shouldUseAnchorPointToPinLayoutRolesToSpace:];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier isHomeScreenContentRequired];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier shouldForceDefaultAnchorPointForTransition];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier _opacitySettings];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier setShouldForceDefaultAnchorPointForTransition:];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier homeScreenBackdropBlurType];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier _layoutSettings];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier initWithAppLayout:];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier isSwitcherWindowVisible];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier appLayoutsToCacheSnapshots];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier shouldPinLayoutRolesToSpace:];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier transitionDidUpdate:];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier isWallpaperRequiredForSwitcher];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier fadeInDelayForSplitViewHandles];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier wallpaperStyle];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier transitionWillBegin:];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier visibleItems];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier shouldPerformCrossfadeForReduceMotion];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier cornersForItem:];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier animationAttributesForItem:];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier opacityForItem:];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier resizeProgressNotificationsForLayoutRole:inAppLayout:];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier perspectiveAngleForItem:];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier topMostItems];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier visibleAppSpaces];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier frameForItem:];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier _isItemZoomingAppLayout:];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier resizeProgressChanged:];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier shouldInterruptForActivity:];
-[SBButterflyHomeToAppsCenterZoomWindowingModifier transitionDidComplete:];
```
