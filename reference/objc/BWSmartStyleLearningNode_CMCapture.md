# `BWSmartStyleLearningNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- Protocols: `BWInferenceFormatProvider`, `BWInferencePixelBufferPoolProvider`, `BWSemanticStyleSceneObserver`
- 102 instance variables, 12 properties, 80 instance methods, 2 class methods

## Instance variables

```
@"FigMetalContext" _metalContext;
@"<MTLCommandQueue>" _thumbnailsGenerationCommandQueue;
# _smartStyleClass;
@"<CMISmartStyleProcessor>" _smartStyleProcessor;
@"<CMISmartStyleProcessor>" _smartStyleProcessorForThumbnailsGeneration;
@"<CMISmartStyleProcessor>" _smartStyleProcessorForFiltering;
# _smartStyleProcessorInputOutputClass;
@"NSMutableArray" _inputMasksSampleBufferQueue;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _styleUpdateLock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _inputMasksSampleBufferQueueLock;
@"NSMutableArray" _inputStyleContainerSampleBufferQueue;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _inputStyleContainerSampleBufferQueueLock;
@"NSMutableDictionary" _configurationDelegatesByPortType;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _configurationDelegatesLock;
@"FigCaptureSmartStyle" _priorStyle;
^{__CVPixelBufferPool=} _priorCoefficientsPixelBufferPool;
^{__CVBuffer=} _priorCoefficientsPixelBuffer;
^{opaqueCMSampleBuffer=} _learnedCoefficientsSampleBuffer;
^{__CVBuffer=} _identityCoefficientsPixelBuffer;
@"NSMutableDictionary" _currentImageStats;
@"NSMutableDictionary" _currentImageStatsExtended;
@"BWFigCaptureISPProcessingSession" _ispSMGProcessingSession;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _semanticStyleSceneLock;
i _semanticStyleSceneType;
B _propagateMasks;
B _preLTMThumbnailFound;
{?="value"q"timescale"i"flags"I"epoch"q} _previousPTS;
B _generateCoefficients;
B _generateImageStats;
I _frameCount;
B _runVMRefiner;
B _runVMRefinerFPRejection;
B _gdcAttachmentsEnabled;
B _useHardwareWeightSegmentMap;
B _useHardwareStreamingRendering;
B _isThumbnailsGenerationSynchronous;
B _squareAspectRatioConfigEnabled;
B _preparedVMRefiner;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _inferenceLock;
@"BWInferenceScheduler" _inferenceScheduler;
@"BWInferenceEngine" _inferenceEngine;
@"BWVideoFormat" _anstMaskVideoFormat;
@"NSMutableDictionary" _refinedVideoFormatByAttachedMediaKey;
@"NSMutableDictionary" _processorVideoFormatsByAttachedMediaKeys;
@"NSMutableDictionary" _processorPixelBufferPoolsByAttachedMediaKeys;
@"NSMutableDictionary" _intermediateVideoFormatsByAttachedMediaKeys;
@"NSMutableDictionary" _intermediatePixelBufferPoolsByAttachedMediaKeys;
@"NSDictionary" _cameraInfoByPortType;
B _firstFrame;
@"NSString" _lastLearnedPortType;
@"NSString" _lastLearnedSynchronizedPortType;
I _learningRate;
I _learningFramesPerSecondUnit;
I _learningMaxFramesPerSecond;
f _statsUpdateDeltaTimeThreshold;
f _anstMasksMatchingTimeInSecondsThreshold;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _timingLock;
f _timeInSecondsUntilNextStatsUpdate;
f _timeInSecondsUntilNextLearning;
@"NSObject<OS_dispatch_queue>" _workQueue;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _workQueueLock;
I _workQueueRenderCount;
I _workQueueLearnCount;
@"FigCaptureSmartStyle" _smartStyleLearned;
@"NSNumber" _srlCurveParameter;
B _smartStyleRenderingRequiredForSRL;
@"NSData" _srlStats;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _lastLearnedROI;
B _learnedLastFrame;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _mostRecentMasksLock;
{?="person"b1"skin"b1"sky"b1} _mostRecentUpdatedMasks;
^{opaqueCMSampleBuffer=} _mostRecentLearnedPersonMaskSampleBuffer;
^{opaqueCMSampleBuffer=} _mostRecentLearnedSkinMaskSampleBuffer;
^{opaqueCMSampleBuffer=} _mostRecentLearnedSkyMaskSampleBuffer;
B _bypassStyleEngineForStandardStyle;
B _runSrlStatsAndEnableStylesIfNeeded;
I _srlPreviewVersion;
^{__CVBuffer=} _targetPixelBufferWithSmartStyleApplied;
B _shouldRefineAllMaskFrames;
B _streamPersonMaskOnlyWhenLearning;
B _streamSkinMaskOnlyWhenLearning;
B _streamSkyMaskOnlyWhenLearning;
Q _filterType;
@"BWPixelBufferPool" _filteredCoefficientsPixelBufferPool;
I _filteredCoefficientsPixelBufferPoolSize;
B _textureStyleEnabled;
^{__CVBuffer=} _targetPixelBufferWithTextureApplied;
@"CMITextureStylesProcessor" _textureStylesProcessor;
B _textureStylesProcessorHasBeenPrepared;
B _enableGlow;
B _enableDiffusion;
B _enableMattify;
B _enableBloom;
@"<MTLBuffer>" _statisticsToShare;
^{__CVBuffer=} _intermediatePixelBuffer;
B _shouldApplyRadialExtension;
B _disableWaitForCoefficientsOnFirstFrame;
B _subjectRelightingEnabled;
B _propagateWeightSegmentMap;
B _propagateWeightSegmentMapScaledForISPSTEN;
@"FigCaptureSmartStyle" _smartStyle;
@"FigCaptureTextureStyle" _textureStyle;
```

