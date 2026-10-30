# `BWVISNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- Protocols: `BWVISProcessorDelegate`, `BWNodeBackPressureSource`
- 77 instance variables, 8 properties, 66 instance methods, 1 class methods

## Instance variables

```
i _stabilizationMethod;
i _stabilizationType;
@"BWVISProcessorControllerConfiguration" _processorControllerConfiguration;
@"BWVISProcessorController" _processorController;
B _flushingProcessor;
@"NSArray" _supportedInputPixelFormats;
@"NSArray" _supportedOutputPixelFormats;
i _maxLossyCompressionLevel;
{?="width"i"height"i} _outputDimensions;
{?="width"i"height"i} _generatedTransformsOutputDimensionsOverride;
i _gpuPriority;
B _sphereVideoEnabled;
B _onlyGeneratingTransforms;
B _stabilizeMetadata;
B _flipHorizontalExcludingIris;
B _liveFlipHorizontal;
i _pipelineTraceID;
B _videoSTFEnabled;
B _videoGreenGhostMitigationEnabled;
B _videoGreenGhostOfflineMetadataEnabled;
B _videoGreenGhostOfflineLightSourceMaskEnabled;
B _lowLightGreenGhostMitigationEnabled;
B _lightSourceMaskAndKeypointDescriptorDataEnabled;
B _fillExtendedRowsOfOutputBuffer;
B _usingExtendedCVISLivePhotoStabilization;
B _stabilizeForLongPressVideo;
i _visExecutionMode;
@"NSDictionary" _offlineCameraInfoByPortType;
f _videoStabilizationOverscanOverride;
B _generatesDroppedSampleMarkerBuffers;
@"BWVideoFormatRequirements" _visOutputFormatRequirements;
@"NSObject<OS_dispatch_semaphore>" _emitSampleBufferSemaphore;
B _firstFrameProcessed;
i _numberOfBuffersEmitted;
i _cinematicLookAheadFrameCount;
d _maxFrameRate;
@"BWIrisStillImageMovieMetadataCache" _irisStillImageMovieMetadataCache;
@"NSNumber" _cachedLivePhotoKeyFrame;
@"NSString" _cachedStillImageKeyFrameSettingsID;
@"BWLimitedGMErrorLogger" _limitedGMErrorLogger;
[10{BWVISMotionTensors="entries"@"NSDictionary""framePTS"{?="value"q"timescale"i"flags"I"epoch"q}}] _frameMotionTensorsRingBuffer;
I _frameMotionTensorsRingBufferWriteIndex;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _frameMotionTensorsRingBuffeLock;
i _outputColorSpaceProperties;
@"BWStats" _ioSurfaceCompressionRatioStats;
i _pixelBufferCompressionType;
Q _totalCompressedDataSize;
Q _totalUncompressedDataSize;
{?="value"q"timescale"i"flags"I"epoch"q} _lastEmittedPTS;
B _frameRateConversionEnabled;
B _stabilizeDepthAttachments;
{?="width"i"height"i} _outputDepthDimensions;
@"NSMutableDictionary" _intermediatePixelBufferResolvedFormats;
@"NSMutableDictionary" _intermediatePixelBufferPools;
B _smartStyleRenderingEnabled;
B _smartStyleReversibilityEnabled;
@"NSDictionary" _smartStyleConfigurationDict;
B _stabilizeForSmartStyleReversibility;
I _smartStyleEditInfosBitmask;
B _lowResImageUsedByVideoEncoderEnabled;
^{opaqueCMFormatDescription=} _lowResImageUsedByVideoEncoderFormatDescription;
B _personSegmentationRenderingEnabled;
@"NSData" _foregroundColorCube;
@"NSData" _backgroundColorCube;
@"NSData" _cameraExtrinsicMatrix;
B _zoomSmoothingEnabled;
B _overrideFinalCropRect;
B _systemIsUnderCriticalThermalPressure;
B _faceStabilizationEnabled;
@"NSDictionary" _faceStabilizationParameters;
{FigCaptureGreenGhostOfflineParams="luxSuperLow"i"luxLow"i"exposureHigh"f"clippedSmall"i"movieThresholdInSecond"f} _greenGhostOfflineParameters;
{FigCaptureGreenGhostStatus="detectedGreenGhostFrameCount"i"greenGhostSampleBufferMetadataDetected"B} _greenGhostStatus;
i _stereoMode;
@"NSObject<OS_dispatch_semaphore>" _processingSemaphore;
@"BWFigCaptureISPProcessingSession" _ispProcessingSession;
@"FigCaptureTextureStyle" _textureStyle;
B _textureStyleRenderingEnabled;
```

## Properties

```
@property (Ti,R,V_cinematicLookAheadFrameCount) cinematicLookAheadFrameCount;
@property (T@"BWFigCaptureISPProcessingSession",&,N,V_ispProcessingSession) ispProcessingSession;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,V_firstFrameProcessed) firstFrameProcessed;
@property (T@"NSObject<OS_dispatch_semaphore>",&,N) emitSampleBufferSemaphore;
```

