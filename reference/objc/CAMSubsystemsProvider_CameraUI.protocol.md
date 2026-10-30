# `CAMSubsystemsProvider` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 15 properties, 15 instance methods, 0 class methods

## Properties

```
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
-[CAMSubsystemsProvider locationController];
-[CAMSubsystemsProvider nebulaDaemonProxyManager];
-[CAMSubsystemsProvider protectionController];
-[CAMSubsystemsProvider motionController];
-[CAMSubsystemsProvider powerController];
-[CAMSubsystemsProvider persistenceController];
-[CAMSubsystemsProvider viewfinderViewController];
-[CAMSubsystemsProvider burstController];
-[CAMSubsystemsProvider keepAliveController];
-[CAMSubsystemsProvider coverScreenManager];
-[CAMSubsystemsProvider remoteShutterController];
-[CAMSubsystemsProvider librarySelectionController];
-[CAMSubsystemsProvider cameraRollController];
-[CAMSubsystemsProvider timelapseController];
-[CAMSubsystemsProvider captureController];
```
