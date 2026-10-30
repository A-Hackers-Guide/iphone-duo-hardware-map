# `SBLockScreenEnvironment` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 26 properties, 26 instance methods, 0 class methods

## Properties

```
@property (T@"UIViewController",R,N) rootViewController;
@property (T@"<SBAutoUnlockRule>",R,N) autoUnlockRule;
@property (T@"<SBBiometricUnlockBehavior>",R,N) biometricUnlockBehavior;
@property (T@"<SBButtonEventsHandler>",R,N) buttonEventsHandler;
@property (T@"<SBApplicationHosting>",R,N) applicationHoster;
@property (T@"<SBFScreenWakeAnimationTarget>",R,N) screenWakeAnimationTarget;
@property (T@"<SBControlCenterPresenting>",R,N) controlCenterPresenter;
@property (T@"<SBLockScreenApplicationLaunching>",R,N) applicationLauncher;
@property (T@"<SBLockScreenBacklightControlling>",R,N) backlightController;
@property (T@"<SBLockScreenBehaviorSuppressing>",R,N) behaviorSuppressor;
@property (T@"<SBLockScreenBlockedStateObserving>",R,N) blockedStateObserver;
@property (T@"<SBLockScreenButtonObserving>",R,N) buttonObserver;
@property (T@"<SBLockScreenCallHandling>",R,N) callController;
@property (T@"<SBLockScreenContentStateProviding>",R,N) contentStateProvider;
@property (T@"<SBLockScreenCustomActionStoring>",R,N) customActionStore;
@property (T@"<SBLockScreenIdleTimerControlling>",R,N) idleTimerController;
@property (T@"<SBLockScreenLockingAndUnlocking>",R,N) lockController;
@property (T@"<SBLockScreenMediaControlsPresenting>",R,N) mediaControlsPresenter;
@property (T@"<SBLockScreenPasscodeViewPresenting>",R,N) passcodeViewPresenter;
@property (T@"<SBLockScreenPluginPresenting>",R,N) pluginPresenter;
@property (T@"<SBLockScreenProximityBehaviorProviding>",R,N) proximityBehaviorProvider;
@property (T@"<SBLockScreenStatusBarTransitioning>",R,N) statusBarTransitionController;
@property (T@"<SBSWidgetMetricsProviding>",R,N) widgetMetricsProvider;
@property (T@"<SBLockScreenSpotlightPresenting>",R,N) spotlightPresenter;
@property (T@"<CSCoverSheetSpotlightPresenting>",R,N) coverSheetSpotlightPresenter;
@property (T@"<SBLockScreenSetupControlling>",R,N) setupController;
```

## Instance methods

```
-[SBLockScreenEnvironment customActionStore];
-[SBLockScreenEnvironment backlightController];
-[SBLockScreenEnvironment rootViewController];
-[SBLockScreenEnvironment applicationHoster];
-[SBLockScreenEnvironment setupController];
-[SBLockScreenEnvironment widgetMetricsProvider];
-[SBLockScreenEnvironment autoUnlockRule];
-[SBLockScreenEnvironment coverSheetSpotlightPresenter];
-[SBLockScreenEnvironment spotlightPresenter];
-[SBLockScreenEnvironment lockController];
-[SBLockScreenEnvironment proximityBehaviorProvider];
-[SBLockScreenEnvironment screenWakeAnimationTarget];
-[SBLockScreenEnvironment idleTimerController];
-[SBLockScreenEnvironment applicationLauncher];
-[SBLockScreenEnvironment biometricUnlockBehavior];
-[SBLockScreenEnvironment pluginPresenter];
-[SBLockScreenEnvironment passcodeViewPresenter];
-[SBLockScreenEnvironment contentStateProvider];
-[SBLockScreenEnvironment mediaControlsPresenter];
-[SBLockScreenEnvironment callController];
-[SBLockScreenEnvironment controlCenterPresenter];
-[SBLockScreenEnvironment blockedStateObserver];
-[SBLockScreenEnvironment buttonEventsHandler];
-[SBLockScreenEnvironment buttonObserver];
-[SBLockScreenEnvironment statusBarTransitionController];
-[SBLockScreenEnvironment behaviorSuppressor];
```
