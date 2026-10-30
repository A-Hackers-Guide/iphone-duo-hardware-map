# `AVCaptureConnection`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 30 properties, 121 instance methods, 5 class methods

## Instance variables

```
@"AVCaptureConnectionInternal" _internal;
B _supportsVideoFieldMode;
q _videoFieldMode;
```

## Properties

```
@property (T@"NSArray",R,N) inputPorts;
@property (T@"AVCaptureOutput",R,N) output;
@property (T@"AVCaptureVideoPreviewLayer",R,N) videoPreviewLayer;
@property (TB,N,GisEnabled) enabled;
@property (TB,R,N,GisActive) active;
@property (T@"NSArray",R,N) audioChannels;
@property (TB,R,N,GisVideoMirroringSupported) supportsVideoMirroring;
@property (TB,N,GisVideoMirrored) videoMirrored;
@property (TB,N) automaticallyAdjustsVideoMirroring;
@property (Td,N) videoRotationAngle;
@property (TB,R,N,GisVideoOrientationSupported) supportsVideoOrientation;
@property (Tq,N) videoOrientation;
@property (TB,R,N,GisVideoFieldModeSupported,V_supportsVideoFieldMode) supportsVideoFieldMode;
@property (Tq,N,V_videoFieldMode) videoFieldMode;
@property (TB,R,N,GisVideoMinFrameDurationSupported) supportsVideoMinFrameDuration;
@property (T{?=qiIq},N) videoMinFrameDuration;
@property (TB,R,N,GisVideoMaxFrameDurationSupported) supportsVideoMaxFrameDuration;
@property (T{?=qiIq},N) videoMaxFrameDuration;
@property (Td,R,N) videoMaxScaleAndCropFactor;
@property (Td,N) videoScaleAndCropFactor;
@property (Tq,N) preferredVideoStabilizationMode;
@property (Tq,R,N) activeVideoStabilizationMode;
@property (TB,R,N,GisVideoStabilizationSupported) supportsVideoStabilization;
@property (TB,R,N,GisVideoStabilizationEnabled) videoStabilizationEnabled;
@property (TB,N) enablesVideoStabilizationWhenAvailable;
@property (TB,R,N,GisCameraIntrinsicMatrixDeliverySupported) cameraIntrinsicMatrixDeliverySupported;
@property (TB,N,GisCameraIntrinsicMatrixDeliveryEnabled) cameraIntrinsicMatrixDeliveryEnabled;
@property (TB,R,N,GisLowLightVideoNoiseReductionSupported) lowLightVideoNoiseReductionSupported;
@property (TB,N) automaticallyEnablesLowLightVideoNoiseReduction;
@property (TB,N,GisLowLightVideoNoiseReductionEnabled) lowLightVideoNoiseReductionEnabled;
```

## Class methods

```
+[AVCaptureConnection initialize];
+[AVCaptureConnection keyPathsForValuesAffectingVideoRotationAngle];
+[AVCaptureConnection keyPathsForValuesAffectingVideoOrientation];
+[AVCaptureConnection connectionWithInputPort:videoPreviewLayer:];
+[AVCaptureConnection connectionWithInputPorts:output:];
```

## Instance methods

