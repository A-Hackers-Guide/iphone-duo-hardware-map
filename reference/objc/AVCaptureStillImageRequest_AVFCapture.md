# `AVCaptureStillImageRequest`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 13 instance methods, 1 class methods

## Instance variables

```
@? _sbufCompletionBlock;
@? _iosurfaceCompletionBlock;
@? _bracketedCaptureCompletionBlock;
q _settingsID;
I _shutterSoundID;
@"AVCaptureBracketedStillImageSettings" _bracketedSettings;
```

## Properties

```
@property (T@?,C,V_sbufCompletionBlock) sbufCompletionBlock;
@property (T@?,C,V_iosurfaceCompletionBlock) iosurfaceCompletionBlock;
@property (T@?,C,V_bracketedCaptureCompletionBlock) bracketedCaptureCompletionBlock;
@property (Tq,V_settingsID) settingsID;
@property (TI,V_shutterSoundID) shutterSoundID;
@property (T@"AVCaptureBracketedStillImageSettings",&,V_bracketedSettings) bracketedSettings;
```

## Class methods

```
+[AVCaptureStillImageRequest request];
```

## Instance methods

```
-[AVCaptureStillImageRequest bracketedSettings];
-[AVCaptureStillImageRequest dealloc];
-[AVCaptureStillImageRequest settingsID];
-[AVCaptureStillImageRequest setSettingsID:];
-[AVCaptureStillImageRequest bracketedCaptureCompletionBlock];
-[AVCaptureStillImageRequest iosurfaceCompletionBlock];
-[AVCaptureStillImageRequest sbufCompletionBlock];
-[AVCaptureStillImageRequest setBracketedCaptureCompletionBlock:];
-[AVCaptureStillImageRequest setBracketedSettings:];
-[AVCaptureStillImageRequest setIosurfaceCompletionBlock:];
-[AVCaptureStillImageRequest setSbufCompletionBlock:];
-[AVCaptureStillImageRequest setShutterSoundID:];
-[AVCaptureStillImageRequest shutterSoundID];
```
