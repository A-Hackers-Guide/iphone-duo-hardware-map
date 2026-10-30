# `SBReachabilityBackgroundView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `SBHomeGrabberDelegate`
- 13 instance variables, 9 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"UIView" _wallpaperContainerView;
@"_SBAdaptiveColorMatrixView" _colorMatrixView;
@"UIViewFloatAnimatableProperty" _colorMatrixOpacityAnimatableProperty;
@"UIView" _topWallpaperView;
@"UIView" _bottomWallpaperView;
@"UIView" _hitTestBlockerView;
q _wallpaperVariant;
@"<PBUIWallpaperPresenting><PBUIWallpaperLegibilityProviding>" _wallpaperPresenter;
@"SBHomeGrabberView" _homeGrabberView;
@"CAShapeLayer" _chevronLayer;
@"UIViewFloatAnimatableProperty" _chevronShapeAnimatableProperty;
d _containerViewYOffset;
d _homeGrabberAdditionalOffset;
```

## Properties

```
@property (Tq,N,V_wallpaperVariant) wallpaperVariant;
@property (Td,N,V_containerViewYOffset) containerViewYOffset;
@property (Td,N,V_homeGrabberAdditionalOffset) homeGrabberAdditionalOffset;
@property (Td,N) homeGrabberAlpha;
@property (Td,N) chevronAlpha;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBReachabilityBackgroundView setChevronAlpha:];
-[SBReachabilityBackgroundView layoutSubviews];
-[SBReachabilityBackgroundView setWallpaperVariant:];
-[SBReachabilityBackgroundView shouldAllowThinStyleForHomeGrabberView:];
-[SBReachabilityBackgroundView additionalEdgeSpacingForHomeGrabberView:];
-[SBReachabilityBackgroundView chevronAlpha];
-[SBReachabilityBackgroundView _setupHomeGrabberView];
-[SBReachabilityBackgroundView wallpaperVariant];
-[SBReachabilityBackgroundView shouldAllowAutoHideForHomeGrabberView:];
-[SBReachabilityBackgroundView _displayCornerRadius];
-[SBReachabilityBackgroundView setHomeGrabberAdditionalOffset:];
-[SBReachabilityBackgroundView _invertColorsChanged:];
-[SBReachabilityBackgroundView _invertColorsIsEnabled];
-[SBReachabilityBackgroundView _newWallpaperViewForVariant:];
-[SBReachabilityBackgroundView _setupChevron];
-[SBReachabilityBackgroundView _setupColorInvertObservation];
-[SBReachabilityBackgroundView _setupCornerContentsImageForWallpaperView:];
-[SBReachabilityBackgroundView _setupHitTestBlockerView];
-[SBReachabilityBackgroundView _updateChevronPathForUpFraction:];
-[SBReachabilityBackgroundView _updateColorMatrixAlpha:];
-[SBReachabilityBackgroundView _updateColorMatrixFilters];
-[SBReachabilityBackgroundView _updateWallpaperViewAnimated:];
-[SBReachabilityBackgroundView _updateWallpaperViewFilters];
-[SBReachabilityBackgroundView containerViewYOffset];
-[SBReachabilityBackgroundView homeGrabberAdditionalOffset];
-[SBReachabilityBackgroundView homeGrabberAlpha];
-[SBReachabilityBackgroundView initWithFrame:wallpaperVariant:wallpaperPresenter:];
-[SBReachabilityBackgroundView setContainerViewYOffset:];
-[SBReachabilityBackgroundView setHomeGrabberAlpha:];
```
