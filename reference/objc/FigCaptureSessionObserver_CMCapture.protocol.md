# `FigCaptureSessionObserver` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 10 instance methods, 0 class methods

## Properties

```
@property (Ti,R) photoThumbnailMaxDimension;
@property (TB,R) photoThumbnailQualitySpecified;
@property (Tf,R) photoThumbnailQuality;
```

## Instance methods

```
-[FigCaptureSessionObserver captureSessionDidReconfigureWhileRunning:];
-[FigCaptureSessionObserver captureSessionWillStart:];
-[FigCaptureSessionObserver captureSession:didCapturePhotoWithStatus:thumbnailData:timestamp:];
-[FigCaptureSessionObserver captureSessionDidFinishMovieRecording:];
-[FigCaptureSessionObserver captureSessionDidStop:];
-[FigCaptureSessionObserver photoThumbnailQuality];
-[FigCaptureSessionObserver photoThumbnailQualitySpecified];
-[FigCaptureSessionObserver photoThumbnailMaxDimension];
-[FigCaptureSessionObserver captureSessionDidStartMovieRecording:];
-[FigCaptureSessionObserver captureSessionDidStart:];
```
