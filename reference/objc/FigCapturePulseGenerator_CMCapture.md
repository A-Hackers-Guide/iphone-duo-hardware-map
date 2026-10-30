# `FigCapturePulseGenerator`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 33 instance variables, 4 properties, 42 instance methods, 3 class methods

## Instance variables

```
^v _deviceHandle;
^v _msgHandleLeader;
^v _msgHandleRear;
^v _msgHandleFront;
^v _msgHandleAltCluster;
B _hasNotifiedDelegateOfClockCreation;
B _disciplinedMSGTimeSyncClock;
Q _timeSyncMSGClockIdentifier;
^v _timeSyncClockRef;
{applemsg_sync_derived_config="timer_sel"I"repeat"B"frame_skip"S"polarity"I"start_base_frame"S"assert_duration"{applemsg_time="whole"q"frac"S"remainder_numerator"S"remainder_denominator"S}"offset"{applemsg_time="whole"q"frac"S"remainder_numerator"S"remainder_denominator"S}} _activeDerivedSyncConfig;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _configureLock;
@"FigCaptureMSGScheduling" _msgScheduling;
B _isExternalSync;
I _uniqueID;
{?="u"(?="rational"{?="numerator"i"denominator"i}"floating"f)"tag"i} _currentFrameRate;
B _timeSyncClockReady;
@"NSString" _loggingPrefix;
@"NSObject<OS_dispatch_source>" _deferredStopTimer;
@"NSObject<OS_dispatch_queue>" _deferredStopQueue;
@"NSObject<OS_dispatch_source>" _compensationDelayTimer;
Q _pendingCompensationOffsetTicks;
Q _pendingCompensationFrameDurationTicks;
Q _desiredCompensationOffsetTicks;
Q _lastAppliedCompensationOffsetTicks;
B _hasPendingCompensationOffset;
@"NSObject<OS_dispatch_source>" _rampDownCompletionTimer;
S _rampDownStartFrame;
Q _rampDownFrameDurationTicks;
B _hasInFlightRampDown;
B _isNotifyingUpdating;
B _msgDebugInterrupts;
@"<FigCapturePulseGeneratorDelegate>" _delegate;
@"<FigCapturePulseGeneratorManagerDelegate>" _managerDelegate;
```

## Properties

```
@property (TI,R,N,V_uniqueID) uniqueID;
@property (TB,R,N,GisTimeSyncClockReady,V_timeSyncClockReady) timeSyncClockReady;
@property (T@"<FigCapturePulseGeneratorDelegate>",W,N,V_delegate) delegate;
@property (T@"<FigCapturePulseGeneratorManagerDelegate>",W,N,V_managerDelegate) managerDelegate;
```

## Class methods

```
+[FigCapturePulseGenerator initialize];
+[FigCapturePulseGenerator kFigCapturePulseGeneratorDeferredStopDelay];
+[FigCapturePulseGenerator kV5XTriggerID];
```

## Instance methods

```
-[FigCapturePulseGenerator stopRunning];
-[FigCapturePulseGenerator debugDescription];
-[FigCapturePulseGenerator _resetState];
-[FigCapturePulseGenerator dealloc];
-[FigCapturePulseGenerator uniqueID];
-[FigCapturePulseGenerator initWithUniqueID:];
-[FigCapturePulseGenerator invalidate];
-[FigCapturePulseGenerator setDelegate:];
-[FigCapturePulseGenerator delegate];
-[FigCapturePulseGenerator _followSyncInit:leader:trigger:];
-[FigCapturePulseGenerator managerDelegate];
-[FigCapturePulseGenerator _applyPendingCompensationOffset];
-[FigCapturePulseGenerator _armRampDownCompletionTimerIfNeeded];
-[FigCapturePulseGenerator _cancelCompensationDelayTimer];
-[FigCapturePulseGenerator _cancelDeferredStop];
-[FigCapturePulseGenerator _configureFollowSync:assertDur:offset:];
-[FigCapturePulseGenerator _configureLeaderSync:frameRate:assertDur:];
-[FigCapturePulseGenerator _disciplineMSGTimeSyncClock:];
-[FigCapturePulseGenerator _followSyncConfig:config:];
-[FigCapturePulseGenerator _getOrCreateTimeSyncMSGClockIdentifier:tsClockIdentifierOut:];
-[FigCapturePulseGenerator _getTimeSyncClock:clockOut:];
-[FigCapturePulseGenerator _leaderSyncConfig:config:];
-[FigCapturePulseGenerator _leaderSyncInit:trigger:];
-[FigCapturePulseGenerator _notifyDelegate:withError:];
-[FigCapturePulseGenerator _resetMsgSyncs];
-[FigCapturePulseGenerator _scheduleDeferredStop];
-[FigCapturePulseGenerator _scheduledApplyToAllFollowersWithOffsetTicks:frameSkip:atLeaderFrameIndex:];
-[FigCapturePulseGenerator _setTimeSyncClockReady:];
-[FigCapturePulseGenerator _startSync:];
-[FigCapturePulseGenerator _startSyncs:];
-[FigCapturePulseGenerator _syncInterruptDisable:];
-[FigCapturePulseGenerator _syncInterruptEnable:];
-[FigCapturePulseGenerator _syncReset:];
-[FigCapturePulseGenerator activeDerivedSyncOffsetWhole];
-[FigCapturePulseGenerator applySignalCompensationDelay:];
-[FigCapturePulseGenerator copyClientAudioClockDeviceUID:];
-[FigCapturePulseGenerator desiredCompensationOffsetTicks];
-[FigCapturePulseGenerator isTimeSyncClockReady];
-[FigCapturePulseGenerator lastAppliedCompensationOffsetTicks];
-[FigCapturePulseGenerator setMSGDebugInterrupts:];
-[FigCapturePulseGenerator setManagerDelegate:];
-[FigCapturePulseGenerator startWithFrameRate:cmClock:externalSync:];
```
