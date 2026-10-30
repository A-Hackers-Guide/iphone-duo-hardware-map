# `SBMousePointerManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKSMousePointerDeviceObserver`, `PSPointerSystemClientControllerDelegate`, `SBMultiDisplayUserInteractionCoordinatorActiveWindowSceneObserver`
- 13 instance variables, 5 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"PSPointerClientController" _pointerClientController;
@"BKSMousePointerService" _mousePointerService;
Q _connectedPointingDevicesCount;
@"PSPointerSystemClientController" _systemClientController;
@"NSHashTable" _observers;
@"<BSInvalidatable>" _mousePointerDeviceObserverToken;
@"<BSInvalidatable>" _serviceKeepAliveAssertion;
@"<BSInvalidatable>" _suppressEventsAssertion;
@"NSMapTable" _springBoardScenesToPointerAssertions;
@"NSMutableDictionary" _sceneToWindowMap;
@"NSMutableDictionary" _sceneToPresenterMap;
B _didAddActiveDisplayObserver;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _rootWindowTransformForEmbeddedDisplay;
```

## Properties

```
@property (T{CGAffineTransform=dddddd},N,V_rootWindowTransformForEmbeddedDisplay) rootWindowTransformForEmbeddedDisplay;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBMousePointerManager removeObserver:];
-[SBMousePointerManager init];
-[SBMousePointerManager dealloc];
-[SBMousePointerManager addObserver:];
-[SBMousePointerManager multiDisplayUserInteractionCoordinator:updatedActiveWindowScene:reason:];
-[SBMousePointerManager _dismissScene:];
-[SBMousePointerManager mousePointerDevicesDidChange:];
-[SBMousePointerManager _handleAssistiveTouchEnabledDidChangeNotification];
-[SBMousePointerManager _notifyObserversPointingDeviceBecameAvailable:];
-[SBMousePointerManager _presentScene:];
-[SBMousePointerManager _setPointerUIDWithConnectedDeviceCount:];
-[SBMousePointerManager _updatePointerAssertionsAndScenes];
-[SBMousePointerManager _updateScenesForPointerWithHardwareAttached:];
-[SBMousePointerManager isHardwarePointingDeviceAttached];
-[SBMousePointerManager pointerClientController:didAddScene:];
-[SBMousePointerManager pointerClientController:sceneDidActivate:];
-[SBMousePointerManager pointerClientController:sceneWillDeactivate:];
-[SBMousePointerManager pointerClientController:willRemoveScene:];
-[SBMousePointerManager requestPointerActivationForScene:];
-[SBMousePointerManager rootWindowTransformForEmbeddedDisplay];
-[SBMousePointerManager setRootWindowTransformForEmbeddedDisplay:];
-[SBMousePointerManager setSystemPointerInteractionContextID:displayWithHardwareIdentifier:];
-[SBMousePointerManager shouldAllowHardwarePointingDevices];
```
