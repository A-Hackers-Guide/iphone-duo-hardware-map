# `AVSampleBufferVideoRenderer`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVMediaDataRequesterConsumer`, `AVFigVideoQueueFactory`, `AVQueuedSampleBufferRenderingInternal`, `AVQueuedSampleBufferRendering`
- 50 instance variables, 19 properties, 106 instance methods, 2 class methods

## Instance variables

```
^{OpaqueFigVideoQueue=} _videoQueue;
B _outputObscured;
q _status;
@"NSError" _error;
@"AVSampleBufferDisplayLayer" _weakDisplayLayer;
B _wasConfiguredWithDisplayLayer;
@"FigVideoDestination" _displayLayerVideoDestination;
@"NSMutableArray" _clientVideoDestinations;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _previousSourceRect;
@"AVApplicationStateMonitor" _applicationStateMonitor;
B _preventsDisplaySleepDuringVideoPlayback;
B _preventsAutomaticBackgroundingDuringVideoPlayback;
B _requiresFlushToResumeDecoding;
B _disallowsVideoLayerDisplayCompositing;
B _shouldWaitForVideoTarget;
B _hasEverEnqueued;
B _isRequestingMediaData;
@"AVMediaDataRequester" _mediaDataRequester;
B _readyForDisplay;
B _aboveHighWaterLevel;
B _createVideoQueueFailed;
@"NSString" _preferredDynamicRange;
@"NSObject<OS_dispatch_queue>" _serialQueue;
@"NSObject<OS_dispatch_queue>" _videoQueueQueue;
@"NSObject<OS_dispatch_queue>" _layerQueue;
@"NSObject<OS_dispatch_queue>" _videoPerformanceMetricsQueue;
@"AVSampleBufferRenderSynchronizer" _weakReferenceToSynchronizer;
B _addedToSynchronizer;
B _controlTimebaseSetByUserIsInUse;
^{OpaqueCMTimebase=} _controlTimebaseSetByUser;
^{OpaqueCMTimebase=} _readOnlyVideoQueueTimebase;
^{OpaqueCMTimebase=} _readOnlyRenderingTimebase;
@"NSMutableArray" _videoOutputs;
@"NSObject<OS_dispatch_queue>" _flushCallbackListQueue;
@"NSObject<OS_dispatch_queue>" _flushCallbackQueue;
@"NSMutableArray" _flushCallbacks;
@"NSObject<OS_dispatch_queue>" _queueForProtectingPrerollCompleteCallback;
@? _pendingPrerollCompleteCallback;
i _pendingPrerollRequestID;
@"NSObject<OS_dispatch_queue>" _queueForCallingPrerollCompleteCallback;
i _upcomingPTSExpectation;
{?="value"q"timescale"i"flags"I"epoch"q} _minimumUpcomingPTS;
@"AVContentKeySession" _weakContentKeySession;
^{opaqueCMFormatDescription=} _lastFormatDescription;
^{OpaqueFigCPECryptor=} _lastCryptor;
@"<AVLoggingIdentifier>" _loggingIdentifier;
@"NSString" _STSLabel;
@ _didFinishSuspensionNotificationToken;
@? _cancelPendingSwiftAsyncEnqueueHandler;
@? _readyForMoreMediaDataHandler;
```

## Properties

```
@property (TB,R) outputObscuredDueToInsufficientExternalProtection;
@property (TB,N) preventsCapture;
@property (TB,N) preventsDisplaySleepDuringVideoPlayback;
@property (TB,N) preventsAutomaticBackgroundingDuringVideoPlayback;
@property (TB,G_disallowsVideoLayerDisplayCompositing,S_setDisallowsVideoLayerDisplayCompositing:) disallowsVideoLayerDisplayCompositing;
@property (T@"NSArray",R,N) outputs;
@property (T@"NSString",C,N,G_STSLabel) STSLabel;
@property (T@?,C,N,G_cancelPendingSwiftAsyncEnqueueHandler,S_setCancelPendingSwiftAsyncEnqueueHandler:) cancelPendingSwiftAsyncEnqueueHandler;
@property (T@?,C,N,G_readyForMoreMediaDataHandler,S_setReadyForMoreMediaDataHandler:) readyForMoreMediaDataHandler;
@property (Tq,R) status;
@property (T@"NSError",R) error;
@property (TB,R) requiresFlushToResumeDecoding;
@property (TB,R,GisReadyForMoreMediaData) readyForMoreMediaData;
@property (TB,R,N) hasSufficientMediaDataForReliablePlaybackStart;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T^{OpaqueCMTimebase=},R,&) timebase;
```

