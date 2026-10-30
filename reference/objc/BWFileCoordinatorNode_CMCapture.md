# `BWFileCoordinatorNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 94 instance variables, 0 properties, 30 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _stagingQueues;
@"NSMutableArray" _pendingIrisRequestMarkerBuffers;
@"FigCaptureRecordingSettings" _settings;
q _currSettingsID;
@"NSArray" _recordingStagingQueues;
i _recordingStagingQueueLimitForVideo;
B _currSettingsPrefersNoInterruptionsByRingtonesAndAlerts;
B _currSettingsIsIris;
B _currSettingsIsIrisMovieRecording;
B _currSettingsIsProRes;
@"NSDictionary" _videoSettings;
{?="u"(?="rational"{?="numerator"i"denominator"i}"floating"f)"tag"i} _maxFrameRate;
@"NSArray" _videoRecordingPrimingQueues;
i _videoRecordingPrimingQueueLimit;
i _recordingState;
@"BWNodeInput" _masterInput;
{?="value"q"timescale"i"flags"I"epoch"q} _inputOffset;
{?="value"q"timescale"i"flags"I"epoch"q} _lastMasterPTS;
{?="value"q"timescale"i"flags"I"epoch"q} _lastMasterDuration;
{?="value"q"timescale"i"flags"I"epoch"q} _lastMasterEndingPTS;
{?="value"q"timescale"i"flags"I"epoch"q} _masterStartingPTS;
{?="value"q"timescale"i"flags"I"epoch"q} _largestStagedSupportingAudioVideoStagedPTS;
{?="value"q"timescale"i"flags"I"epoch"q} _largestAudioPTS;
{?="value"q"timescale"i"flags"I"epoch"q} _largestMetadataPTS;
{?="value"q"timescale"i"flags"I"epoch"q} _masterStoppingPTS;
{?="value"q"timescale"i"flags"I"epoch"q} _stopRecordingPTS;
{?="value"q"timescale"i"flags"I"epoch"q} _stopRecordingAudioOffset;
{?="value"q"timescale"i"flags"I"epoch"q} _stopRecordingObservedLastVideoPTS;
{?="value"q"timescale"i"flags"I"epoch"q} _focusWaitTimeStart;
{?="value"q"timescale"i"flags"I"epoch"q} _torchWaitTimeStart;
{?="value"q"timescale"i"flags"I"epoch"q} _startAfterPTS;
d _focusWaitTime;
d _torchWaitTime;
d _maxFocusWaitTime;
i _firstFrameFocusingMethod;
i _firstFrameAFStatus;
i _numberOfFocusWaitBuffersDropped;
i _numberOfTorchWaitBuffersDropped;
B _focusWaitTimedOut;
B _sendFlushMarkerWhenStopping;
B _haveSeenAudioWhenStarting;
B _lowLatencyCanTransitionEarlyToRecording;
B _lowLatencyCanTossExtraVideoWhenStopping;
B _firstAudioHasBeenProcessed;
^B _haveSeenAudioWhenStartingForIndex;
^B _lowLatencyCanTransitionEarlyToRecordingForIndex;
^B _firstAudioHasBeenProcessedForIndex;
i _terminationErrorCode;
^{OpaqueCMBlockBuffer=} _emptyMetadataSampleData;
r^^{opaqueCMFormatDescription} _formatDescriptionsForInputs;
^{OpaqueFigSimpleMutex=} _stateMutex;
Q _numInputs;
Q _numOutputs;
Q _numVideoInputs;
Q _numAudioInputs;
Q _numMetadataInputs;
Q _numActionOnlyOutputs;
Q _masterInputIndex;
Q _firstAudioInputIndex;
@"NSMutableArray" _idleInputIndicesWaitingForFlush;
B _lowLatencyModeEnabled;
B _flagsLastFrameForVideoCompressor;
B _overCaptureEnabled;
B _overCaptureIsRequested;
B _overCaptureActiveSlaveStreamForcedOff;
B _attachOverCaptureActiveSlaveStreamForcedOffMarkerBuffer;
{?="value"q"timescale"i"flags"I"epoch"q} _firstAudioPTSReadyForRecording;
@"<BWAudioSourceRecordingReadinessDelegate>" _audioSourceDelegate;
@"<BWNodeFileCoordinatorStatusDelegate>" _fileCoordinatorStatusDelegate;
@"BWMotionDataTimeMachine" _motionDataTimeMachine;
@"NSMutableArray" _videoSampleBuffersWaitingForMetadata;
Q _cinematicLookAheadFrameCount;
Q _pendingMotionDataSerialNumber;
Q _largestEmittedLookAheadMotionDataSerialNumber;
B _lookAheadMotionDataPreloadHasBeenAttached;
B _receivedFinalEnqueuedIrisReferenceRequest;
B _timewarpEnabled;
{?="value"q"timescale"i"flags"I"epoch"q} _timewarpFrameDuration;
{?="value"q"timescale"i"flags"I"epoch"q} _timewarpFrameDurationForCapture;
{?="value"q"timescale"i"flags"I"epoch"q} _currTimewarpPTS;
Q _droppedFramesCountDueToISP;
@"NSString" _lastPortType;
i _maxNumberOfConsecutiveVideoFramesAllowedToBeMissingLux;
^i _currNumberOfConsecutiveVideoFramesMissingLux;
^@ _lastSeenLuxMetadata;
@"NSObject<OS_dispatch_semaphore>" _recordingStoppedSemaphore;
B _haveSetupWaitingForRecordingStopState;
i _numEODMessagesReceived;
^i _numBuffersReceivedDuringStartingRecording;
^{?=qiIq} _earliestPTSReceivedDuringStartingRecording;
^{?=qiIq} _latestPTSReceivedDuringStartingRecording;
i _startRecordingTimeoutInSeconds;
@"NSObject<OS_dispatch_source>" _startRecordingTimer;
i _movieRecordingEndOfDataBehavior;
```

## Class methods

```
+[BWFileCoordinatorNode initialize];
```

## Instance methods

```
-[BWFileCoordinatorNode setCinematicLookAheadFrameCount:];
-[BWFileCoordinatorNode renderSampleBuffer:forInput:];
-[BWFileCoordinatorNode flagsLastFrameForVideoCompressor];
-[BWFileCoordinatorNode audioSourceDelegate];
-[BWFileCoordinatorNode init];
-[BWFileCoordinatorNode dealloc];
-[BWFileCoordinatorNode recordingTerminated:];
-[BWFileCoordinatorNode cancelStartRecordingWithSettings:];
-[BWFileCoordinatorNode hasNonLiveConfigurationChanges];
-[BWFileCoordinatorNode resumeRecording];
-[BWFileCoordinatorNode stopRecordingWithErrorCode:setupToAllowWaitingForRecordingToStop:];
-[BWFileCoordinatorNode movieRecordingEndOfDataBehavior];
-[BWFileCoordinatorNode startRecordingWithSettings:videoSettings:maxFrameRate:stopAtPTS:startAfterPTS:];
-[BWFileCoordinatorNode setAudioSourceDelegate:];
-[BWFileCoordinatorNode setFileCoordinatorStatusDelegate:];
-[BWFileCoordinatorNode setMovieRecordingEndOfDataBehavior:];
-[BWFileCoordinatorNode waitForRecordingToStopWithTimeout:];
-[BWFileCoordinatorNode handleDroppedSample:forInput:];
-[BWFileCoordinatorNode updateStopPTS:audioOffset:previousStopPTS:previousAudioOffset:];
-[BWFileCoordinatorNode didReachEndOfDataForConfigurationID:input:];
-[BWFileCoordinatorNode setFlagsLastFrameForVideoCompressor:];
-[BWFileCoordinatorNode fileCoordinatorStatusDelegate];
-[BWFileCoordinatorNode initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:numberOfActionOnlyOutputs:overCaptureEnabled:cinematicAudioEnabled:allowLowLatencyWhenPossible:timewarpTargetFramerate:useTrueVideoFileRecordingStaging:motionDataTimeMachine:videoRecordingPrimingQueueLimit:];
-[BWFileCoordinatorNode nodeSubType];
-[BWFileCoordinatorNode cinematicLookAheadFrameCount];
-[BWFileCoordinatorNode didSelectFormat:forInput:];
-[BWFileCoordinatorNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWFileCoordinatorNode tryToEmitFramesWaitingForMotion];
-[BWFileCoordinatorNode nodeType];
-[BWFileCoordinatorNode pauseRecording];
```
