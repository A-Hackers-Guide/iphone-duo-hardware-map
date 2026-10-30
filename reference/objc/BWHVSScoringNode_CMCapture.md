# `BWHVSScoringNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- Protocols: `BWHVSCandidateFrameManagerDelegate`, `BWPersonalPhotographerDelegate`, `BWInferenceFormatProvider`
- 77 instance variables, 9 properties, 31 instance methods, 1 class methods

## Instance variables

```
@"BWNodeInput" _yuvInput;
@"BWNodeInput" _rawInput;
@"BWNodeInput" _hueMapInput;
@"BWNodeInput" _semanticMasksInput;
@"BWHVSFrame" _lastFrame;
@"BWHVSFrame" _manualFramePendingRegistration;
@"BWSensorRawTimeMachine" _sensorRawTimeMachine;
B _delayYUVInputByOneFrame;
^{opaqueCMSampleBuffer=} _bufferedYUVInputSampleBuffer;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _sharedStateLock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _candidateManagerLock;
@"FigCaptureStillImageSettings" _requestedSettings;
@"BWStillImageCoordinatorNode" _stillImageCoordinator;
q _currentSettingsID;
{?="value"q"timescale"i"flags"I"epoch"q} _lastInitiatedSIFRSbufPTS;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _statusInfoLock;
@"NSMutableDictionary" _statusInfo;
i _consecutiveFramesWithoutSubject;
i _subjectDetectedStabilizationFrames;
@"BWFigVideoCaptureDevice" _captureDevice;
@"NSDictionary" _hvsConfig;
@"NSDictionary" _hvsEmbeddings;
i _captureMode;
@"BWInferenceScheduler" _inferenceScheduler;
I _threadPriority;
@"BWInferenceEngine" _faceQualityInferenceEngine;
@"BWInferenceEngine" _imageEmbeddingInferenceEngine;
@"FigMetalContext" _maskGDCMetalContext;
@"<CMISmartStyleProcessor>" _maskGDCProcessor;
@"BWPixelBufferPool" _gdcMaskOutputPool;
B _enableGDCCorrection;
B _enableGDCCorrectionOnBackSuperWide;
@"NSObject<OS_dispatch_queue>" _imageEmbeddingsDispatchQueue;
@"NSObject<OS_dispatch_queue>" _sharpnessDispatchQueue;
@"NSObject<OS_dispatch_queue>" _faceQualityDispatchQueue;
B _serializeInferences;
B _multiFramePipeliningEnabled;
@"FigCaptureWorkInterval" _workInterval;
@"BWHVSFrameAnalysisTask" _scheduledFrameAnalysisTask;
@"BWHVSCandidateFrameManager" _candidateFrameManager;
i _numProcessedFrames;
i _numFramesWithoutMainSensorRaw;
i _numFramesWithoutSIFRSensorRaw;
i _numFramesWithoutHueMap;
i _numFramesWithoutSemanticMasks;
i _numFramesWithOutOfSyncSemanticMasks;
AB _sessionActive;
AB _sessionFinalizationPending;
AB _wasSessionActive;
AB _manualCapturePending;
I _sessionID;
B _stripSegmentationMask;
B _enableSegmentationMaskFallback;
B _enableFaceQualityInference;
B _enableImageEmbeddingInference;
B _enableSharpnessDetection;
@"FigM2MController" _m2mController;
^{__CVBuffer=} _downscaledYUVPixelBuffer;
* _laplacianScratchBuffer;
Q _laplacianScratchBufferSize;
@"BWHVSEmbeddingAnalysisResult" _prevFrameNetworkOutput;
^f _contextEmbeddingsFP32;
i _numActivePromptEmbeddings;
^f _scoringEmbeddingsFP32;
i _numPromptPairs;
@"NSDictionary" _weightsPerCtx;
@"NSMutableArray" _pinnedGroupIDs;
@"NSString" _loggingPrefix;
@"<BWPersonalPhotographerCaptureRegistrationDelegate>" _delegate;
@"NSObject<OS_dispatch_semaphore>" _lastFrameAvailabilitySemaphore;
@"NSMutableArray" _orientationHistory;
{?="value"q"timescale"i"flags"I"epoch"q} _lastRenderedPTS;
@"NSString" _recommendedMasterPortType;
i _lastProcessedCaptureID;
B _frameSkippingThermalMitigationEnabled;
{?="value"q"timescale"i"flags"I"epoch"q} _earliestAllowedStillImageCaptureHostPTS;
AB _preparedInferences;
```

## Properties

```
@property (T@"BWNodeInput",R,N,V_yuvInput) yuvInput;
@property (T@"BWNodeInput",R,N,V_rawInput) rawInput;
@property (T@"BWNodeInput",R,N,V_hueMapInput) hueMapInput;
@property (T@"BWNodeInput",R,N,V_semanticMasksInput) semanticMasksInput;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tf,R,N) typicalCaptureLatencyInSeconds;
```

## Class methods

```
+[BWHVSScoringNode initialize];
```

## Instance methods

```
-[BWHVSScoringNode initiateManualPersonalPhotographerCapture];
-[BWHVSScoringNode prepareForCurrentConfigurationToBecomeLive];
-[BWHVSScoringNode stopPersonalPhotographerSession];
-[BWHVSScoringNode renderSampleBuffer:forInput:];
-[BWHVSScoringNode outputFormatForAttachedMediaKey:];
-[BWHVSScoringNode intermediateResourceTrackingAllowedForAttachedMediaKey:];
-[BWHVSScoringNode inputVideoFormatForAttachedMediaKey:];
-[BWHVSScoringNode dealloc];
-[BWHVSScoringNode inputInferenceVideoFormatForAttachedMediaKey:];
-[BWHVSScoringNode outputVideoFormatForAttachedMediaKey:];
-[BWHVSScoringNode inputFormatForAttachedMediaKey:];
-[BWHVSScoringNode loadInferenceNetwork];
-[BWHVSScoringNode handleDroppedSample:forInput:];
-[BWHVSScoringNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWHVSScoringNode didReachEndOfDataForConfigurationID:input:];
-[BWHVSScoringNode nodeSubType];
-[BWHVSScoringNode willStopGraph:];
-[BWHVSScoringNode didSelectFormat:forInput:];
-[BWHVSScoringNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWHVSScoringNode nodeType];
-[BWHVSScoringNode rawInput];
-[BWHVSScoringNode currentActiveRequestedSettings];
-[BWHVSScoringNode hueMapInput];
-[BWHVSScoringNode hvsCandidateFrameManager:didRegisterFramesToKeep:framesToDelete:];
-[BWHVSScoringNode initWithCaptureMode:captureDevice:inferenceScheduler:threadPriority:livePhotoCaptureEnabled:delegate:];
-[BWHVSScoringNode semanticMasksInput];
-[BWHVSScoringNode startPersonalPhotographerSessionWithSettings:stillImageCoordinator:];
-[BWHVSScoringNode typicalCaptureLatencyInSeconds];
-[BWHVSScoringNode updateEarliestAllowedStillImageCaptureHostPTS:];
-[BWHVSScoringNode updatePersonalPhotographerOrientationDegrees:mirrored:];
-[BWHVSScoringNode yuvInput];
```
