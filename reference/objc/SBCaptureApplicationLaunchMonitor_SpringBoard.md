# `SBCaptureApplicationLaunchMonitor`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSceneObserver`, `SBCameraViewfinderMonitorObserver`, `SBFCaptureApplicationLaunchMonitoring`
- 10 instance variables, 10 properties, 33 instance methods, 1 class methods

## Instance variables

```
@"BSAbsoluteMachTimer" _monitorTimer;
B _launchRequirementsPublished;
B _firstReadyStatusUpdateComplete;
B _sceneIsReadyForWatchdogging;
B _hasCameraCaptureButtonConfiguration;
B _isCameraInUse;
B _hasTCCAccess;
@"FBScene" _scene;
@"<SBFCaptureApplicationLaunchMonitorDelegate>" _delegate;
@"<SBCameraViewfinderMonitoring>" _viewfinderMonitoringToken;
```

## Properties

```
@property (T@"<SBCameraViewfinderMonitoring>",&,N,V_viewfinderMonitoringToken) viewfinderMonitoringToken;
@property (TB,N,V_hasCameraCaptureButtonConfiguration) hasCameraCaptureButtonConfiguration;
@property (TB,N,V_isCameraInUse) isCameraInUse;
@property (TB,N,V_hasTCCAccess) hasTCCAccess;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"FBScene",R,N,V_scene) scene;
@property (T@"<SBFCaptureApplicationLaunchMonitorDelegate>",R,W,N,V_delegate) delegate;
```

## Class methods

```
+[SBCaptureApplicationLaunchMonitor TCCServer];
```

## Instance methods

```
-[SBCaptureApplicationLaunchMonitor cameraViewfinderMonitorSessionDidBegin:auditToken:];
-[SBCaptureApplicationLaunchMonitor scene:didUpdateSettings:];
-[SBCaptureApplicationLaunchMonitor dealloc];
-[SBCaptureApplicationLaunchMonitor start];
-[SBCaptureApplicationLaunchMonitor sceneContentStateDidChange:];
-[SBCaptureApplicationLaunchMonitor sceneDidInvalidate:];
-[SBCaptureApplicationLaunchMonitor invalidate];
-[SBCaptureApplicationLaunchMonitor scene];
-[SBCaptureApplicationLaunchMonitor delegate];
-[SBCaptureApplicationLaunchMonitor cancel];
-[SBCaptureApplicationLaunchMonitor scene:didUpdateClientSettings:];
-[SBCaptureApplicationLaunchMonitor cameraViewfinderMonitorSessionWillBegin:auditToken:];
-[SBCaptureApplicationLaunchMonitor _cameraViewfinderMonitorSessionDetected:auditToken:];
-[SBCaptureApplicationLaunchMonitor _checkAllRequirementsForScene:];
-[SBCaptureApplicationLaunchMonitor _checkForButtonConfiguration:];
-[SBCaptureApplicationLaunchMonitor _checkForCameraInUseWithAuditToken:];
-[SBCaptureApplicationLaunchMonitor _checkForTCCAccess];
-[SBCaptureApplicationLaunchMonitor _hasCaptureApplicationRequirements];
-[SBCaptureApplicationLaunchMonitor _isCaptureApplicationLaunchMonitorIgnored];
-[SBCaptureApplicationLaunchMonitor _isViewfinderSessionAuditTokenMatching:];
-[SBCaptureApplicationLaunchMonitor _publishLaunchRequirementsIfNeededForScene:forced:];
-[SBCaptureApplicationLaunchMonitor _unmetReason];
-[SBCaptureApplicationLaunchMonitor _updateMonitorTimerIfNeeded];
-[SBCaptureApplicationLaunchMonitor _updateSceneReadyStatusForReason:];
-[SBCaptureApplicationLaunchMonitor hasCameraCaptureButtonConfiguration];
-[SBCaptureApplicationLaunchMonitor hasTCCAccess];
-[SBCaptureApplicationLaunchMonitor initWithScene:delegate:];
-[SBCaptureApplicationLaunchMonitor isCameraInUse];
-[SBCaptureApplicationLaunchMonitor setHasCameraCaptureButtonConfiguration:];
-[SBCaptureApplicationLaunchMonitor setHasTCCAccess:];
-[SBCaptureApplicationLaunchMonitor setIsCameraInUse:];
-[SBCaptureApplicationLaunchMonitor setViewfinderMonitoringToken:];
-[SBCaptureApplicationLaunchMonitor viewfinderMonitoringToken];
```
