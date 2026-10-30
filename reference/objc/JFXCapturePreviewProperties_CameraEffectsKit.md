# `JFXCapturePreviewProperties`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 12 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"PVFrameSet" _cameraFrameSet;
q _renderCameraMode;
d _displayTimestamp;
@"PVTaskToken" _signPostToken;
@"JFXCapturePreviewFrameStats" _frameStats;
@"JFXPerfTimer" _startFrameTimer;
@"NSDictionary" _selfieBGBuffers;
@"NSObject<OS_dispatch_semaphore>" _selfieBGBufferLoadSem;
{CGSize="width"d"height"d} _renderOutputSize;
{CGSize="width"d"height"d} _frameSize;
{?="value"q"timescale"i"flags"I"epoch"q} _renderTime;
```

## Properties

```
@property (T@"PVFrameSet",R,N,V_cameraFrameSet) cameraFrameSet;
@property (Tq,R,N,V_renderCameraMode) renderCameraMode;
@property (T{?=qiIq},R,N,V_renderTime) renderTime;
@property (T{CGSize=dd},R,N,V_renderOutputSize) renderOutputSize;
@property (T{CGSize=dd},R,N,V_frameSize) frameSize;
@property (Td,R,N,V_displayTimestamp) displayTimestamp;
@property (TB,R,N) renderRequiresCrop;
@property (T@"PVTaskToken",R,N,V_signPostToken) signPostToken;
@property (T@"JFXCapturePreviewFrameStats",R,N,V_frameStats) frameStats;
@property (T@"JFXPerfTimer",R,N,V_startFrameTimer) startFrameTimer;
@property (T@"NSDictionary",&,N,V_selfieBGBuffers) selfieBGBuffers;
@property (T@"NSObject<OS_dispatch_semaphore>",&,N,V_selfieBGBufferLoadSem) selfieBGBufferLoadSem;
```

## Instance methods

```
-[JFXCapturePreviewProperties frameSize];
-[JFXCapturePreviewProperties renderTime];
-[JFXCapturePreviewProperties frameStats];
-[JFXCapturePreviewProperties startFrameTimer];
-[JFXCapturePreviewProperties selfieBGBuffers];
-[JFXCapturePreviewProperties cameraFrameSet];
-[JFXCapturePreviewProperties displayTimestamp];
-[JFXCapturePreviewProperties initWithCameraFrameSet:renderCameraMode:renderTime:renderOutputSize:frameSize:];
-[JFXCapturePreviewProperties initWithCameraFrameSet:renderCameraMode:renderTime:renderOutputSize:frameSize:signPostToken:displayTimestamp:frameStats:startFrameTimer:];
-[JFXCapturePreviewProperties renderCameraMode];
-[JFXCapturePreviewProperties renderOutputSize];
-[JFXCapturePreviewProperties renderRequiresCrop];
-[JFXCapturePreviewProperties selfieBGBufferLoadSem];
-[JFXCapturePreviewProperties setSelfieBGBufferLoadSem:];
-[JFXCapturePreviewProperties setSelfieBGBuffers:];
-[JFXCapturePreviewProperties signPostToken];
```
