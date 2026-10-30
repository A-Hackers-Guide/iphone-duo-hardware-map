# `AVCaptureVideoDataOutput`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureOutput`
- Protocols: `AVCaptureDataOutputDelegateOverride`
- 1 instance variables, 18 properties, 76 instance methods, 2 class methods

## Instance variables

```
@"AVCaptureVideoDataOutputInternal" _internal;
```

## Properties

```
@property (T@"<AVCaptureVideoDataOutputSampleBufferDelegate>",R,N) sampleBufferDelegate;
@property (T@"NSObject<OS_dispatch_queue>",R,N) sampleBufferCallbackQueue;
@property (T@"NSDictionary",C,N) videoSettings;
@property (Ti,R,N) recommendedMediaTimeScaleForAssetWriter;
@property (T@"NSArray",R,N) availableVideoCVPixelFormatTypes;
@property (T@"NSArray",R,N) availableVideoCodecTypes;
@property (T{?=qiIq},N) minFrameDuration;
@property (TB,N) alwaysDiscardsLateVideoFrames;
@property (TB,N) automaticallyConfiguresOutputBufferDimensions;
@property (TB,N) deliversPreviewSizedOutputBuffers;
@property (TB) preparesCellularRadioForNetworkConnection;
@property (TB) preservesDynamicHDRMetadata;
@property (T@,R,N) delegateOverride;
@property (T@"NSObject<OS_dispatch_queue>",R,N) delegateOverrideCallbackQueue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AVCaptureVideoDataOutput initialize];
+[AVCaptureVideoDataOutput new];
```

## Instance methods

