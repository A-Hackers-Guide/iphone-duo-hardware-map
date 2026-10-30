# `SBDashBoardLegibilityProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PBUIWallpaperObserver`, `CSLegibilityProviding`
- 2 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"<CSLegibilityProviderDelegate>" _legibilityProviderDelegate;
@"SBWallpaperController" _wallpaperController;
```

## Properties

```
@property (T@"SBWallpaperController",&,N,V_wallpaperController) wallpaperController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<CSLegibilityProviderDelegate>",W,N,V_legibilityProviderDelegate) legibilityProviderDelegate;
```

## Instance methods

```
-[SBDashBoardLegibilityProvider wallpaperDidChangeForVariant:];
-[SBDashBoardLegibilityProvider wallpaperController];
-[SBDashBoardLegibilityProvider _wallpaperLegibilitySettings];
-[SBDashBoardLegibilityProvider initWithWallpaperController:];
-[SBDashBoardLegibilityProvider setLegibilityProviderDelegate:];
-[SBDashBoardLegibilityProvider currentLegibilitySettings];
-[SBDashBoardLegibilityProvider setWallpaperController:];
-[SBDashBoardLegibilityProvider wallpaperLegibilitySettingsDidChange:forVariant:];
-[SBDashBoardLegibilityProvider _notifyDelegate];
-[SBDashBoardLegibilityProvider legibilityProviderDelegate];
```
