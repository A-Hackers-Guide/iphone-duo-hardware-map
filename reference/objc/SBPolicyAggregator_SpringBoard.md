# `SBPolicyAggregator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 14 properties, 66 instance methods, 0 class methods

## Instance variables

```
@"MCProfileConnection" _override_profileConnection;
@"SBSetupManager" _override_setupManager;
@"SBAlertItemsController" _override_alertItemsController;
@"SBApplicationController" _override_applicationController;
@"SBAssistantController" _override_assistantController;
@"SBCommandTabController" _override_commandTabController;
@"SBConferenceManager" _override_conferenceManager;
@"SBRemoteTransientOverlaySessionManager" _override_remoteTransientOverlaySessionManager;
@"SBLockScreenManager" _override_lockScreenManager;
@"SBLockStateAggregator" _override_lockStateAggregator;
@"SBTelephonyManager" _override_telephonyManager;
@"SBBannerManager" _override_bannerManager;
^{__CFBoolean=} _hasCameraCapability;
@"SBLocalDefaults" _defaults;
B _storeDemoAppLockEnabled;
@"FBSDisplayIdentity" _displayIdentity;
```

## Properties

```
@property (T@"FBSDisplayIdentity",R,N,G_displayIdentity,V_displayIdentity) displayIdentity;
@property (T@"SBWindowScene",R,N,G_windowScene) windowScene;
@property (T@"MCProfileConnection",&,N,G_profileConnection,S_setProfileConnection:,V_override_profileConnection) profileConnection;
@property (T@"SBSetupManager",&,N,G_setupManager,S_setSetupManager:,V_override_setupManager) setupManager;
@property (T@"SBAlertItemsController",&,N,G_alertItemsController,S_setAlertItemsController:,V_override_alertItemsController) alertItemsController;
@property (T@"SBApplicationController",&,N,G_applicationController,S_setApplicationController:,V_override_applicationController) applicationController;
@property (T@"SBAssistantController",&,N,G_assistantController,S_setAssistantController:,V_override_assistantController) assistantController;
@property (T@"SBCommandTabController",&,N,G_commandTabController,S_setCommandTabController:,V_override_commandTabController) commandTabController;
@property (T@"SBConferenceManager",&,N,G_conferenceManager,S_setConferenceManager:,V_override_conferenceManager) conferenceManager;
@property (T@"SBRemoteTransientOverlaySessionManager",&,N,G_remoteTransientOverlaySessionManager,S_setRemoteTransientOverlaySessionManager:,V_override_remoteTransientOverlaySessionManager) remoteTransientOverlaySessionManager;
@property (T@"SBLockScreenManager",&,N,G_lockScreenManager,S_setLockScreenManager:,V_override_lockScreenManager) lockScreenManager;
@property (T@"SBLockStateAggregator",&,N,G_lockStateAggregator,S_setLockStateAggregator:,V_override_lockStateAggregator) lockStateAggregator;
@property (T@"SBTelephonyManager",&,N,G_telephonyManager,S_setTelephonyManager:,V_override_telephonyManager) telephonyManager;
@property (T@"SBBannerManager",&,N,G_bannerManager,S_setBannerManager:,V_override_bannerManager) bannerManager;
```

## Instance methods

