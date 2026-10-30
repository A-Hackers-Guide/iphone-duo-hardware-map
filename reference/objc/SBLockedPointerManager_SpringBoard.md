# `SBLockedPointerManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSceneManagerObserver`, `SBLayoutStateTransitionObserver`, `SBDeviceApplicationSceneHandleObserver`, `BSInvalidatable`
- 12 instance variables, 4 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"PSPointerClientController" _pointerClientController;
@"UIApplicationSceneSettingsDiffInspector" _sceneSettingsInspector;
@"NSObject<OS_dispatch_queue>" _stateSerialQueue;
@"NSMutableDictionary" _queue_preferredLockStatusBySceneIdentifier;
@"NSString" _queue_sceneIdentifierThatHasLockedPointer;
@"NSMutableSet" _queue_sceneIdentifiersThatSuppressPreferredLockStatus;
@"<BSInvalidatable>" _queue_backboardLockedPointerAssertion;
@"<BSInvalidatable>" _queue_pointerHiddenAssertion;
@"SBWindowScene" _windowScene;
B _queue_isInvalidated;
@"<SBSceneStore>" _sceneStore;
@"SBSceneManager" _sceneManager;
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
-[SBLockedPointerManager sceneHandle:didDestroyScene:];
-[SBLockedPointerManager layoutStateTransitionCoordinator:transitionDidBeginWithTransitionContext:];
-[SBLockedPointerManager sceneManager:didAddExternalForegroundApplicationSceneHandle:];
-[SBLockedPointerManager _notInvalidated_updateLockForLayoutState:];
-[SBLockedPointerManager _queue_unlockPointer];
-[SBLockedPointerManager _queue_updateLockForLayoutState:];
-[SBLockedPointerManager _shouldAllowPointerLockedForScene:];
-[SBLockedPointerManager sceneManager:didRemoveExternalForegroundApplicationSceneHandle:];
-[SBLockedPointerManager sceneHandle:didUpdateSettingsWithDiff:previousSettings:];
-[SBLockedPointerManager invalidate];
-[SBLockedPointerManager layoutStateTransitionCoordinator:transitionDidEndWithTransitionContext:];
-[SBLockedPointerManager clientWithSceneIdentifier:suppressPreferredLockStatus:];
-[SBLockedPointerManager _setPointerLockStatus:forSceneWithIdentifier:];
-[SBLockedPointerManager _possibleSceneHandleForLockingPointerFromLayoutState:];
-[SBLockedPointerManager clientWithSceneIdentifier:prefersPointerLockStatus:];
-[SBLockedPointerManager _queue_lockPointerForSceneIdentifier:];
-[SBLockedPointerManager _queue_prefersLockForSceneIdentifier:];
-[SBLockedPointerManager initWithSceneStore:sceneManager:windowScene:];
```
