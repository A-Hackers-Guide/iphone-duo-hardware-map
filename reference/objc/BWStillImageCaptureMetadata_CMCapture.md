# `BWStillImageCaptureMetadata`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 32 instance variables, 33 properties, 72 instance methods, 1 class methods

## Instance variables

```
i _snrType;
f _snr;
i _alsLuxLevel;
f _alsRearLuxLevel;
i _deviceType;
i _devicePosition;
@"NSArray" _slaveFocalLengths;
@"NSArray" _slaveLensFNumbers;
f _totalZoomFactor;
f _uiZoomFactor;
f _exifFocalLengthMultiplier;
f _exifFocalLengthOverride;
B _fastCapturePrioritizationEnabled;
B _intelligentDistortionCorrectionEnabled;
B _geometricDistortionCorrectionEnabled;
i _intelligentDistortionCorrectionVersion;
i _deepZoomVersion;
i _systemPressureLevel;
i _cameraControlsStatisticsMaster;
i _smartCamVersion;
{?="value"q"timescale"i"flags"I"epoch"q} _smartCamTimestamp;
@"NSDictionary" _smartCamInferences;
B _isPreviewSmartCamInferences;
i _semanticStyleSceneType;
i _zeroShutterLagFailureReason;
@"NSNumber" _shallowDepthOfFieldEffectSceneStatus;
@"NSDictionary" _previewWhiteBalanceMetadataByPortType;
I _streamingTime;
i _proxyProcessingError;
i _processingError;
@"NSNumber" _ignoredExposureSignals;
@"BWStillImageDuplicateInfo" _duplicateInfo;
```

## Properties

```
@property (TB,N,V_intelligentDistortionCorrectionEnabled) intelligentDistortionCorrectionEnabled;
@property (TB,N,V_geometricDistortionCorrectionEnabled) geometricDistortionCorrectionEnabled;
@property (Ti,N,V_intelligentDistortionCorrectionVersion) intelligentDistortionCorrectionVersion;
@property (Ti,N,V_deepZoomVersion) deepZoomVersion;
@property (Ti,N,V_snrType) snrType;
@property (Tf,N,V_snr) snr;
@property (Ti,N,V_alsLuxLevel) alsLuxLevel;
@property (Tf,N,V_alsRearLuxLevel) alsRearLuxLevel;
@property (Ti,N,V_deviceType) deviceType;
@property (Ti,N,V_devicePosition) devicePosition;
@property (T@"NSArray",&,N,V_slaveFocalLengths) slaveFocalLengths;
@property (T@"NSArray",&,N,V_slaveLensFNumbers) slaveLensFNumbers;
@property (Tf,N,V_totalZoomFactor) totalZoomFactor;
@property (Tf,N,V_uiZoomFactor) uiZoomFactor;
@property (Tf,N,V_exifFocalLengthMultiplier) exifFocalLengthMultiplier;
@property (Tf,N,V_exifFocalLengthOverride) exifFocalLengthOverride;
@property (TB,N,V_fastCapturePrioritizationEnabled) fastCapturePrioritizationEnabled;
@property (Ti,N,V_systemPressureLevel) systemPressureLevel;
@property (Ti,N,V_cameraControlsStatisticsMaster) cameraControlsStatisticsMaster;
@property (Ti,N,V_smartCamVersion) smartCamVersion;
@property (T{?=qiIq},N,V_smartCamTimestamp) smartCamTimestamp;
@property (T@"NSDictionary",&,N,V_smartCamInferences) smartCamInferences;
@property (TB,N,V_isPreviewSmartCamInferences) isPreviewSmartCamInferences;
@property (Ti,N,V_semanticStyleSceneType) semanticStyleSceneType;
@property (T@"NSString",R,N) semanticStyleSceneTypeAsSmartCameraSceneType;
@property (Ti,N,V_zeroShutterLagFailureReason) zeroShutterLagFailureReason;
@property (T@"NSNumber",&,N,V_shallowDepthOfFieldEffectSceneStatus) shallowDepthOfFieldEffectSceneStatus;
@property (T@"NSDictionary",&,N,V_previewWhiteBalanceMetadataByPortType) previewWhiteBalanceMetadataByPortType;
@property (TI,N,V_streamingTime) streamingTime;
@property (Ti,N,V_proxyProcessingError) proxyProcessingError;
@property (Ti,N,V_processingError) processingError;
@property (T@"NSNumber",&,N,V_ignoredExposureSignals) ignoredExposureSignals;
@property (T@"BWStillImageDuplicateInfo",&,N,V_duplicateInfo) duplicateInfo;
```

## Class methods

```
+[BWStillImageCaptureMetadata supportsSecureCoding];
```

## Instance methods

