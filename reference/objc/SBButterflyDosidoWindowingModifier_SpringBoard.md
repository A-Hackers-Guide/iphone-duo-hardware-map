# `SBButterflyDosidoWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 5 instance variables, 1 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _fromAppLayout;
@"SBAppLayout" _toAppLayout;
@"SBAppsRegionModel" _fromAppsRegionModel;
@"NSUUID" _transitionID;
B _shouldSuppressScaleAnimation;
```

## Properties

```
@property (TB,N,V_shouldSuppressScaleAnimation) shouldSuppressScaleAnimation;
```

## Instance methods

```
-[SBButterflyDosidoWindowingModifier homeScreenDimmingAlpha];
-[SBButterflyDosidoWindowingModifier isSwitcherWindowUserInteractionEnabled];
-[SBButterflyDosidoWindowingModifier isHomeScreenContentRequired];
-[SBButterflyDosidoWindowingModifier homeScreenBackdropBlurType];
-[SBButterflyDosidoWindowingModifier _layoutSettings];
-[SBButterflyDosidoWindowingModifier isSwitcherWindowVisible];
-[SBButterflyDosidoWindowingModifier appLayoutsToCacheSnapshots];
-[SBButterflyDosidoWindowingModifier transitionDidUpdate:];
-[SBButterflyDosidoWindowingModifier isWallpaperRequiredForSwitcher];
-[SBButterflyDosidoWindowingModifier wallpaperStyle];
-[SBButterflyDosidoWindowingModifier transitionWillBegin:];
-[SBButterflyDosidoWindowingModifier visibleItems];
-[SBButterflyDosidoWindowingModifier shouldPerformCrossfadeForReduceMotion];
-[SBButterflyDosidoWindowingModifier cornersForItem:];
-[SBButterflyDosidoWindowingModifier animationAttributesForItem:];
-[SBButterflyDosidoWindowingModifier opacityForItem:];
-[SBButterflyDosidoWindowingModifier deckRegionModel];
-[SBButterflyDosidoWindowingModifier appsRegionModel];
-[SBButterflyDosidoWindowingModifier _deckRegionModel];
-[SBButterflyDosidoWindowingModifier _deckRegionModelIncludingAppsRegionModelAppLayouts];
-[SBButterflyDosidoWindowingModifier setShouldSuppressScaleAnimation:];
-[SBButterflyDosidoWindowingModifier shouldInterruptForActivity:];
-[SBButterflyDosidoWindowingModifier shouldSuppressScaleAnimation];
-[SBButterflyDosidoWindowingModifier transitionDidComplete:];
```
