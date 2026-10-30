# `_UINavigationPalette` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 10 properties, 23 instance methods, 0 class methods

## Properties

```
@property (T@"UIView",&,N,S_setBackgroundView:) _backgroundView;
@property (TB,N,S_setPaletteOverridesPinningBar:) _paletteOverridesPinningBar;
@property (T@"UINavigationController",R,N) navController;
@property (TQ,R,N) boundaryEdge;
@property (TB,N,GisPinned) pinned;
@property (TB,N) pinningBarShadowWasHidden;
@property (TB,N) pinningBarShadowIsHidden;
@property (TB,N) paletteShadowIsHidden;
@property (TB,N,GisVisibleWhenPinningBarIsHidden) visibleWhenPinningBarIsHidden;
@property (T{UIEdgeInsets=dddd},N) preferredContentInsets;
```

## Instance methods

```
-[_UINavigationPalette setPinned:];
-[_UINavigationPalette isPinned];
-[_UINavigationPalette _backgroundView];
-[_UINavigationPalette _setBackgroundView:];
-[_UINavigationPalette paletteIsHidden];
-[_UINavigationPalette _setPaletteOverridesPinningBar:];
-[_UINavigationPalette isVisibleWhenPinningBarIsHidden];
-[_UINavigationPalette _paletteOverridesPinningBar];
-[_UINavigationPalette _setLeftConstraintConstant:];
-[_UINavigationPalette _setTopConstraintConstant:];
-[_UINavigationPalette boundaryEdge];
-[_UINavigationPalette isAttached];
-[_UINavigationPalette navController];
-[_UINavigationPalette paletteShadowIsHidden];
-[_UINavigationPalette pinningBarShadowIsHidden];
-[_UINavigationPalette pinningBarShadowWasHidden];
-[_UINavigationPalette preferredContentInsets];
-[_UINavigationPalette setFrame:isAnimating:];
-[_UINavigationPalette setPaletteShadowIsHidden:];
-[_UINavigationPalette setPinningBarShadowIsHidden:];
-[_UINavigationPalette setPinningBarShadowWasHidden:];
-[_UINavigationPalette setPreferredContentInsets:];
-[_UINavigationPalette setVisibleWhenPinningBarIsHidden:];
```
