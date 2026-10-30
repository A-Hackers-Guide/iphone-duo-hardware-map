# `CAMStillImageCaptureRequest`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMCaptureRequest`
- Protocols: `CAMCaptureAdjustmentProvider`, `CAMBurstIdentifierProvider`, `NSCopying`, `NSMutableCopying`, `CAMBurstRequest`, `CAMIrisRequest`, `CAMTimelapseRequest`
- 52 instance variables, 57 properties, 71 instance methods, 1 class methods

## Instance variables

```
@"NSString" _timelapseIdentifier;
@"NSString" _EV0PersistenceUUID;
q _effectFilterType;
q _lightingEffectType;
q _aspectRatioCrop;
Q _maximumBurstLength;
q _flashMode;
q _hdrMode;
q _irisMode;
q _ctmCaptureType;
B _wantsDepthData;
@"NSArray" _adjustmentFilters;
@"NSArray" _originalFilters;
q _photoQualityPrioritization;
B _wantsAutoDualCameraFusion;
B _wantsSemanticSceneFilter;
B _wantsAudioForCapture;
B _wantsShutterSoundSuppression;
I _customShutterSoundID;
B _wantsSquareCrop;
q _nightMode;
@"CAMSemanticStyle" _semanticStyle;
d _destructiveAspectRatioCrop;
B _needsFlipOverride;
B _wantsHighResolutionStills;
B _stillDuringVideo;
@"NSString" _visualIntelligenceAnalysisIdentifier;
d _visualIntelligenceStillUprightDegrees;
@"NSString" _textAnalysisIdentifier;
@"CAMTextRegionResult" _textAnalysisRegion;
{CGSize="width"d"height"d} _desiredPreviewSize;
@"NSString" _burstIdentifier;
@"NSString" _irisIdentifier;
@"NSURL" _localVideoDestinationURL;
@"NSURL" _localCTMVideoDestinationURL;
B _disablesCameraSwitchingDuringRecording;
q _torchMode;
@"NSString" _videoPersistenceUUID;
B _wantsEV0ForHDR;
@"NSString" _EV0IrisIdentifier;
@"NSURL" _EV0LocalVideoDestinationURL;
@"NSString" _EV0VideoPersistenceUUID;
Q _userInitiationTime;
q _maximumPhotoResolution;
B _wantsWhiteBalanceLockedDuringVideoRecording;
q _stereoCaptureStatus;
B _frontRearSimultaneousCaptureEnabled;
B _frontRearSimultaneousCaptureMirrored;
B _textDetectionOverridesOrientation;
B _personalPhotographerSessionEnabled;
@"NSString" _personalPhotographerSessionIdentifier;
@"<CAMStillImageCaptureRequestDelegate>" _delegate;
```

## Properties

