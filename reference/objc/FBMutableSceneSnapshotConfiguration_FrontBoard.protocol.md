# `FBMutableSceneSnapshotConfiguration` (protocol)

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `FBSceneSnapshotConfiguration`
- 0 instance variables, 5 properties, 10 instance methods, 0 class methods

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) frame;
@property (TB,N,GisOpaque) opaque;
@property (T@"NSSet",C,N) layersToExclude;
@property (T@"FBSceneLayer",C,N) backgroundLayer;
@property (TB,N,GisAlternateLayout) alternateLayout;
```

## Instance methods

```
-[FBMutableSceneSnapshotConfiguration backgroundLayer];
-[FBMutableSceneSnapshotConfiguration setOpaque:];
-[FBMutableSceneSnapshotConfiguration isOpaque];
-[FBMutableSceneSnapshotConfiguration setAlternateLayout:];
-[FBMutableSceneSnapshotConfiguration setFrame:];
-[FBMutableSceneSnapshotConfiguration setBackgroundLayer:];
-[FBMutableSceneSnapshotConfiguration layersToExclude];
-[FBMutableSceneSnapshotConfiguration setLayersToExclude:];
-[FBMutableSceneSnapshotConfiguration frame];
-[FBMutableSceneSnapshotConfiguration isAlternateLayout];
```
