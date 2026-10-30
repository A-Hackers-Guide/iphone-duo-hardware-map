# `BWImageQueueSinkNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWSinkNode`
- 87 instance variables, 6 properties, 33 instance methods, 1 class methods

## Instance variables

```
I _imageQueueCapacity;
I _imageQueueWidth;
I _imageQueueHeight;
I _imageQueueRequiredFreeSlots;
^{_CAImageQueue=} _imageQueue;
I _imageQueueSlot;
Q _imageQueueCurrentFreeSlots;
f _imageQueueNominalFrameRate;
@"CMCaptureFrameSenderService" _frameSender;
{?="val"[8I]} _frameSenderClientAuditToken;
i _syncStrategy;
i _liveSyncStrategy;
B _resetPreviewSynchronizerOnNextFrame;
^{OpaqueBWPreviewSynchronizer=} _previewSynchronizer;
d _lastDisplaySamplingTime;
d _lastDisplayVSyncInterval;
d _lastHarmonicFractionalVSyncInterval;
d _lastFramePTS;
d _lastDisplayTime;
d _lateFrameIntervalStartPTS;
d _previousFrameDuration;
Q _framesSinceLastHarmonicCompensation;
B _CAVSyncIntervalWorkaroundEnabled;
B _highLatencyJitterHandlingEnabled;
B _fasterLatencyRecoveryEnabled;
B _driftCompensationTimestampFilteringEnabled;
@"<BWImageQueueSinkNodePreviewTapDelegate>" _previewTapDelegate;
Q _numFramesReceivedForCurrentConfiguration;
{?="value"q"timescale"i"flags"I"epoch"q} _firstReceivedFramePTSBeforeFirstDisplayTimeout;
B _receivingBlackenedFrames;
B _receivingIndicatorCheckBlackenedFrames;
Q _numIndicatorCheckBlackenedFramesReceivedInInterval;
@"NSObject<OS_os_transaction>" _holdingBuffersForClientAssertion;
@"NSMutableArray" _sharedSurfaces;
^Q _sharedBufferIDs;
Q _sharedSurfaceCount;
^{OpaqueFigSimpleMutex=} _surfaceRegistrationMutex;
@"NSMutableArray" _bufferIDsInQueue;
^^{_EnqueuedBufferContext} _enqueuedBufferContexts;
Q _enqueuedBufferContextCount;
B _displayingIndicatorCheckBlackenedFrames;
Q _numIndicatorCheckBlackenedFramesDisplayedInInterval;
B _didFileBlackenedFrameRadar;
{?="value"q"timescale"i"flags"I"epoch"q} _indicatorCheckToleranceBaselinePTS;
@"NSMutableArray" _previewPTSHistory;
^{OpaqueFigSimpleMutex=} _previewPTSHistoryMutex;
@"NSObject<OS_dispatch_queue>" _previewPTSHistoryQueue;
B _resetFirstFrameStateOnConfigurationLive;
{?="value"q"timescale"i"flags"I"epoch"q} _firstFramePTS;
q _firstDisplayedFrameHostTime;
B _didCallFirstFrameAtHostTimeCallback;
B _didCallFirstFrameCallback;
q _previewStartedForCurrentConfigurationHostTime;
q _firstDisplayedFrameForCurrentConfigurationHostTime;
B _didCallFirstFrameForCurrentConfiguration;
B _didEmitFirstFrameSignpost;
{?="value"q"timescale"i"flags"I"epoch"q} _firstDisplayedFrameWithoutBlackeningPTS;
q _firstDisplayedFrameWithoutBlackeningHostTime;
{?="value"q"timescale"i"flags"I"epoch"q} _firstOverCaptureDisplayedFramePTS;
q _firstOverCaptureDisplayedFrameHostTime;
B _didLogFirstOverCaptureFrame;
B _triggerDisplayTimeout;
B _fenceSupportEnabled;
B _fencePortGenerationIDWillChange;
i _framesSinceLastFenceIDWillChange;
i _framesSinceLastFence;
q _lastFencedGenerationID;
i _savedSyncStrategy;
@"CAContext" _imageQueueContext;
i _maxLossyCompressionLevel;
{FigCaptureVideoTransform="mirrored"B"rotationDegrees"i"dimensions"{?="width"i"height"i}} _transform;
@"BWStats" _frameDisplayLatencyStats;
@"BWFigVideoCaptureDevice" _captureDevice;
i _clientPID;
{?="val"[8I]} _clientAuditToken;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _clientPIDLock;
B _videoHDRImageStatisticsEnabled;
B _liveVideoHDRImageStatisticsEnabled;
@"BWLimitedGMErrorLogger" _limitedGMErrorLogger;
B _cleanupImageQueueAtEndOfData;
{?="value"q"timescale"i"flags"I"epoch"q} _firstEnqueuePTS;
{?="value"q"timescale"i"flags"I"epoch"q} _lastMonitoredPTS;
@"FigCaptureFrameRateMonitor" _frameRateMonitor;
B _frameRateEnforcementEnabled;
B _frameRateEnforcementTTREnabled;
B _didEnforceFrameRate;
@"FigCaptureWorkInterval" _workInterval;
```

