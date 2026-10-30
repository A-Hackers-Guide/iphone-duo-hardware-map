# `SBButterflyDeckToAppWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 7 instance variables, 0 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _transitionID;
@"SBWindowingModifier" _deckModifier;
@"SBButterflyAppsLayoutModifier" _appsLayoutModifier;
@"SBAppsRegionModel" _fromAppsRegionModel;
@"SBDeckRegionModel" _fromDeckRegionModel;
q _direction;
B _isActivateAppFromGestureWhileInSwitcherTransition;
```

## Instance methods

```
-[SBButterflyDeckToAppWindowingModifier isSwitcherWindowUserInteractionEnabled];
-[SBButterflyDeckToAppWindowingModifier isHomeScreenContentRequired];
-[SBButterflyDeckToAppWindowingModifier clipsToUnobscuredMarginAtIndex:];
-[SBButterflyDeckToAppWindowingModifier homeScreenBackdropBlurType];
-[SBButterflyDeckToAppWindowingModifier isSwitcherWindowVisible];
-[SBButterflyDeckToAppWindowingModifier appLayoutsToCacheSnapshots];
-[SBButterflyDeckToAppWindowingModifier isWallpaperRequiredForSwitcher];
-[SBButterflyDeckToAppWindowingModifier fadeInDelayForSplitViewHandles];
-[SBButterflyDeckToAppWindowingModifier wallpaperStyle];
-[SBButterflyDeckToAppWindowingModifier transitionWillBegin:];
-[SBButterflyDeckToAppWindowingModifier wantsSceneResizesHostedContextForAppLayout:];
-[SBButterflyDeckToAppWindowingModifier visibleItems];
-[SBButterflyDeckToAppWindowingModifier shouldPerformCrossfadeForReduceMotion];
-[SBButterflyDeckToAppWindowingModifier cornersForItem:];
-[SBButterflyDeckToAppWindowingModifier animationAttributesForItem:];
-[SBButterflyDeckToAppWindowingModifier isLayoutRoleMatchMovedToScene:inAppLayout:];
-[SBButterflyDeckToAppWindowingModifier visibleAppSpaces];
-[SBButterflyDeckToAppWindowingModifier frameForItem:];
-[SBButterflyDeckToAppWindowingModifier deckRegionModel];
-[SBButterflyDeckToAppWindowingModifier appsRegionModel];
-[SBButterflyDeckToAppWindowingModifier _appLayoutToScrollToDuringTransition];
-[SBButterflyDeckToAppWindowingModifier initWithDeckModifier:];
-[SBButterflyDeckToAppWindowingModifier shouldInterruptForActivity:];
-[SBButterflyDeckToAppWindowingModifier transitionDidComplete:];
```
