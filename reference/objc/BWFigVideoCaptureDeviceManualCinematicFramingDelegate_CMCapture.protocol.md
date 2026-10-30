# `BWFigVideoCaptureDeviceManualCinematicFramingDelegate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 6 properties, 15 instance methods, 0 class methods

## Properties

```
@property (Td,N) manualFramingVideoZoomFactor;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) regionOfInterestForCameraControls;
@property (T@?,N) regionOfInterestForCameraControlsChangedHandler;
@property (TB,N,GisRegionOfInterestForCameraControlsFeedbackEnabled) regionOfInterestForCameraControlsFeedbackEnabled;
@property (T{?=BBB{CGRect={CGPoint=dd}{CGSize=dd}}ifffdfff},N) cinematicFramingControls;
@property (TB,N) cinematicFramingControlsSuspended;
```

## Instance methods

```
-[BWFigVideoCaptureDeviceManualCinematicFramingDelegate setRegionOfInterestForCameraControlsFeedbackEnabled:];
-[BWFigVideoCaptureDeviceManualCinematicFramingDelegate startPanningAtPoint:];
-[BWFigVideoCaptureDeviceManualCinematicFramingDelegate setRegionOfInterestForCameraControlsChangedHandler:];
-[BWFigVideoCaptureDeviceManualCinematicFramingDelegate cinematicFramingControlsSuspended];
-[BWFigVideoCaptureDeviceManualCinematicFramingDelegate setCinematicFramingControlsSuspended:];
-[BWFigVideoCaptureDeviceManualCinematicFramingDelegate setCinematicFramingControls:];
-[BWFigVideoCaptureDeviceManualCinematicFramingDelegate isRegionOfInterestForCameraControlsFeedbackEnabled];
-[BWFigVideoCaptureDeviceManualCinematicFramingDelegate cinematicFramingControls];
-[BWFigVideoCaptureDeviceManualCinematicFramingDelegate regionOfInterestForCameraControlsChangedHandler];
-[BWFigVideoCaptureDeviceManualCinematicFramingDelegate performOneShotFraming];
-[BWFigVideoCaptureDeviceManualCinematicFramingDelegate resetFraming];
-[BWFigVideoCaptureDeviceManualCinematicFramingDelegate panWithTranslation:];
-[BWFigVideoCaptureDeviceManualCinematicFramingDelegate regionOfInterestForCameraControls];
-[BWFigVideoCaptureDeviceManualCinematicFramingDelegate manualFramingVideoZoomFactor];
-[BWFigVideoCaptureDeviceManualCinematicFramingDelegate setManualFramingVideoZoomFactor:];
```
