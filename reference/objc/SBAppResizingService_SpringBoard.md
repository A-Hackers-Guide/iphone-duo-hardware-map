# `SBAppResizingService`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionListenerDelegate`, `SBSAppResizingServiceServerInterface`, `SBAppResizingCoordinatorObserver`, `SBLockStateObserving`, `SBUIActiveOrientationObserver`, `SBRemoteAppResizingSessionDelegate`
- 8 instance variables, 5 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"SBAppResizingCoordinator" _coordinator;
@"SBSSKDisplayProfileManager" _displayProfileManager;
@"SBWindowSceneManager" _windowSceneManager;
@"BSServiceConnectionListener" _listener;
@"NSMutableSet" _connections;
@"NSMutableSet" _allRemoteSessions;
@"SBRemoteAppResizingSession" _currentRemoteSession;
q _unavailabilityReasons;
```

## Properties

```
@property (Tq,N,S_setUnavailabilityReasons:,V_unavailabilityReasons) unavailabilityReasons;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAppResizingService activeInterfaceOrientationDidChangeToOrientation:willAnimateWithDuration:fromOrientation:];
-[SBAppResizingService listener:didReceiveConnection:withContext:];
-[SBAppResizingService windowSceneDidDisconnect:];
-[SBAppResizingService unavailabilityReasons];
-[SBAppResizingService activeInterfaceOrientationWillChangeToOrientation:];
-[SBAppResizingService lockStateProvider:didUpdateIsUILocked:];
-[SBAppResizingService windowSceneDidConnect:];
-[SBAppResizingService acquireAssertionForDisplay:preferredSize:resizingCornerRadius:];
-[SBAppResizingService clientEndedResizing];
-[SBAppResizingService updatePreferredSize:forAssertionWithIdentifier:];
-[SBAppResizingService _isAnySceneLocked];
-[SBAppResizingService _sendResizingStatusToConnection:];
-[SBAppResizingService _setUnavailabilityReasons:];
-[SBAppResizingService _startObservingLockEvents:];
-[SBAppResizingService currentRemoteSession];
-[SBAppResizingService initWithCoordinator:displayProfileManager:windowSceneManager:startupInterfaceOrientation:];
-[SBAppResizingService remoteAppResizingSessionDidInvalidate:];
-[SBAppResizingService resizingCoordinator:didUpdateActiveSession:];
-[SBAppResizingService resizingCoordinator:didUpdateResizingPossible:preferredSize:];
```