```
@property (T@"NSString",R,C,N,V_timelapseIdentifier) timelapseIdentifier;
@property (T@"NSString",R,C,N,V_EV0PersistenceUUID) EV0PersistenceUUID;
@property (Tq,R,N,V_effectFilterType) effectFilterType;
@property (Tq,R,N,V_lightingEffectType) lightingEffectType;
@property (Tq,R,N,V_aspectRatioCrop) aspectRatioCrop;
@property (TQ,R,N,V_maximumBurstLength) maximumBurstLength;
@property (Tq,R,N,V_flashMode) flashMode;
@property (Tq,R,N,V_hdrMode) hdrMode;
@property (Tq,R,N,V_irisMode) irisMode;
@property (TB,R,N,V_wantsDepthData) wantsDepthData;
@property (T@"NSArray",R,N,V_adjustmentFilters) adjustmentFilters;
@property (T@"NSArray",R,N,V_originalFilters) originalFilters;
@property (Tq,R,N,V_photoQualityPrioritization) photoQualityPrioritization;
@property (TB,R,N,V_wantsAutoDualCameraFusion) wantsAutoDualCameraFusion;
@property (TB,R,N,V_wantsSemanticSceneFilter) wantsSemanticSceneFilter;
@property (TB,R,N,V_wantsAudioForCapture) wantsAudioForCapture;
@property (TB,N,V_wantsShutterSoundSuppression) wantsShutterSoundSuppression;
@property (TI,R,N,V_customShutterSoundID) customShutterSoundID;
@property (TB,R,N,V_wantsSquareCrop) wantsSquareCrop;
@property (Td,R,N,V_destructiveAspectRatioCrop) destructiveAspectRatioCrop;
@property (TB,R,N,V_needsFlipOverride) needsFlipOverride;
@property (TB,R,N,V_wantsHighResolutionStills) wantsHighResolutionStills;
@property (TB,R,N,V_stillDuringVideo) stillDuringVideo;
@property (Tq,R,N,V_ctmCaptureType) ctmCaptureType;
@property (TB,R,N,GisCTMVideo) CTMVideo;
@property (Tq,R,N,V_nightMode) nightMode;
@property (T@"CAMSemanticStyle",R,N,V_semanticStyle) semanticStyle;
@property (T{CGSize=dd},R,N,V_desiredPreviewSize) desiredPreviewSize;
@property (T@"NSString",R,C,N,V_burstIdentifier) burstIdentifier;
@property (T@"NSString",R,C,N,V_irisIdentifier) irisIdentifier;
@property (T@"NSString",R,C,N,V_visualIntelligenceAnalysisIdentifier) visualIntelligenceAnalysisIdentifier;
@property (Td,R,N,V_visualIntelligenceStillUprightDegrees) visualIntelligenceStillUprightDegrees;
@property (T@"NSString",R,C,N,V_textAnalysisIdentifier) textAnalysisIdentifier;
@property (T@"CAMTextRegionResult",R,C,N,V_textAnalysisRegion) textAnalysisRegion;
@property (T@"NSURL",R,C,N,V_localVideoDestinationURL) localVideoDestinationURL;
@property (T@"NSURL",R,C,N,V_localCTMVideoDestinationURL) localCTMVideoDestinationURL;
@property (TB,R,N,V_disablesCameraSwitchingDuringRecording) disablesCameraSwitchingDuringRecording;
@property (Tq,R,N,V_torchMode) torchMode;
@property (T@"NSString",R,C,N,V_videoPersistenceUUID) videoPersistenceUUID;
@property (TB,R,N,V_wantsEV0ForHDR) wantsEV0ForHDR;
@property (T@"NSString",R,C,N,V_EV0IrisIdentifier) EV0IrisIdentifier;
@property (T@"NSURL",R,C,N,V_EV0LocalVideoDestinationURL) EV0LocalVideoDestinationURL;
@property (T@"NSString",R,C,N,V_EV0VideoPersistenceUUID) EV0VideoPersistenceUUID;
@property (TQ,R,N,V_userInitiationTime) userInitiationTime;
@property (T@"<CAMStillImageCaptureRequestDelegate>",R,W,N,V_delegate) delegate;
@property (Tq,R,N,V_maximumPhotoResolution) maximumPhotoResolution;
@property (TB,R,N,V_wantsWhiteBalanceLockedDuringVideoRecording) wantsWhiteBalanceLockedDuringVideoRecording;
@property (Tq,R,N,V_stereoCaptureStatus) stereoCaptureStatus;
@property (TB,R,N,GisFrontRearSimultaneousCaptureEnabled,V_frontRearSimultaneousCaptureEnabled) frontRearSimultaneousCaptureEnabled;
@property (TB,R,N,GisFrontRearSimultaneousCaptureMirrored,V_frontRearSimultaneousCaptureMirrored) frontRearSimultaneousCaptureMirrored;
@property (TB,R,N,V_textDetectionOverridesOrientation) textDetectionOverridesOrientation;
@property (TB,R,N,GisPersonalPhotographerSessionEnabled,V_personalPhotographerSessionEnabled) personalPhotographerSessionEnabled;
@property (T@"NSString",R,C,N,V_personalPhotographerSessionIdentifier) personalPhotographerSessionIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAMStillImageCaptureRequest rawPixelFormatTypeForPhotoOutput:];
```

## Instance methods

