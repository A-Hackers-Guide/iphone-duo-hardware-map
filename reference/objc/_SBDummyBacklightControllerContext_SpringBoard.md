# `_SBDummyBacklightControllerContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBBacklightControllerContextProviding`, `BLSHBacklightHostObservable`, `BLSBacklightChangeRequestable`
- 7 instance variables, 25 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"CADisplay" _caDisplay;
B _transitioning;
@"SBWindowScene" _windowScene;
q _backlightState;
Q _backlightStateChangeTimestamp;
q _backlightDisplayMode;
q _flipbookState;
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
@property (Tq,R,N,V_backlightDisplayMode) backlightDisplayMode;
@property (TQ,R,N,V_backlightStateChangeTimestamp) backlightStateChangeTimestamp;
@property (T@"NSString",R,C,N) backlightStateDescription;
@property (Tq,R,N,V_backlightState) backlightState;
@property (Tq,R,N,V_flipbookState) flipbookState;
@property (TB,R,N,GisTransitioning,V_transitioning) transitioning;
@property (TB,R,N,GisAlwaysOnEnabled) alwaysOnEnabled;
@property (TB,R,N) deviceSupportsAlwaysOn;
@property (T@"<BLSDisplay>",R,N) display;
```

## Instance methods

```
-[_SBDummyBacklightControllerContext wakeLogger];
-[_SBDummyBacklightControllerContext lockScreenManager];
-[_SBDummyBacklightControllerContext display];
-[_SBDummyBacklightControllerContext deviceSupportsAlwaysOn];
-[_SBDummyBacklightControllerContext blsBacklight];
-[_SBDummyBacklightControllerContext backlightStateChangeTimestamp];
-[_SBDummyBacklightControllerContext isAlwaysOnEnabled];
-[_SBDummyBacklightControllerContext backlightDisplayMode];
-[_SBDummyBacklightControllerContext removeObserver:];
-[_SBDummyBacklightControllerContext isTransitioning];
-[_SBDummyBacklightControllerContext performChangeRequest:];
-[_SBDummyBacklightControllerContext flipbookState];
-[_SBDummyBacklightControllerContext backlightStateDescription];
-[_SBDummyBacklightControllerContext initWithWindowScene:];
-[_SBDummyBacklightControllerContext addObserver:];
-[_SBDummyBacklightControllerContext backlightState];
-[_SBDummyBacklightControllerContext idleTimerDefaults];
-[_SBDummyBacklightControllerContext screenWakeAnimationController];
-[_SBDummyBacklightControllerContext proximitySensorManager];
-[_SBDummyBacklightControllerContext windowScene];
-[_SBDummyBacklightControllerContext backlightCoordinator];
-[_SBDummyBacklightControllerContext HIDUISensorModeController];
-[_SBDummyBacklightControllerContext CADisplay];
-[_SBDummyBacklightControllerContext appendWindowSceneToNotificationUserInfo:];
-[_SBDummyBacklightControllerContext blsConcreteBacklight];
-[_SBDummyBacklightControllerContext screenSleepCoordinator];
```
