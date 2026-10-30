# `SBWindowSceneOrientationLockManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 5 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"SBWindowScene" _windowScene;
q _lockedDeviceOrientation;
@"<BSInvalidatable>" _stateCaptureHandle;
```

## Properties

```
@property (T@"SBWindowScene",R,W,N) windowScene;
@property (TB,R,N,GisUserLocked) userLocked;
@property (Tq,R,N) lockedDeviceOrientation;
@property (Tq,R,N) lockedInterfaceOrientation;
@property (TB,R,N,GisLandscapeOverrideEnabled) landscapeOverrideEnabled;
```

## Instance methods

```
-[SBWindowSceneOrientationLockManager lock:];
-[SBWindowSceneOrientationLockManager dealloc];
-[SBWindowSceneOrientationLockManager initWithWindowScene:];
-[SBWindowSceneOrientationLockManager description];
-[SBWindowSceneOrientationLockManager lock];
-[SBWindowSceneOrientationLockManager windowScene];
-[SBWindowSceneOrientationLockManager _surfaceType];
-[SBWindowSceneOrientationLockManager unlock];
-[SBWindowSceneOrientationLockManager _sharedManager];
-[SBWindowSceneOrientationLockManager _applyPersistedLockState];
-[SBWindowSceneOrientationLockManager _isPerDisplayLockEnabled];
-[SBWindowSceneOrientationLockManager _persistLockedOrientation];
-[SBWindowSceneOrientationLockManager _persistLockedOrientation:forSurfaceType:];
-[SBWindowSceneOrientationLockManager isLandscapeOverrideEnabled];
-[SBWindowSceneOrientationLockManager isUserLocked];
-[SBWindowSceneOrientationLockManager lockedDeviceOrientation];
-[SBWindowSceneOrientationLockManager lockedInterfaceOrientation];
```
