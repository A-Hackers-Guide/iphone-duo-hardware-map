# `SBExtendedDisplayController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBBacklightCoordinatorObserver`, `SBMousePointerHardwareConnectionObserver`, `SBHIDKeyboardMonitoring`, `SBWindowSceneAttachmentObserving`
- 9 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"SBExternalDisplayDefaults" _externalDisplayDefaults;
@"SBAppSwitcherDefaults" _appSwitcherDefaults;
@"NSMutableSet" _defaultsObservers;
B _isEmbeddedBacklightOn;
@"<BSInvalidatable>" _keyboardMonitor;
@"BSContinuousMachTimer" _hardwareConnectionWindow;
@"SBExternalDisplayEducationSession" _educationSession;
@"SBBacklightCoordinator" _backlightCoordinator;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (T@"SBWindowScene",W,N,V_windowScene) windowScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBExtendedDisplayController setWindowScene:];
-[SBExtendedDisplayController windowSceneDidDisconnect:];
-[SBExtendedDisplayController mousePointerManager:hardwarePointingDeviceAttachedDidChange:];
-[SBExtendedDisplayController backlightCoordinator:didUpdateAggregateBacklightState:fromSource:];
-[SBExtendedDisplayController windowSceneDidConnect:];
-[SBExtendedDisplayController windowScene];
-[SBExtendedDisplayController backlightCoordinator:willUpdateAggregateBacklightState:fromSource:];
-[SBExtendedDisplayController _areAllRequiredHardwareAvailable];
-[SBExtendedDisplayController _hardwareAvailabilityChanged];
-[SBExtendedDisplayController _reevaluateMirroringEnablement];
-[SBExtendedDisplayController _setupDisplayArrangementObserver];
-[SBExtendedDisplayController _setupMirroringEnabledObserver];
-[SBExtendedDisplayController _shouldIgnoreEmbeddedBacklightChangingSource:];
-[SBExtendedDisplayController _updateDisplayPreferences];
-[SBExtendedDisplayController connectedKeyboardSetDidChange:];
-[SBExtendedDisplayController initWithBacklightCoordinator:];
```