```
-[CAMStillImageCaptureRequest wantsSquareCrop];
-[CAMStillImageCaptureRequest EV0IrisIdentifier];
-[CAMStillImageCaptureRequest stereoCaptureStatus];
-[CAMStillImageCaptureRequest hdrMode];
-[CAMStillImageCaptureRequest userInitiationTime];
-[CAMStillImageCaptureRequest textAnalysisRegion];
-[CAMStillImageCaptureRequest irisLocalVideoDestinationURLForEV0:];
-[CAMStillImageCaptureRequest timelapseIdentifier];
-[CAMStillImageCaptureRequest adjustmentFilters];
-[CAMStillImageCaptureRequest lightingEffectType];
-[CAMStillImageCaptureRequest originalFilters];
-[CAMStillImageCaptureRequest shouldProtectPersistenceForVideo];
-[CAMStillImageCaptureRequest wantsDepthData];
-[CAMStillImageCaptureRequest customShutterSoundID];
-[CAMStillImageCaptureRequest stillDuringVideo];
-[CAMStillImageCaptureRequest photoQualityPrioritization];
-[CAMStillImageCaptureRequest EV0PersistenceUUID];
-[CAMStillImageCaptureRequest maximumPhotoResolution];
-[CAMStillImageCaptureRequest videoPersistenceUUID];
-[CAMStillImageCaptureRequest irisIdentifier];
-[CAMStillImageCaptureRequest wantsAutoDualCameraFusion];
-[CAMStillImageCaptureRequest localCTMVideoDestinationURL];
-[CAMStillImageCaptureRequest capturePhotoSettingsWithContext:];
-[CAMStillImageCaptureRequest wantsAudioForCapture];
-[CAMStillImageCaptureRequest hasAdjustments];
-[CAMStillImageCaptureRequest isCTMVideo];
-[CAMStillImageCaptureRequest irisVideoPersistenceUUIDForEV0:];
-[CAMStillImageCaptureRequest needsFlipOverride];
-[CAMStillImageCaptureRequest aspectRatioCrop];
-[CAMStillImageCaptureRequest _configureRawFileFormat:context:rawPixelFormatType:];
-[CAMStillImageCaptureRequest captureRequest];
-[CAMStillImageCaptureRequest irisStillImagePersistenceUUIDForEV0:];
-[CAMStillImageCaptureRequest _sanitizeCapturePhotoSettings:withContext:];
-[CAMStillImageCaptureRequest wantsEV0ForHDR];
-[CAMStillImageCaptureRequest nightMode];
-[CAMStillImageCaptureRequest isPersonalPhotographerSessionEnabled];
-[CAMStillImageCaptureRequest EV0LocalVideoDestinationURL];
-[CAMStillImageCaptureRequest wantsHighResolutionStills];
-[CAMStillImageCaptureRequest irisMode];
-[CAMStillImageCaptureRequest mutableCopyWithZone:];
-[CAMStillImageCaptureRequest isEV0LocalVideoDestinationURL:];
-[CAMStillImageCaptureRequest init];
-[CAMStillImageCaptureRequest burstIdentifier];
-[CAMStillImageCaptureRequest isFrontRearSimultaneousCaptureMirrored];
-[CAMStillImageCaptureRequest isFrontRearSimultaneousCaptureEnabled];
-[CAMStillImageCaptureRequest initWithRequest:distinctPersistence:];
-[CAMStillImageCaptureRequest EV0VideoPersistenceUUID];
-[CAMStillImageCaptureRequest desiredPreviewSize];
-[CAMStillImageCaptureRequest wantsShutterSoundSuppression];
-[CAMStillImageCaptureRequest irisIdentifierForEV0:];
-[CAMStillImageCaptureRequest visualIntelligenceStillUprightDegrees];
-[CAMStillImageCaptureRequest maximumBurstLength];
-[CAMStillImageCaptureRequest ctmCaptureType];
-[CAMStillImageCaptureRequest torchMode];
-[CAMStillImageCaptureRequest destructiveAspectRatioCrop];
-[CAMStillImageCaptureRequest semanticStyle];
-[CAMStillImageCaptureRequest delegate];
-[CAMStillImageCaptureRequest wantsWhiteBalanceLockedDuringVideoRecording];
-[CAMStillImageCaptureRequest disablesCameraSwitchingDuringRecording];
-[CAMStillImageCaptureRequest personalPhotographerSessionIdentifier];
-[CAMStillImageCaptureRequest effectFilterType];
-[CAMStillImageCaptureRequest needsLivePhotoCaptureResumedOnPhotoOutput:];
-[CAMStillImageCaptureRequest flashMode];
-[CAMStillImageCaptureRequest textAnalysisIdentifier];
-[CAMStillImageCaptureRequest visualIntelligenceAnalysisIdentifier];
-[CAMStillImageCaptureRequest copyWithZone:];
-[CAMStillImageCaptureRequest _configurePhotoSettings:shouldIgnoreInitiationSettingsProperties:context:];
-[CAMStillImageCaptureRequest wantsSemanticSceneFilter];
-[CAMStillImageCaptureRequest setWantsShutterSoundSuppression:];
-[CAMStillImageCaptureRequest localVideoDestinationURL];
-[CAMStillImageCaptureRequest textDetectionOverridesOrientation];
```
