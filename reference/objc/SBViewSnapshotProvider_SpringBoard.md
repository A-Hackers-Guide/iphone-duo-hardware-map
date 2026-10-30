# `SBViewSnapshotProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"UIView" _view;
q _orientation;
B _includeWindowSceneWallpaper;
@? _completionBlock;
d _delay;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (T@?,C,N,V_completionBlock) completionBlock;
@property (Td,N,V_delay) delay;
@property (TB,N,V_includeWindowSceneWallpaper) includeWindowSceneWallpaper;
```

## Instance methods

```
-[SBViewSnapshotProvider setCompletionBlock:];
-[SBViewSnapshotProvider completionBlock];
-[SBViewSnapshotProvider snapshot];
-[SBViewSnapshotProvider delay];
-[SBViewSnapshotProvider setDelay:];
-[SBViewSnapshotProvider windowScene];
-[SBViewSnapshotProvider setIncludeWindowSceneWallpaper:];
-[SBViewSnapshotProvider _createSnapshotOfWallpaperAndWindow:];
-[SBViewSnapshotProvider includeWindowSceneWallpaper];
-[SBViewSnapshotProvider initWithWindowScene:view:orientation:];
-[SBViewSnapshotProvider snapshotAsynchronously:withImageBlock:];
-[SBViewSnapshotProvider snapshotWithImageBlock:];
```
