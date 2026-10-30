# `SBAppSwitcherSnapshotCacheEntry`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _fromFullSizeSnapshotRequest;
B _needsUpdate;
@"SBAppLayout" _appLayout;
@"SBDisplayItem" _displayItem;
@"XBApplicationSnapshot" _snapshot;
@"UIImage" _snapshotImage;
```

## Properties

```
@property (T@"SBAppLayout",&,N,V_appLayout) appLayout;
@property (T@"SBDisplayItem",&,N,V_displayItem) displayItem;
@property (T@"XBApplicationSnapshot",&,N,V_snapshot) snapshot;
@property (T@"UIImage",&,N,V_snapshotImage) snapshotImage;
@property (Tq,R,N) role;
@property (TB,N,V_fromFullSizeSnapshotRequest) fromFullSizeSnapshotRequest;
@property (TB,N,V_needsUpdate) needsUpdate;
```

## Instance methods

```
-[SBAppSwitcherSnapshotCacheEntry snapshotImage];
-[SBAppSwitcherSnapshotCacheEntry needsUpdate];
-[SBAppSwitcherSnapshotCacheEntry setSnapshot:];
-[SBAppSwitcherSnapshotCacheEntry snapshot];
-[SBAppSwitcherSnapshotCacheEntry setAppLayout:];
-[SBAppSwitcherSnapshotCacheEntry appLayout];
-[SBAppSwitcherSnapshotCacheEntry displayItem];
-[SBAppSwitcherSnapshotCacheEntry setDisplayItem:];
-[SBAppSwitcherSnapshotCacheEntry role];
-[SBAppSwitcherSnapshotCacheEntry description];
-[SBAppSwitcherSnapshotCacheEntry setNeedsUpdate:];
-[SBAppSwitcherSnapshotCacheEntry setFromFullSizeSnapshotRequest:];
-[SBAppSwitcherSnapshotCacheEntry _matchesAppLayout:displayItem:];
-[SBAppSwitcherSnapshotCacheEntry fromFullSizeSnapshotRequest];
-[SBAppSwitcherSnapshotCacheEntry setSnapshotImage:];
```
