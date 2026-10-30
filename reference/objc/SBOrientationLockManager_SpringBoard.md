# `SBOrientationLockManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 24 instance methods, 1 class methods

## Instance variables

```
q _canonicalUserLockedDeviceOrientation;
q _previousCanonicalUserLockedDeviceOrientation;
^{__CFRunLoopObserver=} _runLoopObserver;
B _landscapeOverrideEnabled;
```

## Properties

```
@property (TB,R,N,GisLandscapeOverrideEnabled,V_landscapeOverrideEnabled) landscapeOverrideEnabled;
```

## Class methods

```
+[SBOrientationLockManager sharedInstance];
```

## Instance methods

```
-[SBOrientationLockManager isEffectivelyLocked];
-[SBOrientationLockManager succinctDescriptionBuilder];
-[SBOrientationLockManager init];
-[SBOrientationLockManager lock:];
-[SBOrientationLockManager dealloc];
-[SBOrientationLockManager descriptionWithMultilinePrefix:];
-[SBOrientationLockManager succinctDescription];
-[SBOrientationLockManager description];
-[SBOrientationLockManager lock];
-[SBOrientationLockManager unlock];
-[SBOrientationLockManager descriptionBuilderWithMultilinePrefix:];
-[SBOrientationLockManager _handler_runLoopObserverDispose];
-[SBOrientationLockManager _persistedUserLockOrientation];
-[SBOrientationLockManager _setupRunLoopObserverIfNecessaryForOrientation:andInitialLockState:];
-[SBOrientationLockManager _updateLockStateWithChanges:];
-[SBOrientationLockManager _updateLockStateWithOrientation:forceUpdateHID:changes:];
-[SBOrientationLockManager effectiveLockedOrientation];
-[SBOrientationLockManager isLandscapeOverrideEnabled];
-[SBOrientationLockManager isUserLocked];
-[SBOrientationLockManager restoreLandscapeOverrideFromDefaults];
-[SBOrientationLockManager restoreStateFromPrefs];
-[SBOrientationLockManager userLockOrientation];
-[SBOrientationLockManager userLockedDeviceOrientationForWindowScene:];
-[SBOrientationLockManager userLockedInterfaceOrientationForWindowScene:];
```
