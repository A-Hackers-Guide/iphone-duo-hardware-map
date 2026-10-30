# `FcuSessionObserver`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FigCaptureSessionObserver`
- 1 instance variables, 8 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _anySessionsStarted;
```

## Properties

```
@property (TB,V_anySessionsStarted) anySessionsStarted;
@property (Ti,R) photoThumbnailMaxDimension;
@property (TB,R) photoThumbnailQualitySpecified;
@property (Tf,R) photoThumbnailQuality;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FcuSessionObserver captureSessionDidReconfigureWhileRunning:];
-[FcuSessionObserver captureSessionWillStart:];
-[FcuSessionObserver captureSession:didCapturePhotoWithStatus:thumbnailData:timestamp:];
-[FcuSessionObserver captureSessionDidFinishMovieRecording:];
-[FcuSessionObserver captureSessionDidStop:];
-[FcuSessionObserver photoThumbnailQuality];
-[FcuSessionObserver photoThumbnailQualitySpecified];
-[FcuSessionObserver photoThumbnailMaxDimension];
-[FcuSessionObserver captureSessionDidStartMovieRecording:];
-[FcuSessionObserver captureSessionDidStart:];
-[FcuSessionObserver anySessionsStarted];
-[FcuSessionObserver setAnySessionsStarted:];
```
