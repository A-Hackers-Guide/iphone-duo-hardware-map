# `BWAudioSourceNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWSourceNode`
- Protocols: `BWAudioSourceRecordingReadinessDelegate`, `BWZoomCompletionDelegate`
- 69 instance variables, 9 properties, 44 instance methods, 2 class methods

## Instance variables

```
[3@"BWNodeOutput"] _outputsByMicSourcePosition;
@"NSDictionary" _sourceRequirements;
@"AVAudioSession" _audioSession;
@"NSString" _MXSessionAudioMode;
B _useDecoupledIO;
B _prefersNoInterruptionsByRingtonesAndAlerts;
@"NSObject<OS_dispatch_queue>" _audioSessionSetRecordingRelatedPropertyQueue;
B _audioSessionIsProxy;
B _doNotResetAudioCategoryOnNextInactive;
B _keepAudioSessionActiveOnStop;
B _isConfiguredForContinuityCapture;
B _didBeginInterruption;
B _doEndInterruption;
B _isAppAudioSession;
B _configuresSession;
B _mixWithOthersEnabled;
B _allowHQBluetoothRecording;
d _sessionRequiredSampleRate;
{?="val"[8I]} _clientAuditToken;
i _clientPID;
Q _clientSDKVersionToken;
@"NSString" _clientAudioClockDeviceUID;
@"NSNumber" _preferredIOBufferDuration;
^{OpaqueCMClock=} _clock;
I _audioDeviceID;
^{opaqueCMFormatDescription=} _auOutputFormatDescription;
I _pullDuration;
^{OpaqueAudioComponentInstance=} _audioUnit;
I _auSubType;
^{opaqueCMSimpleQueue=} _renderProcErrorQueue;
^{opaqueCMSimpleQueue=} _inactiveBuffersQueue;
^{opaqueCMSimpleQueue=} _activeBuffersQueue;
Q _nextExpectedHostTime;
{?="value"q"timescale"i"flags"I"epoch"q} _nextExpectedSampleTime;
{?="value"q"timescale"i"flags"I"epoch"q} _ioprocTimeStampDeltaLimit;
{?="value"q"timescale"i"flags"I"epoch"q} _prevPTS;
I _prevNumFrames;
@"NSObject<OS_dispatch_queue>" _generateSamplesDispatchQueue;
B _streamStarted;
B _endOfDataMarkerSent;
B _levelMeteringEnabled;
i _audioLevelUnits;
{?="value"q"timescale"i"flags"I"epoch"q} _latencyOffset;
@"NSObject<OS_dispatch_source>" _silenceTimer;
q _auRenderCount;
q _silenceFramesGeneratedSinceLastAURenderProc;
{TimestampedAudioBufferList="allocator"^{__CFAllocator}"auRenderCount"q"dataBytesCapacity"I"numFrames"I"pts"{?="value"q"timescale"i"flags"I"epoch"q}"abl"^{AudioBufferList}"numPrependedSilenceFrames"I"sampleTime"d} _currentSilenceBuffer;
@"NSObject<OS_dispatch_queue>" _preparedToRecordHandlerCallbackQueue;
B _livePhotoCaptureEnabled;
i _audioCaptureMode;
B _windNoiseRemovalEnabled;
B _cinematicVideoCaptureEnabled;
B _videoRecordingEnabled;
B _flipStereoAudioCaptureChannels;
f _stereoAudioCapturePairedCameraBaseFieldOfView;
f _stereoAudioCapturePairedCameraZoomFactor;
@"NSObject<OS_dispatch_queue>" _zoomHandlerQueue;
q _maxZoomFrequencyNanos;
q _nextZoomTime;
@"NSObject<OS_dispatch_source>" _zoomTimer;
f _nextZoomFactor;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _zoomLock;
B _silenceFramesFillingDisabled;
B _audioPlayingToBuiltinSpeaker;
B _isAudioOnlyRecordingSession;
B _stopSourceAsynchronously;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _startGroupLock;
@"NSObject<OS_dispatch_group>" _startGroup;
@"AVAudioFormat" _remoteIOOutputFormat;
```

## Properties

