# `BWMemoryAnalyticsPayload`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWCoreAnalyticsPayload`
- 58 instance variables, 37 properties, 75 instance methods, 0 class methods

## Instance variables

```
i _buttonMashRate0Counter;
@"NSDate" _creationTime;
B _burst;
B _captureDevicePositionFront;
B _captureDevicePositionBack;
B _captureDeviceTypeBravo;
B _captureDeviceTypeLiDAR;
B _captureDeviceTypeOther;
B _captureDeviceTypePearl;
B _captureDeviceTypeSuperBravo;
B _captureDeviceTypeWideBravo;
B _capturePortTypeBackSuperWide;
B _capturePortTypeBackTelephoto;
B _capturePortTypeOther;
B _capturePortTypeBack;
B _captureResolutionDefault;
B _captureResolutionEnhanced;
B _captureResolutionUltraHigh;
B _captureTypeUB;
B _captureTypeDeepFusion;
B _captureTypeLearnedFusion;
B _captureTypeAdaptiveFusion;
B _captureTypeDigitalFlash;
B _captureTypeOther;
B _captureTypeWYSIWYG;
B _greenGhostMitigation;
B _scaledStillCaptureTaken;
B _intelligentDistortionCorrection;
B _livePhoto;
B _proRaw;
B _proRawPlusProcessedPhotoEncoding;
B _quickTakeVideo;
B _faceDetectedInScene;
B _photographicStyleUsed;
B _enhancedResolutionPortraitSuggested;
B _enhancedResolutionPortraitApplied;
I _maxButtonMashCount;
B _portraitRequested;
B _portraitDepthGenerationAttempted;
B _portraitEffectApplied;
B _cinematicVideo;
B _hdrVideo;
B _proResVideo;
i _colorSpace;
I _videoMaxFrameRate;
I _videoMinDimension;
i _maxVideoStabilizationMethod;
i _videoStabilizationStrength;
I _videoRecordingCount;
B _dockKitDeviceConnected;
B _graphHasVideoDataOutput;
B _graphContainsMovieFilePipeline;
B _graphContainsDepthDataPipeline;
@"NSString" _clientApplicationID;
I _captureCount;
Q _peakFootprintDifference;
B _clientIsCameraOrDerivative;
i _deviceType;
```

## Properties

