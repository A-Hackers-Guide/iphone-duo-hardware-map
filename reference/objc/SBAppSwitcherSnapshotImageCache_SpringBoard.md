# `SBAppSwitcherSnapshotImageCache`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBUIActiveOrientationObserver`
- 17 instance variables, 9 properties, 55 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _snapshotQueue;
@"NSObject<OS_dispatch_queue>" _controlQueue;
@"NSMutableDictionary" _cachedSnapshots;
@"NSMutableDictionary" _cacheEntryUpdateObservers;
@"NSMutableDictionary" _snapshotRequestsCurrentlyBeingLoaded;
Q _snapshotRequestSequenceID;
q _lastKnownInterfaceOrientation;
q _lastKnownUserInterfaceStyle;
@"SBAppSwitcherSettings" _settings;
@"<BSInvalidatable>" _stateCaptureInvalidatable;
B _shouldPurgeNilEntries;
@"SBApplicationController" _applicationController;
B _reloadsSnapshotsForActiveInterfaceOrientationChange;
@"NSArray" _queue_cachableAppLayouts;
@"NSArray" _queue_fullSizeCachableAppLayouts;
@"<SBAppSwitcherSnapshotImageCacheDelegate>" _delegate;
@"NSString" _debugName;
```

## Properties

```
@property (T@"<SBAppSwitcherSnapshotImageCacheDelegate>",W,N,V_delegate) delegate;
@property (T@"NSArray",C,N,V_queue_cachableAppLayouts) cachableAppLayouts;
@property (T@"NSArray",C,N,V_queue_fullSizeCachableAppLayouts) fullSizeCachableAppLayouts;
@property (TB,N,V_reloadsSnapshotsForActiveInterfaceOrientationChange) reloadsSnapshotsForActiveInterfaceOrientationChange;
@property (T@"NSString",C,N,V_debugName) debugName;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAppSwitcherSnapshotImageCache activeInterfaceOrientationDidChangeToOrientation:willAnimateWithDuration:fromOrientation:];
-[SBAppSwitcherSnapshotImageCache setCachableAppLayouts:];
-[SBAppSwitcherSnapshotImageCache reloadsSnapshotsForActiveInterfaceOrientationChange];
-[SBAppSwitcherSnapshotImageCache _purgeAllSnapshots];
-[SBAppSwitcherSnapshotImageCache reloadSnapshotForDisplayItem:];
-[SBAppSwitcherSnapshotImageCache _setSnapshotNeedsUpdateForDisplayItem:];
-[SBAppSwitcherSnapshotImageCache _isValidSnapshotRequest:];
-[SBAppSwitcherSnapshotImageCache setReloadsSnapshotsForActiveInterfaceOrientationChange:];
-[SBAppSwitcherSnapshotImageCache _purgeLowPriorityFullSizeSnapshots];
-[SBAppSwitcherSnapshotImageCache init];
-[SBAppSwitcherSnapshotImageCache _purgeSnapshotRequestsForDisplayItem:withReason:];
-[SBAppSwitcherSnapshotImageCache _createDownscaledVariantForRequestIfNeeded:snapshot:displayItem:sceneHandle:application:];
-[SBAppSwitcherSnapshotImageCache _addObserver:forDisplayItem:inAppLayout:];
-[SBAppSwitcherSnapshotImageCache _purgeSnapshotRequest:withReason:];
-[SBAppSwitcherSnapshotImageCache _updateCacheForDisplayItem:];
-[SBAppSwitcherSnapshotImageCache _cachableAppLayoutsRequiringFullSizeSnapshots];
-[SBAppSwitcherSnapshotImageCache setDebugName:];
-[SBAppSwitcherSnapshotImageCache _setShouldPurgeNilEntry:];
-[SBAppSwitcherSnapshotImageCache dealloc];
-[SBAppSwitcherSnapshotImageCache fullSizeCachableAppLayouts];
-[SBAppSwitcherSnapshotImageCache _addCacheEntryForImage:fromRequest:];
-[SBAppSwitcherSnapshotImageCache removeSnapshotObserver:];
-[SBAppSwitcherSnapshotImageCache _updateCache];
-[SBAppSwitcherSnapshotImageCache _loadSnapshotForRequest:withDisplayItem:inAppLayout:];
-[SBAppSwitcherSnapshotImageCache addSnapshotUpdateObserver:forDisplayItem:inAppLayout:];
-[SBAppSwitcherSnapshotImageCache _cachableAppLayoutsForTesting];
-[SBAppSwitcherSnapshotImageCache _purgeAllSnapshotRequests];
-[SBAppSwitcherSnapshotImageCache activeInterfaceOrientationWillChangeToOrientation:];
-[SBAppSwitcherSnapshotImageCache _purgeSnapshotsForKey:];
-[SBAppSwitcherSnapshotImageCache _appLayoutsInPriorityOrder];
-[SBAppSwitcherSnapshotImageCache _isValidAppLayout:withSnapshot:givenCachableAppLayouts:];
-[SBAppSwitcherSnapshotImageCache _purgeLowPriorityFullSizeSnapshotRequests];
-[SBAppSwitcherSnapshotImageCache _enqueueSnapshotRequestsForCachableAppLayouts:forFullSizeSnapshots:];
-[SBAppSwitcherSnapshotImageCache setDelegate:];
-[SBAppSwitcherSnapshotImageCache _updateActiveOrientationObservingIfNeeded];
-[SBAppSwitcherSnapshotImageCache _asynchronouslyLoadSnapshotFromRequest:];
-[SBAppSwitcherSnapshotImageCache initWithDelegate:applicationController:];
-[SBAppSwitcherSnapshotImageCache _purgeLowPrioritySnapshots];
-[SBAppSwitcherSnapshotImageCache _orientationForAppLayout:];
-[SBAppSwitcherSnapshotImageCache cachableAppLayouts];
-[SBAppSwitcherSnapshotImageCache debugName];
-[SBAppSwitcherSnapshotImageCache _initWithDelegate:applicationController:settings:];
-[SBAppSwitcherSnapshotImageCache delegate];
-[SBAppSwitcherSnapshotImageCache _snapshotChanged:];
-[SBAppSwitcherSnapshotImageCache _updateObserversForDisplayItem:inAppLayout:withCacheEntry:];
-[SBAppSwitcherSnapshotImageCache _cacheSnapshotForRequest:withDisplayItem:inAppLayout:];
-[SBAppSwitcherSnapshotImageCache description];
-[SBAppSwitcherSnapshotImageCache _createSnapshotRequestWithDisplayItem:inAppLayout:forFullSizeSnapshot:];
-[SBAppSwitcherSnapshotImageCache setFullSizeCachableAppLayouts:];
-[SBAppSwitcherSnapshotImageCache _purgeLowPrioritySnapshotRequests];
-[SBAppSwitcherSnapshotImageCache _representedApplicationSceneEntityForDisplayItem:];
-[SBAppSwitcherSnapshotImageCache reloadSnapshotsForInterfaceStyleChange:];
-[SBAppSwitcherSnapshotImageCache _enqueueNextSnapshotRequestIfNecessary];
-[SBAppSwitcherSnapshotImageCache _keepGoingForRequest:];
-[SBAppSwitcherSnapshotImageCache _snapshotImage:finishedLoadingForRequest:];
```
