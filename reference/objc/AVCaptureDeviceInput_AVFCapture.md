# `AVCaptureDeviceInput`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureInput`
- 1 instance variables, 16 properties, 91 instance methods, 2 class methods

## Instance variables

```
@"AVCaptureDeviceInputInternal" _internal;
```

## Properties

```
@property (T@"AVCaptureDevice",R,N) device;
@property (TB,N) unifiedAutoExposureDefaultsEnabled;
@property (T{?=qiIq},N) videoMinFrameDurationOverride;
@property (TB,R,N,GisLockedVideoFrameDurationSupported) lockedVideoFrameDurationSupported;
@property (T{?=qiIq},N) activeLockedVideoFrameDuration;
@property (TB,R,N,GisExternalSyncSupported) externalSyncSupported;
@property (T{?=qiIq},R,N) activeExternalSyncVideoFrameDuration;
@property (T@"AVExternalSyncDevice",R,N) externalSyncDevice;
@property (Tq,N) multichannelAudioMode;
@property (TB,R,N,GisWindNoiseRemovalSupported) windNoiseRemovalSupported;
@property (TB,N,GisWindNoiseRemovalEnabled) windNoiseRemovalEnabled;
@property (TB,R,N,GisAudioZoomSupported) audioZoomSupported;
@property (TB,N,GisAudioZoomEnabled) audioZoomEnabled;
@property (TB,R,N,GisCinematicVideoCaptureSupported) cinematicVideoCaptureSupported;
@property (TB,N,GisCinematicVideoCaptureEnabled) cinematicVideoCaptureEnabled;
@property (Tf,N) simulatedAperture;
```

## Class methods

```
+[AVCaptureDeviceInput initialize];
+[AVCaptureDeviceInput deviceInputWithDevice:error:];
```

## Instance methods

