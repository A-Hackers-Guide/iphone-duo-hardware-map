# `VTAggregator`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 0 properties, 30 instance methods, 1 class methods

## Instance variables

```
Q _currentState;
d _lastAggTime;
d _cumulativeUptime;
d _cumulativeDowntime;
d _lastAggTimeFalseWakeUp;
Q _numFalseWakeUp;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_dispatch_source>" _timer;
@"NSString" _languageCode;
@"NSString" _assetString;
```

## Class methods

```
+[VTAggregator sharedAggregator];
```

## Instance methods

```
-[VTAggregator init];
-[VTAggregator setLanguageCode:];
-[VTAggregator logFalseWakeUp:];
-[VTAggregator logTdPsrSATDetectionWaitTimeMs:];
-[VTAggregator setAssetString:];
-[VTAggregator _addValueForScalarKey:withValue:];
-[VTAggregator _logUptime];
-[VTAggregator _makeKey:];
-[VTAggregator _makeKeyWithLanguageAndAssetString:];
-[VTAggregator _makeKeyWithLanguageCode:];
-[VTAggregator _pushValueForDistributionKey:withValue:];
-[VTAggregator cumulativeUptime:cumulativeDowntime:reset:];
-[VTAggregator logActivation];
-[VTAggregator logProfileUpdateNumDeletedUttsStrategy:];
-[VTAggregator logProfileUpdateNumDiscardedUttsPHS:];
-[VTAggregator logProfileUpdateNumPrunedUttsPHS:];
-[VTAggregator logProfileUpdateNumRetainedUttsPHS:];
-[VTAggregator logProfileUpdateScoreMSE:];
-[VTAggregator logProfileUpdateUtt:withScore:];
-[VTAggregator logRecognizerTimedOut];
-[VTAggregator logSecondPassResult:];
-[VTAggregator logTdPsrExtraAudioSamplesProcessed:];
-[VTAggregator logTdPsrFailedDuringSATDetection];
-[VTAggregator logTdPsrFailedDuringSATRetraining];
-[VTAggregator logTdPsrSATDetectionTimedOut];
-[VTAggregator logTdPsrSATRetrainingTimedOut];
-[VTAggregator logTdPsrSATRetrainingWaitTimeMs:];
-[VTAggregator logTimeVoiceTriggerTransitionsToState:];
-[VTAggregator logVoiceProfilePruningFailureWithReasonCode:];
-[VTAggregator logZeroRunAudio:];
```
