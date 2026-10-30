# `SBCrossfadeDosidoSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 4 instance variables, 1 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"SBHomeScreenSwitcherModifier" _homeScreenModifier;
@"SBAppLayout" _fromAppLayout;
@"SBAppLayout" _toAppLayout;
B _fullScreenTransition;
```

## Properties

```
@property (TB,N,GisFullScreenTransition,V_fullScreenTransition) fullScreenTransition;
```

## Instance methods

```
-[SBCrossfadeDosidoSwitcherModifier scaleForIndex:];
-[SBCrossfadeDosidoSwitcherModifier homeScreenScale];
-[SBCrossfadeDosidoSwitcherModifier homeScreenBackdropBlurProgress];
-[SBCrossfadeDosidoSwitcherModifier homeScreenDimmingAlpha];
-[SBCrossfadeDosidoSwitcherModifier isSwitcherWindowUserInteractionEnabled];
-[SBCrossfadeDosidoSwitcherModifier homeScreenAlpha];
-[SBCrossfadeDosidoSwitcherModifier isHomeScreenContentRequired];
-[SBCrossfadeDosidoSwitcherModifier _opacitySettings];
-[SBCrossfadeDosidoSwitcherModifier transactionCompletionOptions];
-[SBCrossfadeDosidoSwitcherModifier animationAttributesForLayoutElement:];
-[SBCrossfadeDosidoSwitcherModifier homeScreenBackdropBlurType];
-[SBCrossfadeDosidoSwitcherModifier topMostLayoutElements];
-[SBCrossfadeDosidoSwitcherModifier isSwitcherWindowVisible];
-[SBCrossfadeDosidoSwitcherModifier initWithTransitionID:fromAppLayout:toAppLayout:];
-[SBCrossfadeDosidoSwitcherModifier appLayoutsToCacheSnapshots];
-[SBCrossfadeDosidoSwitcherModifier isWallpaperRequiredForSwitcher];
-[SBCrossfadeDosidoSwitcherModifier visibleAppLayouts];
-[SBCrossfadeDosidoSwitcherModifier setFullScreenTransition:];
-[SBCrossfadeDosidoSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBCrossfadeDosidoSwitcherModifier _isFromAppLayoutAtIndex:];
-[SBCrossfadeDosidoSwitcherModifier wallpaperStyle];
-[SBCrossfadeDosidoSwitcherModifier frameForIndex:];
-[SBCrossfadeDosidoSwitcherModifier transitionWillBegin];
-[SBCrossfadeDosidoSwitcherModifier wallpaperScale];
-[SBCrossfadeDosidoSwitcherModifier _isToOrFromAppLayoutAtIndex:];
-[SBCrossfadeDosidoSwitcherModifier _shouldEnsureHomeScreenVisible];
-[SBCrossfadeDosidoSwitcherModifier isFullScreenTransition];
-[SBCrossfadeDosidoSwitcherModifier _isToAppLayoutAtIndex:];
```
