# `SBDashBoardWallpaperProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CSWallpaperProviding`
- 1 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"SBWallpaperController" _wallpaperController;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDashBoardWallpaperProvider takeInSwitcherAssertionWithReason:];
-[SBDashBoardWallpaperProvider preferredSalientContentRectangle];
-[SBDashBoardWallpaperProvider adaptiveTimeHonorsPreferredSalientContentRectangle];
-[SBDashBoardWallpaperProvider updateSalientContentRectangle:];
-[SBDashBoardWallpaperProvider suspendWallpaperAnimationForReason:];
-[SBDashBoardWallpaperProvider initWithWallpaperController:];
-[SBDashBoardWallpaperProvider createWallpaperFloatingViewForReason:ignoreReplica:];
-[SBDashBoardWallpaperProvider setWallpaperFloatingLayerContainerView:forReason:withAnimationFactory:];
-[SBDashBoardWallpaperProvider createCoverSheetWallpaperView];
-[SBDashBoardWallpaperProvider createCoverSheetWallpaperViewWithTransformOptions:];
-[SBDashBoardWallpaperProvider wallpaperClientDidRotateFromInterfaceOrientation:];
-[SBDashBoardWallpaperProvider wallpaperClientWillAnimateRotationToInterfaceOrientation:duration:];
-[SBDashBoardWallpaperProvider wallpaperClientWillRotateToInterfaceOrientation:duration:];
```
