# `CAMSubsystems`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMSubsystemsProvider`
- 16 instance variables, 20 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _configuredFromLaunchOptions;
@"CAMViewfinderViewController" _viewfinderViewController;
@"CAMCoverScreenManager" _coverScreenManager;
@"CAMCameraRollController" _cameraRollController;
@"CUCaptureController" _captureController;
@"CAMTimelapseController" _timelapseController;
@"CAMPersistenceController" _persistenceController;
@"CAMMotionController" _motionController;
@"CAMLocationController" _locationController;
@"CAMPowerController" _powerController;
@"CAMBurstController" _burstController;
@"CAMKeepAliveController" _keepAliveController;
@"CAMProtectionController" _protectionController;
@"CAMRemoteShutterController" _remoteShutterController;
@"CAMLibrarySelectionController" _librarySelectionController;
@"CAMNebulaDaemonProxyManager" _nebulaDaemonProxyManager;
```

## Properties

```
@property (TB,R,N,GisConfiguredFromLaunchOptions,V_configuredFromLaunchOptions) configuredFromLaunchOptions;
@property (T@"CAMViewfinderViewController",R,N,V_viewfinderViewController) viewfinderViewController;
@property (T@"CAMCoverScreenManager",R,N,V_coverScreenManager) coverScreenManager;
@property (T@"CAMCameraRollController",R,N,V_cameraRollController) cameraRollController;
@property (T@"CUCaptureController",R,N,V_captureController) captureController;
@property (T@"CAMTimelapseController",R,N,V_timelapseController) timelapseController;
@property (T@"CAMPersistenceController",R,N,V_persistenceController) persistenceController;
@property (T@"CAMMotionController",R,N,V_motionController) motionController;
@property (T@"CAMLocationController",R,N,V_locationController) locationController;
@property (T@"CAMPowerController",R,N,V_powerController) powerController;
@property (T@"CAMBurstController",R,N,V_burstController) burstController;
@property (T@"CAMKeepAliveController",R,N,V_keepAliveController) keepAliveController;
@property (T@"CAMProtectionController",R,N,V_protectionController) protectionController;
@property (T@"CAMRemoteShutterController",R,N,V_remoteShutterController) remoteShutterController;
@property (T@"CAMLibrarySelectionController",R,N,V_librarySelectionController) librarySelectionController;
@property (T@"CAMNebulaDaemonProxyManager",R,N,V_nebulaDaemonProxyManager) nebulaDaemonProxyManager;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMSubsystems init];
-[CAMSubsystems locationController];
-[CAMSubsystems nebulaDaemonProxyManager];
-[CAMSubsystems protectionController];
-[CAMSubsystems motionController];
-[CAMSubsystems powerController];
-[CAMSubsystems persistenceController];
-[CAMSubsystems viewfinderViewController];
-[CAMSubsystems burstController];
-[CAMSubsystems keepAliveController];
-[CAMSubsystems coverScreenManager];
-[CAMSubsystems remoteShutterController];
-[CAMSubsystems librarySelectionController];
-[CAMSubsystems cameraRollController];
-[CAMSubsystems timelapseController];
-[CAMSubsystems captureController];
-[CAMSubsystems initWithPreferenceOverrides:];
-[CAMSubsystems isConfiguredFromLaunchOptions];
```
