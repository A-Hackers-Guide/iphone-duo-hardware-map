# `SBContinuousFoldResizeMorphCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _transitions;
@"NSHashTable" _surfaces;
```

## Instance methods

```
-[SBContinuousFoldResizeMorphCoordinator init];
-[SBContinuousFoldResizeMorphCoordinator dealloc];
-[SBContinuousFoldResizeMorphCoordinator invalidate];
-[SBContinuousFoldResizeMorphCoordinator _sceneResizeLayoutDidFinish:];
-[SBContinuousFoldResizeMorphCoordinator _advanceSideIfReady:transition:];
-[SBContinuousFoldResizeMorphCoordinator _advanceReadySidesForTransition:];
-[SBContinuousFoldResizeMorphCoordinator _buildAndInstallOverlayForSide:transition:];
-[SBContinuousFoldResizeMorphCoordinator _checkTeardownForTransition:];
-[SBContinuousFoldResizeMorphCoordinator _markSideSnapshotReady:transition:generation:overlay:];
-[SBContinuousFoldResizeMorphCoordinator _noteRelayoutDoneForSceneIdentifier:];
-[SBContinuousFoldResizeMorphCoordinator _rebuildInstalledSidesForTransition:];
-[SBContinuousFoldResizeMorphCoordinator _sceneDidUpdateForMoveToNewDisplay:];
-[SBContinuousFoldResizeMorphCoordinator _setState:forTransition:];
-[SBContinuousFoldResizeMorphCoordinator _startFadeForSide:transition:];
-[SBContinuousFoldResizeMorphCoordinator _teardownTransition:];
-[SBContinuousFoldResizeMorphCoordinator beginTransitionForAppLayout:outgoingContentView:bundleIdentifier:sceneIdentifier:];
-[SBContinuousFoldResizeMorphCoordinator foldTransitionDidEndForAppLayout:];
-[SBContinuousFoldResizeMorphCoordinator registerSide:installInView:underlyingContentView:frame:anchorEdge:forAppLayout:];
-[SBContinuousFoldResizeMorphCoordinator registerSurface:];
-[SBContinuousFoldResizeMorphCoordinator unregisterSurface:];
```
