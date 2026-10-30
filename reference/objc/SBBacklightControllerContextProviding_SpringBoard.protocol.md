# `SBBacklightControllerContextProviding` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 12 properties, 12 instance methods, 0 class methods

## Properties

```
@property (T@"CADisplay",R,N) CADisplay;
@property (T@"SBLockScreenManager",R,N) lockScreenManager;
@property (T@"SBIdleTimerDefaults",R,N) idleTimerDefaults;
@property (T@"<BLSHBacklightHostObservable><BLSBacklightChangeRequestable>",R,N) blsBacklight;
@property (T@"<BLSBacklightStateObservable><BLSBacklightChangeRequestable>",R,N) blsConcreteBacklight;
@property (T@"SBScreenSleepCoordinator",R,N) screenSleepCoordinator;
@property (T@"SBScreenWakeAnimationController",R,N) screenWakeAnimationController;
@property (T@"SBWakeLogger",R,N) wakeLogger;
@property (T@"SBHIDUISensorModeController",R,N) HIDUISensorModeController;
@property (T@"SBProximitySensorManager",R,N) proximitySensorManager;
@property (T@"SBBacklightCoordinator",R,N) backlightCoordinator;
@property (T@"SBWindowScene",R,W,N) windowScene;
```

## Instance methods

```
-[SBBacklightControllerContextProviding wakeLogger];
-[SBBacklightControllerContextProviding lockScreenManager];
-[SBBacklightControllerContextProviding blsBacklight];
-[SBBacklightControllerContextProviding idleTimerDefaults];
-[SBBacklightControllerContextProviding screenWakeAnimationController];
-[SBBacklightControllerContextProviding proximitySensorManager];
-[SBBacklightControllerContextProviding windowScene];
-[SBBacklightControllerContextProviding backlightCoordinator];
-[SBBacklightControllerContextProviding HIDUISensorModeController];
-[SBBacklightControllerContextProviding CADisplay];
-[SBBacklightControllerContextProviding blsConcreteBacklight];
-[SBBacklightControllerContextProviding screenSleepCoordinator];
```
