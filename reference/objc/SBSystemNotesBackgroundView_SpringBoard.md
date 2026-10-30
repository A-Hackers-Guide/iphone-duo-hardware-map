# `SBSystemNotesBackgroundView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `PTSettingsKeyObserver`, `SBApplicationSceneBackgroundView`
- 3 instance variables, 9 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"UIView" _tintView;
@"UIVisualEffectView" _backgroundEffectView;
@"SBSystemNotesAppearanceSettings" _appearanceSettings;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,?,N,GisFullscreen) fullscreen;
@property (Tq,?,N) wallpaperStyle;
@property (TB,?,N) needsClassicModeBackground;
@property (TB,?,N) shouldUseBrightMaterial;
@property (TQ,?,N) transformOptions;
```

## Instance methods

```
-[SBSystemNotesBackgroundView dealloc];
-[SBSystemNotesBackgroundView settings:changedValueForKey:];
-[SBSystemNotesBackgroundView initWithFrame:];
-[SBSystemNotesBackgroundView _updateTintView];
-[SBSystemNotesBackgroundView _backgroundColorFromSettings:];
```
