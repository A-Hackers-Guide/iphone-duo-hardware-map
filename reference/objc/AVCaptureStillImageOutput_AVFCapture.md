# `AVCaptureStillImageOutput`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureOutput`
- 1 instance variables, 10 properties, 59 instance methods, 6 class methods

## Instance variables

```
@"AVCaptureStillImageOutputInternal" _internal;
```

## Properties

```
@property (T@"NSDictionary",C,N) outputSettings;
@property (T@"NSArray",R,N) availableImageDataCVPixelFormatTypes;
@property (T@"NSArray",R,N) availableImageDataCodecTypes;
@property (TB,R,N,GisStillImageStabilizationSupported) stillImageStabilizationSupported;
@property (TB,N) automaticallyEnablesStillImageStabilizationWhenAvailable;
@property (TB,R,N,GisStillImageStabilizationActive) stillImageStabilizationActive;
@property (TB,N,GisHighResolutionStillImageOutputEnabled) highResolutionStillImageOutputEnabled;
@property (TB,R,N,GisCameraSensorOrientationCompensationSupported) cameraSensorOrientationCompensationSupported;
@property (TB,N,GisCameraSensorOrientationCompensationEnabled) cameraSensorOrientationCompensationEnabled;
@property (TB,R,GisCapturingStillImage) capturingStillImage;
```

## Class methods

```
+[AVCaptureStillImageOutput initialize];
+[AVCaptureStillImageOutput new];
+[AVCaptureStillImageOutput _copyAttachmentsAndPropagateFaceRegionsToExifAuxDictionaryForSampleBuffer:];
+[AVCaptureStillImageOutput jpegStillImageNSDataRepresentation:];
+[AVCaptureStillImageOutput jpegStillImageNSDataRepresentationForSurface:size:metadata:];
+[AVCaptureStillImageOutput maxStillImageJPEGDataSize];
```

## Instance methods

```
-[AVCaptureStillImageOutput canAddConnection:failureReason:];
-[AVCaptureStillImageOutput outputSettings];
-[AVCaptureStillImageOutput isStillImageStabilizationSupported];
-[AVCaptureStillImageOutput handleReactionEffectsActiveChangedForDevice:];
-[AVCaptureStillImageOutput handleCenterStageActiveChangedForDevice:];
-[AVCaptureStillImageOutput isCapturingStillImage];
-[AVCaptureStillImageOutput init];
-[AVCaptureStillImageOutput safelyHandleServerConnectionDeathForFigCaptureSession:];
-[AVCaptureStillImageOutput isCameraSensorOrientationCompensationSupported];
-[AVCaptureStillImageOutput isLensStabilizationDuringBracketedCaptureSupported];
-[AVCaptureStillImageOutput detachSafelyFromFigCaptureSession:];
-[AVCaptureStillImageOutput dealloc];
-[AVCaptureStillImageOutput handleNotification:payload:];
-[AVCaptureStillImageOutput _setStillImageStabilizationAutomaticallyEnabled:];
-[AVCaptureStillImageOutput setOutputSettings:];
-[AVCaptureStillImageOutput handleChangedActiveFormat:forDevice:];
-[AVCaptureStillImageOutput shutterSound];
-[AVCaptureStillImageOutput setNoiseReductionEnabled:];
-[AVCaptureStillImageOutput handleBackgroundBlurActiveChangedForDevice:];
-[AVCaptureStillImageOutput setCameraSensorOrientationCompensationEnabled:];
-[AVCaptureStillImageOutput setShutterSound:];
-[AVCaptureStillImageOutput handleBackgroundReplacementActiveChangedForDevice:];
-[AVCaptureStillImageOutput isCameraSensorOrientationCompensationEnabled];
-[AVCaptureStillImageOutput connectionMediaTypes];
-[AVCaptureStillImageOutput removeConnection:];
-[AVCaptureStillImageOutput _updateCameraSensorOrientationCompensationSupportedForDevice:];
-[AVCaptureStillImageOutput handleStudioLightingActiveChangedForDevice:];
-[AVCaptureStillImageOutput attachSafelyToFigCaptureSession:];
-[AVCaptureStillImageOutput outputSizeForSourceFormat:];
-[AVCaptureStillImageOutput addConnection:error:];
-[AVCaptureStillImageOutput captureStillImageAsynchronouslyFromConnection:completionHandler:];
-[AVCaptureStillImageOutput isStillImageStabilizationActive];
-[AVCaptureStillImageOutput _bracketedSettingsAreValid:fromConnection:exceptionReason:];
-[AVCaptureStillImageOutput _figCaptureStillImageSettingsForBracketedCaptureSettingsArray:fromConnection:];
-[AVCaptureStillImageOutput _figCaptureStillImageSettingsForConnection:];
-[AVCaptureStillImageOutput _preparedForBracketedCaptureWithSettings:];
-[AVCaptureStillImageOutput _updateLensStabilizationDuringBracketedCaptureSupportedForDevice:];
-[AVCaptureStillImageOutput _updateMaxBracketedStillImageCaptureCountForSourceFormat:];
-[AVCaptureStillImageOutput automaticallyEnablesStillImageStabilizationWhenAvailable];
-[AVCaptureStillImageOutput availableImageDataCVPixelFormatTypes];
-[AVCaptureStillImageOutput availableImageDataCodecTypes];
-[AVCaptureStillImageOutput captureStillImageBracketAsynchronouslyFromConnection:withSettingsArray:completionHandler:];
-[AVCaptureStillImageOutput captureStillImageSurfaceAsynchronouslyFromConnection:completionHandler:];
-[AVCaptureStillImageOutput clearPreparedBracketIfNeeded];
-[AVCaptureStillImageOutput firstActiveConnection];
-[AVCaptureStillImageOutput handleNotificationForPrepareRequest:withPayload:];
-[AVCaptureStillImageOutput handleNotificationForRequest:withPayload:imageIsEV0:];
-[AVCaptureStillImageOutput imageDataFormatType];
-[AVCaptureStillImageOutput isHighResolutionStillImageOutputEnabled];
-[AVCaptureStillImageOutput isLensStabilizationDuringBracketedCaptureEnabled];
-[AVCaptureStillImageOutput isNoiseReductionEnabled];
-[AVCaptureStillImageOutput maxBracketedCaptureStillImageCount];
-[AVCaptureStillImageOutput prepareToCaptureStillImageBracketFromConnection:withSettingsArray:completionHandler:];
-[AVCaptureStillImageOutput previewImageSize];
-[AVCaptureStillImageOutput setAutomaticallyEnablesStillImageStabilizationWhenAvailable:];
-[AVCaptureStillImageOutput setHighResolutionStillImageOutputEnabled:];
-[AVCaptureStillImageOutput setLensStabilizationDuringBracketedCaptureEnabled:];
-[AVCaptureStillImageOutput setPreviewImageSize:];
-[AVCaptureStillImageOutput updateSISSupportedForSourceDevice:];
```
