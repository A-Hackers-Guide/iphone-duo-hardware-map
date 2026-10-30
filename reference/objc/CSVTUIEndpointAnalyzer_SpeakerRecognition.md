# `CSVTUIEndpointAnalyzer`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SNResultsObserving`
- 25 instance variables, 29 properties, 64 instance methods, 1 class methods

## Instance variables

```
B _isAnchorTimeBuffered;
B _shouldDetectTwoShot;
B _didEnterTwoshot;
B _finishedSkippingSamplesForVT;
@"<CSVTUIEndpointAnalyzerDelegate>" _delegate;
Q _activeChannel;
@"SNAudioStreamAnalyzer" _snAudioStreamAnalyzer;
Q _framePosition;
Q _nnvadState;
Q _numSamplesReceived;
Q _numSamplesProcessedBeforeAnchorTime;
Q _anchorMachAbsTime;
Q _currentRequestSampleRate;
@"AVAudioFormat" _currentRequestAudioFormat;
d _vtEndInSecs;
Q _vtEndInSampleCount;
d _vtExtraAudioAtStartInMs;
d _nnvadAudioOriginInMs;
@"NSObject<OS_dispatch_queue>" _queue;
@"<CSAudioFileWriter>" _audioFileWriter;
d _firstAudioSampleSensorTimestamp;
q _firstSampleId;
Q _numSamplesSkippedForVT;
d _startWaitTime;
d _endWaitTime;
```

## Properties

```
@property (T@"SNAudioStreamAnalyzer",&,N,V_snAudioStreamAnalyzer) snAudioStreamAnalyzer;
@property (TQ,N,V_framePosition) framePosition;
@property (TQ,N,V_nnvadState) nnvadState;
@property (TQ,N,V_numSamplesReceived) numSamplesReceived;
@property (TQ,N,V_numSamplesProcessedBeforeAnchorTime) numSamplesProcessedBeforeAnchorTime;
@property (TQ,N,V_anchorMachAbsTime) anchorMachAbsTime;
@property (TB,N,V_isAnchorTimeBuffered) isAnchorTimeBuffered;
@property (TQ,N,V_currentRequestSampleRate) currentRequestSampleRate;
@property (T@"AVAudioFormat",&,N,V_currentRequestAudioFormat) currentRequestAudioFormat;
@property (Td,N,V_vtEndInSecs) vtEndInSecs;
@property (TQ,N,V_vtEndInSampleCount) vtEndInSampleCount;
@property (Td,N,V_vtExtraAudioAtStartInMs) vtExtraAudioAtStartInMs;
@property (Td,N,V_nnvadAudioOriginInMs) nnvadAudioOriginInMs;
@property (TB,N,V_shouldDetectTwoShot) shouldDetectTwoShot;
@property (TB,N,V_didEnterTwoshot) didEnterTwoshot;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"<CSAudioFileWriter>",&,N,V_audioFileWriter) audioFileWriter;
@property (Td,N,V_firstAudioSampleSensorTimestamp) firstAudioSampleSensorTimestamp;
@property (Tq,N,V_firstSampleId) firstSampleId;
@property (TQ,N,V_numSamplesSkippedForVT) numSamplesSkippedForVT;
@property (TB,N,V_finishedSkippingSamplesForVT) finishedSkippingSamplesForVT;
@property (Td,N,V_startWaitTime) startWaitTime;
@property (Td,N,V_endWaitTime) endWaitTime;
@property (T@"<CSVTUIEndpointAnalyzerDelegate>",W,N,V_delegate) delegate;
@property (TQ,N,V_activeChannel) activeChannel;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CSVTUIEndpointAnalyzer timeStampString];
```

## Instance methods

