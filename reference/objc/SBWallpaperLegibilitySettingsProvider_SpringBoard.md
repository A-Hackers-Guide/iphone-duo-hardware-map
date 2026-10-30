# `SBWallpaperLegibilitySettingsProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PBUIWallpaperObserver`, `SBFLegibilitySettingsProvider`
- 3 instance variables, 6 properties, 7 instance methods, 0 class methods

## Instance variables

```
q _variant;
@"SBWallpaperController" _wallpaperController;
@"<SBFLegibilitySettingsProviderDelegate>" _delegate;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"_UILegibilitySettings",R,N) legibilitySettings;
@property (T@"<SBFLegibilitySettingsProviderDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[SBWallpaperLegibilitySettingsProvider wallpaperDidChangeForVariant:];
-[SBWallpaperLegibilitySettingsProvider dealloc];
-[SBWallpaperLegibilitySettingsProvider setDelegate:];
-[SBWallpaperLegibilitySettingsProvider delegate];
-[SBWallpaperLegibilitySettingsProvider legibilitySettings];
-[SBWallpaperLegibilitySettingsProvider wallpaperLegibilitySettingsDidChange:forVariant:];
-[SBWallpaperLegibilitySettingsProvider initWithVariant:wallpaperController:];
```