```
-[AVCaptureConnection isLowLightVideoNoiseReductionEnabled];
-[AVCaptureConnection videoFieldMode];
-[AVCaptureConnection videoRotationAngle];
-[AVCaptureConnection setVideoFieldMode:];
-[AVCaptureConnection sourceDeviceInput];
-[AVCaptureConnection isVideoDeviceOrientationCorrectionSupported];
-[AVCaptureConnection isVideoGreenGhostMitigationSupported];
-[AVCaptureConnection videoRetainedBufferCountHint];
-[AVCaptureConnection isDebugMetadataSidecarFileEnabled];
-[AVCaptureConnection setVideoRotationAngle:];
-[AVCaptureConnection isVideoZoomSmoothingSupported];
-[AVCaptureConnection observeValueForKeyPath:ofObject:change:context:];
-[AVCaptureConnection setPreferredVideoStabilizationMode:];
-[AVCaptureConnection _updateLowLightVideoNoiseReductionSupported];
-[AVCaptureConnection isCameraIntrinsicMatrixDeliveryEnabled];
-[AVCaptureConnection changeSeed];
-[AVCaptureConnection setVideoGreenGhostMitigationEnabled:];
-[AVCaptureConnection setVideoMirrored:];
-[AVCaptureConnection initWithInputPorts:output:];
-[AVCaptureConnection isVideoMirroringSupported];
-[AVCaptureConnection setDebugMetadataSidecarFileEnabled:];
-[AVCaptureConnection setAutomaticallyEnablesLowLightVideoNoiseReduction:];
-[AVCaptureConnection preferredVideoStabilizationMode];
-[AVCaptureConnection _updateCameraIntrinsicMatrixDeliverySupported];
-[AVCaptureConnection _setVideoRotationAngle:];
-[AVCaptureConnection _supportsV68ThirdPartyCompatibilityRotation];
-[AVCaptureConnection isVideoDeviceOrientationCorrectionEnabled];
-[AVCaptureConnection setVideoMinFrameDuration:];
-[AVCaptureConnection isVideoRotationAngleSupported:];
-[AVCaptureConnection dealloc];
-[AVCaptureConnection setVideoRetainedBufferCountHint:];
-[AVCaptureConnection isLivePhotoMetadataWritingSupported];
-[AVCaptureConnection videoOrientation];
-[AVCaptureConnection updateAudioChannelsArray];
-[AVCaptureConnection setVideoMirroringMethodForMovieRecording:];
-[AVCaptureConnection isVideoDBGFileEnabled];
-[AVCaptureConnection _setActive:];
-[AVCaptureConnection videoMaxFrameDuration];
-[AVCaptureConnection videoMirroringMethodForMovieRecording];
-[AVCaptureConnection initWithInputPort:videoPreviewLayer:];
-[AVCaptureConnection isVideoMinFrameDurationSet];
-[AVCaptureConnection setVideoMaxFrameDuration:];
-[AVCaptureConnection _videoOrientation];
-[AVCaptureConnection isVideoGreenGhostMitigationEnabled];
-[AVCaptureConnection setCameraIntrinsicMatrixDeliveryEnabled:];
-[AVCaptureConnection _handleChangedActiveFormat:forDevice:formatMediaType:];
-[AVCaptureConnection supportedVideoMirroringMethodsForMovieRecording];
-[AVCaptureConnection bumpChangeSeed];
-[AVCaptureConnection _setVideoMinFrameDuration:];
-[AVCaptureConnection isEnabled];
-[AVCaptureConnection videoPreviewLayer];
-[AVCaptureConnection isLive];
-[AVCaptureConnection isVideoMaxFrameDurationSupported];
-[AVCaptureConnection isVideoStabilizationSupported];
-[AVCaptureConnection livePhotoMetadataWritingEnabled];
-[AVCaptureConnection _updatePropertiesForFormat:];
-[AVCaptureConnection enablesVideoStabilizationWhenAvailable];
-[AVCaptureConnection _indexOfAudioLevelChannel:];
-[AVCaptureConnection _setLowLightVideoNoiseReductionEnabled:];
-[AVCaptureConnection _videoMaxFrameDuration];
-[AVCaptureConnection isVideoZoomSmoothingEnabled];
-[AVCaptureConnection videoMinFrameDuration];
-[AVCaptureConnection _setVideoOrientation:];
-[AVCaptureConnection isCameraIntrinsicMatrixDeliverySupported];
-[AVCaptureConnection _updateMaxScaleAndCropFactorForFormat:];
-[AVCaptureConnection setEnabled:];
-[AVCaptureConnection clientRetainedBufferCount];
-[AVCaptureConnection isVideoMinFrameDurationSupported];
-[AVCaptureConnection _updateZoomSmoothingSupported];
-[AVCaptureConnection isTrulyDisabled];
-[AVCaptureConnection getPeakAudioLevelForChannel:];
-[AVCaptureConnection isLowLightVideoNoiseReductionSupported];
-[AVCaptureConnection setEnablesVideoStabilizationWhenAvailable:];
-[AVCaptureConnection setVideoZoomSmoothingEnabled:];
-[AVCaptureConnection _setVideoMirrored:];
-[AVCaptureConnection sourcesFromFrontFacingCamera];
-[AVCaptureConnection updateAudioLevelsArray];
-[AVCaptureConnection videoScaleAndCropFactor];
-[AVCaptureConnection figCaptureConnectionConfigurationForSessionPreset:allConnections:];
-[AVCaptureConnection setupInternalStorage];
-[AVCaptureConnection description];
-[AVCaptureConnection isVideoMirrored];
-[AVCaptureConnection setVideoOrientation:];
-[AVCaptureConnection getAvgAudioLevelForChannel:];
-[AVCaptureConnection _v68ThirdPartyCompatibilityVideoRotationAngle];
-[AVCaptureConnection isVideoOrientationSupported];
-[AVCaptureConnection sourcesFromExternalCamera];
-[AVCaptureConnection audioChannels];
-[AVCaptureConnection _updateActiveVideoStabilizationMode:bumpChangeSeed:];
-[AVCaptureConnection connectionID];
-[AVCaptureConnection videoMaxScaleAndCropFactor];
-[AVCaptureConnection setupObservers];
-[AVCaptureConnection setVideoScaleAndCropFactor:];
-[AVCaptureConnection isActive];
-[AVCaptureConnection output];
-[AVCaptureConnection session];
-[AVCaptureConnection setLivePhotoMetadataWritingEnabled:];
-[AVCaptureConnection _updateSupportedVideoMirroringMethodsForMovieRecording];
-[AVCaptureConnection isVideoRetainedBufferCountHintSupported];
-[AVCaptureConnection isVideoMaxFrameDurationSet];
-[AVCaptureConnection mediaType];
-[AVCaptureConnection setVideoDBGFileEnabled:];
-[AVCaptureConnection sourceDevice];
-[AVCaptureConnection inputPortFormatDescriptionChanged:];
-[AVCaptureConnection isVideoStabilizationEnabled];
-[AVCaptureConnection isVideoFieldModeSupported];
-[AVCaptureConnection setAutomaticallyAdjustsVideoMirroring:];
-[AVCaptureConnection automaticallyEnablesLowLightVideoNoiseReduction];
-[AVCaptureConnection activeVideoStabilizationMode];
-[AVCaptureConnection _setV68ThirdPartyCompatibilityVideoRotationAngle:];
-[AVCaptureConnection automaticallyAdjustsVideoMirroring];
-[AVCaptureConnection _v68ThirdPartyCompatibilityRotationMode];
-[AVCaptureConnection _videoMinFrameDuration];
-[AVCaptureConnection inputPorts];
-[AVCaptureConnection setLowLightVideoNoiseReductionEnabled:];
-[AVCaptureConnection _updateVideoGreenGhostMitigationSupported];
-[AVCaptureConnection _resolveActiveVideoStabilizationMode:format:];
-[AVCaptureConnection setVideoDeviceOrientationCorrectionEnabled:];
-[AVCaptureConnection _outputIsPreviewSizedVideoDataOutput];
-[AVCaptureConnection _additionalContentRotationDegreesForV68ThirdPartyCompatibility];
-[AVCaptureConnection teardownObservers];
```