```
-[CSVTUIEndpointAnalyzer request:didFailWithError:];
-[CSVTUIEndpointAnalyzer audioFileWriter];
-[CSVTUIEndpointAnalyzer setAudioFileWriter:];
-[CSVTUIEndpointAnalyzer init];
-[CSVTUIEndpointAnalyzer queue];
-[CSVTUIEndpointAnalyzer setDelegate:];
-[CSVTUIEndpointAnalyzer delegate];
-[CSVTUIEndpointAnalyzer activeChannel];
-[CSVTUIEndpointAnalyzer setQueue:];
-[CSVTUIEndpointAnalyzer setActiveChannel:];
-[CSVTUIEndpointAnalyzer setFramePosition:];
-[CSVTUIEndpointAnalyzer framePosition];
-[CSVTUIEndpointAnalyzer setEndWaitTime:];
-[CSVTUIEndpointAnalyzer endWaitTime];
-[CSVTUIEndpointAnalyzer setStartWaitTime:];
-[CSVTUIEndpointAnalyzer startWaitTime];
-[CSVTUIEndpointAnalyzer setVtEndInSampleCount:];
-[CSVTUIEndpointAnalyzer vtEndInSampleCount];
-[CSVTUIEndpointAnalyzer firstAudioSampleSensorTimestamp];
-[CSVTUIEndpointAnalyzer anchorMachAbsTime];
-[CSVTUIEndpointAnalyzer currentRequestSampleRate];
-[CSVTUIEndpointAnalyzer handleVoiceTriggerWithActivationInfo:];
-[CSVTUIEndpointAnalyzer isAnchorTimeBuffered];
-[CSVTUIEndpointAnalyzer numSamplesProcessedBeforeAnchorTime];
-[CSVTUIEndpointAnalyzer processAudioSamplesAsynchronously:];
-[CSVTUIEndpointAnalyzer recordingStoppedForReason:];
-[CSVTUIEndpointAnalyzer request:didProduceResult:];
-[CSVTUIEndpointAnalyzer setAnchorMachAbsTime:];
-[CSVTUIEndpointAnalyzer setCurrentRequestSampleRate:];
-[CSVTUIEndpointAnalyzer setFirstAudioSampleSensorTimestamp:];
-[CSVTUIEndpointAnalyzer setIsAnchorTimeBuffered:];
-[CSVTUIEndpointAnalyzer setNumSamplesProcessedBeforeAnchorTime:];
-[CSVTUIEndpointAnalyzer setSnAudioStreamAnalyzer:];
-[CSVTUIEndpointAnalyzer setVtExtraAudioAtStartInMs:];
-[CSVTUIEndpointAnalyzer snAudioStreamAnalyzer];
-[CSVTUIEndpointAnalyzer stopEndpointer];
-[CSVTUIEndpointAnalyzer vtExtraAudioAtStartInMs];
-[CSVTUIEndpointAnalyzer didEnterTwoshot];
-[CSVTUIEndpointAnalyzer _checkSNObservationForEndpoint:];
-[CSVTUIEndpointAnalyzer setVtEndInSecs:];
-[CSVTUIEndpointAnalyzer _checkSNObservationForStartpoint:];
-[CSVTUIEndpointAnalyzer _effectiveAudioTimeInSecsForSNObservation:];
-[CSVTUIEndpointAnalyzer _pcmBufferForAudioChunk:];
-[CSVTUIEndpointAnalyzer _reportEndpointAtTsInSecs:];
-[CSVTUIEndpointAnalyzer _reportStartpointAtTsInSecs:];
-[CSVTUIEndpointAnalyzer currentRequestAudioFormat];
-[CSVTUIEndpointAnalyzer finishedSkippingSamplesForVT];
-[CSVTUIEndpointAnalyzer firstSampleId];
-[CSVTUIEndpointAnalyzer nnvadAudioOriginInMs];
-[CSVTUIEndpointAnalyzer nnvadState];
-[CSVTUIEndpointAnalyzer numSamplesReceived];
-[CSVTUIEndpointAnalyzer numSamplesSkippedForVT];
-[CSVTUIEndpointAnalyzer resetForNewRequestWithSampleRate:];
-[CSVTUIEndpointAnalyzer setCurrentRequestAudioFormat:];
-[CSVTUIEndpointAnalyzer setDidEnterTwoshot:];
-[CSVTUIEndpointAnalyzer setFinishedSkippingSamplesForVT:];
-[CSVTUIEndpointAnalyzer setFirstSampleId:];
-[CSVTUIEndpointAnalyzer setNnvadAudioOriginInMs:];
-[CSVTUIEndpointAnalyzer setNnvadState:];
-[CSVTUIEndpointAnalyzer setNumSamplesReceived:];
-[CSVTUIEndpointAnalyzer setNumSamplesSkippedForVT:];
-[CSVTUIEndpointAnalyzer setShouldDetectTwoShot:];
-[CSVTUIEndpointAnalyzer shouldDetectTwoShot];
-[CSVTUIEndpointAnalyzer vtEndInSecs];
```
