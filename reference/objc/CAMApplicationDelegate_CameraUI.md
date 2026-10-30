# `CAMApplicationDelegate`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIResponder`
- Protocols: `UNUserNotificationCenterDelegate`, `CAMSystemMenuControllerDelegate`, `UIApplicationDelegate`, `CAMSubsystemsProvider`
- 5 instance variables, 24 properties, 68 instance methods, 0 class methods

## Instance variables

```
@"UIWindow" _window;
@"UIWindow" _coverScreenWindow;
@"UIWindow" _shutterBuddyWindow;
@"CAMSubsystems" _subsystems;
@"CAMSystemMenuController" _systemMenuController;
```

## Properties

```
@property (T@"CAMSubsystems",&,N,V_subsystems) subsystems;
@property (T@"CAMSystemMenuController",&,N,V_systemMenuController) systemMenuController;
@property (T@"UIWindow",&,N,V_window) window;
@property (T@"UIWindow",&,N,V_coverScreenWindow) coverScreenWindow;
@property (T@"UIWindow",&,N,V_shutterBuddyWindow) shutterBuddyWindow;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"CAMViewfinderViewController",R,N) viewfinderViewController;
@property (T@"CAMCoverScreenManager",R,N) coverScreenManager;
@property (T@"CAMCameraRollController",R,N) cameraRollController;
@property (T@"CUCaptureController",R,N) captureController;
@property (T@"CAMTimelapseController",R,N) timelapseController;
@property (T@"CAMPersistenceController",R,N) persistenceController;
@property (T@"CAMMotionController",R,N) motionController;
@property (T@"CAMLocationController",R,N) locationController;
@property (T@"CAMPowerController",R,N) powerController;
@property (T@"CAMBurstController",R,N) burstController;
@property (T@"CAMKeepAliveController",R,N) keepAliveController;
@property (T@"CAMProtectionController",R,N) protectionController;
@property (T@"CAMRemoteShutterController",R,N) remoteShutterController;
@property (T@"CAMLibrarySelectionController",R,N) librarySelectionController;
@property (T@"CAMNebulaDaemonProxyManager",R,N) nebulaDaemonProxyManager;
```

## Instance methods

```
-[CAMApplicationDelegate shouldEnableCaptureMenuCommand];
-[CAMApplicationDelegate prepareForDefaultImageSnapshotForScreen:];
-[CAMApplicationDelegate shouldEnableTimerMenuCommand];
-[CAMApplicationDelegate shouldEnableFlipCameraMenuCommand];
-[CAMApplicationDelegate shouldEnableFlashMenuCommand];
-[CAMApplicationDelegate currentCaptureModes];
-[CAMApplicationDelegate currentCaptureMode];
-[CAMApplicationDelegate application:configurationForConnectingSceneSession:options:];
-[CAMApplicationDelegate handleLivePhotoModeMenuAction:];
-[CAMApplicationDelegate validateCommand:];
-[CAMApplicationDelegate userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:];
-[CAMApplicationDelegate cleanupCoverScreenForWindowScene:];
-[CAMApplicationDelegate application:didDiscardSceneSessions:];
-[CAMApplicationDelegate _isNotificationTooOld:];
-[CAMApplicationDelegate setShutterBuddyWindow:];
-[CAMApplicationDelegate sceneDelegate:disconnectedScene:];
-[CAMApplicationDelegate currentFlashMode];
-[CAMApplicationDelegate buildMenuWithBuilder:];
-[CAMApplicationDelegate currentLivePhotoMode];
-[CAMApplicationDelegate locationController];
-[CAMApplicationDelegate nebulaDaemonProxyManager];
-[CAMApplicationDelegate handleCaptureMenuAction:];
-[CAMApplicationDelegate coverScreenSceneDelegate:receivedScene:];
-[CAMApplicationDelegate setCoverScreenWindow:];
-[CAMApplicationDelegate window];
-[CAMApplicationDelegate protectionController];
-[CAMApplicationDelegate handleCameraSettingsMenuAction:];
-[CAMApplicationDelegate _checkInternalInstallBundlesAndAlertIfIncompatible];
-[CAMApplicationDelegate motionController];
-[CAMApplicationDelegate shutterBuddyWindow];
-[CAMApplicationDelegate handleFlipCameraMenuAction:];
-[CAMApplicationDelegate subsystems];
-[CAMApplicationDelegate handleFlashMenuAction:];
-[CAMApplicationDelegate powerController];
-[CAMApplicationDelegate persistenceController];
-[CAMApplicationDelegate viewfinderViewController];
-[CAMApplicationDelegate _requestAuthorizationForNotificationCenter:];
-[CAMApplicationDelegate burstController];
-[CAMApplicationDelegate handleCameraRollMenuAction:];
-[CAMApplicationDelegate keepAliveController];
-[CAMApplicationDelegate handleTimerMenuAction:];
-[CAMApplicationDelegate isShowingCameraRoll];
-[CAMApplicationDelegate currentTimerDuration];
-[CAMApplicationDelegate coverScreenManager];
-[CAMApplicationDelegate applicationWillTerminate:];
-[CAMApplicationDelegate sceneDelegate:receivedScene:preferenceOverrides:];
-[CAMApplicationDelegate setSystemMenuController:];
-[CAMApplicationDelegate shouldEnableLivePhotoMenuCommand];
-[CAMApplicationDelegate cleanupShutterBuddyForWindowScene:];
-[CAMApplicationDelegate remoteShutterController];
-[CAMApplicationDelegate cameraIsRecording];
-[CAMApplicationDelegate coverScreenWindow];
-[CAMApplicationDelegate sceneDelegate:continueUserActivity:];
-[CAMApplicationDelegate librarySelectionController];
-[CAMApplicationDelegate updateShortcutItemsForApplication:];
-[CAMApplicationDelegate sceneDelegate:requestedActionForPreferenceOverrides:];
-[CAMApplicationDelegate _userInfoForMode:devicePosition:];
-[CAMApplicationDelegate cameraRollController];
-[CAMApplicationDelegate _internalInstall_presentBundleAlertForBundleInfo:];
-[CAMApplicationDelegate userNotificationCenter:willPresentNotification:withCompletionHandler:];
-[CAMApplicationDelegate systemMenuController];
-[CAMApplicationDelegate timelapseController];
-[CAMApplicationDelegate _internalInstall_prepareCheckedBundleVersions];
-[CAMApplicationDelegate setWindow:];
-[CAMApplicationDelegate setSubsystems:];
-[CAMApplicationDelegate captureController];
-[CAMApplicationDelegate shutterBuddySceneDelegate:receivedScene:];
-[CAMApplicationDelegate handleCaptureModeMenuAction:];
```