## Properties

```
@property (T^{_CAImageQueue=},R,N) imageQueue;
@property (TI,R,N) imageQueueSlot;
@property (T@"<BWImageQueueSinkNodePreviewTapDelegate>",N,V_previewTapDelegate) previewTapDelegate;
@property (T@"BWFigVideoCaptureDevice",&,N,V_captureDevice) captureDevice;
@property (TB,N,V_cleanupImageQueueAtEndOfData) cleanupImageQueueAtEndOfData;
@property (T@"FigCaptureFrameRateMonitor",R,N) frameRateMonitor;
```

## Class methods

```
+[BWImageQueueSinkNode initialize];
```

## Instance methods

```
-[BWImageQueueSinkNode updateClientAuditToken:];
-[BWImageQueueSinkNode videoHDRImageStatisticsEnabled];
-[BWImageQueueSinkNode prepareForCurrentConfigurationToBecomeLive];
-[BWImageQueueSinkNode setVideoHDRImageStatisticsEnabled:];
-[BWImageQueueSinkNode setCaptureDevice:];
-[BWImageQueueSinkNode renderSampleBuffer:forInput:];
-[BWImageQueueSinkNode setFenceSupportEnabled:];
-[BWImageQueueSinkNode imageQueueSlot];
-[BWImageQueueSinkNode setMaxLossyCompressionLevel:];
-[BWImageQueueSinkNode captureDevice];
-[BWImageQueueSinkNode syncStrategy];
-[BWImageQueueSinkNode maxLossyCompressionLevel];
-[BWImageQueueSinkNode previewTapDelegate];
-[BWImageQueueSinkNode dealloc];
-[BWImageQueueSinkNode initWithHFRSupport:ispJitterCompensationEnabled:clientAuditToken:sinkID:frameRateEnforcementEnabled:sharesBuffersWithPrimaryImageQueue:];
-[BWImageQueueSinkNode setCleanupImageQueueAtEndOfData:];
-[BWImageQueueSinkNode frameRateMonitor];
-[BWImageQueueSinkNode setTransform:];
-[BWImageQueueSinkNode hasNonLiveConfigurationChanges];
-[BWImageQueueSinkNode transform];
-[BWImageQueueSinkNode previewPTSDisplayedAtHostTime:allowingExtrapolation:];
-[BWImageQueueSinkNode cleanupImageQueueAtEndOfData];
-[BWImageQueueSinkNode handleDroppedSample:forInput:];
-[BWImageQueueSinkNode didReachEndOfDataForConfigurationID:input:];
-[BWImageQueueSinkNode inputConnectionWillBeEnabled];
-[BWImageQueueSinkNode fencePortGenerationIDWillChange];
-[BWImageQueueSinkNode nodeSubType];
-[BWImageQueueSinkNode imageQueue];
-[BWImageQueueSinkNode fenceSupportEnabled];
-[BWImageQueueSinkNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWImageQueueSinkNode setPreviewTapDelegate:];
-[BWImageQueueSinkNode registerSurfacesFromSourcePool:];
-[BWImageQueueSinkNode setSyncStrategy:];
```