```
@property (TB,N,V_burst) burst;
@property (TI,R,N,V_captureCount) captureCount;
@property (TB,N,V_clientIsCameraOrDerivative) clientIsCameraOrDerivative;
@property (T@"NSString",C,N,V_clientApplicationID) clientApplicationID;
@property (Ti,N,V_deviceType) deviceType;
@property (TB,N,V_graphHasVideoDataOutput) graphHasVideoDataOutput;
@property (TB,N,V_graphContainsMovieFilePipeline) graphContainsMovieFilePipeline;
@property (TB,N,V_graphContainsDepthDataPipeline) graphContainsDepthDataPipeline;
@property (TB,N,V_greenGhostMitigation) greenGhostMitigation;
@property (TB,N,V_scaledStillCaptureTaken) scaledStillCaptureTaken;
@property (TB,N,V_intelligentDistortionCorrection) intelligentDistortionCorrection;
@property (TB,N,V_livePhoto) livePhoto;
@property (TB,N,V_proRaw) proRaw;
@property (TB,N,V_proRawPlusProcessedPhotoEncoding) proRawPlusProcessedPhotoEncoding;
@property (TB,N,V_quickTakeVideo) quickTakeVideo;
@property (TB,N,V_portraitRequested) portraitRequested;
@property (TB,N,V_portraitDepthGenerationAttempted) portraitDepthGenerationAttempted;
@property (TB,N,V_portraitEffectApplied) portraitEffectApplied;
@property (TB,N,V_faceDetectedInScene) faceDetectedInScene;
@property (TB,N,V_photographicStyleUsed) photographicStyleUsed;
@property (TB,N,V_enhancedResolutionPortraitSuggested) enhancedResolutionPortraitSuggested;
@property (TB,N,V_enhancedResolutionPortraitApplied) enhancedResolutionPortraitApplied;
@property (TQ,N,V_peakFootprintDifference) peakFootprintDifference;
@property (TB,N,V_cinematicVideo) cinematicVideo;
@property (TB,N,V_hdrVideo) hdrVideo;
@property (TB,N,V_proResVideo) proResVideo;
@property (TI,N,V_videoMaxFrameRate) videoMaxFrameRate;
@property (TI,N,V_videoMinDimension) videoMinDimension;
@property (TI,N,V_videoRecordingCount) videoRecordingCount;
@property (Ti,N,V_maxVideoStabilizationMethod) maxVideoStabilizationMethod;
@property (Ti,N,V_videoStabilizationStrength) videoStabilizationStrength;
@property (TB,N,V_dockKitDeviceConnected) dockKitDeviceConnected;
@property (Ti,N,V_colorSpace) colorSpace;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWMemoryAnalyticsPayload setVideoStabilizationStrength:];
-[BWMemoryAnalyticsPayload setDeviceType:];
-[BWMemoryAnalyticsPayload livePhoto];
-[BWMemoryAnalyticsPayload videoStabilizationStrength];
-[BWMemoryAnalyticsPayload burst];
-[BWMemoryAnalyticsPayload setFaceDetectedInScene:];
-[BWMemoryAnalyticsPayload eventDictionary];
-[BWMemoryAnalyticsPayload proRawPlusProcessedPhotoEncoding];
-[BWMemoryAnalyticsPayload portraitEffectApplied];
-[BWMemoryAnalyticsPayload videoMinDimension];
-[BWMemoryAnalyticsPayload setColorSpace:];
-[BWMemoryAnalyticsPayload photographicStyleUsed];
-[BWMemoryAnalyticsPayload addDeviceType:];
-[BWMemoryAnalyticsPayload setPeakFootprintDifference:];
-[BWMemoryAnalyticsPayload hdrVideo];
-[BWMemoryAnalyticsPayload setLivePhoto:];
-[BWMemoryAnalyticsPayload init];
-[BWMemoryAnalyticsPayload setHdrVideo:];
-[BWMemoryAnalyticsPayload deviceType];
-[BWMemoryAnalyticsPayload clientIsCameraOrDerivative];
-[BWMemoryAnalyticsPayload greenGhostMitigation];
-[BWMemoryAnalyticsPayload setClientIsCameraOrDerivative:];
-[BWMemoryAnalyticsPayload setVideoRecordingCount:];
-[BWMemoryAnalyticsPayload setGraphContainsDepthDataPipeline:];
-[BWMemoryAnalyticsPayload dealloc];
-[BWMemoryAnalyticsPayload maxVideoStabilizationMethod];
-[BWMemoryAnalyticsPayload dockKitDeviceConnected];
-[BWMemoryAnalyticsPayload setPhotographicStyleUsed:];
-[BWMemoryAnalyticsPayload graphHasVideoDataOutput];
-[BWMemoryAnalyticsPayload enhancedResolutionPortraitSuggested];
-[BWMemoryAnalyticsPayload setGreenGhostMitigation:];
-[BWMemoryAnalyticsPayload cinematicVideo];
-[BWMemoryAnalyticsPayload reset];
-[BWMemoryAnalyticsPayload scaledStillCaptureTaken];
-[BWMemoryAnalyticsPayload addCaptureType:];
-[BWMemoryAnalyticsPayload portraitDepthGenerationAttempted];
-[BWMemoryAnalyticsPayload setClientApplicationID:];
-[BWMemoryAnalyticsPayload setScaledStillCaptureTaken:];
-[BWMemoryAnalyticsPayload videoMaxFrameRate];
-[BWMemoryAnalyticsPayload proResVideo];
-[BWMemoryAnalyticsPayload colorSpace];
-[BWMemoryAnalyticsPayload faceDetectedInScene];
-[BWMemoryAnalyticsPayload setPortraitRequested:];
-[BWMemoryAnalyticsPayload setGraphHasVideoDataOutput:];
-[BWMemoryAnalyticsPayload eventName];
-[BWMemoryAnalyticsPayload setGraphContainsMovieFilePipeline:];
-[BWMemoryAnalyticsPayload portraitRequested];
-[BWMemoryAnalyticsPayload graphContainsMovieFilePipeline];
-[BWMemoryAnalyticsPayload captureCount];
-[BWMemoryAnalyticsPayload updateButtonMash:];
-[BWMemoryAnalyticsPayload proRaw];
-[BWMemoryAnalyticsPayload setMaxVideoStabilizationMethod:];
-[BWMemoryAnalyticsPayload videoRecordingCount];
-[BWMemoryAnalyticsPayload setDockKitDeviceConnected:];
-[BWMemoryAnalyticsPayload setVideoMinDimension:];
-[BWMemoryAnalyticsPayload setPortraitEffectApplied:];
-[BWMemoryAnalyticsPayload enhancedResolutionPortraitApplied];
-[BWMemoryAnalyticsPayload quickTakeVideo];
-[BWMemoryAnalyticsPayload addHighResolutionFlavor:];
-[BWMemoryAnalyticsPayload peakFootprintDifference];
-[BWMemoryAnalyticsPayload setEnhancedResolutionPortraitApplied:];
-[BWMemoryAnalyticsPayload setIntelligentDistortionCorrection:];
-[BWMemoryAnalyticsPayload setProResVideo:];
-[BWMemoryAnalyticsPayload setPortraitDepthGenerationAttempted:];
-[BWMemoryAnalyticsPayload setProRawPlusProcessedPhotoEncoding:];
-[BWMemoryAnalyticsPayload setProRaw:];
-[BWMemoryAnalyticsPayload setEnhancedResolutionPortraitSuggested:];
-[BWMemoryAnalyticsPayload addPortType:];
-[BWMemoryAnalyticsPayload setQuickTakeVideo:];
-[BWMemoryAnalyticsPayload intelligentDistortionCorrection];
-[BWMemoryAnalyticsPayload setVideoMaxFrameRate:];
-[BWMemoryAnalyticsPayload graphContainsDepthDataPipeline];
-[BWMemoryAnalyticsPayload clientApplicationID];
-[BWMemoryAnalyticsPayload setCinematicVideo:];
-[BWMemoryAnalyticsPayload setBurst:];
```
