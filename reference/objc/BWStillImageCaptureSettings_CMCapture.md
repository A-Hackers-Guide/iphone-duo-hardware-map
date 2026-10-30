# `BWStillImageCaptureSettings`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 24 instance variables, 20 properties, 57 instance methods, 2 class methods

## Instance variables

```
q _settingsID;
i _captureType;
Q _captureFlags;
Q _sceneFlags;
B _deliverOriginalImage;
B _deliverSushiRaw;
B _deliverDeferredPhotoProxyImage;
B _downgradedDeepFusionEnhancedResolutionCapture;
Q _learnedNRStereoPhotoFrameFlag;
@"BWFrameStatisticsByPortType" _frameStatisticsByPortType;
@"NSDictionary" _streamSelectorDebugInfo;
@"BWStillImageCaptureMetadata" _metadata;
@"NSString" _primaryPortType;
@"NSArray" _captureStreamSettings;
i _timeMachineReferenceFrameBracketedCaptureSequenceNumber;
{?="value"q"timescale"i"flags"I"epoch"q} _lastTimeMachinePTS;
@"NSString" _applicationID;
q _stillImageRequestTime;
f _scaleFactor;
@"NSString" _cmioCompressedFormat;
B _cmioHighResolutionPhotoEnabled;
i _cmioFlashMode;
i _cmioQualityPrioritization;
{?="width"i"height"i} _cmioMaxPhotoDimensions;
```

## Properties

```
@property (Tq,R,N,V_settingsID) settingsID;
@property (Ti,R,N,V_captureType) captureType;
@property (TQ,R,N,V_captureFlags) captureFlags;
@property (TQ,N,V_sceneFlags) sceneFlags;
@property (TB,R,N,V_deliverOriginalImage) deliverOriginalImage;
@property (TB,R,N,V_deliverSushiRaw) deliverSushiRaw;
@property (TB,N,V_deliverDeferredPhotoProxyImage) deliverDeferredPhotoProxyImage;
@property (TB,R,N,V_downgradedDeepFusionEnhancedResolutionCapture) downgradedDeepFusionEnhancedResolutionCapture;
@property (TQ,N,V_learnedNRStereoPhotoFrameFlag) learnedNRStereoPhotoFrameFlag;
@property (T@"NSString",&,N,V_primaryPortType) primaryPortType;
@property (T@"NSArray",R,N) secondaryPortTypes;
@property (T@"NSArray",R,N) portTypes;
@property (T@"NSArray",R,N,V_captureStreamSettings) captureStreamSettings;
@property (Ti,R,N) bracketedCaptureSequenceNumberForOISLongExposure;
@property (TB,R,N) expectReferenceFrameBracketedCaptureSequenceNumber;
@property (Ti,N,V_timeMachineReferenceFrameBracketedCaptureSequenceNumber) timeMachineReferenceFrameBracketedCaptureSequenceNumber;
@property (T{?=qiIq},N,V_lastTimeMachinePTS) lastTimeMachinePTS;
@property (T@"NSString",C,N,V_applicationID) applicationID;
@property (Tq,N,V_stillImageRequestTime) stillImageRequestTime;
@property (Tf,N,V_scaleFactor) scaleFactor;
```

## Class methods

```
+[BWStillImageCaptureSettings supportsSecureCoding];
+[BWStillImageCaptureSettings initialize];
```

## Instance methods

```
-[BWStillImageCaptureSettings setApplicationID:];
-[BWStillImageCaptureSettings applicationID];
-[BWStillImageCaptureSettings deliverSushiRaw];
-[BWStillImageCaptureSettings portTypes];
-[BWStillImageCaptureSettings setLearnedNRStereoPhotoFrameFlag:];
-[BWStillImageCaptureSettings timeMachineReferenceFrameBracketedCaptureSequenceNumber];
-[BWStillImageCaptureSettings sceneFlags];
-[BWStillImageCaptureSettings setCmioFlashMode:];
-[BWStillImageCaptureSettings updateForLearnedNRMissingEVZero:missingEVMinus:];
-[BWStillImageCaptureSettings cannotProcessDeepFusionEnhancedResolution];
-[BWStillImageCaptureSettings setSceneFlags:];
-[BWStillImageCaptureSettings setScaleFactor:];
-[BWStillImageCaptureSettings secondaryPortTypes];
-[BWStillImageCaptureSettings downgradedDeepFusionEnhancedResolutionCapture];
-[BWStillImageCaptureSettings updateForFusionMissingEVMinus:missingHDRErrorRecoveryEVZero:];
-[BWStillImageCaptureSettings setCmioHighResolutionPhotoEnabled:];
-[BWStillImageCaptureSettings dealloc];
-[BWStillImageCaptureSettings captureFlags];
-[BWStillImageCaptureSettings settingsID];
-[BWStillImageCaptureSettings setCmioMaxPhotoDimensions:];
-[BWStillImageCaptureSettings setCmioQualityPrioritization:];
-[BWStillImageCaptureSettings streamSelectorDebugInfo];
-[BWStillImageCaptureSettings setTimeMachineReferenceFrameBracketedCaptureSequenceNumber:];
-[BWStillImageCaptureSettings cmioHighResolutionPhotoEnabled];
-[BWStillImageCaptureSettings metadata];
-[BWStillImageCaptureSettings cmioCompressedFormat];
-[BWStillImageCaptureSettings setDeliverDeferredPhotoProxyImage:];
-[BWStillImageCaptureSettings captureType];
-[BWStillImageCaptureSettings setCmioCompressedFormat:];
-[BWStillImageCaptureSettings captureStreamSettingsForPortType:];
-[BWStillImageCaptureSettings cmioFlashMode];
-[BWStillImageCaptureSettings learnedNRStereoPhotoFrameFlag];
-[BWStillImageCaptureSettings setLastTimeMachinePTS:];
-[BWStillImageCaptureSettings scaleFactor];
-[BWStillImageCaptureSettings encodeWithCoder:];
-[BWStillImageCaptureSettings setMetadata:];
-[BWStillImageCaptureSettings disableAWBReflow];
-[BWStillImageCaptureSettings hash];
-[BWStillImageCaptureSettings captureStreamSettings];
-[BWStillImageCaptureSettings description];
-[BWStillImageCaptureSettings cmioMaxPhotoDimensions];
-[BWStillImageCaptureSettings initWithCoder:];
-[BWStillImageCaptureSettings bracketedCaptureSequenceNumberForOISLongExposure];
-[BWStillImageCaptureSettings deliverOriginalImage];
-[BWStillImageCaptureSettings setPrimaryPortType:];
-[BWStillImageCaptureSettings cmioQualityPrioritization];
-[BWStillImageCaptureSettings expectReferenceFrameBracketedCaptureSequenceNumber];
-[BWStillImageCaptureSettings setStillImageRequestTime:];
-[BWStillImageCaptureSettings cannotProcessDepthPhotos];
-[BWStillImageCaptureSettings lastTimeMachinePTS];
-[BWStillImageCaptureSettings frameStatisticsByPortType];
-[BWStillImageCaptureSettings initWithSettingsID:captureType:captureFlags:sceneFlags:frameStatisticsByPortType:deliverOriginalImage:deliverSushiRaw:captureStreamSettings:];
-[BWStillImageCaptureSettings isEqual:];
-[BWStillImageCaptureSettings stillImageRequestTime];
-[BWStillImageCaptureSettings deliverDeferredPhotoProxyImage];
-[BWStillImageCaptureSettings primaryPortType];
-[BWStillImageCaptureSettings setStreamSelectorDebugInfo:];
```
