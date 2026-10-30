# `_UINavigationBarBridgingPalette`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UINavigationBarPalette`
- Protocols: `_UINavigationPalette`
- 1 instance variables, 14 properties, 36 instance methods, 0 class methods

## Instance variables

```
@"UIView" _temporaryBackgroundView;
```

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
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UINavigationBarBridgingPalette _updateBackgroundView];
-[_UINavigationBarBridgingPalette _backgroundView];
-[_UINavigationBarBridgingPalette _setBackgroundView:];
-[_UINavigationBarBridgingPalette setSize:];
-[_UINavigationBarBridgingPalette _setupBackgroundViewIfNecessary];
-[_UINavigationBarBridgingPalette paletteIsHidden];
-[_UINavigationBarBridgingPalette _setPaletteOverridesPinningBar:];
-[_UINavigationBarBridgingPalette isVisibleWhenPinningBarIsHidden];
-[_UINavigationBarBridgingPalette _attachedPinningTopBar];
-[_UINavigationBarBridgingPalette _configureConstraintsForBackground:];
-[_UINavigationBarBridgingPalette _configurePaletteConstraintsForBoundary];
-[_UINavigationBarBridgingPalette _disableConstraints];
-[_UINavigationBarBridgingPalette _enableConstraints];
-[_UINavigationBarBridgingPalette _paletteOverridesPinningBar];
-[_UINavigationBarBridgingPalette _resetConstraintConstants:];
-[_UINavigationBarBridgingPalette _resetHeightConstraintConstant];
-[_UINavigationBarBridgingPalette _setAttached:didComplete:];
-[_UINavigationBarBridgingPalette _setLeftConstraintConstant:];
-[_UINavigationBarBridgingPalette _setSize:];
-[_UINavigationBarBridgingPalette _setTopConstraintConstant:];
-[_UINavigationBarBridgingPalette _shouldUpdateBackground];
-[_UINavigationBarBridgingPalette _updateBackgroundConstraintsIfNecessary];
-[_UINavigationBarBridgingPalette boundaryEdge];
-[_UINavigationBarBridgingPalette isAttached];
-[_UINavigationBarBridgingPalette navController];
-[_UINavigationBarBridgingPalette paletteShadowIsHidden];
-[_UINavigationBarBridgingPalette pinningBarShadowIsHidden];
-[_UINavigationBarBridgingPalette pinningBarShadowWasHidden];
-[_UINavigationBarBridgingPalette preferredContentInsets];
-[_UINavigationBarBridgingPalette resetBackgroundConstraints];
-[_UINavigationBarBridgingPalette setFrame:isAnimating:];
-[_UINavigationBarBridgingPalette setPaletteShadowIsHidden:];
-[_UINavigationBarBridgingPalette setPinningBarShadowIsHidden:];
-[_UINavigationBarBridgingPalette setPinningBarShadowWasHidden:];
-[_UINavigationBarBridgingPalette setPreferredContentInsets:];
-[_UINavigationBarBridgingPalette setVisibleWhenPinningBarIsHidden:];
```
