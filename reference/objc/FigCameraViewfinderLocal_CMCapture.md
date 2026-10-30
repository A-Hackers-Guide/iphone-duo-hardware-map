# `FigCameraViewfinderLocal`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCameraViewfinder`
- Protocols: `FigCaptureSessionObserver`
- 3 instance variables, 7 properties, 14 instance methods, 2 class methods

## Instance variables

```
B _observing;
@"NSDictionary" _options;
@"FigCameraViewfinderSessionLocal" _activeViewfinderSession;
```

## Properties

```
@property (Ti,R) photoThumbnailMaxDimension;
@property (TB,R) photoThumbnailQualitySpecified;
@property (Tf,R) photoThumbnailQuality;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FigCameraViewfinderLocal initialize];
+[FigCameraViewfinderLocal cameraViewfinder];
```

## Instance methods

```
-[FigCameraViewfinderLocal captureSessionDidReconfigureWhileRunning:];
-[FigCameraViewfinderLocal captureSessionWillStart:];
-[FigCameraViewfinderLocal init];
-[FigCameraViewfinderLocal captureSession:didCapturePhotoWithStatus:thumbnailData:timestamp:];
-[FigCameraViewfinderLocal stop];
-[FigCameraViewfinderLocal startWithOptions:];
-[FigCameraViewfinderLocal dealloc];
-[FigCameraViewfinderLocal captureSessionDidFinishMovieRecording:];
-[FigCameraViewfinderLocal captureSessionDidStop:];
-[FigCameraViewfinderLocal photoThumbnailQuality];
-[FigCameraViewfinderLocal photoThumbnailQualitySpecified];
-[FigCameraViewfinderLocal photoThumbnailMaxDimension];
-[FigCameraViewfinderLocal captureSessionDidStartMovieRecording:];
-[FigCameraViewfinderLocal captureSessionDidStart:];
```
