# `SSRSpeakerRecognitionOrchestrator`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SSRSpeakerRecognizerDelegate`, `SSRVoiceActivityDetectorDelegate`
- 23 instance variables, 21 properties, 49 instance methods, 0 class methods

## Instance variables

```
d _lastScoreReportTimeStamp;
d _lastSegmentStartTime;
Q _segmentCounter;
Q _numSamplesAddedToSpeakerRecognizers;
B _endAudioCalled;
B _startPointReported;
@"SSRSpeakerRecognitionContext" _context;
@"<SSRSpeakerRecognitionOrchestratorDelegate>" _delegate;
@"<CSAudioFileWriter>" _ssrUttLogger;
Q _myriadResult;
@"<SSRSpeakerRecognizer>" _psrRecognizer;
@"<SSRSpeakerRecognizer>" _satRecognizer;
@"SSRVoiceActivityDetector" _vad;
@"NSDictionary" _psrLastSpeakerInfo;
@"NSDictionary" _satLastSpeakerInfo;
@"NSDictionary" _combinedScores;
@"NSDictionary" _psrFinalSpeakerInfo;
@"NSDictionary" _satFinalSpeakerInfo;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSString" _debugUtteranceAudioFilePath;
@"NSString" _debugUtteranceJsonFilePath;
@"NSObject<OS_os_transaction>" _transaction;
@"NSString" _transDesc;
```

## Properties

```
@property (T@"SSRSpeakerRecognitionContext",&,N,V_context) context;
@property (T@"<SSRSpeakerRecognitionOrchestratorDelegate>",W,N,V_delegate) delegate;
@property (T@"<CSAudioFileWriter>",&,N,V_ssrUttLogger) ssrUttLogger;
@property (TQ,N,V_myriadResult) myriadResult;
@property (T@"<SSRSpeakerRecognizer>",&,N,V_psrRecognizer) psrRecognizer;
@property (T@"<SSRSpeakerRecognizer>",&,N,V_satRecognizer) satRecognizer;
@property (T@"SSRVoiceActivityDetector",&,N,V_vad) vad;
@property (T@"NSDictionary",&,N,V_psrLastSpeakerInfo) psrLastSpeakerInfo;
@property (T@"NSDictionary",&,N,V_satLastSpeakerInfo) satLastSpeakerInfo;
@property (T@"NSDictionary",&,N,V_combinedScores) combinedScores;
@property (T@"NSDictionary",&,N,V_psrFinalSpeakerInfo) psrFinalSpeakerInfo;
@property (T@"NSDictionary",&,N,V_satFinalSpeakerInfo) satFinalSpeakerInfo;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSString",&,N,V_debugUtteranceAudioFilePath) debugUtteranceAudioFilePath;
@property (T@"NSString",&,N,V_debugUtteranceJsonFilePath) debugUtteranceJsonFilePath;
@property (T@"NSObject<OS_os_transaction>",&,N,V_transaction) transaction;
@property (T@"NSString",&,N,V_transDesc) transDesc;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SSRSpeakerRecognitionOrchestrator setTransaction:];
-[SSRSpeakerRecognitionOrchestrator transaction];
-[SSRSpeakerRecognitionOrchestrator dealloc];
-[SSRSpeakerRecognitionOrchestrator queue];
-[SSRSpeakerRecognitionOrchestrator setDelegate:];
-[SSRSpeakerRecognitionOrchestrator setContext:];
-[SSRSpeakerRecognitionOrchestrator delegate];
-[SSRSpeakerRecognitionOrchestrator context];
-[SSRSpeakerRecognitionOrchestrator setQueue:];
-[SSRSpeakerRecognitionOrchestrator endAudio];
-[SSRSpeakerRecognitionOrchestrator processAudio:numSamples:];
-[SSRSpeakerRecognitionOrchestrator getPSRProcessingTime];
-[SSRSpeakerRecognitionOrchestrator initWithContext:withDelegate:error:];
-[SSRSpeakerRecognitionOrchestrator resetWithContext:];
-[SSRSpeakerRecognitionOrchestrator SSRVoiceActivityDetector:didDetectStartPointAt:];
-[SSRSpeakerRecognitionOrchestrator setDebugUtteranceAudioFilePath:];
-[SSRSpeakerRecognitionOrchestrator setVad:];
-[SSRSpeakerRecognitionOrchestrator updateDebugFilePathsForSegment:];
-[SSRSpeakerRecognitionOrchestrator vad];
-[SSRSpeakerRecognitionOrchestrator SSRVoiceActivityDetector:didDetectEndPointAt:];
-[SSRSpeakerRecognitionOrchestrator _logSpeakerIdProcessorScoreDelayWithScoreInfo:hasFinished:];
-[SSRSpeakerRecognitionOrchestrator _resetWithContext:];
-[SSRSpeakerRecognitionOrchestrator combinedScores];
-[SSRSpeakerRecognitionOrchestrator debugUtteranceAudioFilePath];
-[SSRSpeakerRecognitionOrchestrator debugUtteranceJsonFilePath];
-[SSRSpeakerRecognitionOrchestrator getLatestVoiceRecognitionInfo];
-[SSRSpeakerRecognitionOrchestrator myriadResult];
-[SSRSpeakerRecognitionOrchestrator orchestratorScoresWithPSRScores:withSATScores:withSegmentStartTime:];
-[SSRSpeakerRecognitionOrchestrator psrFinalSpeakerInfo];
-[SSRSpeakerRecognitionOrchestrator psrLastSpeakerInfo];
-[SSRSpeakerRecognitionOrchestrator psrRecognizer];
-[SSRSpeakerRecognitionOrchestrator satFinalSpeakerInfo];
-[SSRSpeakerRecognitionOrchestrator satLastSpeakerInfo];
-[SSRSpeakerRecognitionOrchestrator satRecognizer];
-[SSRSpeakerRecognitionOrchestrator setCombinedScores:];
-[SSRSpeakerRecognitionOrchestrator setDebugUtteranceJsonFilePath:];
-[SSRSpeakerRecognitionOrchestrator setMyriadResult:];
-[SSRSpeakerRecognitionOrchestrator setPsrFinalSpeakerInfo:];
-[SSRSpeakerRecognitionOrchestrator setPsrLastSpeakerInfo:];
-[SSRSpeakerRecognitionOrchestrator setPsrRecognizer:];
-[SSRSpeakerRecognitionOrchestrator setSatFinalSpeakerInfo:];
-[SSRSpeakerRecognitionOrchestrator setSatLastSpeakerInfo:];
-[SSRSpeakerRecognitionOrchestrator setSatRecognizer:];
-[SSRSpeakerRecognitionOrchestrator setSsrUttLogger:];
-[SSRSpeakerRecognitionOrchestrator setTransDesc:];
-[SSRSpeakerRecognitionOrchestrator speakerRecognizer:hasSpeakerIdInfo:];
-[SSRSpeakerRecognitionOrchestrator speakerRecognizerFinishedProcessing:withFinalSpeakerIdInfo:];
-[SSRSpeakerRecognitionOrchestrator ssrUttLogger];
-[SSRSpeakerRecognitionOrchestrator transDesc];
```