## Class methods

```
+[BWVISNode initialize];
```

## Instance methods

```
-[BWVISNode generatedTransformsOutputDimensionsOverride];
-[BWVISNode setSmartStyleRenderingEnabled:];
-[BWVISNode setLowResImageUsedByVideoEncoderEnabled:];
-[BWVISNode ispProcessingSession];
-[BWVISNode sphereVideoEnabled];
-[BWVISNode frameRateConversionEnabled];
-[BWVISNode setEmitSampleBufferSemaphore:];
-[BWVISNode prepareForCurrentConfigurationToBecomeLive];
-[BWVISNode emitSampleBufferSemaphore];
-[BWVISNode setIspProcessingSession:];
-[BWVISNode setSmartStyleConfigurationDict:];
-[BWVISNode smartStyleReversibilityEnabled];
-[BWVISNode setSphereVideoEnabled:];
-[BWVISNode cameraExtrinsicMatrix];
-[BWVISNode setPipelineTraceID:];
-[BWVISNode pipelineTraceID];
-[BWVISNode smartStyleRenderingEnabled];
-[BWVISNode videoSTFEnabled];
-[BWVISNode setOutputColorSpaceProperties:];
-[BWVISNode renderSampleBuffer:forInput:];
-[BWVISNode setSmartStyleReversibilityEnabled:];
-[BWVISNode setOutputDimensions:];
-[BWVISNode setFirstFrameProcessed:];
-[BWVISNode setVideoGreenGhostMitigationEnabled:];
-[BWVISNode flipHorizontalExcludingIris];
-[BWVISNode setMaxLossyCompressionLevel:];
-[BWVISNode setFrameRateConversionEnabled:];
-[BWVISNode flush];
-[BWVISNode maxLossyCompressionLevel];
-[BWVISNode dealloc];
-[BWVISNode willStartProcessingBuffer:withStatus:];
-[BWVISNode outputDimensions];
-[BWVISNode videoGreenGhostMitigationEnabled];
-[BWVISNode setFlipHorizontalExcludingIris:];
-[BWVISNode initWithSensorIDDict:stabilizationMethod:stabilizationType:ispProcessingSession:maxSupportedFrameRate:activeMaxFrameRate:gpuPriority:metalSubmissionAndCompletionQueuePriority:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:stereoMode:videoStabilizationOverscanOverride:videoStabilizationStrength:zoomSmoothingEnabled:applyFrameCropOffset:motionMetadataPreloadingEnabled:visExecutionMode:livePhotoCleanOutputRect:cameraInfoByPortType:cvisExtendedLookAheadDuration:distortionCorrectionEnabledPortTypes:distortionCompensationEnabledPortTypes:minDistanceForBravoParallaxShift:videoGreenGhostOfflineMetadataEnabled:videoGreenGhostOfflineLightSourceMaskEnabled:lightSourceMaskAndKeypointDescriptorDataEnabled:attachStabilizedOutputCameraTrajectory:systemIsUnderCriticalThermalPressure:textureStyleRenderingEnabled:faceAwareVideoStabilizationEnabled:];
-[BWVISNode hasNonLiveConfigurationChanges];
-[BWVISNode setProcessingSemaphore:];
-[BWVISNode setIrisVISCleanOutputRect:];
-[BWVISNode setTextureStyle:];
-[BWVISNode processingSemaphore];
-[BWVISNode setVideoSTFEnabled:];
-[BWVISNode setOutputDepthDimensions:];
-[BWVISNode firstFrameProcessed];
-[BWVISNode stabilizeDepthAttachments];
-[BWVISNode handleDroppedSample:forInput:];
-[BWVISNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWVISNode lowResImageUsedByVideoEncoderEnabled];
-[BWVISNode didReachEndOfDataForConfigurationID:input:];
-[BWVISNode setStabilizeDepthAttachments:];
-[BWVISNode personSegmentationRenderingEnabled];
-[BWVISNode irisStillImageMovieMetadataCache];
-[BWVISNode setPersonSegmentationRenderingEnabled:];
-[BWVISNode nodeSubType];
-[BWVISNode setGeneratesDroppedSampleMarkerBuffers:];
-[BWVISNode outputColorSpaceProperties];
-[BWVISNode didCompleteProcessingOfBuffer:withStatus:];
-[BWVISNode cinematicLookAheadFrameCount];
-[BWVISNode generatesDroppedSampleMarkerBuffers];
-[BWVISNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWVISNode smartStyleConfigurationDict];
-[BWVISNode outputDepthDimensions];
-[BWVISNode setIrisStillImageMovieMetadataCache:];
-[BWVISNode setCameraExtrinsicMatrix:];
-[BWVISNode nodeType];
-[BWVISNode irisVISCleanOutputRect];
-[BWVISNode setGeneratedTransformsOutputDimensionsOverride:];
```
