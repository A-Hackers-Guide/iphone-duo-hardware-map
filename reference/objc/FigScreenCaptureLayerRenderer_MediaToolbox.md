# `FigScreenCaptureLayerRenderer`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FigScreenCaptureFrameHandlerDelegate`
- 12 instance variables, 10 properties, 19 instance methods, 0 class methods

## Instance variables

```
q _displayID;
@"CALayer" _layer;
{CGSize="width"d"height"d} _captureSize;
{?="value"q"timescale"i"flags"I"epoch"q} _minFrameInterval;
@"FigScreenCaptureConfiguration" _captureConfiguration;
@"NSObject<OS_dispatch_queue>" _captureQueue;
@"FigScreenCaptureController" _controller;
^{OpaqueFigImageQueue=} _figImageQueue;
@"<FigScreenCaptureLayerRendererDelegate>" _delegate;
q _deliveredFrameCount;
q _droppedFrameCount;
B _applyTransform;
```

## Properties

```
@property (T@"<FigScreenCaptureLayerRendererDelegate>",W,N) delegate;
@property (T{?=qiIq},N) minFrameInterval;
@property (TB,R,N) isCapturing;
@property (TQ,R,N) deliveredFrameCount;
@property (TQ,R,N) droppedFrameCount;
@property (TB,N) applyTransform;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FigScreenCaptureLayerRenderer isCapturing];
-[FigScreenCaptureLayerRenderer stopCapture];
-[FigScreenCaptureLayerRenderer dealloc];
-[FigScreenCaptureLayerRenderer setDelegate:];
-[FigScreenCaptureLayerRenderer delegate];
-[FigScreenCaptureLayerRenderer startCapture];
-[FigScreenCaptureLayerRenderer _stopCaptureOnQueue];
-[FigScreenCaptureLayerRenderer applyTransform];
-[FigScreenCaptureLayerRenderer deliveredFrameCount];
-[FigScreenCaptureLayerRenderer droppedFrameCount];
-[FigScreenCaptureLayerRenderer initWithDisplayID:layer:captureSize:];
-[FigScreenCaptureLayerRenderer initWithLayer:captureConfiguration:];
-[FigScreenCaptureLayerRenderer minFrameInterval];
-[FigScreenCaptureLayerRenderer resumeCapture];
-[FigScreenCaptureLayerRenderer screenCaptureController:didFailWithStatus:];
-[FigScreenCaptureLayerRenderer screenCaptureController:didReceiveSampleBuffer:transformFlags:];
-[FigScreenCaptureLayerRenderer setApplyTransform:];
-[FigScreenCaptureLayerRenderer setMinFrameInterval:];
-[FigScreenCaptureLayerRenderer suspendCapture];
```
