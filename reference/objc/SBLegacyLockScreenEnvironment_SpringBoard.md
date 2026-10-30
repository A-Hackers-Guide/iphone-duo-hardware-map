# `SBLegacyLockScreenEnvironment`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `SBLockScreenEnvironment`
- 1 instance variables, 30 properties, 32 instance methods, 0 class methods

## Instance variables

```
@"SBLockScreenViewControllerBase" _lockScreenViewController;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
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
-[SBLegacyLockScreenEnvironment customActionStore];
-[SBLegacyLockScreenEnvironment backlightController];
-[SBLegacyLockScreenEnvironment rootViewController];
-[SBLegacyLockScreenEnvironment applicationHoster];
-[SBLegacyLockScreenEnvironment setupController];
-[SBLegacyLockScreenEnvironment widgetMetricsProvider];
-[SBLegacyLockScreenEnvironment autoUnlockRule];
-[SBLegacyLockScreenEnvironment coverSheetSpotlightPresenter];
-[SBLegacyLockScreenEnvironment spotlightPresenter];
-[SBLegacyLockScreenEnvironment lockController];
-[SBLegacyLockScreenEnvironment succinctDescriptionBuilder];
-[SBLegacyLockScreenEnvironment proximityBehaviorProvider];
-[SBLegacyLockScreenEnvironment screenWakeAnimationTarget];
-[SBLegacyLockScreenEnvironment idleTimerController];
-[SBLegacyLockScreenEnvironment applicationLauncher];
-[SBLegacyLockScreenEnvironment descriptionWithMultilinePrefix:];
-[SBLegacyLockScreenEnvironment biometricUnlockBehavior];
-[SBLegacyLockScreenEnvironment pluginPresenter];
-[SBLegacyLockScreenEnvironment succinctDescription];
-[SBLegacyLockScreenEnvironment passcodeViewPresenter];
-[SBLegacyLockScreenEnvironment contentStateProvider];
-[SBLegacyLockScreenEnvironment mediaControlsPresenter];
-[SBLegacyLockScreenEnvironment callController];
-[SBLegacyLockScreenEnvironment controlCenterPresenter];
-[SBLegacyLockScreenEnvironment blockedStateObserver];
-[SBLegacyLockScreenEnvironment buttonEventsHandler];
-[SBLegacyLockScreenEnvironment description];
-[SBLegacyLockScreenEnvironment buttonObserver];
-[SBLegacyLockScreenEnvironment statusBarTransitionController];
-[SBLegacyLockScreenEnvironment behaviorSuppressor];
-[SBLegacyLockScreenEnvironment descriptionBuilderWithMultilinePrefix:];
-[SBLegacyLockScreenEnvironment initWithLockScreenViewController:];
```
