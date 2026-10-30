# `SBWindowSceneContextProviding` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 65 properties, 65 instance methods, 0 class methods

## Properties

```
@property (T@"SBAlertItemsController",R,N) alertItemsController;
@property (T@"SBAmbientPresentationController",R,N) ambientPresentationController;
@property (T@"SBDisplayAppInteractionEventSource",R,N) appInteractionEventSource;
@property (T@"<SBAssistantSceneControlling>",R,N) assistantController;
@property (T@"<SBFAuthenticationStatusProvider>",R,N) authenticationStatusProvider;
@property (T@"BNBannerController",R,N) bannerController;
@property (T@"SBBacklightController",R,N) backlightController;
@property (T@"SBCompanionScenePresenter",R,N) companionScenePresenter;
@property (T@"SBControlCenterController",R,N) controlCenterController;
@property (T@"SBCoverSheetPresentationManager",R,N) coverSheetPresentationManager;
@property (T@"CSCoverSheetViewController",R,N) coverSheetViewController;
@property (T@"<FBSDisplayLayoutPublishing>",R,N) displayLayoutPublisher;
@property (T@"SBFloatingDockController",R,N) floatingDockController;
@property (T@"SBHIDUISensorModeController",R,N) HIDUISensorModeController;
@property (T@"SBHomeAffordanceInteractionManager",R,N) homeAffordanceInteractionManager;
@property (T@"SBHomeScreenController",R,N) homeScreenController;
@property (T@"<SBHUDControlling>",R,N) hudController;
@property (T@"SBSceneLayoutStateProvider",R,N) layoutStateProvider;
@property (T@"SBMainDisplayLayoutStateManager",R,N) layoutStateManager;
@property (T@"SBLayoutStateTransitionCoordinator",R,N) layoutStateTransitionCoordinator;
@property (T@"SBLiftToWakeController",R,N) liftToWakeController;
@property (T@"SBLockedPointerManager",R,N) lockedPointerManager;
@property (T@"SBLockScreenManager",R,N) lockScreenManager;
@property (T@"SBLockStateAggregator",R,N) lockStateAggregator;
@property (T@"SBMedusaHostedKeyboardWindowController",R,N) medusaHostedKeyboardWindowController;
@property (T@"<SBLockStateProviding>",R,N) uiLockStateProvider;
@property (T@"SBModalAlertPresentationCoordinator",R,N) modalAlertPresentationCoordinator;
@property (T@"SBModalLibraryController",R,N) modalLibraryController;
@property (T@"SBModalUIFluidDismissGestureManager",R,N) modalUIFluidDismissGestureManager;
@property (T@"SBWindowScenePIPManager",R,N) pictureInPictureManager;
@property (T@"<SBProximityBacklightPolicy>",R,N) proximityBacklightPolicy;
@property (T@"SBProximitySensorManager",R,N) proximitySensorManager;
@property (T@"SBReachabilityController",R,N) reachabilityController;
@property (T@"SBRecordingIndicatorManager",R,N) recordingIndicatorManager;
@property (T@"SBRecordingIndicatorDisplayPowerManager",R,N) indicatorDisplayPowerManager;
@property (T@"SBManagedDisplayController",R,N) managedDisplayController;
@property (T@"SBPhoneRLController",R,N) phoneRLController;
@property (T@"SBScreenSleepController",R,N) screenSleepController;
@property (T@"<SBFSecureDisplayStateProviding>",R,N) secureDisplayStateProvider;
@property (T@"SBSwitcherController",R,N) switcherController;
@property (T@"<SBSystemApertureControlling>",R,N) systemApertureController;
@property (T@"SBSystemGestureManager",R,N) systemGestureManager;
@property (T@"SBSystemPointerInteractionManager",R,N) systemPointerInteractionManager;
@property (T@"SBTouchSuppressionManager",R,N) touchSuppressionManager;
@property (T@"TRAArbiter",R,N) traitsArbiter;
@property (T@"SBTraitsPipelineManager",R,N) traitsPipelineManager;
@property (T@"SBWindowSceneOrientationLockManager",R,N) orientationLockManager;
@property (T@"<SBTransientOverlayPresenting>",R,N) transientOverlayPresenter;
@property (T@"SBWallpaperController",R,N) wallpaperController;
@property (T@"SBWindowHidingManager",R,N) windowHidingManager;
@property (T@"SBFZStackResolver",R,N) zStackResolver;
@property (T@"SBTransientUIInteractionManager",R,N) transientUIInteractionManager;
@property (T@"<SBUICommandValidating>",R,N) commandValidator;
@property (T@"SBHardwareButtonBezelEffectsCoordinator",R,N) hardwareButtonBezelEffectsCoordinator;
@property (T@"SBIconController",R,N) iconController;
@property (T@"SBCommandTabController",R,N) commandTabController;
@property (T@"SBInteractiveScreenshotGestureManager",R,N) interactiveScreenshotGestureManager;
@property (T@"SBMenuBarManager",R,N) menuBarManager;
@property (T@"SBPolicyAggregator",R,N) policyAggregator;
@property (T@"SBWindowSceneAccessorySceneProvider",R,N) accessorySceneProvider;
@property (T@"_SBManualDisplayActivationShieldWindow",R,N) manualActivationShieldWindow;
@property (T@"SBWindowSceneAuxiliaryContentController",R,N) auxiliaryContentController;
@property (T@"SBContinuousFoldController",R,N) continuousFoldController;
@property (T@"SBWindowSceneDisplayContentModeContext",R,N) displayContentModeContext;
@property (Tq,R,N) surfaceType;
```