```
-[BWStillImageCaptureMetadata setSystemPressureLevel:];
-[BWStillImageCaptureMetadata setSnr:];
-[BWStillImageCaptureMetadata setDeviceType:];
-[BWStillImageCaptureMetadata setSemanticStyleSceneType:];
-[BWStillImageCaptureMetadata setIgnoredExposureSignals:];
-[BWStillImageCaptureMetadata ignoredExposureSignals];
-[BWStillImageCaptureMetadata snr];
-[BWStillImageCaptureMetadata semanticStyleSceneType];
-[BWStillImageCaptureMetadata exifFocalLengthMultiplier];
-[BWStillImageCaptureMetadata setFastCapturePrioritizationEnabled:];
-[BWStillImageCaptureMetadata fastCapturePrioritizationEnabled];
-[BWStillImageCaptureMetadata setUiZoomFactor:];
-[BWStillImageCaptureMetadata setGeometricDistortionCorrectionEnabled:];
-[BWStillImageCaptureMetadata setDeepZoomVersion:];
-[BWStillImageCaptureMetadata setIntelligentDistortionCorrectionEnabled:];
-[BWStillImageCaptureMetadata geometricDistortionCorrectionEnabled];
-[BWStillImageCaptureMetadata deepZoomVersion];
-[BWStillImageCaptureMetadata setSmartCamVersion:];
-[BWStillImageCaptureMetadata alsRearLuxLevel];
-[BWStillImageCaptureMetadata smartCamVersion];
-[BWStillImageCaptureMetadata setSnrType:];
-[BWStillImageCaptureMetadata slaveFocalLengths];
-[BWStillImageCaptureMetadata alsLuxLevel];
-[BWStillImageCaptureMetadata init];
-[BWStillImageCaptureMetadata setSlaveFocalLengths:];
-[BWStillImageCaptureMetadata totalZoomFactor];
-[BWStillImageCaptureMetadata deviceType];
-[BWStillImageCaptureMetadata exifFocalLengthOverride];
-[BWStillImageCaptureMetadata dealloc];
-[BWStillImageCaptureMetadata setIntelligentDistortionCorrectionVersion:];
-[BWStillImageCaptureMetadata cameraControlsStatisticsMaster];
-[BWStillImageCaptureMetadata setExifFocalLengthMultiplier:];
-[BWStillImageCaptureMetadata setPreviewWhiteBalanceMetadataByPortType:];
-[BWStillImageCaptureMetadata slaveLensFNumbers];
-[BWStillImageCaptureMetadata isPreviewSmartCamInferences];
-[BWStillImageCaptureMetadata setTotalZoomFactor:];
-[BWStillImageCaptureMetadata setDuplicateInfo:];
-[BWStillImageCaptureMetadata setIsPreviewSmartCamInferences:];
-[BWStillImageCaptureMetadata setStreamingTime:];
-[BWStillImageCaptureMetadata setProcessingError:];
-[BWStillImageCaptureMetadata intelligentDistortionCorrectionVersion];
-[BWStillImageCaptureMetadata duplicateInfo];
-[BWStillImageCaptureMetadata setSlaveLensFNumbers:];
-[BWStillImageCaptureMetadata setSmartCamTimestamp:];
-[BWStillImageCaptureMetadata encodeWithCoder:];
-[BWStillImageCaptureMetadata intelligentDistortionCorrectionEnabled];
-[BWStillImageCaptureMetadata setCameraControlsStatisticsMaster:];
-[BWStillImageCaptureMetadata devicePosition];
-[BWStillImageCaptureMetadata systemPressureLevel];
-[BWStillImageCaptureMetadata setZeroShutterLagFailureReason:];
-[BWStillImageCaptureMetadata hash];
-[BWStillImageCaptureMetadata snrType];
-[BWStillImageCaptureMetadata calculateSemanticStyleSceneType];
-[BWStillImageCaptureMetadata setAlsRearLuxLevel:];
-[BWStillImageCaptureMetadata setShallowDepthOfFieldEffectSceneStatus:];
-[BWStillImageCaptureMetadata setSmartCamInferences:];
-[BWStillImageCaptureMetadata smartCamInferences];
-[BWStillImageCaptureMetadata proxyProcessingError];
-[BWStillImageCaptureMetadata initWithCoder:];
-[BWStillImageCaptureMetadata streamingTime];
-[BWStillImageCaptureMetadata smartCamTimestamp];
-[BWStillImageCaptureMetadata zeroShutterLagFailureReason];
-[BWStillImageCaptureMetadata setAlsLuxLevel:];
-[BWStillImageCaptureMetadata processingError];
-[BWStillImageCaptureMetadata semanticStyleSceneTypeAsSmartCameraSceneType];
-[BWStillImageCaptureMetadata isEqual:];
-[BWStillImageCaptureMetadata shallowDepthOfFieldEffectSceneStatus];
-[BWStillImageCaptureMetadata previewWhiteBalanceMetadataByPortType];
-[BWStillImageCaptureMetadata setProxyProcessingError:];
-[BWStillImageCaptureMetadata setDevicePosition:];
-[BWStillImageCaptureMetadata setExifFocalLengthOverride:];
-[BWStillImageCaptureMetadata uiZoomFactor];
```
