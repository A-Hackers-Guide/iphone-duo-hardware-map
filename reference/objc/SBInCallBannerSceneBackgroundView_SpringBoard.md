# `SBInCallBannerSceneBackgroundView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `SBApplicationSceneBackgroundView`
- 8 instance variables, 10 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"_UIBackdropView" _backdropView;
Q _transformOptions;
@"SBWallpaperEffectView" _wallpaperEffectView;
q _wallpaperVariant;
@"<PBUIWallpaperPresenting><PBUIWallpaperLegibilityProviding>" _wallpaperPresenter;
B _fullscreen;
d _wallpaperAlpha;
q _wallpaperStyle;
```

## Properties

```
@property (Td,N,V_wallpaperAlpha) wallpaperAlpha;
@property (Tq,N,V_wallpaperStyle) wallpaperStyle;
@property (TB,?,N,GisFullscreen,V_fullscreen) fullscreen;
@property (TB,?,N) needsClassicModeBackground;
@property (TB,?,N) shouldUseBrightMaterial;
@property (TQ,?,N) transformOptions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBInCallBannerSceneBackgroundView setFullscreen:];
-[SBInCallBannerSceneBackgroundView isFullscreen];
-[SBInCallBannerSceneBackgroundView wallpaperStyle];
-[SBInCallBannerSceneBackgroundView layoutSubviews];
-[SBInCallBannerSceneBackgroundView setWallpaperStyle:];
-[SBInCallBannerSceneBackgroundView initWithFrame:wallpaperPresenter:];
-[SBInCallBannerSceneBackgroundView _updateBackdropView];
-[SBInCallBannerSceneBackgroundView initWithFrame:wallpaperVariant:transformOptions:wallpaperPresenter:];
-[SBInCallBannerSceneBackgroundView setWallpaperAlpha:];
-[SBInCallBannerSceneBackgroundView wallpaperAlpha];
```
