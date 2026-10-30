# `CAMPanoramaProcessor`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _capturingPanorama;
@"<CAMPanoramaProcessorDelegate>" _delegate;
@"CAMPanoramaCaptureRequest" _request;
q _photoEncodingBehavior;
q _direction;
@"NSMutableDictionary" __initialMetadataByRequestUUID;
^{OpaqueFigSampleBufferProcessor=} __processor;
^{ct_green_tea_logger_s=} __greenTeaLogger;
{CGSize="width"d"height"d} _previewSize;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _referenceBounds;
```

## Properties

```
@property (TB,N,GisCapturingPanorama,S_setCapturingPanorama:,V_capturingPanorama) capturingPanorama;
@property (T@"CAMPanoramaCaptureRequest",&,N,S_setRequest:,V_request) request;
@property (T@"NSMutableDictionary",R,N,V__initialMetadataByRequestUUID) _initialMetadataByRequestUUID;
@property (T^{OpaqueFigSampleBufferProcessor=},R,N,V__processor) _processor;
@property (T^{ct_green_tea_logger_s=},R,N,V__greenTeaLogger) _greenTeaLogger;
@property (T@"<CAMPanoramaProcessorDelegate>",R,W,N,V_delegate) delegate;
@property (Tq,R,N,V_photoEncodingBehavior) photoEncodingBehavior;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_referenceBounds) referenceBounds;
@property (T{CGSize=dd},R,N,V_previewSize) previewSize;
@property (Tq,N,V_direction) direction;
```

## Instance methods

```
-[CAMPanoramaProcessor referenceBounds];
-[CAMPanoramaProcessor photoEncodingBehavior];
-[CAMPanoramaProcessor dealloc];
-[CAMPanoramaProcessor setDirection:];
-[CAMPanoramaProcessor isCapturingPanorama];
-[CAMPanoramaProcessor request];
-[CAMPanoramaProcessor startPanoramaCaptureWithRequest:];
-[CAMPanoramaProcessor direction];
-[CAMPanoramaProcessor invalidate];
-[CAMPanoramaProcessor _greenTeaLogger];
-[CAMPanoramaProcessor delegate];
-[CAMPanoramaProcessor previewSize];
-[CAMPanoramaProcessor processSampleBuffer:];
-[CAMPanoramaProcessor _initialMetadataByRequestUUID];
-[CAMPanoramaProcessor _processor];
-[CAMPanoramaProcessor _setCapturingPanorama:];
-[CAMPanoramaProcessor _setRequest:];
-[CAMPanoramaProcessor initWithDelegate:encodingBehavior:referenceBounds:];
-[CAMPanoramaProcessor processPanoramaCaptureWithRequest:completionHandler:];
-[CAMPanoramaProcessor stopPanoramaCapture];
```
