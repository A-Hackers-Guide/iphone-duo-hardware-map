# `BWIrisStagingNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 82 instance variables, 4 properties, 39 instance methods, 1 class methods

## Instance variables

```
{?="value"q"timescale"i"flags"I"epoch"q} _bufferingTime;
{?="value"q"timescale"i"flags"I"epoch"q} _targetFrameDuration;
{?="value"q"timescale"i"flags"I"epoch"q} _beginIrisMovieCaptureTime;
{?="value"q"timescale"i"flags"I"epoch"q} _endIrisMovieCaptureTime;
B _stagingSuspended;
B _flushAndSuspendPending;
{?="value"q"timescale"i"flags"I"epoch"q} _stagingResumedTime;
B _compressSynchronizedSlaveAttachedMedia;
{?="value"q"timescale"i"flags"I"epoch"q} _frameGovernorNextFrameThreshold;
{?="value"q"timescale"i"flags"I"epoch"q} _frameGovernorReferenceTime;
{?="value"q"timescale"i"flags"I"epoch"q} _readyToEmitPTS;
{?="value"q"timescale"i"flags"I"epoch"q} _lastProcessedVideoPTS;
{?="value"q"timescale"i"flags"I"epoch"q} _masterMovieStartPTS;
@"NSURL" _temporaryMovieDirectoryURL;
@"NSURL" _masterMovieURL;
@"NSURL" _spatialOverCaptureMasterMovieURL;
@"NSMutableArray" _stagingQueues;
@"NSMutableArray" _lastEmittedBuffers;
@"NSMutableArray" _droppedFramePTSs;
B _valveOpen;
B _finishingAllEnqueuedRequests;
B _valveDraining;
B _emittedFirstAudio;
B _valveOpenForMomentCaptureMovieRecording;
{?="value"q"timescale"i"flags"I"epoch"q} _valveDiscontinuitySearchLimit;
q _valveOpenerSettingsID;
@"NSMutableArray" _irisRequestsInFlight;
@"NSMutableArray" _irisRequestsSoonToBeEmitted;
i _emittedIrisRequestCount;
^{OpaqueFigSimpleMutex=} _stateMutex;
^{?=qiIq} _firstEmittedPTSArray;
^{OpaqueCMClock=} _masterClock;
i _trimMethod;
B _vitalityScoringEnabled;
{?="major"S"minor"S"patch"S} _vitalityScoringSmartCameraPipelineVersion;
@"FigIrisAutoTrimmer" _trimmer;
{?="value"q"timescale"i"flags"I"epoch"q} _firstTrimStartPTS;
B _trimLivePhotoMovieAtWideAndSuperWideAutoSwitching;
Q _inferencesInputIndex;
@"BWInferenceScheduler" _inferenceScheduler;
@"BWMotionDataPreserver" _motionDataPreserver;
@"BWIrisSequenceAdjuster" _sequenceAdjusterBackingStore;
@"BWIrisSequenceAdjuster" _sequenceAdjuster;
@"BWMotionDataTimeMachine" _motionDataTimeMachine;
i _visMotionMetadataPreloadingMode;
@"<BWIrisStagingNodeIrisRequestDelegate>" _delegate;
Q _compressedBufferPoolAllocationTimeoutMS;
f _intermediateJPEGCompressionQuality;
f _intermediateJPEGCompressionRate;
i _intermediateJPEGDownstreamRetainedBufferCount;
i _intermediateJPEGSurfaceLocalRetainedBufferCount;
i _additionalCompressedBufferCount;
@"BWIntermediateJPEGCompressor" _intermediateJPEGCompressor;
@"BWIntermediateJPEGCompressor" _synchronizedSlaveJPEGCompressor;
B _doingJPEGCompression;
@"NSDictionary" _cameraInfoByPortType;
^Q _emissionMap;
B _haveSeenFirstAudioSampleBuffer;
B _haveSeenFirstVideoSampleBuffer;
B _readyToReceiveRequests;
@"NSObject<OS_dispatch_group>" _readyToReceiveRequestsGroup;
Q _minimumPrerollFrames;
f _videoStabilizationOverscanOverride;
B _captureDeviceHasOverCaptureEnabled;
f _spatialOverCapturePercentageToApply;
@"NSString" _recommendedMasterPortType;
i _lastRecommendedMasterSelectionReason;
{?="value"q"timescale"i"flags"I"epoch"q} _lastReceivedVideoTime;
@"BWStats" _overallVideoFrameReceptionStats;
@"BWStats" _valveActiveVideoFrameReceptionStats;
@"BWLimitedGMErrorLogger" _limitedGMErrorLogger;
i _numberOfVideoFramesReceived;
B _subjectRelightingEnabled;
B _firstIrisRequestRequiresSubjectRelightingHasBeenProcessed;
@"BWSubjectRelightingCalculator" _subjectRelightingCalculator;
@"BWSubjectRelightingCalculatorResult" _subjectRelightingResult;
B _applyPreviewShift;
B _reachedEndOfData;
B _smartStyleRenderingEnabled;
B _smartStyleReversibilityEnabled;
B _smartFramingEnabled;
B _textureStyleRenderingEnabled;
```

