# `CSVTUITrainingSessionWithPayload`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CSVTUITrainingSession`
- Protocols: `SFSpeechRecognitionTaskDelegate`, `_TtP18SpeakerRecognition32SSRSpeechTranscriberIntfDelegate_`, `CSVTUIAudioSessionDelegate`, `CSVTUIEndPointDelegate`
- 9 instance variables, 5 properties, 32 instance methods, 0 class methods

## Instance variables

```
B _detectBOS;
B _ASRResultReceived;
B _reportedStopListening;
B _utteranceStored;
B _awaitingTranscriberFinal;
Q _numSamplesFed;
Q _bestTriggerSampleStart;
Q _extraSamplesAtStart;
@"NSDictionary" _voiceTriggerEventInfo;
```

## Properties

```
@property (T@"NSDictionary",&,N,V_voiceTriggerEventInfo) voiceTriggerEventInfo;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CSVTUITrainingSessionWithPayload setVoiceTriggerEventInfo:];
-[CSVTUITrainingSessionWithPayload voiceTriggerEventInfo];
-[CSVTUITrainingSessionWithPayload speechRecognitionTask:didFinishRecognition:];
-[CSVTUITrainingSessionWithPayload speechRecognitionTask:didFinishSuccessfully:];
-[CSVTUITrainingSessionWithPayload speechRecognitionTask:didHypothesizeTranscription:];
-[CSVTUITrainingSessionWithPayload _deferCloseForTranscriberFinal];
-[CSVTUITrainingSessionWithPayload _firedEndPointTimeout];
-[CSVTUITrainingSessionWithPayload _firedTranscriberFinalTimeout];
-[CSVTUITrainingSessionWithPayload _firedVoiceTriggerTimeout];
-[CSVTUITrainingSessionWithPayload _getSessionEOSTimeout];
-[CSVTUITrainingSessionWithPayload _handleFinalResult:];
-[CSVTUITrainingSessionWithPayload _handlePartialText:shouldWaitForFinal:];
-[CSVTUITrainingSessionWithPayload _registerEndPointTimeout];
-[CSVTUITrainingSessionWithPayload _registerForceEndPointTimeout];
-[CSVTUITrainingSessionWithPayload _registerTranscriberFinalTimeout];
-[CSVTUITrainingSessionWithPayload _registerVoiceTriggerTimeout];
-[CSVTUITrainingSessionWithPayload _reportStopListening];
-[CSVTUITrainingSessionWithPayload audioSessionDidStartRecording:error:];
-[CSVTUITrainingSessionWithPayload audioSessionDidStopRecording:];
-[CSVTUITrainingSessionWithPayload audioSessionErrorDidOccur:];
-[CSVTUITrainingSessionWithPayload audioSessionRecordBufferAvailable:];
-[CSVTUITrainingSessionWithPayload audioSessionUnsupportedAudioRoute];
-[CSVTUITrainingSessionWithPayload closeSessionWithStatus:successfully:];
-[CSVTUITrainingSessionWithPayload didDetectBeginOfSpeech];
-[CSVTUITrainingSessionWithPayload didDetectEndOfSpeech:];
-[CSVTUITrainingSessionWithPayload handleAudioInput:];
-[CSVTUITrainingSessionWithPayload matchRecognitionResult:withMatchedBlock:withNonMatchedBlock:];
-[CSVTUITrainingSessionWithPayload shouldHandleSession];
-[CSVTUITrainingSessionWithPayload shouldMatchPayload];
-[CSVTUITrainingSessionWithPayload speechTranscriber:didReceiveFinalResult:];
-[CSVTUITrainingSessionWithPayload speechTranscriber:didReceivePartialResult:];
-[CSVTUITrainingSessionWithPayload startTraining];
```
