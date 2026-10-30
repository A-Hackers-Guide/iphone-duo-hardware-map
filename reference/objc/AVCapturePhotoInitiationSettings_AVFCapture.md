# `AVCapturePhotoInitiationSettings`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 6 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"AVCapturePhotoInitiationSettingsInternal" _internal;
```

## Properties

```
@property (TQ,R,N) timestamp;
@property (Tq,R,N) uniqueID;
@property (Tq,N) flashMode;
@property (TB,N,GisAutoStillImageStabilizationEnabled) autoStillImageStabilizationEnabled;
@property (Tq,N) HDRMode;
@property (TB,N) burstQualityCaptureEnabled;
```

## Class methods

```
+[AVCapturePhotoInitiationSettings photoInitiationSettingsWithUserInitiatedRequestTimestamp:];
```

## Instance methods

```
-[AVCapturePhotoInitiationSettings setHDRMode:];
-[AVCapturePhotoInitiationSettings dealloc];
-[AVCapturePhotoInitiationSettings timestamp];
-[AVCapturePhotoInitiationSettings setBurstQualityCaptureEnabled:];
-[AVCapturePhotoInitiationSettings uniqueID];
-[AVCapturePhotoInitiationSettings setFlashMode:];
-[AVCapturePhotoInitiationSettings flashMode];
-[AVCapturePhotoInitiationSettings setAutoStillImageStabilizationEnabled:];
-[AVCapturePhotoInitiationSettings burstQualityCaptureEnabled];
-[AVCapturePhotoInitiationSettings isAutoStillImageStabilizationEnabled];
-[AVCapturePhotoInitiationSettings HDRMode];
-[AVCapturePhotoInitiationSettings _initWithTimestamp:];
```
