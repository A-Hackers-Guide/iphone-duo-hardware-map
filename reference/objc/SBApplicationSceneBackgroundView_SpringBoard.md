# `SBApplicationSceneBackgroundView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `SBApplicationSceneBackgroundView`
- 7 instance variables, 9 properties, 14 instance methods, 0 class methods

## Instance variables

```
q _wallpaperStyle;
@"SBWallpaperEffectView" _backgroundWallpaperEffectView;
B _needsClassicModeBackground;
@"<PBUIWallpaperPresenting><PBUIWallpaperLegibilityProviding>" _wallpaperPresenter;
B _fullscreen;
B _shouldUseBrightMaterial;
Q _transformOptions;
```

## Properties

```
@property (TB,?,N,GisFullscreen,V_fullscreen) fullscreen;
@property (Tq,?,N,V_wallpaperStyle) wallpaperStyle;
@property (TB,?,N,V_needsClassicModeBackground) needsClassicModeBackground;
@property (TB,?,N,V_shouldUseBrightMaterial) shouldUseBrightMaterial;
@property (TQ,?,N,V_transformOptions) transformOptions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBApplicationSceneBackgroundView transformOptions];
-[SBApplicationSceneBackgroundView setFullscreen:];
-[SBApplicationSceneBackgroundView setTransformOptions:];
-[SBApplicationSceneBackgroundView shouldUseBrightMaterial];
-[SBApplicationSceneBackgroundView isFullscreen];
-[SBApplicationSceneBackgroundView wallpaperStyle];
-[SBApplicationSceneBackgroundView setNeedsClassicModeBackground:];
-[SBApplicationSceneBackgroundView description];
-[SBApplicationSceneBackgroundView setShouldUseBrightMaterial:];
-[SBApplicationSceneBackgroundView needsClassicModeBackground];
-[SBApplicationSceneBackgroundView setWallpaperStyle:withAnimationSettings:];
-[SBApplicationSceneBackgroundView setWallpaperStyle:];
-[SBApplicationSceneBackgroundView initWithFrame:wallpaperPresenter:];
-[SBApplicationSceneBackgroundView _setupBackground];
```
