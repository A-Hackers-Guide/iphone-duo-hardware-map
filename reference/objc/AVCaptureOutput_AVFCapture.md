# `AVCaptureOutput`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 3 properties, 54 instance methods, 6 class methods

## Instance variables

```
@"AVCaptureOutputInternal" _outputInternal;
```

## Properties

```
@property (T@"NSArray",R,N) connections;
@property (TB,R,N,GisDeferredStartSupported) deferredStartSupported;
@property (TB,N,GisDeferredStartEnabled) deferredStartEnabled;
```

## Class methods

```
+[AVCaptureOutput initialize];
+[AVCaptureOutput allOutputSubclasses];
+[AVCaptureOutput availableVideoCodecTypesForSourceDevice:sourceFormat:outputDimensions:fileType:videoCodecTypesAllowList:];
+[AVCaptureOutput dataDroppedReasonFromSampleBuffer:];
+[AVCaptureOutput supportedProResCodecTypes];
+[AVCaptureOutput supportedProResRawCodecTypes];
```

## Instance methods

```
-[AVCaptureOutput canAddConnection:failureReason:];
-[AVCaptureOutput handleReactionEffectsActiveChangedForDevice:];
-[AVCaptureOutput rectForMetadataOutputRectOfInterest:];
-[AVCaptureOutput appliesOrientationWithPhysicalRotationForConnection:];
-[AVCaptureOutput handleCenterStageActiveChangedForDevice:];
-[AVCaptureOutput changeSeed];
-[AVCaptureOutput connections];
-[AVCaptureOutput safelyHandleServerConnectionDeathForFigCaptureSession:];
-[AVCaptureOutput appliesMirroringWithPhysicalFlipForConnection:];
-[AVCaptureOutput detachSafelyFromFigCaptureSession:];
-[AVCaptureOutput dealloc];
-[AVCaptureOutput metadataOutputRectOfInterestForRect:];
-[AVCaptureOutput isDeferredStartEnabled];
-[AVCaptureOutput updateVideoSettingsForConnection:];
-[AVCaptureOutput bumpChangeSeed];
-[AVCaptureOutput setSession:];
-[AVCaptureOutput requiredOutputFormatForConnection:];
-[AVCaptureOutput connectionWithMediaType:];
-[AVCaptureOutput handleChangedActiveFormat:forDevice:];
-[AVCaptureOutput detachFromFigCaptureSession:];
-[AVCaptureOutput handleBackgroundBlurActiveChangedForDevice:];
-[AVCaptureOutput handleBackgroundReplacementActiveChangedForDevice:];
-[AVCaptureOutput connectionMediaTypes];
-[AVCaptureOutput attachToFigCaptureSession:];
-[AVCaptureOutput removeConnection:];
-[AVCaptureOutput setSinkID:];
-[AVCaptureOutput performFigCaptureSessionOperationSafelyUsingBlock:];
-[AVCaptureOutput session];
-[AVCaptureOutput handlePreviewSizedOutputBuffersDidChangeForVideoDataOutput:];
-[AVCaptureOutput hasRequiredOutputFormatForConnection:];
-[AVCaptureOutput handleStudioLightingActiveChangedForDevice:];
-[AVCaptureOutput setDeferredStartEnabled:];
-[AVCaptureOutput isDeferredStartSupported];
-[AVCaptureOutput attachSafelyToFigCaptureSession:];
-[AVCaptureOutput sinkID];
-[AVCaptureOutput outputSizeForSourceFormat:];
-[AVCaptureOutput addConnection:error:];
-[AVCaptureOutput _invokeClientCompositingCallbackForSettingsID:compositingData:];
-[AVCaptureOutput liveConnections];
-[AVCaptureOutput _inputForConnection:];
-[AVCaptureOutput _recommendedAudioOutputSettingsForConnection:sourceSettings:fileType:spatialAudioChannelLayoutTag:];
-[AVCaptureOutput _recommendedVideoOutputSettingsForConnection:sourceSettings:videoCodec:isIris:outputFileURL:];
-[AVCaptureOutput firstEnabledConnectionForMediaType:];
-[AVCaptureOutput getTransform:mirroredOut:rollAdjustmentOut:forConnection:];
-[AVCaptureOutput handleChangedDynamicAspectRatio:forFormat:];
-[AVCaptureOutput handleServerConnectionDeathForFigCaptureSession:];
-[AVCaptureOutput handleVideoStabilizationModeChangedForConnection:];
-[AVCaptureOutput handleVideoStabilizationStrengthChangedForDevice:];
-[AVCaptureOutput initSubclass];
-[AVCaptureOutput performBlockOnSessionNotifyingThread:];
-[AVCaptureOutput recommendedCinematicAudioOutputSettingsForConnection:fileType:isProResCapture:];
-[AVCaptureOutput recommendedOutputSettingsForConnection:sourceSettings:videoCodecType:fileType:isIris:outputFileURL:spatialAudioChannelLayoutTag:];
-[AVCaptureOutput transformedMetadataObjectForMetadataObject:connection:];
-[AVCaptureOutput updateMetadataTransformForSourceFormat:aspectRatio:];
```
