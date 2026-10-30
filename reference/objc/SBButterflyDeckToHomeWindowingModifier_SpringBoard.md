# `SBButterflyDeckToHomeWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 5 instance variables, 0 properties, 30 instance methods, 0 class methods

## Instance variables

```
q _direction;
@"SBDeckRegionModel" _toDeckRegionModel;
@"SBDeckRegionModel" _fromDeckRegionModel;
@"SBWindowingModifier" _deckLayoutModifier;
@"NSUUID" _transitionID;
```

## Instance methods

```
-[SBButterflyDeckToHomeWindowingModifier isSwitcherWindowUserInteractionEnabled];
-[SBButterflyDeckToHomeWindowingModifier containerStatusBarAnimationDuration];
-[SBButterflyDeckToHomeWindowingModifier isHomeScreenContentRequired];
-[SBButterflyDeckToHomeWindowingModifier clipsToUnobscuredMarginAtIndex:];
-[SBButterflyDeckToHomeWindowingModifier homeScreenBackdropBlurType];
-[SBButterflyDeckToHomeWindowingModifier isSwitcherWindowVisible];
-[SBButterflyDeckToHomeWindowingModifier appLayoutsToCacheSnapshots];
-[SBButterflyDeckToHomeWindowingModifier transitionDidUpdate:];
-[SBButterflyDeckToHomeWindowingModifier isWallpaperRequiredForSwitcher];
-[SBButterflyDeckToHomeWindowingModifier wallpaperStyle];
-[SBButterflyDeckToHomeWindowingModifier transitionWillBegin:];
-[SBButterflyDeckToHomeWindowingModifier shadowForItem:];
-[SBButterflyDeckToHomeWindowingModifier visibleItems];
-[SBButterflyDeckToHomeWindowingModifier shouldPerformCrossfadeForReduceMotion];
-[SBButterflyDeckToHomeWindowingModifier cornersForItem:];
-[SBButterflyDeckToHomeWindowingModifier shouldUseBrightMaterialForIndex:];
-[SBButterflyDeckToHomeWindowingModifier animationAttributesForItem:];
-[SBButterflyDeckToHomeWindowingModifier opacityForItem:];
-[SBButterflyDeckToHomeWindowingModifier dimmingAlphaForItem:];
-[SBButterflyDeckToHomeWindowingModifier timerFired:];
-[SBButterflyDeckToHomeWindowingModifier _isEffectivelyHome];
-[SBButterflyDeckToHomeWindowingModifier frameForItem:];
-[SBButterflyDeckToHomeWindowingModifier titleStyleForItem:];
-[SBButterflyDeckToHomeWindowingModifier deckRegionModel];
-[SBButterflyDeckToHomeWindowingModifier _appLayoutsForSwitcher];
-[SBButterflyDeckToHomeWindowingModifier _dismissForEmptySwitcherResponseName];
-[SBButterflyDeckToHomeWindowingModifier _isItemInDeck:];
-[SBButterflyDeckToHomeWindowingModifier initWithDeckModifier:];
-[SBButterflyDeckToHomeWindowingModifier shouldInterruptForActivity:];
-[SBButterflyDeckToHomeWindowingModifier transitionDidComplete:];
```