## Properties

```
@property (T@"FigCaptureSmartStyle",&,N,V_smartStyle) smartStyle;
@property (T@"FigCaptureTextureStyle",&,N,V_textureStyle) textureStyle;
@property (TB,N,V_disableWaitForCoefficientsOnFirstFrame) disableWaitForCoefficientsOnFirstFrame;
@property (TB,N,V_subjectRelightingEnabled) subjectRelightingEnabled;
@property (T@"NSNumber",R,N,V_srlCurveParameter) srlCurveParameter;
@property (T@"NSDictionary",&,N) cameraInfoByPortType;
@property (TB,N,V_propagateWeightSegmentMap) propagateWeightSegmentMap;
@property (TB,N,V_propagateWeightSegmentMapScaledForISPSTEN) propagateWeightSegmentMapScaledForISPSTEN;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWSmartStyleLearningNode initialize];
+[BWSmartStyleLearningNode newISPSMGProcessingSession:];
```

## Instance methods

```
-[BWSmartStyleLearningNode prepareForCurrentConfigurationToBecomeLive];
-[BWSmartStyleLearningNode preparedOutputPixelBufferPoolForAttachedMediaKey:format:];
-[BWSmartStyleLearningNode semanticStyleSceneTypeDidChange:];
-[BWSmartStyleLearningNode _unpackSbufFromPrimaryCameraStream:portTypeToLearn:synchronizedPortTypeToLearn:];
-[BWSmartStyleLearningNode _setupCommonInputsForInputPixelBuffer:outputPixelBuffer:];
-[BWSmartStyleLearningNode setCameraInfoByPortType:];
-[BWSmartStyleLearningNode _tuningParametersForPortType:];
-[BWSmartStyleLearningNode cameraInfoByPortType];
-[BWSmartStyleLearningNode renderSampleBuffer:forInput:];
-[BWSmartStyleLearningNode _createIdentityCoefficientsFromSampleBuffer:to:];
-[BWSmartStyleLearningNode propagateWeightSegmentMap];
-[BWSmartStyleLearningNode _setupPersonDataFromMetadata:maxFaceCount:];
-[BWSmartStyleLearningNode _setupBloomForSkinMask:metadataDict:effectsToRender:];
-[BWSmartStyleLearningNode outputFormatForAttachedMediaKey:];
-[BWSmartStyleLearningNode _getContainerAssetsFromSampleBuffer:outputUnstyledThumbnailSampleBuffer:outputLinearThumbnailSampleBuffer:outputWeightSegmentMapSampleBuffer:];
-[BWSmartStyleLearningNode removeSmartStyleISPApplyConfigurationDelegate:forPortType:];
-[BWSmartStyleLearningNode intermediateResourceTrackingAllowedForAttachedMediaKey:];
-[BWSmartStyleLearningNode _setupDiffusionForPersonMask:forSkinMaskPixelBuffer:metadataDict:intensity:effectsToRender:];
-[BWSmartStyleLearningNode textureStyle];
-[BWSmartStyleLearningNode smartStyle];
-[BWSmartStyleLearningNode inputVideoFormatForAttachedMediaKey:];
-[BWSmartStyleLearningNode _getSampleBufferPresentationTimeStamp:];
-[BWSmartStyleLearningNode _updateISPSTENConfigurationsWithCoefficients:onPortType:onSynchronizedLearnedPortType:];
-[BWSmartStyleLearningNode setSmartStyle:];
-[BWSmartStyleLearningNode _asynchronouslyDecrementLearnCount];
-[BWSmartStyleLearningNode _setupInputMaskForPixelBuffer:maskType:maskIsOptional:metadataDict:];
-[BWSmartStyleLearningNode dealloc];
-[BWSmartStyleLearningNode processMaskSampleBuffer:];
-[BWSmartStyleLearningNode setSubjectRelightingEnabled:];
-[BWSmartStyleLearningNode _initVMRefinerInference];
-[BWSmartStyleLearningNode _asynchronouslyDecrementRenderCount];
-[BWSmartStyleLearningNode hasNonLiveConfigurationChanges];
-[BWSmartStyleLearningNode setPropagateWeightSegmentMap:];
-[BWSmartStyleLearningNode disableWaitForCoefficientsOnFirstFrame];
-[BWSmartStyleLearningNode _releaseResources];
-[BWSmartStyleLearningNode setTextureStyle:];
-[BWSmartStyleLearningNode inputInferenceVideoFormatForAttachedMediaKey:];
-[BWSmartStyleLearningNode outputVideoFormatForAttachedMediaKey:];
-[BWSmartStyleLearningNode _blitMasksToOutputPools:unstyledSampleBuffer:currentPTS:];
-[BWSmartStyleLearningNode _setupGlowForPersonMask:metadataDict:linearThumbnail:linearThumbnailMetadata:intensity:effectsToRender:statistics:];
-[BWSmartStyleLearningNode inputFormatForAttachedMediaKey:];
-[BWSmartStyleLearningNode _blendedTuningParametersForPortType:intensity:effectiveIntensityOut:];
-[BWSmartStyleLearningNode _getPortTypeFromMetadataDict:];
-[BWSmartStyleLearningNode _createSmartStyleContainerFromSampleBuffer:unstyledThumbnailSampleBuffer:linearThumbnailSampleBuffer:weightSegmentMapSampleBuffer:to:];
-[BWSmartStyleLearningNode loadInferenceNetwork];
-[BWSmartStyleLearningNode _setupProcessorFullImageSizeAndRegionToRenderPixelBuffer:];
-[BWSmartStyleLearningNode setDisableWaitForCoefficientsOnFirstFrame:];
-[BWSmartStyleLearningNode subjectRelightingEnabled];
-[BWSmartStyleLearningNode _asynchronouslyLearnWithContainer:inputUnstyledSampleBuffer:withUnrefinedMasks:portTypeToLearn:synchronizedPortTypeToLearn:withStats:withStatsExtended:styleToLearn:currentTextureStyle:shouldLearn:shouldBypass:];
-[BWSmartStyleLearningNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWSmartStyleLearningNode _loadAndConfigureSmartStyleBundle];
-[BWSmartStyleLearningNode didReachEndOfDataForConfigurationID:input:];
-[BWSmartStyleLearningNode _cropAndUndistortWeightSegmentMap:unstyledSampleBuffer:doGDC:toPixelBuffer:];
-[BWSmartStyleLearningNode _asynchronouslySignalEvent:];
-[BWSmartStyleLearningNode _newPixelBufferWithDimensions:pixelFormat:name:];
-[BWSmartStyleLearningNode _extractANSTMasks:forPTS:];
-[BWSmartStyleLearningNode _updateCurrentSmartStyleMetadata:onSbuf:];
-[BWSmartStyleLearningNode _runFalsePositiveRejectionOnPixelBuffer:unrefinedPixelBuffer:];
-[BWSmartStyleLearningNode addSmartStyleISPApplyConfigurationDelegate:forPortType:];
-[BWSmartStyleLearningNode _setupLinearImageFromPixelBuffer:linearImageMetadata:];
-[BWSmartStyleLearningNode srlCurveParameter];
-[BWSmartStyleLearningNode nodeSubType];
-[BWSmartStyleLearningNode _filterCoefficients:metadata:timestamp:outputPixelBuffer:];
-[BWSmartStyleLearningNode setPropagateWeightSegmentMapScaledForISPSTEN:];
-[BWSmartStyleLearningNode propagateWeightSegmentMapScaledForISPSTEN];
-[BWSmartStyleLearningNode _cropAndScaleMasks:unstyledSampleBuffer:currentPTS:applyGDC:useIntermediatePool:];
-[BWSmartStyleLearningNode initWithOutputs:masksRefinerEnabled:propagateMasks:ispSMGProcessingSession:squareAspectRatioConfigEnabled:hardwareStreamingRenderingEnabled:textureStyleEnabled:subjectRelightingPreviewVersion:];
-[BWSmartStyleLearningNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWSmartStyleLearningNode _asynchronouslyRenderSampleBuffer:outputLinearThumbnailSampleBuffer:outputUnstyledThumbnailSampleBuffer:outputWeightSegmentMapSampleBuffer:synchronizingEvent:];
-[BWSmartStyleLearningNode _propagateMostRecentMasksAndLearnedFlagToSampleBuffer:metadataDict:];
-[BWSmartStyleLearningNode _updateTextureStyleEnableFlagsForMetadataDict:];
-[BWSmartStyleLearningNode _findCorrespondingSmartStyleContainerWithMasks:outputSmartStyleContainer:];
-[BWSmartStyleLearningNode _deepCopyMasks:];
-[BWSmartStyleLearningNode _createCoefficientsFromSampleBuffer:to:];
-[BWSmartStyleLearningNode _computePriorCoefficientsForStyle:];
-[BWSmartStyleLearningNode nodeType];
-[BWSmartStyleLearningNode _isEffectEnabled:inEffectOrder:];
-[BWSmartStyleLearningNode processVideoSampleBuffer:frameEmitted:];
-[BWSmartStyleLearningNode _runInferences:unstyledSampleBuffer:withMasks:currentPTS:];
-[BWSmartStyleLearningNode _setupMattifyForSkinMask:metadataDict:intensity:effectsToRender:];
```