```
@property (T@"NSArray",R,N) audioLevels;
@property (TB,R,N,V_didBeginInterruption) didBeginInterruption;
@property (TB,N,V_doNotResetAudioCategoryOnNextInactive) doNotResetAudioCategoryOnNextInactive;
@property (TB,N,V_keepAudioSessionActiveOnStop) keepAudioSessionActiveOnStop;
@property (TB,N) stopSourceAsynchronously;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWAudioSourceNode initialize];
+[BWAudioSourceNode audioSourceNodeWithAttributes:sessionPreset:clock:doConfigureAudio:doMixWithOthers:doAllowHQBluetoothRecording:audioSession:isAppAudioSession:doEndInterruption:audioSessionIsProxy:audioIsPlayingToBuiltinSpeaker:audioSessionActivatedByBWGraph:clientAuditToken:clientSDKVersionToken:clientOSVersionSupportsDecoupledIO:clientAudioClockDeviceUID:preferredIOBufferDuration:audioCaptureConnectionConfigurations:isConfiguredForContinuityCapture:isAudioOnlyRecordingSession:remoteIOOutputFormat:levelMeteringEnabled:outErr:];
```

## Instance methods

```
-[BWAudioSourceNode setDoNotResetAudioCategoryOnNextInactive:];
-[BWAudioSourceNode start:];
-[BWAudioSourceNode clock];
-[BWAudioSourceNode prepareForCurrentConfigurationToBecomeLive];
-[BWAudioSourceNode setStereoAudioCapturePairedCameraBaseFieldOfView:];
-[BWAudioSourceNode windNoiseRemovalEnabled];
-[BWAudioSourceNode setAudioCaptureMode:];
-[BWAudioSourceNode setWindNoiseRemovalEnabled:];
-[BWAudioSourceNode stereoAudioCapturePairedCameraBaseFieldOfView];
-[BWAudioSourceNode setLivePhotoCaptureEnabled:];
-[BWAudioSourceNode outputForMicSourcePosition:];
-[BWAudioSourceNode doNotResetAudioCategoryOnNextInactive];
-[BWAudioSourceNode setFlipStereoAudioCaptureChannels:];
-[BWAudioSourceNode makeCurrentConfigurationLive];
-[BWAudioSourceNode zoomCommandHandler:didApplyZoomFactor:zoomFactorWithoutFudge:targetZoomFactor:rampComplete:rampCommandID:];
-[BWAudioSourceNode mixWithOthersActive];
-[BWAudioSourceNode isAudioPlayingToBuiltinSpeaker];
-[BWAudioSourceNode audioLevels];
-[BWAudioSourceNode audioCaptureMode];
-[BWAudioSourceNode setStereoAudioCapturePairedCameraZoomFactor:];
-[BWAudioSourceNode setKeepAudioSessionActiveOnStop:];
-[BWAudioSourceNode dealloc];
-[BWAudioSourceNode didBeginInterruption];
-[BWAudioSourceNode makeOutputsLiveIfNeeded];
-[BWAudioSourceNode flipStereoAudioCaptureChannels];
-[BWAudioSourceNode setCinematicVideoCaptureEnabled:];
-[BWAudioSourceNode hasNonLiveConfigurationChanges];
-[BWAudioSourceNode setStopSourceAsynchronously:];
-[BWAudioSourceNode updateWithAudioSession:clientAuditToken:];
-[BWAudioSourceNode setVideoRecordingEnabled:];
-[BWAudioSourceNode prepareToStartRecordingWithOrientation:recordingSettingsID:prefersNoInterruptionsByRingtonesAndAlerts:completionHandler:];
-[BWAudioSourceNode cinematicVideoCaptureEnabled];
-[BWAudioSourceNode livePhotoCaptureEnabled];
-[BWAudioSourceNode stopSourceAsynchronously];
-[BWAudioSourceNode stereoAudioCapturePairedCameraZoomFactor];
-[BWAudioSourceNode mixWithOthersEnabled];
-[BWAudioSourceNode keepAudioSessionActiveOnStop];
-[BWAudioSourceNode unprepareForRecording];
-[BWAudioSourceNode updateStereoAudioCapturePairedCameraBaseFieldOfView:zoomFactor:];
-[BWAudioSourceNode stop:];
-[BWAudioSourceNode nodeSubType];
-[BWAudioSourceNode messageDispatchQueueForOutput:];
-[BWAudioSourceNode videoRecordingEnabled];
-[BWAudioSourceNode setMixWithOthersEnabled:];
```
