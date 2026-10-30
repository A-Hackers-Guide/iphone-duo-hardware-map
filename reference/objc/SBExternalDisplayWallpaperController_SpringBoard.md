# `SBExternalDisplayWallpaperController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFZStackParticipantDelegate`, `BSInvalidatable`
- 4 instance variables, 8 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"SBFWindow" _window;
@"SBFZStackParticipant" _zStackParticipant;
@"SBWindowScene" _windowScene;
@"PRSWallpaperObserver" _wallpaperObserver;
```

## Properties

```
@property (T@"SBFWindow",&,N,V_window) window;
@property (T@"SBFZStackParticipant",&,N,V_zStackParticipant) zStackParticipant;
@property (T@"SBWindowScene",W,N,V_windowScene) windowScene;
@property (T@"PRSWallpaperObserver",&,N,V_wallpaperObserver) wallpaperObserver;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBExternalDisplayWallpaperController zStackParticipant];
-[SBExternalDisplayWallpaperController setZStackParticipant:];
-[SBExternalDisplayWallpaperController setWindowScene:];
-[SBExternalDisplayWallpaperController zStackParticipant:updatePreferences:];
-[SBExternalDisplayWallpaperController dealloc];
-[SBExternalDisplayWallpaperController window];
-[SBExternalDisplayWallpaperController zStackParticipantDidChange:];
-[SBExternalDisplayWallpaperController zStackParticipant:updateZOrderPreferences:];
-[SBExternalDisplayWallpaperController invalidate];
-[SBExternalDisplayWallpaperController windowScene];
-[SBExternalDisplayWallpaperController setWindow:];
-[SBExternalDisplayWallpaperController _teardown];
-[SBExternalDisplayWallpaperController initWithWindowScene:requiresTraitsParticipant:];
-[SBExternalDisplayWallpaperController setWallpaperObserver:];
-[SBExternalDisplayWallpaperController wallpaperObserver];
```
