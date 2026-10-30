# `SBScreenSleepController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBScreenWakeAnimationControllerDelegate`
- 15 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"SBScreenWakeAnimationController" _screenWakeAnimationController;
@"SBLockScreenManager" _lockScreenManager;
@"SBBacklightController" _backlightController;
@"<SBFAuthenticationStatusProvider>" _authenticationStatusProvider;
@"<SBFAuthenticationAssertionProviding>" _authenticationAssertionProvider;
@"SBAlertItemsController" _alertItemsController;
@"SBWindowScene" _windowScene;
B _didLock;
i _lastLockSource;
@"NSDictionary" _lastLockOptions;
Q _transitionGeneration;
B _sleepTransitionInProgress;
@"SBAlwaysOnSettings" _alwaysOnSettings;
@"SBScreenSleepTransitionWindow" _transitionWindow;
@"<BLSHBacklightSceneHostEnvironment>" _backlightSceneHostEnvironment;
```

## Properties

```
@property (T@"SBWindowScene",R,W,N,G_windowScene,V_windowScene) windowScene;
@property (T@"<BLSHBacklightSceneHostEnvironment>",R,N,V_backlightSceneHostEnvironment) backlightSceneHostEnvironment;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBScreenSleepController _windowScene];
-[SBScreenSleepController _ambientPresentationController];
-[SBScreenSleepController backlightSceneHostEnvironment];
-[SBScreenSleepController _performLock];
-[SBScreenSleepController _performLockAnimated:];
-[SBScreenSleepController _setTransitionWindowVisible:animated:completion:];
-[SBScreenSleepController _shouldPresentAmbientOnSleepAndLock];
-[SBScreenSleepController initWithScreenWakeAnimationController:lockScreenManager:backlightController:authenticationStatusProvider:authenticationAssertionProvider:alertItemsController:windowScene:];
-[SBScreenSleepController sleepAndLockUIFromSource:completion:];
-[SBScreenSleepController sleepAndLockUIFromSource:lockOptions:completion:];
-[SBScreenSleepController targetBacklightStateForSource:isWake:];
-[SBScreenSleepController transitionToVisualState:fromVisualState:animated:completion:];
```