```
-[AVCaptureVideoDataOutput isSceneStabilityMetadataEnabled];
-[AVCaptureVideoDataOutput isSceneStabilityMetadataSupported];
-[AVCaptureVideoDataOutput videoSettings];
-[AVCaptureVideoDataOutput canAddConnection:failureReason:];
-[AVCaptureVideoDataOutput _handleNotification:payload:];
-[AVCaptureVideoDataOutput preservesDynamicHDRMetadata];
-[AVCaptureVideoDataOutput observeValueForKeyPath:ofObject:change:context:];
-[AVCaptureVideoDataOutput _processSampleBuffer:];
-[AVCaptureVideoDataOutput setSampleBufferDelegate:queue:];
-[AVCaptureVideoDataOutput isVideoSettingsAspectRatioOverrideEnabled];
-[AVCaptureVideoDataOutput appliesOrientationWithPhysicalRotationForConnection:];
-[AVCaptureVideoDataOutput setPreparesCellularRadioForNetworkConnection:];
-[AVCaptureVideoDataOutput minFrameDuration];
-[AVCaptureVideoDataOutput _updateAvailableVideoCVPixelFormatTypesForConnection:];
-[AVCaptureVideoDataOutput init];
-[AVCaptureVideoDataOutput _handleLocalQueueMessage:];
-[AVCaptureVideoDataOutput appliesMirroringWithPhysicalFlipForConnection:];
-[AVCaptureVideoDataOutput setPreservesDynamicHDRMetadata:];
-[AVCaptureVideoDataOutput sampleBufferDelegate];
-[AVCaptureVideoDataOutput requestedBufferAttachments];
-[AVCaptureVideoDataOutput setMinFrameDuration:];
-[AVCaptureVideoDataOutput detachSafelyFromFigCaptureSession:];
-[AVCaptureVideoDataOutput dealloc];
-[AVCaptureVideoDataOutput isVideoSettingsDimensionsOverrideEnabled];
-[AVCaptureVideoDataOutput outputScalingModeForSourceFormat:];
-[AVCaptureVideoDataOutput setSceneStabilityMetadataEnabled:];
-[AVCaptureVideoDataOutput availableVideoCodecTypes];
-[AVCaptureVideoDataOutput recommendedVideoSettingsForAssetWriterWithOutputFileType:];
-[AVCaptureVideoDataOutput recommendedVideoSettingsForVideoCodecType:assetWriterOutputFileType:outputFileURL:];
-[AVCaptureVideoDataOutput _updateRemoteQueue:];
-[AVCaptureVideoDataOutput updateVideoSettingsForConnection:];
-[AVCaptureVideoDataOutput allLossyVideoCVPixelFormatTypesEnabled];
-[AVCaptureVideoDataOutput setPanoRecordingInProgress:];
-[AVCaptureVideoDataOutput _updateDeliversPreviewSizedOutputBuffersForConnection:sessionPreset:];
-[AVCaptureVideoDataOutput recommendedMediaTimeScaleForAssetWriter];
-[AVCaptureVideoDataOutput requiredOutputFormatForConnection:];
-[AVCaptureVideoDataOutput availableVideoCVPixelFormatTypes];
-[AVCaptureVideoDataOutput getTransformedDetectedObjectsInfoFromSampleBuffer:connection:];
-[AVCaptureVideoDataOutput handleChangedActiveFormat:forDevice:];
-[AVCaptureVideoDataOutput isVideoSettingsAspectRatioOverrideSupported];
-[AVCaptureVideoDataOutput setAlwaysDiscardsLateVideoFrames:];
-[AVCaptureVideoDataOutput setVideoSettingsAspectRatioOverrideEnabled:];
-[AVCaptureVideoDataOutput setVideoSettingsDimensionsOverrideEnabled:];
-[AVCaptureVideoDataOutput sampleBufferCallbackQueue];
-[AVCaptureVideoDataOutput automaticallyConfiguresOutputBufferDimensions];
-[AVCaptureVideoDataOutput preparesCellularRadioForNetworkConnection];
-[AVCaptureVideoDataOutput supportedAssetWriterOutputFileTypes];
-[AVCaptureVideoDataOutput setDeliversPreviewSizedOutputBuffers:];
-[AVCaptureVideoDataOutput fullyPopulatedVideoSettingsForSettingsDictionary:connection:];
-[AVCaptureVideoDataOutput recommendedMovieMetadataForVideoCodecType:assetWriterOutputFileType:];
-[AVCaptureVideoDataOutput _handleRemoteQueueOperation:];
-[AVCaptureVideoDataOutput connectionMediaTypes];
-[AVCaptureVideoDataOutput _updateVideoSettingsForConnection:connectionBeingAdded:];
-[AVCaptureVideoDataOutput deliversPreviewSizedOutputBuffers];
-[AVCaptureVideoDataOutput removeConnection:];
-[AVCaptureVideoDataOutput _updateLocalQueue:];
-[AVCaptureVideoDataOutput setAllLossyVideoCVPixelFormatTypesEnabled:];
-[AVCaptureVideoDataOutput hasRequiredOutputFormatForConnection:];
-[AVCaptureVideoDataOutput setVideoSettings:];
-[AVCaptureVideoDataOutput setRequestedBufferAttachments:];
-[AVCaptureVideoDataOutput alwaysDiscardsLateVideoFrames];
-[AVCaptureVideoDataOutput delegateOverrideCallbackQueue];
-[AVCaptureVideoDataOutput vettedVideoSettingsForSettingsDictionary:connection:];
-[AVCaptureVideoDataOutput attachSafelyToFigCaptureSession:];
-[AVCaptureVideoDataOutput availableVideoCodecTypesForAssetWriterWithOutputFileType:];
-[AVCaptureVideoDataOutput updateClientVideoSettingsForAspectRatio:];
-[AVCaptureVideoDataOutput setAutomaticallyConfiguresOutputBufferDimensions:];
-[AVCaptureVideoDataOutput outputSizeForSourceFormat:];
-[AVCaptureVideoDataOutput isVideoSettingsAspectRatioOverrideOptimized];
-[AVCaptureVideoDataOutput setDelegateOverride:delegateOverrideCallbackQueue:];
-[AVCaptureVideoDataOutput supportedVideoSettingsKeys];
-[AVCaptureVideoDataOutput _setMinFrameDuration:];
-[AVCaptureVideoDataOutput recommendedVideoSettingsForVideoCodecType:assetWriterOutputFileType:];
-[AVCaptureVideoDataOutput isPanoRecordingInProgress];
-[AVCaptureVideoDataOutput addConnection:error:];
-[AVCaptureVideoDataOutput delegateOverride];
```
