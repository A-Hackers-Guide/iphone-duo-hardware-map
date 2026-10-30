# `SBOrientationLockService`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionListenerDelegate`, `SBSOrientationLockServiceServerInterface`
- 4 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"SBWindowSceneManager" _windowSceneManager;
@"BSServiceConnectionListener" _listener;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSMutableSet" _lock_connections;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBOrientationLockService listener:didReceiveConnection:withContext:];
-[SBOrientationLockService isOrientationLockedForTargets:completion:];
-[SBOrientationLockService lockOrientationForTargets:completion:];
-[SBOrientationLockService lockedOrientationForTargets:completion:];
-[SBOrientationLockService supportedOrientationLockTargetsWithCompletion:];
-[SBOrientationLockService unlockOrientationForTargets:completion:];
-[SBOrientationLockService _windowSceneForSurfaceType:];
-[SBOrientationLockService _windowScenesForTargetMask:];
-[SBOrientationLockService initWithWindowSceneManager:];
```
