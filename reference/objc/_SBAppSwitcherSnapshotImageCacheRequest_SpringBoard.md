# `_SBAppSwitcherSnapshotImageCacheRequest`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 5 instance variables, 9 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _loadFullSizeSnapshot;
Q _sequenceID;
@"SBAppLayout" _appLayout;
@"SBDisplayItem" _displayItem;
@"XBApplicationSnapshot" _snapshot;
```

## Properties

```
@property (TQ,R,N,V_sequenceID) sequenceID;
@property (TB,N,V_loadFullSizeSnapshot) loadFullSizeSnapshot;
@property (T@"SBAppLayout",&,N,V_appLayout) appLayout;
@property (T@"SBDisplayItem",&,N,V_displayItem) displayItem;
@property (T@"XBApplicationSnapshot",&,N,V_snapshot) snapshot;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_SBAppSwitcherSnapshotImageCacheRequest setSnapshot:];
-[_SBAppSwitcherSnapshotImageCacheRequest succinctDescriptionBuilder];
-[_SBAppSwitcherSnapshotImageCacheRequest snapshot];
-[_SBAppSwitcherSnapshotImageCacheRequest setAppLayout:];
-[_SBAppSwitcherSnapshotImageCacheRequest appLayout];
-[_SBAppSwitcherSnapshotImageCacheRequest descriptionWithMultilinePrefix:];
-[_SBAppSwitcherSnapshotImageCacheRequest succinctDescription];
-[_SBAppSwitcherSnapshotImageCacheRequest displayItem];
-[_SBAppSwitcherSnapshotImageCacheRequest setDisplayItem:];
-[_SBAppSwitcherSnapshotImageCacheRequest description];
-[_SBAppSwitcherSnapshotImageCacheRequest sequenceID];
-[_SBAppSwitcherSnapshotImageCacheRequest descriptionBuilderWithMultilinePrefix:];
-[_SBAppSwitcherSnapshotImageCacheRequest initWithSequenceID:];
-[_SBAppSwitcherSnapshotImageCacheRequest loadFullSizeSnapshot];
-[_SBAppSwitcherSnapshotImageCacheRequest setLoadFullSizeSnapshot:];
```