```
-[SBPolicyAggregator _windowScene];
-[SBPolicyAggregator _telephonyManager];
-[SBPolicyAggregator _conferenceManager];
-[SBPolicyAggregator _setBannerManager:];
-[SBPolicyAggregator initWithDefaults:displayIdentity:];
-[SBPolicyAggregator reloadDemoDefaults];
-[SBPolicyAggregator _allowsCapabilityHomeScreenEditingWithExplanation:];
-[SBPolicyAggregator _allowsCapabilityLockScreenCameraSupportedWithExplanation:];
-[SBPolicyAggregator _hasFullySetUpUserWithExplanation:];
-[SBPolicyAggregator allowsCapability:];
-[SBPolicyAggregator _allowsCapabilityLockScreenControlCenterWithExplanation:];
-[SBPolicyAggregator _allowsCapabilityAssistantEnabledWithExplanation:];
-[SBPolicyAggregator allowsTransitionRequest:];
-[SBPolicyAggregator _setRemoteTransientOverlaySessionManager:];
-[SBPolicyAggregator _allowsCapabilityPosterSwitcherWithExplanation:];
-[SBPolicyAggregator _allowsCapabilityHardwareButtonBezelEffectsEdgeLight:];
-[SBPolicyAggregator _commandTabController];
-[SBPolicyAggregator _displayIdentity];
-[SBPolicyAggregator _allowsCapabilityLockScreenCameraSwipeWithExplanation:];
-[SBPolicyAggregator _allowsCapabilityUnlockToPluginSpecifiedApplicationWithExplanation:];
-[SBPolicyAggregator _allowsCapabilityLockScreenTodayViewWithExplanation:];
-[SBPolicyAggregator _setProfileConnection:];
-[SBPolicyAggregator _lockScreenManager];
-[SBPolicyAggregator _dictationInfoOnScreen];
-[SBPolicyAggregator _bannerManager];
-[SBPolicyAggregator _alertItemsController];
-[SBPolicyAggregator _allowsCapabilityVoiceControlWithExplanation:];
-[SBPolicyAggregator allowsCapability:explanation:];
-[SBPolicyAggregator _allowsCapabilityLockScreenBulletinWithExplanation:];
-[SBPolicyAggregator _allowsCapabilitySendMediaCommandWithExplanation:];
-[SBPolicyAggregator _allowsCapabilityLockScreenCameraWithExplanation:];
-[SBPolicyAggregator _setConferenceManager:];
-[SBPolicyAggregator _setupManager];
-[SBPolicyAggregator _allowsCapabilityAssistantWithExplanation:];
-[SBPolicyAggregator _remoteTransientOverlaySessionManager];
-[SBPolicyAggregator _allowsCapabilitySearchOnLockScreenWithExplanation:];
-[SBPolicyAggregator _allowsCapabilityQuickNoteWithExplanation:];
-[SBPolicyAggregator _allowsCapabilityCoverSheetSpotlightWithExplanation:];
-[SBPolicyAggregator _allowsCapabilityControlCenterEditingWithExplanation:];
-[SBPolicyAggregator _setSetupManager:];
-[SBPolicyAggregator _setLockStateAggregator:];
-[SBPolicyAggregator _allowsCapabilitySystemGestureWithExplanation:];
-[SBPolicyAggregator _allowsCapabilityCoverSheetWithExplanation:];
-[SBPolicyAggregator _setLockScreenManager:];
-[SBPolicyAggregator _setTelephonyManager:];
-[SBPolicyAggregator _allowsCapabilityScreenshotWithExplanation:];
-[SBPolicyAggregator _allowsCapabilityControlCenterWithExplanation:];
-[SBPolicyAggregator _allowsCapabilityLockScreenNotificationCenterWithExplanation:];
-[SBPolicyAggregator _allowsCapabilityDismissCoverSheetWithExplanation:];
-[SBPolicyAggregator _setApplicationController:];
-[SBPolicyAggregator _allowsCapabilityTodayViewWithExplanation:];
-[SBPolicyAggregator _profileConnection];
-[SBPolicyAggregator _assistantController];
-[SBPolicyAggregator _allowsNotificationOrControlCenterWithExplanation:];
-[SBPolicyAggregator _lockStateAggregator];
-[SBPolicyAggregator _allowsCapabilityLoginWindowWithExplanation:];
-[SBPolicyAggregator _allowsCapabilitySpotlightWithExplanation:];
-[SBPolicyAggregator _allowsCapabilityLiftToWakeWithExplanation:];
-[SBPolicyAggregator _applicationController];
-[SBPolicyAggregator _allowsCapabilityWallpaperEditingWithExplanation:];
-[SBPolicyAggregator _setAssistantController:];
-[SBPolicyAggregator _allowsCapabilitySuggestedApplicationWithExplanation:];
-[SBPolicyAggregator _allowsCapabilityCommandTabWithExplanation:];
-[SBPolicyAggregator _allowsCapabilityLogoutWithExplanation:];
-[SBPolicyAggregator _setAlertItemsController:];
-[SBPolicyAggregator _setCommandTabController:];
```
