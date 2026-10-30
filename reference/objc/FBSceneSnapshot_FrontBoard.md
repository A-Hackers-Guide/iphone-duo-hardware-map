# `FBSceneSnapshot`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 7 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"FBScene" _scene;
@"<FBSceneSnapshotInternalConfiguration>" _config;
@"FBSceneSnapshotContext" _context;
@"_FBSSnapshot" _snapshot;
```

## Properties

```
@property (T@"FBScene",R,N,V_scene) scene;
@property (T@"<FBSceneSnapshotConfiguration>",R,C,N,V_config) configuration;
@property (T@"FBSceneSnapshotContext",R,C,N,V_context) context;
@property (TB,R,N) hasProtectedContent;
@property (T@"IOSurface",R,N) IOSurface;
@property (T@"IOSurface",R,N) fallbackIOSurface;
@property (T^{CGImage=},R,N) CGImage;
```

## Instance methods

```
-[FBSceneSnapshot CGImage];
-[FBSceneSnapshot hasProtectedContent];
-[FBSceneSnapshot configuration];
-[FBSceneSnapshot scene];
-[FBSceneSnapshot context];
-[FBSceneSnapshot IOSurface];
-[FBSceneSnapshot fallbackIOSurface];
-[FBSceneSnapshot capture];
-[FBSceneSnapshot initWithScene:context:];
```
