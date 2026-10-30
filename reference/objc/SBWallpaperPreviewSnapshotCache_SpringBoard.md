# `SBWallpaperPreviewSnapshotCache`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFolderObserver`, `PBUIWallpaperObserver`
- 6 instance variables, 4 properties, 20 instance methods, 2 class methods

## Instance variables

```
@"SBWallpaperController" _wallpaperController;
@"BSUIMappedImageCache" _imageCache;
q _invalidatedLocations;
@"SBIconController" _iconController;
@"SBBacklightController" _backlightController;
@"SBIconModel" _model;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBWallpaperPreviewSnapshotCache cacheKeyForVariant:options:];
+[SBWallpaperPreviewSnapshotCache cacheKeyForVariant:options:scalingWidth:];
```

## Instance methods

```
-[SBWallpaperPreviewSnapshotCache wallpaperDidChangeForVariant:];
-[SBWallpaperPreviewSnapshotCache folder:didMoveIcon:];
-[SBWallpaperPreviewSnapshotCache init];
-[SBWallpaperPreviewSnapshotCache dealloc];
-[SBWallpaperPreviewSnapshotCache folder:didAddIcons:removedIcons:];
-[SBWallpaperPreviewSnapshotCache folder:didReplaceIcon:withIcon:];
-[SBWallpaperPreviewSnapshotCache _modelDidLayout];
-[SBWallpaperPreviewSnapshotCache _backlightFadeFinished];
-[SBWallpaperPreviewSnapshotCache _homeScreenSnapshotProviderWithOptions:wallpaperImage:];
-[SBWallpaperPreviewSnapshotCache _iconControllerDidChangeIconModel:];
-[SBWallpaperPreviewSnapshotCache _lockScreenSnapshotProviderWithOptions:wallpaperImage:];
-[SBWallpaperPreviewSnapshotCache _modelWillLayout];
-[SBWallpaperPreviewSnapshotCache _orientationForOptions:];
-[SBWallpaperPreviewSnapshotCache _switchToIconModel:];
-[SBWallpaperPreviewSnapshotCache initWithImageCache:iconController:wallpaperController:backlightController:];
-[SBWallpaperPreviewSnapshotCache invalidateSnapshotsForLocations:];
-[SBWallpaperPreviewSnapshotCache mappedWallpaperPreviewForKey:];
-[SBWallpaperPreviewSnapshotCache mappedWallpaperPreviewForScaledSnapshot:variant:cacheKey:];
-[SBWallpaperPreviewSnapshotCache regenerateSnapshotsForLocations:];
-[SBWallpaperPreviewSnapshotCache snapshotProviderForVariant:options:wallpaperImage:];
```
