# `SBWallpaperIconStyleCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PBUIWallpaperObserver`
- 9 instance variables, 10 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"PBUIHomeVariantStyleState" _posterStyleState;
@"<BSInvalidatable>" _stateCapturer;
@"NSHashTable" _observers;
@"PBUIHomeVariantStyleState" _lastNotifiedPosterStyleState;
@"PUIStylePickerHomeScreenConfiguration" _lastNotifiedStyleConfiguration;
@"UIColor" _caseAccentColor;
@"PUIStylePickerHomeScreenConfiguration" _currentStyleConfiguration;
@"SBWallpaperControllerCoordinator" _wallpaperControllerCoordinator;
@"SBHomeScreenDefaults" _homeScreenDefaults;
```

## Properties

```
@property (T@"SBWallpaperControllerCoordinator",R,N,V_wallpaperControllerCoordinator) wallpaperControllerCoordinator;
@property (T@"SBHomeScreenDefaults",R,N,V_homeScreenDefaults) homeScreenDefaults;
@property (TB,D,N,GisWallpaperDimmed) wallpaperDimmed;
@property (TB,N) shouldUseLargeHomeScreenIcons;
@property (T@"PUIStylePickerHomeScreenConfiguration",&,N,V_currentStyleConfiguration) currentStyleConfiguration;
@property (T@"BSColor",&,D,N) currentTintColor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBWallpaperIconStyleCoordinator wallpaperDidChangeForVariant:];
-[SBWallpaperIconStyleCoordinator homeScreenDefaults];
-[SBWallpaperIconStyleCoordinator _postersStyleStateDidChange];
-[SBWallpaperIconStyleCoordinator removeIconStyleObserver:];
-[SBWallpaperIconStyleCoordinator isWallpaperDimmed];
-[SBWallpaperIconStyleCoordinator addIconStyleObserver:];
-[SBWallpaperIconStyleCoordinator fetchWallpaperProminentColor:];
-[SBWallpaperIconStyleCoordinator initWithWallpaperControllerCoordinator:homeScreenDefaults:];
-[SBWallpaperIconStyleCoordinator setCurrentTintColor:];
-[SBWallpaperIconStyleCoordinator dealloc];
-[SBWallpaperIconStyleCoordinator _setupObservers];
-[SBWallpaperIconStyleCoordinator _fetchPosterStyleState];
-[SBWallpaperIconStyleCoordinator _issueUpdates:];
-[SBWallpaperIconStyleCoordinator _resetStateExpectingUpdates];
-[SBWallpaperIconStyleCoordinator shouldUseLargeHomeScreenIcons];
-[SBWallpaperIconStyleCoordinator setWallpaperDimmed:];
-[SBWallpaperIconStyleCoordinator _notifyObserversOfUpdatedPostersStyleState];
-[SBWallpaperIconStyleCoordinator _fetchStyleConfiguration];
-[SBWallpaperIconStyleCoordinator currentStyleConfiguration];
-[SBWallpaperIconStyleCoordinator posterStyleState];
-[SBWallpaperIconStyleCoordinator _setupStateCapture];
-[SBWallpaperIconStyleCoordinator setCurrentStyleConfiguration:];
-[SBWallpaperIconStyleCoordinator currentTintColor];
-[SBWallpaperIconStyleCoordinator _emitPowerLogForStyleUpdateWithConfiguration:styleState:oldConfiguration:];
-[SBWallpaperIconStyleCoordinator _currentWallpaperController];
-[SBWallpaperIconStyleCoordinator setShouldUseLargeHomeScreenIcons:];
-[SBWallpaperIconStyleCoordinator _enclosureAccentColor];
-[SBWallpaperIconStyleCoordinator wallpaperWillChangeForVariant:];
-[SBWallpaperIconStyleCoordinator wallpaperControllerCoordinator];
```
