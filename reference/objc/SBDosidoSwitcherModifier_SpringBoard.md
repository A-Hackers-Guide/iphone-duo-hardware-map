# `SBDosidoSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 4 instance variables, 1 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _fromAppLayout;
@"SBAppLayout" _toAppLayout;
Q _direction;
B _shouldSuppressScaleAnimation;
```

## Properties

```
@property (TB,N,V_shouldSuppressScaleAnimation) shouldSuppressScaleAnimation;
```

## Instance methods

```
-[SBDosidoSwitcherModifier isSwitcherWindowUserInteractionEnabled];
-[SBDosidoSwitcherModifier isHomeScreenContentRequired];
-[SBDosidoSwitcherModifier cornerRadiiForIndex:];
-[SBDosidoSwitcherModifier shouldAsyncRenderUntilDelay:];
-[SBDosidoSwitcherModifier animationAttributesForLayoutElement:];
-[SBDosidoSwitcherModifier adjustedAppLayoutsForAppLayouts:];
-[SBDosidoSwitcherModifier homeScreenBackdropBlurType];
-[SBDosidoSwitcherModifier _layoutSettings];
-[SBDosidoSwitcherModifier isSwitcherWindowVisible];
-[SBDosidoSwitcherModifier appLayoutsToCacheSnapshots];
-[SBDosidoSwitcherModifier transitionWillUpdate];
-[SBDosidoSwitcherModifier isWallpaperRequiredForSwitcher];
-[SBDosidoSwitcherModifier visibleAppLayouts];
-[SBDosidoSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBDosidoSwitcherModifier wallpaperStyle];
-[SBDosidoSwitcherModifier transitionWillBegin];
-[SBDosidoSwitcherModifier handleSwipeToKillEvent:];
-[SBDosidoSwitcherModifier initWithTransitionID:fromAppLayout:toAppLayout:direction:];
-[SBDosidoSwitcherModifier setShouldSuppressScaleAnimation:];
-[SBDosidoSwitcherModifier shouldSuppressScaleAnimation];
```