## Properties

```
@property (T@"NSURL",R) temporaryMovieDirectoryURL;
@property (T@"BWMotionDataTimeMachine",R) motionDataTimeMachine;
@property (T{?=qiIq}) beginIrisMovieCaptureTime;
@property (T{?=qiIq}) endIrisMovieCaptureTime;
```

## Class methods

```
+[BWIrisStagingNode initialize];
```

## Instance methods

```
-[BWIrisStagingNode prepareForCurrentConfigurationToBecomeLive];
-[BWIrisStagingNode setApplyPreviewShift:];
-[BWIrisStagingNode setMasterClock:];
-[BWIrisStagingNode setVitalityScoringSmartCameraPipelineVersion:];
-[BWIrisStagingNode _indexOfBufferBeforeOrEqualToPTS:inputIndex:applyFrameDropsMitigation:];
-[BWIrisStagingNode renderSampleBuffer:forInput:];
-[BWIrisStagingNode setBeginIrisMovieCaptureTime:];
-[BWIrisStagingNode allInputsHaveReachedState:];
-[BWIrisStagingNode setIntermediateJPEGDownstreamRetainedBufferCount:];
-[BWIrisStagingNode closeValve];
-[BWIrisStagingNode setStagingQueues:];
-[BWIrisStagingNode prepareToFinishAllEnqueuedIrisRequestsWithEndTime:];
-[BWIrisStagingNode setBufferingTime:];
-[BWIrisStagingNode dealloc];
-[BWIrisStagingNode beginIrisMovieCaptureTime];
-[BWIrisStagingNode setTargetFrameDuration:];
-[BWIrisStagingNode masterClock];
-[BWIrisStagingNode temporaryMovieDirectoryURL];
-[BWIrisStagingNode waitUntilReadyToReceiveRequestsWithTimeout:];
-[BWIrisStagingNode bufferingTime];
-[BWIrisStagingNode endIrisMovieCaptureTime];
-[BWIrisStagingNode valveIsOpen];
-[BWIrisStagingNode intermediateJPEGDownstreamRetainedBufferCount];
-[BWIrisStagingNode handleDroppedSample:forInput:];
-[BWIrisStagingNode initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:autoTrimMethod:vitalityScoringEnabled:captureDeviceHasOverCaptureEnabled:overCaptureEnabled:depthEnabled:videoStabilizationOverscanOverride:sequenceAdjusterEnabled:visMotionMetadataPreloadingMode:frameReconstructionEnabled:subjectRelightingEnabled:intermediateJPEGCompressionQuality:intermediateJPEGCompressionRate:maxLossyCompressionLevel:temporaryMovieDirectoryURL:cameraInfoByPortType:smartStyleRenderingEnabled:smartStyleReversibilityEnabled:smartFramingEnabled:textureStyleRenderingEnabled:irisRequestDelegate:inferenceScheduler:];
-[BWIrisStagingNode applyPreviewShift];
-[BWIrisStagingNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWIrisStagingNode didReachEndOfDataForConfigurationID:input:];
-[BWIrisStagingNode motionDataTimeMachine];
-[BWIrisStagingNode setEndIrisMovieCaptureTime:];
-[BWIrisStagingNode targetFrameDuration];
-[BWIrisStagingNode openValveWithIrisRequest:];
-[BWIrisStagingNode setMomentCaptureMovieRecordingMasterEndTime:forRequestWithSettingsID:];
-[BWIrisStagingNode enqueueIrisRequest:];
-[BWIrisStagingNode vitalityScoringSmartCameraPipelineVersion];
-[BWIrisStagingNode nodeSubType];
-[BWIrisStagingNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWIrisStagingNode handleNodeError:forInput:];
-[BWIrisStagingNode nodeType];
```
