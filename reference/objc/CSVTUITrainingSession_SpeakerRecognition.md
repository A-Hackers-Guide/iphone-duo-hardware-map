# `CSVTUITrainingSession`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SFSpeechRecognitionTaskDelegate`, `_TtP18SpeakerRecognition32SSRSpeechTranscriberIntfDelegate_`, `CSVTUIAudioSessionDelegate`, `CSVTUIEndPointDelegate`
- 34 instance variables, 8 properties, 54 instance methods, 0 class methods

## Instance variables

```
q _status;
q _utteranceId;
q _sessionNumber;
@"NSString" _locale;
@"NSUUID" _mhUUID;
Q _phId;
@"NSString" _vtAssetConfigVersion;
@"<CSVTUIKeywordDetectorProtocol>" _keywordDetector;
@"<CSVTUIAudioSession>" _audioSession;
@"SFSpeechRecognizer" _speechRecognizer;
@"SFSpeechAudioBufferRecognitionRequest" _speechRecognitionRequest;
@"SFSpeechRecognitionTask" _speechRecognitionTask;
@"NSTimer" _masterTimer;
@"NSMutableArray" _pcmBufArray;
B _resultReported;
B _sessionProcess;
B _sessionSuspended;
B _ASRErrorOccured;
B _speechStartDetected;
B _didFirstPassTrigger;
B _snrCheckEnabled;
@"<CSVTUITrainingSessionDelegate>" _sessionDelegate;
@? _trainingCompletion;
@? _trainingCompletionWithResult;
@"NSObject<OS_dispatch_queue>" _queue;
@"CSVTUITrainingSessionHelper" _helper;
q _numRequiredTrailingSamples;
q _numTrailingSamples;
@"CSAudioZeroCounter" _continuousZeroCounter;
B _shouldUseEnhancedSpeechTranscriber;
f _snrThreshold;
@"NSString" _referenceString;
@"_TtC18SpeakerRecognition24SSRSpeechTranscriberIntf" _speechTranscriber;
@"NSDictionary" _voiceTriggerEventInfo;
```

## Properties

```
@property (T@"_TtC18SpeakerRecognition24SSRSpeechTranscriberIntf",&,N,V_speechTranscriber) speechTranscriber;
@property (T@"NSDictionary",&,N,V_voiceTriggerEventInfo) voiceTriggerEventInfo;
@property (Tf,N,V_snrThreshold) snrThreshold;
@property (T@"NSString",C,N,V_referenceString) referenceString;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CSVTUITrainingSession setVoiceTriggerEventInfo:];
-[CSVTUITrainingSession voiceTriggerEventInfo];
-[CSVTUITrainingSession speechRecognitionTask:didHypothesizeTranscription:];
-[CSVTUITrainingSession snrThreshold];
-[CSVTUITrainingSession suspendTraining];
-[CSVTUITrainingSession referenceString];
-[CSVTUITrainingSession stopMasterTimer];
-[CSVTUITrainingSession _registerEndPointTimeout];
-[CSVTUITrainingSession audioSessionDidStartRecording:error:];
-[CSVTUITrainingSession audioSessionDidStopRecording:];
-[CSVTUITrainingSession audioSessionErrorDidOccur:];
-[CSVTUITrainingSession audioSessionRecordBufferAvailable:];
-[CSVTUITrainingSession audioSessionUnsupportedAudioRoute];
-[CSVTUITrainingSession closeSessionWithCompletion:];
-[CSVTUITrainingSession closeSessionWithStatus:successfully:];
-[CSVTUITrainingSession closeSessionWithStatus:successfully:complete:];
-[CSVTUITrainingSession closeSessionWithStatus:successfully:voiceTriggerEventInfo:completeWithResult:];
-[CSVTUITrainingSession computeRequiredTrailingSamples];
-[CSVTUITrainingSession createDigitalZeroReporterWithVoiceTriggerEventInfo:withSessionStatus:];
-[CSVTUITrainingSession didDetectBeginOfSpeech];
-[CSVTUITrainingSession didDetectEndOfSpeech:];
-[CSVTUITrainingSession feedSpeechRecognitionTrailingSamplesWithCompletedBlock:];
-[CSVTUITrainingSession feedSpeechRecognitionWithPCMBuffer];
-[CSVTUITrainingSession finishSpeechRecognitionTask];
-[CSVTUITrainingSession getTrainingAudioStatusWithVTEI:digitalZeroReporter:];
-[CSVTUITrainingSession handleAudioBufferForVTWithAudioInput:withDetectedBlock:];
-[CSVTUITrainingSession handleAudioInput:];
-[CSVTUITrainingSession handleMasterTimeout:];
-[CSVTUITrainingSession hasLiveSpeechTranscriber];
-[CSVTUITrainingSession hasUsableRecognizer];
-[CSVTUITrainingSession initWithUtteranceId:sessionNumber:Locale:audioSession:keywordDetector:speechRecognizer:speechRecognitionRequest:sessionDelegate:sessionDispatchQueue:zeroCounter:snrCheckEnabled:snrThreshold:completion:];
-[CSVTUITrainingSession initWithUtteranceId:sessionNumber:Locale:vtAssetConfigVersion:audioSession:keywordDetector:speechRecognizer:speechRecognitionRequest:sessionDelegate:sessionDispatchQueue:mhUUID:zeroCounter:snrCheckEnabled:snrThreshold:completionWithResult:];
-[CSVTUITrainingSession logTrainingSessionCompleteWithVoiceTriggerEventInfo:];
-[CSVTUITrainingSession numSamplesInPCMBuffer];
-[CSVTUITrainingSession pushAudioInputIntoPCMBuffer:];
-[CSVTUITrainingSession recognitionUsesWERCheck];
-[CSVTUITrainingSession recognizedTextPassesWERCheck:];
-[CSVTUITrainingSession requestTriggeredUtterance:];
-[CSVTUITrainingSession resultAlreadyReported];
-[CSVTUITrainingSession resumeTraining];
-[CSVTUITrainingSession setReferenceString:];
-[CSVTUITrainingSession setSnrThreshold:];
-[CSVTUITrainingSession setSpeechTranscriber:];
-[CSVTUITrainingSession setupEnhancedSpeechRecognizer];
-[CSVTUITrainingSession setupPhraseSpotter];
-[CSVTUITrainingSession setupSpeechRecognitionTaskWithVoiceTriggerEventInfo:];
-[CSVTUITrainingSession speechTranscriber];
-[CSVTUITrainingSession speechTranscriber:didFinishWithError:];
-[CSVTUITrainingSession speechTranscriber:didReceiveFinalResult:];
-[CSVTUITrainingSession speechTranscriber:didReceivePartialResult:];
-[CSVTUITrainingSession startMasterTimerWithTimeout:];
-[CSVTUITrainingSession startTraining];
-[CSVTUITrainingSession trimBeginingOfPCMBufferWithVoiceTriggerEventInfo:];
-[CSVTUITrainingSession updateMeterAndForward];
```
