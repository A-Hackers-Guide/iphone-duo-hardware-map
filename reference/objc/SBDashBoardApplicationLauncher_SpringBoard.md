# `SBDashBoardApplicationLauncher`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CSExternalEventHandling`, `CSPosterSwitcherPrewarming`, `SBLockScreenApplicationLaunching`, `CSApplicationLaunching`, `CSCameraPrewarming`
- 13 instance variables, 9 properties, 47 instance methods, 0 class methods

## Instance variables

```
@"SBWindowScene" _windowScene;
@"SBApplicationController" _applicationController;
@"BSEventQueue" _eventQueue;
@"SBInProcessSecureAppAction" _secureAppAction;
@"NSMutableDictionary" _currentPrewarmIdentifiersToReasons;
@"NSMutableDictionary" _prewarmIdentifiersToCancelTimers;
B _cameraIsPrewarming;
B _cameraPrewarmSucceeded;
B _posterSwitcherIsPrewarming;
@"NSTimer" _posterSwitcherPrewarmCancelTimer;
@"CSCoverSheetViewController" _coverSheetViewController;
@"SBSecureAppManager" _secureAppManager;
@"<SBDashBoardCaptureLaunchPolicy>" _captureLaunchPolicy;
```

## Properties

```
@property (T@"CSCoverSheetViewController",W,N,V_coverSheetViewController) coverSheetViewController;
@property (T@"SBSecureAppManager",W,N,V_secureAppManager) secureAppManager;
@property (T@"<SBDashBoardCaptureLaunchPolicy>",&,N,V_captureLaunchPolicy) captureLaunchPolicy;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C,N) coverSheetIdentifier;
@property (Tq,R,N) participantState;
```

## Instance methods

```
-[SBDashBoardApplicationLauncher coverSheetViewController];
-[SBDashBoardApplicationLauncher handleEvent:];
-[SBDashBoardApplicationLauncher wouldHandleButtonEvent:];
-[SBDashBoardApplicationLauncher dealloc];
-[SBDashBoardApplicationLauncher initWithWindowScene:applicationController:];
-[SBDashBoardApplicationLauncher setCoverSheetViewController:];
-[SBDashBoardApplicationLauncher handleTransitionRequest:];
-[SBDashBoardApplicationLauncher conformsToCSEventHandling];
-[SBDashBoardApplicationLauncher coverSheetIdentifier];
-[SBDashBoardApplicationLauncher secureAppManager];
-[SBDashBoardApplicationLauncher participantState];
-[SBDashBoardApplicationLauncher launchQuickNote];
-[SBDashBoardApplicationLauncher _activateCameraEntity:animated:actions:completion:];
-[SBDashBoardApplicationLauncher cancelPosterSwitcherPrewarm];
-[SBDashBoardApplicationLauncher launchCaptureApplication:];
-[SBDashBoardApplicationLauncher notePosterSwitcherPrewarmWasUsed];
-[SBDashBoardApplicationLauncher notePrewarmRequestEndedForIdentifier:];
-[SBDashBoardApplicationLauncher notePrewarmRequestWasUsefulForIdentifier:];
-[SBDashBoardApplicationLauncher prewarmCameraForIdentifier:prewarmReason:];
-[SBDashBoardApplicationLauncher prewarmConfigurationForIdentifier:];
-[SBDashBoardApplicationLauncher prewarmPosterSwitcher];
-[SBDashBoardApplicationLauncher _activateAppSceneBelowDashBoard:hostableEntity:secureAppType:withActions:interactive:completion:];
-[SBDashBoardApplicationLauncher _activateAppWithURL:];
-[SBDashBoardApplicationLauncher _activateCameraEntity:animated:asOverlay:viaSwitcherModal:request:actions:completion:];
-[SBDashBoardApplicationLauncher _attemptToUnlockToApplication:actions:completion:];
-[SBDashBoardApplicationLauncher _attemptToUnlockToCameraCompletion:];
-[SBDashBoardApplicationLauncher _backgroundLaunchWithBundleIdentifier:isCaptureApplicationLaunch:];
-[SBDashBoardApplicationLauncher _canHandleTransitionRequest:outActivatingSceneEntity:];
-[SBDashBoardApplicationLauncher _canPresentApplicationSceneEntity:fromSource:toDestination:];
-[SBDashBoardApplicationLauncher _captureExtensionBundleIdentifierForContainingApplication:];
-[SBDashBoardApplicationLauncher _coolCameraIfNecessaryForBundleIdentifier:prewarmReason:];
-[SBDashBoardApplicationLauncher _endPosterSwitcherPrewarm];
-[SBDashBoardApplicationLauncher _isCoverSheetHostingEntity:];
-[SBDashBoardApplicationLauncher _isCoverSheetHostingHostableEntity:];
-[SBDashBoardApplicationLauncher _presentApplicationSceneEntity:source:fromRequest:withResult:];
-[SBDashBoardApplicationLauncher _prewarmCameraForBundleIdentifier:prewarmReason:];
-[SBDashBoardApplicationLauncher _prewarmWithConfiguration:prewarmReason:];
-[SBDashBoardApplicationLauncher _reallyActivateAppSceneWithEntity:interactive:withCompletion:];
-[SBDashBoardApplicationLauncher _stopTrackingPrewarmReason:];
-[SBDashBoardApplicationLauncher captureApplicationForSceneEntity:];
-[SBDashBoardApplicationLauncher captureLaunchPolicy];
-[SBDashBoardApplicationLauncher currentActivePrewarmReasons];
-[SBDashBoardApplicationLauncher notePrewarmRequestEndedForIdentifier:prewarmReason:];
-[SBDashBoardApplicationLauncher presentationManager:bestIconViewForIdentifier:];
-[SBDashBoardApplicationLauncher prewarmCameraForIdentifier:];
-[SBDashBoardApplicationLauncher setCaptureLaunchPolicy:];
-[SBDashBoardApplicationLauncher setSecureAppManager:];
```
