# `_TtC8CameraUI20CAMDockKitController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_TtP11DockKitCore32XPCTrackingSummaryClientProtocol_`, `_TtP11DockKitCore28XPCSystemEventClientProtocol_`
- 11 instance variables, 0 properties, 17 instance methods, 0 class methods

## Instance variables

```
DockKitCore.DockCoreManager manager;
DockKitCore.DKPanoramaController panoController;
DockKitCore.TrackingStand ? accessory;
os.Logger logger;
DockKitCore.ConnectedState connectedState;
DockKitCore.TrackingButtonState trackingState;
__C.CAMCaptureMode captureMode;
DockKitCore.TrackingSummaryInternal ? lastTrackingSummary;
Foundation.Date trackingSummaryResetTime;
_$sSo19CAMMotionControllerCSgXw motionController;
(objc_protocol 0x1bed26d30) ? cameraControllerDelegate;
```

## Instance methods

```
-[_TtC8CameraUI20CAMDockKitController init];
-[_TtC8CameraUI20CAMDockKitController setDelegate:];
-[_TtC8CameraUI20CAMDockKitController captureModeDidChange:];
-[_TtC8CameraUI20CAMDockKitController disconnectedWithErr:];
-[_TtC8CameraUI20CAMDockKitController initWithMotionController:];
-[_TtC8CameraUI20CAMDockKitController isConnectedAndTracking];
-[_TtC8CameraUI20CAMDockKitController isTrackingLocked];
-[_TtC8CameraUI20CAMDockKitController matchingTrackedSubjectForAnstID:];
-[_TtC8CameraUI20CAMDockKitController panoramaCaptureDidStart:];
-[_TtC8CameraUI20CAMDockKitController panoramaCaptureDidStop:];
-[_TtC8CameraUI20CAMDockKitController panoramaDriftingY:];
-[_TtC8CameraUI20CAMDockKitController panoramaPaintingUpdatedWithCurrentSpeed:maxAllowedSpeed:];
-[_TtC8CameraUI20CAMDockKitController shouldShowTrackingSummaryViews];
-[_TtC8CameraUI20CAMDockKitController systemEventDataWithInfo:data:];
-[_TtC8CameraUI20CAMDockKitController tapToTrackTriggeredAtPoint:devicePosition:];
-[_TtC8CameraUI20CAMDockKitController trackingSummaryDataDebugWithInfo:data:];
-[_TtC8CameraUI20CAMDockKitController trackingSummaryDataWithInfo:data:];
```
