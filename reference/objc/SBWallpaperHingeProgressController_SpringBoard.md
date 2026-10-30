# `SBWallpaperHingeProgressController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBBacklightControllerObserver`, `FBSDisplayLayoutPublisherObserving`
- 7 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"SBWallpaperController" _wallpaperController;
@"SBBacklightController" _backlightController;
@"<FBSDisplayLayoutPublishing>" _displayLayoutPublisher;
B _backlightOn;
B _lockScreenIsTopElement;
B _homeScreenWallpaperVisible;
B _enabled;
```

## Properties

```
@property (TB,N,GisHomeScreenWallpaperVisible,V_homeScreenWallpaperVisible) homeScreenWallpaperVisible;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBWallpaperHingeProgressController backlightController:didTransitionToBacklightState:source:];
-[SBWallpaperHingeProgressController dealloc];
-[SBWallpaperHingeProgressController publisher:didUpdateLayout:withTransition:];
-[SBWallpaperHingeProgressController _updateEnabledState];
-[SBWallpaperHingeProgressController _isLockScreenTopElementInLayout:];
-[SBWallpaperHingeProgressController _wallpaperSceneIdentifier];
-[SBWallpaperHingeProgressController initWithWallpaperController:backlightController:displayLayoutPublisher:];
-[SBWallpaperHingeProgressController isHomeScreenWallpaperVisible];
-[SBWallpaperHingeProgressController setHomeScreenWallpaperVisible:];
```
