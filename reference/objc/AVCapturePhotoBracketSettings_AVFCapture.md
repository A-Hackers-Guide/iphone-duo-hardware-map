# `AVCapturePhotoBracketSettings`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCapturePhotoSettings`
- 1 instance variables, 2 properties, 19 instance methods, 3 class methods

## Instance variables

```
@"AVCapturePhotoBracketSettingsInternal" _bracketSettingsInternal;
```

## Properties

```
@property (T@"NSArray",R,N) bracketedSettings;
@property (TB,N,GisLensStabilizationEnabled) lensStabilizationEnabled;
```

## Class methods

```
+[AVCapturePhotoBracketSettings initialize];
+[AVCapturePhotoBracketSettings photoBracketSettingsWithRawPixelFormatType:processedFormat:bracketedSettings:];
+[AVCapturePhotoBracketSettings photoBracketSettingsWithRawPixelFormatType:rawFileType:processedFormat:processedFileType:bracketedSettings:];
```

## Instance methods

```
-[AVCapturePhotoBracketSettings bracketedSettings];
-[AVCapturePhotoBracketSettings debugDescription];
-[AVCapturePhotoBracketSettings setHDRMode:];
-[AVCapturePhotoBracketSettings setAutoDualCameraFusionEnabled:];
-[AVCapturePhotoBracketSettings dealloc];
-[AVCapturePhotoBracketSettings setLensStabilizationEnabled:];
-[AVCapturePhotoBracketSettings setLivePhotoMovieFileURL:];
-[AVCapturePhotoBracketSettings setLivePhotoMovieFileURLForOriginalPhoto:];
-[AVCapturePhotoBracketSettings _initWithFormat:processedFileType:rawPixelFormatType:rawFileType:bracketedSettings:uniqueID:exceptionReason:];
-[AVCapturePhotoBracketSettings setFlashMode:];
-[AVCapturePhotoBracketSettings setEV0PhotoDeliveryEnabled:];
-[AVCapturePhotoBracketSettings setAutoRedEyeReductionEnabled:];
-[AVCapturePhotoBracketSettings description];
-[AVCapturePhotoBracketSettings setLivePhotoMovieMetadata:];
-[AVCapturePhotoBracketSettings setAutoStillImageStabilizationEnabled:];
-[AVCapturePhotoBracketSettings isLensStabilizationEnabled];
-[AVCapturePhotoBracketSettings copyWithZone:];
-[AVCapturePhotoBracketSettings setAutoVirtualDeviceFusionEnabled:];
-[AVCapturePhotoBracketSettings setLivePhotoMovieMetadataForOriginalPhoto:];
```
