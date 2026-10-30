# `SBBacklightControllerDefaultContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBBacklightControllerContextProviding`
- 4 instance variables, 16 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"CADisplay" _caDisplay;
@"<BLSHBacklightHostObservable><BLSBacklightChangeRequestable>" _blsBacklight;
@"BLSBacklight" _blsConcreteBacklight;
@"SBWindowScene" _windowScene;
```

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
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBBacklightControllerDefaultContext wakeLogger];
-[SBBacklightControllerDefaultContext lockScreenManager];
-[SBBacklightControllerDefaultContext blsBacklight];
-[SBBacklightControllerDefaultContext initWithWindowScene:];
-[SBBacklightControllerDefaultContext idleTimerDefaults];
-[SBBacklightControllerDefaultContext screenWakeAnimationController];
-[SBBacklightControllerDefaultContext proximitySensorManager];
-[SBBacklightControllerDefaultContext windowScene];
-[SBBacklightControllerDefaultContext backlightCoordinator];
-[SBBacklightControllerDefaultContext HIDUISensorModeController];
-[SBBacklightControllerDefaultContext CADisplay];
-[SBBacklightControllerDefaultContext blsConcreteBacklight];
-[SBBacklightControllerDefaultContext screenSleepCoordinator];
```
