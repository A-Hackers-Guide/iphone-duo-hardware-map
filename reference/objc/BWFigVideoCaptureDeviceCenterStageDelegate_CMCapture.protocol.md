# `BWFigVideoCaptureDeviceCenterStageDelegate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 7 properties, 15 instance methods, 0 class methods

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) regionOfInterestForCameraControls;
@property (T@?,N) regionOfInterestForCameraControlsChangedHandler;
@property (TB,N,GisRegionOfInterestForCameraControlsFeedbackEnabled) regionOfInterestForCameraControlsFeedbackEnabled;
@property (T{?=BBB{CGRect={CGPoint=dd}{CGSize=dd}}ifffdfff},N) cinematicFramingControls;
@property (TB,N) cinematicFramingControlsSuspended;
@property (Tq,R,N) singleFaceDetectedCumulativeTime;
@property (Tq,R,N) multipleFacesDetectedCumulativeTime;
```

## Instance methods

```
-[BWFigVideoCaptureDeviceCenterStageDelegate setRegionOfInterestForCameraControlsFeedbackEnabled:];
-[BWFigVideoCaptureDeviceCenterStageDelegate setRegionOfInterestForCameraControlsChangedHandler:];
-[BWFigVideoCaptureDeviceCenterStageDelegate cinematicFramingControlsSuspended];
-[BWFigVideoCaptureDeviceCenterStageDelegate didChangeCenterStageMetadataDeliveryEnabled:];
-[BWFigVideoCaptureDeviceCenterStageDelegate didChangeCenterStageFramingMode:];
-[BWFigVideoCaptureDeviceCenterStageDelegate setCinematicFramingControlsSuspended:];
-[BWFigVideoCaptureDeviceCenterStageDelegate setCinematicFramingControls:];
-[BWFigVideoCaptureDeviceCenterStageDelegate isRegionOfInterestForCameraControlsFeedbackEnabled];
-[BWFigVideoCaptureDeviceCenterStageDelegate cinematicFramingControls];
-[BWFigVideoCaptureDeviceCenterStageDelegate didChangeCenterStageRectOfInterest:];
-[BWFigVideoCaptureDeviceCenterStageDelegate regionOfInterestForCameraControlsChangedHandler];
-[BWFigVideoCaptureDeviceCenterStageDelegate multipleFacesDetectedCumulativeTime];
-[BWFigVideoCaptureDeviceCenterStageDelegate regionOfInterestForCameraControls];
-[BWFigVideoCaptureDeviceCenterStageDelegate singleFaceDetectedCumulativeTime];
-[BWFigVideoCaptureDeviceCenterStageDelegate restrictCenterStageFieldOfViewToWide:];
```
