# `_UINavigationControllerPalette`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UINavigationPalette`
- 15 instance variables, 22 properties, 61 instance methods, 0 class methods

## Instance variables

```
@"_UIBarBackground" _backgroundView;
@"_UIBarBackgroundLayoutLegacy" _backgroundViewLayout;
d _backgroundUnderlapHeight;
{?="isAttached"b1"attachmentIsChanging"b1"restartPaletteTransitionIfNecessary"b1"pinned"b1"pinningBarShadowIsHidden"b1"paletteShadowIsHidden"b1"pinningBarShadowWasHidden"b1} _paletteFlags;
B __paletteOverridesPinningBar;
B _visibleWhenPinningBarIsHidden;
B __palettePinningBarHidden;
Q _boundaryEdge;
@"UINavigationController" _navController;
@"UIViewController" __unpinnedController;
@ __pinningBar;
@"NSArray" __constraints;
@"NSArray" __backgroundConstraints;
{CGSize="width"d"height"d} __size;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _preferredContentInsets;
```

## Properties

```
@property (T@"UIViewController",N,V__unpinnedController) _unpinnedController;
@property (T@,N,S_setPinningBar:,V__pinningBar) _pinningBar;
@property (TB,R,N,G_attachmentIsChanging) _attachmentIsChanging;
@property (TB,N,S_setRestartPaletteTransitionIfNecessary:) _restartPaletteTransitionIfNecessary;
@property (T@"NSArray",&,N,S_setConstraints:,V__constraints) _constraints;
@property (T{CGSize=dd},N,S_setSize:,V__size) _size;
@property (T@"NSArray",&,N,S_setBackgroundConstraints:,V__backgroundConstraints) _backgroundConstraints;
@property (TB,N,G_isPalettePinningBarHidden,S_setPalettePinningBarHidden:,V__palettePinningBarHidden) _palettePinningBarHidden;
@property (T@"UIView",&,N,S_setBackgroundView:) _backgroundView;
@property (TB,N,S_setPaletteOverridesPinningBar:,V__paletteOverridesPinningBar) _paletteOverridesPinningBar;
@property (T@"UINavigationController",R,N,V_navController) navController;
@property (TQ,R,N,V_boundaryEdge) boundaryEdge;
@property (TB,N,GisPinned) pinned;
@property (TB,N) pinningBarShadowWasHidden;
@property (TB,N) pinningBarShadowIsHidden;
@property (TB,N) paletteShadowIsHidden;
@property (TB,N,GisVisibleWhenPinningBarIsHidden,V_visibleWhenPinningBarIsHidden) visibleWhenPinningBarIsHidden;
@property (T{UIEdgeInsets=dddd},N,V_preferredContentInsets) preferredContentInsets;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UINavigationControllerPalette setPinned:];
-[_UINavigationControllerPalette _setConstraints:];
-[_UINavigationControllerPalette isPinned];
-[_UINavigationControllerPalette _constraints];
-[_UINavigationControllerPalette dealloc];
-[_UINavigationControllerPalette _updateBackgroundView];
-[_UINavigationControllerPalette _backgroundView];
-[_UINavigationControllerPalette _setBackgroundView:];
-[_UINavigationControllerPalette setFrame:];
-[_UINavigationControllerPalette didMoveToSuperview];
-[_UINavigationControllerPalette _setPinningBar:];
-[_UINavigationControllerPalette _setupBackgroundViewIfNecessary];
-[_UINavigationControllerPalette paletteIsHidden];
-[_UINavigationControllerPalette _setPaletteOverridesPinningBar:];
-[_UINavigationControllerPalette isVisibleWhenPinningBarIsHidden];
-[_UINavigationControllerPalette _attachedPinningTopBar];
-[_UINavigationControllerPalette _attachmentIsChanging];
-[_UINavigationControllerPalette _backgroundConstraints];
-[_UINavigationControllerPalette _backgroundViewLayout];
-[_UINavigationControllerPalette _configureConstraintsForBackground:];
-[_UINavigationControllerPalette _configurePaletteConstraintsForBoundary];
-[_UINavigationControllerPalette _disableConstraints];
-[_UINavigationControllerPalette _enableConstraints];
-[_UINavigationControllerPalette _initWithNavigationController:forEdge:];
-[_UINavigationControllerPalette _isPalettePinningBarHidden];
-[_UINavigationControllerPalette _paletteOverridesPinningBar];
-[_UINavigationControllerPalette _pinningBar];
-[_UINavigationControllerPalette _propagateBackgroundToContents];
-[_UINavigationControllerPalette _resetConstraintConstants:];
-[_UINavigationControllerPalette _resetHeightConstraintConstant];
-[_UINavigationControllerPalette _restartPaletteTransitionIfNecessary];
-[_UINavigationControllerPalette _setAttached:didComplete:];
-[_UINavigationControllerPalette _setAttachmentIsChanging:];
-[_UINavigationControllerPalette _setBackgroundConstraints:];
-[_UINavigationControllerPalette _setLeftConstraintConstant:];
-[_UINavigationControllerPalette _setPalettePinningBarHidden:];
-[_UINavigationControllerPalette _setRestartPaletteTransitionIfNecessary:];
-[_UINavigationControllerPalette _setSize:];
-[_UINavigationControllerPalette _setTopConstraintConstant:];
-[_UINavigationControllerPalette _setVisualAltitude:];
-[_UINavigationControllerPalette _setVisualAltitudeBias:];
-[_UINavigationControllerPalette _shouldUpdateBackground];
-[_UINavigationControllerPalette _size];
-[_UINavigationControllerPalette _supportsSpecialSearchBarTransitions];
-[_UINavigationControllerPalette _unpinnedController];
-[_UINavigationControllerPalette _updateBackgroundConstraintsIfNecessary];
-[_UINavigationControllerPalette _updateLayoutForCurrentConfiguration];
-[_UINavigationControllerPalette boundaryEdge];
-[_UINavigationControllerPalette isAttached];
-[_UINavigationControllerPalette navController];
-[_UINavigationControllerPalette paletteShadowIsHidden];
-[_UINavigationControllerPalette pinningBarShadowIsHidden];
-[_UINavigationControllerPalette pinningBarShadowWasHidden];
-[_UINavigationControllerPalette preferredContentInsets];
-[_UINavigationControllerPalette setFrame:isAnimating:];
-[_UINavigationControllerPalette setPaletteShadowIsHidden:];
-[_UINavigationControllerPalette setPinningBarShadowIsHidden:];
-[_UINavigationControllerPalette setPinningBarShadowWasHidden:];
-[_UINavigationControllerPalette setPreferredContentInsets:];
-[_UINavigationControllerPalette setVisibleWhenPinningBarIsHidden:];
-[_UINavigationControllerPalette set_unpinnedController:];
```
