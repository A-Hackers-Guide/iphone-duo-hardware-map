# `SBNCScreenController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CMPocketStateDelegate`, `SBIdleTimerResetSource`, `SBWindowSceneAttachmentObserving`
- 7 instance variables, 11 properties, 31 instance methods, 0 class methods

## Instance variables

```
B _turnOnScreenForOutOfPocketEvent;
I _powerAssertionID;
@"SBBacklightCoordinator" _backlightCoordinator;
@"SBLockScreenCoordinator" _lockScreenCoordinator;
@"NSHashTable" _windowScenes;
@"CMPocketStateManager" _pocketStateManager;
@"NSString" _powerAssertionName;
```

## Properties

```
@property (T@"SBBacklightCoordinator",&,N,V_backlightCoordinator) backlightCoordinator;
@property (T@"SBLockScreenCoordinator",&,N,V_lockScreenCoordinator) lockScreenCoordinator;
@property (T@"NSHashTable",&,N,V_windowScenes) windowScenes;
@property (T@"CMPocketStateManager",&,N,V_pocketStateManager) pocketStateManager;
@property (TB,N,V_turnOnScreenForOutOfPocketEvent) turnOnScreenForOutOfPocketEvent;
@property (T@"NSString",C,N,V_powerAssertionName) powerAssertionName;
@property (TI,N,V_powerAssertionID) powerAssertionID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBNCScreenController init];
-[SBNCScreenController windowSceneDidDisconnect:];
-[SBNCScreenController setWindowScenes:];
-[SBNCScreenController windowScenes];
-[SBNCScreenController setBacklightCoordinator:];
-[SBNCScreenController pocketStateManager:didUpdateState:];
-[SBNCScreenController _isDeviceUILocked];
-[SBNCScreenController _releasePowerAssertion];
-[SBNCScreenController resetAutomaticLockStateForNotificationRequest:];
-[SBNCScreenController windowSceneDidConnect:];
-[SBNCScreenController backlightCoordinator];
-[SBNCScreenController lockScreenCoordinator];
-[SBNCScreenController setLockScreenCoordinator:];
-[SBNCScreenController powerAssertionID];
-[SBNCScreenController pocketStateManager];
-[SBNCScreenController setPocketStateManager:];
-[SBNCScreenController canTurnOnScreenForNotificationRequest:];
-[SBNCScreenController turnOnScreenForOutOfPocketEvent];
-[SBNCScreenController _cancelTurnOnScreenForOutOfPocketEvents];
-[SBNCScreenController _createOrResetPowerAssertionWithTimeout:];
-[SBNCScreenController _turnOnScreen];
-[SBNCScreenController _turnOnScreenForOutOfPocketEventBeforeTimeInterval:];
-[SBNCScreenController _turnOnScreenForOutOfPocketEventIfNecessary];
-[SBNCScreenController _turnOnScreenForPocketMode];
-[SBNCScreenController initWithBacklightCoordinator:lockScreenCoordinator:];
-[SBNCScreenController powerAssertionName];
-[SBNCScreenController setPowerAssertionID:];
-[SBNCScreenController setPowerAssertionName:];
-[SBNCScreenController setTurnOnScreenForOutOfPocketEvent:];
-[SBNCScreenController turnOnScreenForNotificationRequest:];
-[SBNCScreenController turnOnScreenIfPossibleForNotificationRequest:];
```
