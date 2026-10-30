# `FBSceneSnapshotConfiguration` (protocol)

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 11 properties, 11 instance methods, 0 class methods

## Properties

```
@property (T@"FBSSceneSettings",R,C,N) settings;
@property (Td,R,N) scale;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) frame;
@property (TB,R,N,GisOpaque) opaque;
@property (Tq,R,N) orientation;
@property (T@"NSSet",R,C,N) layersToExclude;
@property (T@"FBSceneLayer",R,C,N) backgroundLayer;
@property (TB,R,N,GisAlternateLayout) alternateLayout;
@property (TB,R,N) clientAllowsProtectedContent;
@property (T@"NSDate",R,N) expirationDate;
@property (T@,R,N) userInfo;
```

## Instance methods

```
-[FBSceneSnapshotConfiguration expirationDate];
-[FBSceneSnapshotConfiguration settings];
-[FBSceneSnapshotConfiguration backgroundLayer];
-[FBSceneSnapshotConfiguration orientation];
-[FBSceneSnapshotConfiguration userInfo];
-[FBSceneSnapshotConfiguration isOpaque];
-[FBSceneSnapshotConfiguration scale];
-[FBSceneSnapshotConfiguration layersToExclude];
-[FBSceneSnapshotConfiguration frame];
-[FBSceneSnapshotConfiguration clientAllowsProtectedContent];
-[FBSceneSnapshotConfiguration isAlternateLayout];
```
