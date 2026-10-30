# `CAMPanoramaViewController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `CAMPanoramaViewDelegate`, `CAMPanoramaChangeDelegate`
- 7 instance variables, 12 properties, 27 instance methods, 0 class methods

## Instance variables

```
B _painting;
q _layoutStyle;
q _devicePosition;
@"CAMAnalyticsCaptureEvent" _analyticsCaptureEvent;
@"CUCaptureController" __captureController;
q __captureOrientation;
@"UITapGestureRecognizer" __directionChangeGestureRecognizer;
```

## Properties

```
@property (T@"CUCaptureController",R,N,V__captureController) _captureController;
@property (TB,N,GisPainting,S_setPainting:,V_painting) painting;
@property (Tq,N,S_setCaptureOrientation:,V__captureOrientation) _captureOrientation;
@property (T@"UITapGestureRecognizer",R,N,V__directionChangeGestureRecognizer) _directionChangeGestureRecognizer;
@property (T@"CAMPanoramaView",R,N) panoramaView;
@property (Tq,N,V_layoutStyle) layoutStyle;
@property (Tq,N,V_devicePosition) devicePosition;
@property (T@"CAMAnalyticsCaptureEvent",&,N,V_analyticsCaptureEvent) analyticsCaptureEvent;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMPanoramaViewController setLayoutStyle:];
-[CAMPanoramaViewController layoutStyle];
-[CAMPanoramaViewController _captureController];
-[CAMPanoramaViewController _directionChangeGestureRecognizer];
-[CAMPanoramaViewController _captureOrientation];
-[CAMPanoramaViewController panoramaView:didUpdateInstruction:];
-[CAMPanoramaViewController didChangeToCaptureOrientation:];
-[CAMPanoramaViewController startProcessingPanorama];
-[CAMPanoramaViewController stopPainting];
-[CAMPanoramaViewController panoramaViewDidRequestSynchronizedDirectionChange:toDirection:];
-[CAMPanoramaViewController _handleDirectionChange:];
-[CAMPanoramaViewController _canShowWhileLocked];
-[CAMPanoramaViewController _setPainting:];
-[CAMPanoramaViewController loadView];
-[CAMPanoramaViewController updateWithStatus:];
-[CAMPanoramaViewController devicePosition];
-[CAMPanoramaViewController panoramaView];
-[CAMPanoramaViewController setAnalyticsCaptureEvent:];
-[CAMPanoramaViewController initWithCoder:];
-[CAMPanoramaViewController finishedProcessingPanorama];
-[CAMPanoramaViewController startPainting];
-[CAMPanoramaViewController isPainting];
-[CAMPanoramaViewController setDevicePosition:];
-[CAMPanoramaViewController panoramaConfigurationDidChangeWithDirection:];
-[CAMPanoramaViewController initWithCaptureController:layoutStyle:];
-[CAMPanoramaViewController analyticsCaptureEvent];
-[CAMPanoramaViewController _setCaptureOrientation:];
```