```
-[AVCaptureDeviceInput isWindNoiseRemovalSupported];
-[AVCaptureDeviceInput ports];
-[AVCaptureDeviceInput clock];
-[AVCaptureDeviceInput remoteIOOutputFormat];
-[AVCaptureDeviceInput activeLockedVideoFrameDuration];
-[AVCaptureDeviceInput reactionEffectsAllowed];
-[AVCaptureDeviceInput unifiedAutoExposureDefaultsEnabled];
-[AVCaptureDeviceInput setMultichannelAudioMode:];
-[AVCaptureDeviceInput isVisionDataDeliveryEnabled];
-[AVCaptureDeviceInput _audioCaptureModeForMultichannelAudioMode:];
-[AVCaptureDeviceInput setBuiltInMicrophoneStereoAudioCaptureEnabled:];
-[AVCaptureDeviceInput isAudioZoomSupported];
-[AVCaptureDeviceInput isMaxGainOverrideSupported];
-[AVCaptureDeviceInput _isSpatialVideoCaptureEnabledOnMFO:];
-[AVCaptureDeviceInput sensitiveContentAnalyzerEnabled];
-[AVCaptureDeviceInput _applyVideoMinFrameDurationOverride];
-[AVCaptureDeviceInput setMaxGainOverride:];
-[AVCaptureDeviceInput isCinematicVideoCaptureEnabled];
-[AVCaptureDeviceInput setBackgroundBlurAllowed:];
-[AVCaptureDeviceInput isBuiltInMicrophoneStereoAudioCaptureSupported];
-[AVCaptureDeviceInput videoDevice];
-[AVCaptureDeviceInput portsWithMediaType:sourceDeviceType:sourceDevicePosition:];
-[AVCaptureDeviceInput setAudioCaptureMode:];
-[AVCaptureDeviceInput setWindNoiseRemovalEnabled:];
-[AVCaptureDeviceInput externalSyncDevice];
-[AVCaptureDeviceInput setGenlockSignalCompensationDelay:];
-[AVCaptureDeviceInput updateSupportedProperties];
-[AVCaptureDeviceInput maxGainOverride];
-[AVCaptureDeviceInput multiCamPorts];
-[AVCaptureDeviceInput isBackgroundBlurAllowed];
-[AVCaptureDeviceInput _handleNotification:payload:];
-[AVCaptureDeviceInput portraitLightingEffectStrength];
-[AVCaptureDeviceInput videoMinFrameDurationOverride];
-[AVCaptureDeviceInput observeValueForKeyPath:ofObject:change:context:];
-[AVCaptureDeviceInput _updateLockedVideoFrameDurationSupported];
-[AVCaptureDeviceInput setBackgroundReplacementAllowed:];
-[AVCaptureDeviceInput device];
-[AVCaptureDeviceInput setUnifiedAutoExposureDefaultsEnabled:];
-[AVCaptureDeviceInput init];
-[AVCaptureDeviceInput setCenterStageAllowed:];
-[AVCaptureDeviceInput _resetPortraitLightingEffectStrength];
-[AVCaptureDeviceInput setAudioZoomEnabled:];
-[AVCaptureDeviceInput multichannelAudioMode];
-[AVCaptureDeviceInput _authorizedToUseDeviceAndRequestIfNecessary:];
-[AVCaptureDeviceInput audioCaptureMode];
-[AVCaptureDeviceInput isAudioCaptureModeSupported:];
-[AVCaptureDeviceInput detachSafelyFromFigCaptureSession:];
-[AVCaptureDeviceInput followExternalSyncDevice:videoFrameDuration:delegate:];
-[AVCaptureDeviceInput notReadyError];
-[AVCaptureDeviceInput setSensitiveContentAnalyzerXPCObject:];
-[AVCaptureDeviceInput dealloc];
-[AVCaptureDeviceInput _sourceFormatDidChange:];
-[AVCaptureDeviceInput setActiveLockedVideoFrameDuration:];
-[AVCaptureDeviceInput _bumpChangeSeedForFirstPortWithMediaType:];
-[AVCaptureDeviceInput activeExternalSyncVideoFrameDuration];
-[AVCaptureDeviceInput isCinematicVideoCaptureSupported];
-[AVCaptureDeviceInput setCinematicVideoCaptureEnabled:];
-[AVCaptureDeviceInput setSimulatedAperture:];
-[AVCaptureDeviceInput isAudioZoomEnabled];
-[AVCaptureDeviceInput isCenterStageAllowed];
-[AVCaptureDeviceInput unfollowExternalSyncDevice];
-[AVCaptureDeviceInput setStudioLightingAllowed:];
-[AVCaptureDeviceInput setSession:];
-[AVCaptureDeviceInput setRemoteIOOutputFormat:];
-[AVCaptureDeviceInput isWindNoiseRemovalEnabled];
-[AVCaptureDeviceInput handleChangedActiveFormat:forDevice:];
-[AVCaptureDeviceInput isBuiltInMicrophoneStereoAudioCaptureEnabled];
-[AVCaptureDeviceInput isCameraCalibrationDataDeliveryEnabled];
-[AVCaptureDeviceInput initWithDevice:error:];
-[AVCaptureDeviceInput isBackgroundReplacementAllowed];
-[AVCaptureDeviceInput isLockedVideoFrameDurationSupported];
-[AVCaptureDeviceInput setVideoMinFrameDurationOverride:];
-[AVCaptureDeviceInput sensitiveContentAnalyzerXPCObject];
-[AVCaptureDeviceInput description];
-[AVCaptureDeviceInput _resetSimulatedAperture];
-[AVCaptureDeviceInput _applyActiveLockedVideoFrameDuration];
-[AVCaptureDeviceInput isExternalSyncSupported];
-[AVCaptureDeviceInput setPortraitLightingEffectStrength:];
-[AVCaptureDeviceInput _resetCinematicVideoCaptureSupported];
-[AVCaptureDeviceInput isMultichannelAudioModeSupported:];
-[AVCaptureDeviceInput simulatedAperture];
-[AVCaptureDeviceInput _updateExternalSyncSupported];
-[AVCaptureDeviceInput setCameraCalibrationDataDeliveryEnabled:];
-[AVCaptureDeviceInput _resetActiveLockedVideoFrameDurationWithFormatChanged:];
-[AVCaptureDeviceInput setSensitiveContentAnalyzerEnabled:];
-[AVCaptureDeviceInput attachSafelyToFigCaptureSession:];
-[AVCaptureDeviceInput setVisionDataDeliveryEnabled:];
-[AVCaptureDeviceInput _resetVideoMinFrameDurationOverride];
-[AVCaptureDeviceInput setReactionEffectsAllowed:];
-[AVCaptureDeviceInput isStudioLightingAllowed];
-[AVCaptureDeviceInput _applyActiveExternalSyncVideoFrameDuration];
```
