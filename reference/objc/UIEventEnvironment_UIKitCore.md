# `UIEventEnvironment`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 24 instance variables, 2 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"UIApplication" _application;
@"NSMutableArray" _eventQueue;
@"UIEvent" _event;
@"UIMotionEvent" _motionEvent;
@"UIRemoteControlEvent" _remoteControlEvent;
@"NSMutableDictionary" _dragEventsByContextAndSessionIDPair;
B _isSystemApplication;
@"NSMutableSet" _windowsWithActiveTouchMaps;
B _hasSeenAnyPencilEvents;
@"UIPressesEvent" _fallbackPressesEvent;
@"UIPhysicalKeyboardEvent" _fallbackPhysicalKeyboardEvent;
@"UIWheelEvent" _fallbackWheelEvent;
Q _sceneDidDisconnectInternalNotificationToken;
Q _sceneWillConnectInternalNotificationToken;
@"NSMapTable" _eventRegistryByScene;
@"NSHashTable" _invalidatedAndDisconnectedScenes;
@"NSMapTable" _pressesMapByScene;
@"NSMapTable" _currentNudgePressTypeByScene;
@"NSMutableDictionary" _fallbackPressMap;
@"NSMapTable" _currentTouchByScene;
^{__CFDictionary=} _touchMapsByWindow;
q _disableTouchCoalescingCount;
@"NSMutableDictionary" _estimatedTouchRecordsByContextIDAndEstimationIndex;
@"NSMutableArray" _estimatedTouchRecordsInIncomingOrder;
```

## Properties

```
@property (T@"UIApplication",N,V_application) application;
@property (T@"NSMutableArray",&,N,V_eventQueue) eventQueue;
```

## Instance methods

```
-[UIEventEnvironment eventQueue];
-[UIEventEnvironment setEventQueue:];
-[UIEventEnvironment initWithApplication:];
-[UIEventEnvironment pointerLockStateDidChange:];
-[UIEventEnvironment sceneDidDisconnect:];
-[UIEventEnvironment application];
-[UIEventEnvironment sceneDidActivate:];
-[UIEventEnvironment setApplication:];
-[UIEventEnvironment dealloc];
-[UIEventEnvironment sceneWillConnect:];
```
