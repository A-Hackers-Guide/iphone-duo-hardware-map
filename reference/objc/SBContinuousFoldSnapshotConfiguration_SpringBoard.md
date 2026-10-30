# `SBContinuousFoldSnapshotConfiguration`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _snapshotOpaque;
B _fadesSnapshotOutOnCancellation;
@"UIWindow" _snapshotSourceWindow;
@"UIWindow" _cloakingTargetWindow;
@"NSArray" _snapshotUnderlayWindows;
```

## Properties

```
@property (T@"UIWindow",W,N,V_snapshotSourceWindow) snapshotSourceWindow;
@property (T@"UIWindow",W,N,V_cloakingTargetWindow) cloakingTargetWindow;
@property (TB,N,GisSnapshotOpaque,V_snapshotOpaque) snapshotOpaque;
@property (T@"NSArray",C,N,V_snapshotUnderlayWindows) snapshotUnderlayWindows;
@property (TB,N,V_fadesSnapshotOutOnCancellation) fadesSnapshotOutOnCancellation;
```

## Instance methods

```
-[SBContinuousFoldSnapshotConfiguration cloakingTargetWindow];
-[SBContinuousFoldSnapshotConfiguration fadesSnapshotOutOnCancellation];
-[SBContinuousFoldSnapshotConfiguration isSnapshotOpaque];
-[SBContinuousFoldSnapshotConfiguration setCloakingTargetWindow:];
-[SBContinuousFoldSnapshotConfiguration setFadesSnapshotOutOnCancellation:];
-[SBContinuousFoldSnapshotConfiguration setSnapshotOpaque:];
-[SBContinuousFoldSnapshotConfiguration setSnapshotSourceWindow:];
-[SBContinuousFoldSnapshotConfiguration setSnapshotUnderlayWindows:];
-[SBContinuousFoldSnapshotConfiguration snapshotSourceWindow];
-[SBContinuousFoldSnapshotConfiguration snapshotUnderlayWindows];
```