## Instance methods

```
-[SBWindowSceneContextProviding homeScreenController];
-[SBWindowSceneContextProviding coverSheetViewController];
-[SBWindowSceneContextProviding recordingIndicatorManager];
-[SBWindowSceneContextProviding iconController];
-[SBWindowSceneContextProviding layoutStateProvider];
-[SBWindowSceneContextProviding switcherController];
-[SBWindowSceneContextProviding reachabilityController];
-[SBWindowSceneContextProviding hudController];
-[SBWindowSceneContextProviding backlightController];
-[SBWindowSceneContextProviding coverSheetPresentationManager];
-[SBWindowSceneContextProviding wallpaperController];
-[SBWindowSceneContextProviding alertItemsController];
-[SBWindowSceneContextProviding lockScreenManager];
-[SBWindowSceneContextProviding modalLibraryController];
-[SBWindowSceneContextProviding systemPointerInteractionManager];
-[SBWindowSceneContextProviding layoutStateManager];
-[SBWindowSceneContextProviding floatingDockController];
-[SBWindowSceneContextProviding uiLockStateProvider];
-[SBWindowSceneContextProviding authenticationStatusProvider];
-[SBWindowSceneContextProviding surfaceType];
-[SBWindowSceneContextProviding hardwareButtonBezelEffectsCoordinator];
-[SBWindowSceneContextProviding lockedPointerManager];
-[SBWindowSceneContextProviding commandTabController];
-[SBWindowSceneContextProviding windowHidingManager];
-[SBWindowSceneContextProviding indicatorDisplayPowerManager];
-[SBWindowSceneContextProviding accessorySceneProvider];
-[SBWindowSceneContextProviding traitsPipelineManager];
-[SBWindowSceneContextProviding policyAggregator];
-[SBWindowSceneContextProviding medusaHostedKeyboardWindowController];
-[SBWindowSceneContextProviding layoutStateTransitionCoordinator];
-[SBWindowSceneContextProviding screenSleepController];
-[SBWindowSceneContextProviding touchSuppressionManager];
-[SBWindowSceneContextProviding interactiveScreenshotGestureManager];
-[SBWindowSceneContextProviding bannerController];
-[SBWindowSceneContextProviding transientOverlayPresenter];
-[SBWindowSceneContextProviding assistantController];
-[SBWindowSceneContextProviding homeAffordanceInteractionManager];
-[SBWindowSceneContextProviding lockStateAggregator];
-[SBWindowSceneContextProviding systemGestureManager];
-[SBWindowSceneContextProviding auxiliaryContentController];
-[SBWindowSceneContextProviding pictureInPictureManager];
-[SBWindowSceneContextProviding secureDisplayStateProvider];
-[SBWindowSceneContextProviding menuBarManager];
-[SBWindowSceneContextProviding displayLayoutPublisher];
-[SBWindowSceneContextProviding traitsArbiter];
-[SBWindowSceneContextProviding liftToWakeController];
-[SBWindowSceneContextProviding modalUIFluidDismissGestureManager];
-[SBWindowSceneContextProviding phoneRLController];
-[SBWindowSceneContextProviding systemApertureController];
-[SBWindowSceneContextProviding managedDisplayController];
-[SBWindowSceneContextProviding appInteractionEventSource];
-[SBWindowSceneContextProviding proximitySensorManager];
-[SBWindowSceneContextProviding displayContentModeContext];
-[SBWindowSceneContextProviding ambientPresentationController];
-[SBWindowSceneContextProviding commandValidator];
-[SBWindowSceneContextProviding orientationLockManager];
-[SBWindowSceneContextProviding companionScenePresenter];
-[SBWindowSceneContextProviding HIDUISensorModeController];
-[SBWindowSceneContextProviding zStackResolver];
-[SBWindowSceneContextProviding manualActivationShieldWindow];
-[SBWindowSceneContextProviding modalAlertPresentationCoordinator];
-[SBWindowSceneContextProviding controlCenterController];
-[SBWindowSceneContextProviding transientUIInteractionManager];
-[SBWindowSceneContextProviding continuousFoldController];
-[SBWindowSceneContextProviding proximityBacklightPolicy];
```
