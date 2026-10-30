# `BWRemoteQueueSinkNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWSinkNode`
- 63 instance variables, 2 properties, 35 instance methods, 1 class methods

## Instance variables

```
B _mediaTypeIsVideo;
B _mediaTypeIsSecureVideo;
B _mediaTypeIsPointCloud;
B _mediaTypeIsAudio;
^{remoteQueueSenderOpaque=} _remoteQueueSender;
^{OpaqueFigSimpleMutex=} _peerTerminationMutex;
^{shmemPoolOpaque=} _sharedMemoryPool;
^{__CFAllocator=} _sharedMemoryPoolCFAllocator;
B _peerTerminated;
^{localQueueOpaque=} _localQueue;
I _numberOfMediaBuffersLocallyEnqueued;
I _numberOfMediaBuffersLocallyDequeued;
@"<BWRemoteQueueSinkNodeDelegate>" _delegate;
i _clientVideoRetainedBufferCount;
B _discardsLateSampleBuffers;
B _attachPanoramaMetadata;
B _sentDiagnosticMetadataForPanorama;
B _disableFlatDictionaryVDOMetadata;
^{OpaqueFigFlatDictionaryKeySpec=} _makerNoteKeySpec;
B _cameraSupportsFlash;
B _attachDetectedObjectsInfo;
B _removeCameraIntrinsicMatrixAttachment;
^{opaqueCMFormatDescription=} _cachedFormatDescription;
{?="value"q"timescale"i"flags"I"epoch"q} _lastPTS;
i _receiverPID;
{?="val"[8I]} _receiverAuditToken;
B _clientIsCaptureServerDaemon;
B _panoramaRequiresLTMLocking;
@"BWSceneStabilityMonitor" _stabilityMonitor;
@"FigCaptureTrie" _requestedBufferAttachmentsTrie;
@"CMCaptureFrameSenderService" _frameSender;
B _frameSenderSupportEnabled;
@"NSString" _clientApplicationID;
q _totalNumberOfFrames;
q _totalNumberOfFramesDropped;
q _totalNumberOfISPFramesDropped;
@"FigCaptureFrameRateMonitor" _frameRateMonitor;
@"BWVideoDataOutputAnalyticsPayload" _analyticsPayload;
{?="value"q"timescale"i"flags"I"epoch"q} _firstPTS;
B _proresVideo;
B _proresRawVideo;
@"BWMovieLevelMetadataForProResRaw" _movieLevelMetadataForProResRaw;
@"NSDictionary" _cameraInfoByPortType;
^{OpaqueFigSimpleMutex=} _stateMutex;
B _didNotifyFirstFrame;
B _videoHDRImageStatisticsEnabled;
B _panoRecordingInProgress;
B _panoRecordingAlreadyInProgress;
f _accumulatedAbsTranslationX;
f _accumulatedAbsTranslationY;
@"NSString" _panoPortType;
f _panoScalingFactor;
f _minAbsTranslationX;
f _minAbsTranslationY;
f _maxAbsTranslationX;
f _maxAbsTranslationY;
f _initialFocusDistance;
f _initialExposureTime;
f _minLux;
f _maxLux;
f _accumulatedLux;
i _numFrames;
@"BWPixelBufferPool" _currentConfigurationPixelBufferPool;
```

## Properties

```
@property (T@"<BWRemoteQueueSinkNodeDelegate>",N,V_delegate) delegate;
@property (T@"NSArray",R,N) movieLevelMetadata;
```

## Class methods

```
+[BWRemoteQueueSinkNode initialize];
```

## Instance methods

```
-[BWRemoteQueueSinkNode updateClientAuditToken:];
-[BWRemoteQueueSinkNode videoHDRImageStatisticsEnabled];
-[BWRemoteQueueSinkNode prepareForCurrentConfigurationToBecomeLive];
-[BWRemoteQueueSinkNode movieLevelMetadata];
-[BWRemoteQueueSinkNode discardsLateSampleBuffers];
-[BWRemoteQueueSinkNode setVideoHDRImageStatisticsEnabled:];
-[BWRemoteQueueSinkNode setRequestedBufferAttachmentsTrie:];
-[BWRemoteQueueSinkNode setCameraSupportsFlash:];
-[BWRemoteQueueSinkNode renderSampleBuffer:forInput:];
-[BWRemoteQueueSinkNode cameraSupportsFlash];
-[BWRemoteQueueSinkNode setRemoveCameraIntrinsicMatrixAttachment:];
-[BWRemoteQueueSinkNode panoRecordingInProgress];
-[BWRemoteQueueSinkNode dealloc];
-[BWRemoteQueueSinkNode clientVideoRetainedBufferCount];
-[BWRemoteQueueSinkNode setSceneStabilityMetadataEnabled:];
-[BWRemoteQueueSinkNode setDiscardsLateSampleBuffers:];
-[BWRemoteQueueSinkNode frameSenderSupportEnabled];
-[BWRemoteQueueSinkNode setFrameSenderSupportEnabled:];
-[BWRemoteQueueSinkNode setPanoRecordingInProgress:];
-[BWRemoteQueueSinkNode removeCameraIntrinsicMatrixAttachment];
-[BWRemoteQueueSinkNode setDelegate:];
-[BWRemoteQueueSinkNode sceneStabilityMetadataEnabled];
-[BWRemoteQueueSinkNode setPanoramaRequiresLTMLocking:];
-[BWRemoteQueueSinkNode setAttachPanoramaMetadata:];
-[BWRemoteQueueSinkNode handleDroppedSample:forInput:];
-[BWRemoteQueueSinkNode delegate];
-[BWRemoteQueueSinkNode didReachEndOfDataForConfigurationID:input:];
-[BWRemoteQueueSinkNode initWithMediaType:clientAuditToken:sinkID:cameraInfoByPortType:];
-[BWRemoteQueueSinkNode panoramaRequiresLTMLocking];
-[BWRemoteQueueSinkNode setClientVideoRetainedBufferCount:];
-[BWRemoteQueueSinkNode attachPanoramaMetadata];
-[BWRemoteQueueSinkNode nodeSubType];
-[BWRemoteQueueSinkNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWRemoteQueueSinkNode registerSurfacesFromSourcePool:];
-[BWRemoteQueueSinkNode requestedBufferAttachmentsTrie];
```
