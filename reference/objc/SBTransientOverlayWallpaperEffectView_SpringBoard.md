# `SBTransientOverlayWallpaperEffectView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 4 instance variables, 2 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"SBWallpaperEffectView" _wallpaperEffectView;
@"_UIDirectionalRotationView" _wallpaperRotationView;
@"<PBUIWallpaperPresenting><PBUIWallpaperLegibilityProviding>" _wallpaperPresenter;
q _containerOrientation;
```

## Properties

```
@property (Tq,N,V_containerOrientation) containerOrientation;
@property (Tq,N) wallpaperStyle;
```

## Instance methods

```
-[SBTransientOverlayWallpaperEffectView containerOrientation];
-[SBTransientOverlayWallpaperEffectView setContainerOrientation:];
-[SBTransientOverlayWallpaperEffectView wallpaperStyle];
-[SBTransientOverlayWallpaperEffectView layoutSubviews];
-[SBTransientOverlayWallpaperEffectView setTransitionState:];
-[SBTransientOverlayWallpaperEffectView setWallpaperStyle:];
-[SBTransientOverlayWallpaperEffectView prepareToAnimateToTransitionState:];
-[SBTransientOverlayWallpaperEffectView _currentWallpaperTransform];
-[SBTransientOverlayWallpaperEffectView _updateWallpaperGeometry];
-[SBTransientOverlayWallpaperEffectView initWithFrame:wallpaperVariant:wallpaperPresenter:];
```
