# `SBAbstractWindowSceneDelegate`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBWindowSceneContextProviding`, `SBWindowSceneDelegate`
- 6 instance variables, 76 properties, 101 instance methods, 0 class methods

## Instance variables

```
@"SBWindowScene" _windowScene;
@"SBHardwareButtonZStackClient" _hardwareButtonZStackClient;
@"SBWindowSceneContext" _windowSceneContext;
@"<BSInvalidatable>" _pointerAssertion;
@"SBApplicationController" _applicationController;
B _invalidated;
```

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
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"SBWindowScene",W,N,V_windowScene) windowScene;
@property (T@"UIWindow",?,&,N) window;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N) hasIdleTimerBehaviors;
```

## Instance methods

```
-[SBAbstractWindowSceneDelegate homeScreenController];
-[SBAbstractWindowSceneDelegate coverSheetViewController];
-[SBAbstractWindowSceneDelegate recordingIndicatorManager];
-[SBAbstractWindowSceneDelegate _objc_initiateDealloc];
-[SBAbstractWindowSceneDelegate iconController];
-[SBAbstractWindowSceneDelegate layoutStateProvider];
-[SBAbstractWindowSceneDelegate switcherController];
-[SBAbstractWindowSceneDelegate reachabilityController];
-[SBAbstractWindowSceneDelegate hudController];
-[SBAbstractWindowSceneDelegate backlightController];
-[SBAbstractWindowSceneDelegate coverSheetPresentationManager];
-[SBAbstractWindowSceneDelegate idleTimerProvider:didProposeBehavior:forReason:];
-[SBAbstractWindowSceneDelegate wallpaperController];
-[SBAbstractWindowSceneDelegate alertItemsController];
-[SBAbstractWindowSceneDelegate lockScreenManager];
-[SBAbstractWindowSceneDelegate modalLibraryController];
-[SBAbstractWindowSceneDelegate setWindowScene:];
-[SBAbstractWindowSceneDelegate systemPointerInteractionManager];
-[SBAbstractWindowSceneDelegate layoutStateManager];
-[SBAbstractWindowSceneDelegate _traitsDelegateForWindowRole:];
-[SBAbstractWindowSceneDelegate floatingDockController];
-[SBAbstractWindowSceneDelegate sceneDidDisconnect:];
-[SBAbstractWindowSceneDelegate uiLockStateProvider];
-[SBAbstractWindowSceneDelegate authenticationStatusProvider];
-[SBAbstractWindowSceneDelegate surfaceType];
-[SBAbstractWindowSceneDelegate hardwareButtonBezelEffectsCoordinator];
-[SBAbstractWindowSceneDelegate setManualActivationShieldWindow:];
-[SBAbstractWindowSceneDelegate init];
-[SBAbstractWindowSceneDelegate lockedPointerManager];
-[SBAbstractWindowSceneDelegate commandTabController];
-[SBAbstractWindowSceneDelegate _configureForConnectingWindowScene:windowSceneContext:];
-[SBAbstractWindowSceneDelegate dealloc];
-[SBAbstractWindowSceneDelegate windowHidingManager];
-[SBAbstractWindowSceneDelegate indicatorDisplayPowerManager];
-[SBAbstractWindowSceneDelegate accessorySceneProvider];
-[SBAbstractWindowSceneDelegate traitsPipelineManager];
-[SBAbstractWindowSceneDelegate policyAggregator];
-[SBAbstractWindowSceneDelegate _shouldManageParticipantWithRole:];
-[SBAbstractWindowSceneDelegate medusaHostedKeyboardWindowController];
-[SBAbstractWindowSceneDelegate layoutStateTransitionCoordinator];
-[SBAbstractWindowSceneDelegate _shouldHandleWindowWillBecomeHiddenForRole:];
-[SBAbstractWindowSceneDelegate screenSleepController];
-[SBAbstractWindowSceneDelegate touchSuppressionManager];
-[SBAbstractWindowSceneDelegate isInvalidated];
-[SBAbstractWindowSceneDelegate interactiveScreenshotGestureManager];
-[SBAbstractWindowSceneDelegate setInvalidated:];
-[SBAbstractWindowSceneDelegate bannerController];
-[SBAbstractWindowSceneDelegate transientOverlayPresenter];
-[SBAbstractWindowSceneDelegate assistantController];
-[SBAbstractWindowSceneDelegate homeAffordanceInteractionManager];
-[SBAbstractWindowSceneDelegate lockStateAggregator];
-[SBAbstractWindowSceneDelegate resetIdleTimerIfNecessary];
-[SBAbstractWindowSceneDelegate systemGestureManager];
-[SBAbstractWindowSceneDelegate scene:willConnectToSession:options:];
-[SBAbstractWindowSceneDelegate auxiliaryContentController];
-[SBAbstractWindowSceneDelegate pictureInPictureManager];
-[SBAbstractWindowSceneDelegate secureDisplayStateProvider];
-[SBAbstractWindowSceneDelegate _createTraitsPipelineManagerForWindowScene:];
-[SBAbstractWindowSceneDelegate menuBarManager];
-[SBAbstractWindowSceneDelegate displayLayoutPublisher];
-[SBAbstractWindowSceneDelegate traitsArbiter];
-[SBAbstractWindowSceneDelegate liftToWakeController];
-[SBAbstractWindowSceneDelegate proposeBehaviorForReason:];
-[SBAbstractWindowSceneDelegate hasIdleTimerBehaviors];
-[SBAbstractWindowSceneDelegate modalUIFluidDismissGestureManager];
-[SBAbstractWindowSceneDelegate phoneRLController];
-[SBAbstractWindowSceneDelegate systemApertureController];
-[SBAbstractWindowSceneDelegate managedDisplayController];
-[SBAbstractWindowSceneDelegate appInteractionEventSource];
-[SBAbstractWindowSceneDelegate proximitySensorManager];
-[SBAbstractWindowSceneDelegate displayContentModeContext];
-[SBAbstractWindowSceneDelegate ambientPresentationController];
-[SBAbstractWindowSceneDelegate commandValidator];
-[SBAbstractWindowSceneDelegate windowScene];
-[SBAbstractWindowSceneDelegate orientationLockManager];
-[SBAbstractWindowSceneDelegate companionScenePresenter];
-[SBAbstractWindowSceneDelegate HIDUISensorModeController];
-[SBAbstractWindowSceneDelegate zStackResolver];
-[SBAbstractWindowSceneDelegate manualActivationShieldWindow];
-[SBAbstractWindowSceneDelegate modalAlertPresentationCoordinator];
-[SBAbstractWindowSceneDelegate controlCenterController];
-[SBAbstractWindowSceneDelegate transientUIInteractionManager];
-[SBAbstractWindowSceneDelegate coordinatorRequestedIdleTimerBehavior:];
-[SBAbstractWindowSceneDelegate continuousFoldController];
-[SBAbstractWindowSceneDelegate proximityBacklightPolicy];
-[SBAbstractWindowSceneDelegate _windowScene:levelForWindow:preferredLevel:];
-[SBAbstractWindowSceneDelegate _windowScene:window:didUpdateSupportedInterfaceOrientations:preferredOrientation:];
-[SBAbstractWindowSceneDelegate _windowScene:windowDidBecomeVisible:];
-[SBAbstractWindowSceneDelegate _windowScene:windowWillAttach:];
-[SBAbstractWindowSceneDelegate _windowScene:windowWillBecomeHidden:];
-[SBAbstractWindowSceneDelegate _windowScene:windowWillBecomeVisible:];
-[SBAbstractWindowSceneDelegate _windowScene:windowWillDetach:];
-[SBAbstractWindowSceneDelegate windowScene:didUpdateCoordinateSpace:interfaceOrientation:traitCollection:];
-[SBAbstractWindowSceneDelegate _sceneHandlesDisablingIdleTimer];
-[SBAbstractWindowSceneDelegate _acquireParticipantForWindow:reason:];
-[SBAbstractWindowSceneDelegate _configureTraitsArbiter];
-[SBAbstractWindowSceneDelegate _displayLayoutPublisherForWindowScene:];
-[SBAbstractWindowSceneDelegate _isWindowContentVisible:];
-[SBAbstractWindowSceneDelegate _participantForWindow:];
-[SBAbstractWindowSceneDelegate _sbWindowSceneContext];
-[SBAbstractWindowSceneDelegate _setParticipant:forWindow:];
```