## Class methods

```
+[AVSampleBufferVideoRenderer initialize];
+[AVSampleBufferVideoRenderer automaticallyNotifiesObserversForKey:];
```

## Instance methods

```
-[AVSampleBufferVideoRenderer outputs];
-[AVSampleBufferVideoRenderer removeOutput:];
-[AVSampleBufferVideoRenderer timebase];
-[AVSampleBufferVideoRenderer _setRequiresFlushToResumeDecoding:];
-[AVSampleBufferVideoRenderer setToneMapToStandardDynamicRange:];
-[AVSampleBufferVideoRenderer _disallowsVideoLayerDisplayCompositing];
-[AVSampleBufferVideoRenderer _updateVideoTargetsOnVideoQueue];
-[AVSampleBufferVideoRenderer setControlTimebase:];
-[AVSampleBufferVideoRenderer flushWithRemovalOfDisplayedImage:completionHandler:];
-[AVSampleBufferVideoRenderer setDisplayLayerVisibility:];
-[AVSampleBufferVideoRenderer outputObscuredDueToInsufficientExternalProtection];
-[AVSampleBufferVideoRenderer _updatePreferredDynamicRange];
-[AVSampleBufferVideoRenderer addSampleBufferDisplayLayer:];
-[AVSampleBufferVideoRenderer attachToContentKeySession:contentKeyBoss:failedSinceAlreadyAttachedToAnotherSession:];
-[AVSampleBufferVideoRenderer setPreferredDynamicRange:];
-[AVSampleBufferVideoRenderer recommendedPixelBufferAttributes];
-[AVSampleBufferVideoRenderer _setStatus:error:];
-[AVSampleBufferVideoRenderer _cancelPendingSwiftAsyncEnqueueHandler];
-[AVSampleBufferVideoRenderer isReadyForDisplay];
-[AVSampleBufferVideoRenderer resetUpcomingSampleBufferPresentationTimeExpectations];
-[AVSampleBufferVideoRenderer isReadyForMoreMediaData];
-[AVSampleBufferVideoRenderer videoPerformanceMetrics];
-[AVSampleBufferVideoRenderer stopRequestingMediaData];
-[AVSampleBufferVideoRenderer _setUpcomingPresentationTimeExpectations:minimumPresentationTime:];
-[AVSampleBufferVideoRenderer _didFinishSuspension:];
-[AVSampleBufferVideoRenderer init];
-[AVSampleBufferVideoRenderer flush];
-[AVSampleBufferVideoRenderer setPreventsCapture:];
-[AVSampleBufferVideoRenderer hasSufficientMediaDataForReliablePlaybackStart];
-[AVSampleBufferVideoRenderer controlTimebase];
-[AVSampleBufferVideoRenderer videoQueueErrorRequiresRebuild:];
-[AVSampleBufferVideoRenderer copyVideoQueue];
-[AVSampleBufferVideoRenderer setVideoLayerGeometryFlipped:];
-[AVSampleBufferVideoRenderer _completedDecodeForPrerollForRequestID:];
-[AVSampleBufferVideoRenderer addVideoTarget:];
-[AVSampleBufferVideoRenderer dealloc];
-[AVSampleBufferVideoRenderer requestMediaDataWhenReadyOnQueue:usingBlock:];
-[AVSampleBufferVideoRenderer setPreventsAutomaticBackgroundingDuringVideoPlayback:];
-[AVSampleBufferVideoRenderer expectMonotonicallyIncreasingUpcomingSampleBufferPresentationTimes];
-[AVSampleBufferVideoRenderer _statusString:];
-[AVSampleBufferVideoRenderer preferredDynamicRange];
-[AVSampleBufferVideoRenderer enqueueSampleBuffer:];
-[AVSampleBufferVideoRenderer requiresFlushToResumeDecoding];
-[AVSampleBufferVideoRenderer status];
-[AVSampleBufferVideoRenderer _refreshAboveHighWaterLevelAndAlwaysStartRequestMediaDataIfRequesting:];
-[AVSampleBufferVideoRenderer _addFigVideoQueueListeners];
-[AVSampleBufferVideoRenderer _setDisallowsVideoLayerDisplayCompositing:];
-[AVSampleBufferVideoRenderer _copyVideoQueue];
-[AVSampleBufferVideoRenderer _updateVideoOutputs];
-[AVSampleBufferVideoRenderer _setUpFigVideoQueueControlTimebase:];
-[AVSampleBufferVideoRenderer _createVideoQueue:errorStep:];
-[AVSampleBufferVideoRenderer error];
-[AVSampleBufferVideoRenderer preventsDisplaySleepDuringVideoPlayback];
-[AVSampleBufferVideoRenderer createVideoQueue:];
-[AVSampleBufferVideoRenderer enqueueSampleBuffer:bufferEnqueueingInfo:];
-[AVSampleBufferVideoRenderer _unitTest_simulateLostDecoderState];
-[AVSampleBufferVideoRenderer _readOnlyVideoQueueTimebase];
-[AVSampleBufferVideoRenderer expectMinimumUpcomingSampleBufferPresentationTime:];
-[AVSampleBufferVideoRenderer _commonLoggingIdentifier];
-[AVSampleBufferVideoRenderer setContentKeySession:];
-[AVSampleBufferVideoRenderer _fireDisplayLayerNotificationNowThenReleaseOnMainThread:userInfo:];
-[AVSampleBufferVideoRenderer setSTSLabel:];
-[AVSampleBufferVideoRenderer _allVideoDestinations];
-[AVSampleBufferVideoRenderer _enqueueSingleSampleBuffer:bufferEnqueueingInfo:];
-[AVSampleBufferVideoRenderer _nameForLogging];
-[AVSampleBufferVideoRenderer _removeFigVideoQueueListeners];
-[AVSampleBufferVideoRenderer _flushComplete];
-[AVSampleBufferVideoRenderer _setOutputObscuredDueToInsufficientExternalProtection:];
-[AVSampleBufferVideoRenderer _STSLabelPublisher];
-[AVSampleBufferVideoRenderer attachedToExternalContentKeySession];
-[AVSampleBufferVideoRenderer _isCreateVideoQueueErrorRetryable:];
-[AVSampleBufferVideoRenderer prerollDecodeWithCompletionHandler:];
-[AVSampleBufferVideoRenderer preventsCapture];
-[AVSampleBufferVideoRenderer description];
-[AVSampleBufferVideoRenderer triggerReportForError:description:];
-[AVSampleBufferVideoRenderer _isReadyForMoreMediaDataOnSerialQueue];
-[AVSampleBufferVideoRenderer currentFigVideoQueueFactory];
-[AVSampleBufferVideoRenderer copyFigSampleBufferAudioRenderer:];
-[AVSampleBufferVideoRenderer _readyForMoreMediaDataHandler];
-[AVSampleBufferVideoRenderer _createVideoQueueFailed];
-[AVSampleBufferVideoRenderer _setReadyForMoreMediaDataHandler:];
-[AVSampleBufferVideoRenderer setRenderSynchronizer:error:];
-[AVSampleBufferVideoRenderer addOutput:];
-[AVSampleBufferVideoRenderer contentKeySession];
-[AVSampleBufferVideoRenderer _allVideoDestinationsOnSerialQueue];
-[AVSampleBufferVideoRenderer preventsAutomaticBackgroundingDuringVideoPlayback];
-[AVSampleBufferVideoRenderer simulateOrphanedSynchronizerStateForTesting];
-[AVSampleBufferVideoRenderer setShouldWaitForVideoTarget:];
-[AVSampleBufferVideoRenderer shouldWaitForVideoTarget];
-[AVSampleBufferVideoRenderer _hasEverEnqueued];
-[AVSampleBufferVideoRenderer loadVideoPerformanceMetricsWithCompletionHandler:];
-[AVSampleBufferVideoRenderer _callOldPrerollCompletionHandlerWithSuccess:andSetNewPrerollCompletionHandler:forRequestID:];
-[AVSampleBufferVideoRenderer _setSynchronizerTimebase:error:];
-[AVSampleBufferVideoRenderer removeDisplayLayer];
-[AVSampleBufferVideoRenderer setPreventsDisplaySleepDuringVideoPlayback:];
-[AVSampleBufferVideoRenderer _STSLabel];
-[AVSampleBufferVideoRenderer _setCreateVideoQueueFailedWithOSStatus:];
-[AVSampleBufferVideoRenderer isConfiguredWithVideoOutput];
-[AVSampleBufferVideoRenderer _displayLayer];
-[AVSampleBufferVideoRenderer copyDisplayedPixelBuffer];
-[AVSampleBufferVideoRenderer _setContentLayerOnFigVideoQueue:];
-[AVSampleBufferVideoRenderer setReadyForDisplayWithoutKVO:];
-[AVSampleBufferVideoRenderer _initializeTimebases];
-[AVSampleBufferVideoRenderer _setCancelPendingSwiftAsyncEnqueueHandler:];
-[AVSampleBufferVideoRenderer _resetStatusWithOSStatus:];
-[AVSampleBufferVideoRenderer flushAndRemoveImage];
```
