# `SBSceneSnapshotDataProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `XBSnapshotDataProvider`
- 7 instance variables, 5 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"FBSceneSnapshot" _snapshot;
@"XBSnapshotDataProviderContext" _context;
d _scaleFactor;
@"UIImage" _cachedImage;
@"SBFallbackSnapshotDataProvider" _fallbackSnapshotDataProvider;
@"IOSurface" _processedSurface;
B _hasProtectedContent;
```

## Properties

```
@property (T@"XBSnapshotDataProviderContext",R,&,N,V_context) context;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSceneSnapshotDataProvider hasProtectedContent];
-[SBSceneSnapshotDataProvider context];
-[SBSceneSnapshotDataProvider invalidateImage];
-[SBSceneSnapshotDataProvider IOSurfaceForFormat:];
-[SBSceneSnapshotDataProvider _invalidateSnapshotData];
-[SBSceneSnapshotDataProvider fallbackSnapshotDataProvider];
-[SBSceneSnapshotDataProvider fetchImageForFormat:];
-[SBSceneSnapshotDataProvider initWithSceneSnapshot:scaleFactor:];
```
