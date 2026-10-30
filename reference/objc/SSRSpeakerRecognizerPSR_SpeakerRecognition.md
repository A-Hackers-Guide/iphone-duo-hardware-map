# `SSRSpeakerRecognizerPSR`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SSRSpeakerAnalyzerPSRDelegate`, `SSRSpeakerRecognizer`
- 12 instance variables, 17 properties, 34 instance methods, 0 class methods

## Instance variables

```
B _processingEnded;
@"SSRSpeakerRecognitionContext" _spIdCtx;
@"NSString" _sessionId;
@"NSDictionary" _lastSpeakerInfo;
@"<SSRSpeakerRecognizerDelegate>" _delegate;
@"NSString" _invocationStyleStr;
Q _extraSamplesAtStart;
Q _vtEndInSampleCount;
Q _endInSampleCount;
Q _numSamplesProcessed;
Q _totalNumSamplesReceived;
@"SSRSpeakerAnalyzerPSR" _psrAnalyzer;
```

## Properties

```
@property (T@"SSRSpeakerRecognitionContext",&,N,V_spIdCtx) spIdCtx;
@property (T@"NSString",&,N,V_sessionId) sessionId;
@property (T@"NSDictionary",&,N,V_lastSpeakerInfo) lastSpeakerInfo;
@property (T@"<SSRSpeakerRecognizerDelegate>",W,N,V_delegate) delegate;
@property (T@"NSString",&,N,V_invocationStyleStr) invocationStyleStr;
@property (TQ,N,V_extraSamplesAtStart) extraSamplesAtStart;
@property (TQ,N,V_vtEndInSampleCount) vtEndInSampleCount;
@property (TQ,N,V_endInSampleCount) endInSampleCount;
@property (TQ,N,V_numSamplesProcessed) numSamplesProcessed;
@property (TB,N,V_processingEnded) processingEnded;
@property (TQ,N,V_totalNumSamplesReceived) totalNumSamplesReceived;
@property (T@"SSRSpeakerAnalyzerPSR",&,N,V_psrAnalyzer) psrAnalyzer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSDictionary",R,N) lastScoreCard;
```

## Instance methods

```
-[SSRSpeakerRecognizerPSR sessionId];
-[SSRSpeakerRecognizerPSR setSessionId:];
-[SSRSpeakerRecognizerPSR dealloc];
-[SSRSpeakerRecognizerPSR initWithContext:delegate:];
-[SSRSpeakerRecognizerPSR setDelegate:];
-[SSRSpeakerRecognizerPSR delegate];
-[SSRSpeakerRecognizerPSR endAudio];
-[SSRSpeakerRecognizerPSR extraSamplesAtStart];
-[SSRSpeakerRecognizerPSR setExtraSamplesAtStart:];
-[SSRSpeakerRecognizerPSR numSamplesProcessed];
-[SSRSpeakerRecognizerPSR setNumSamplesProcessed:];
-[SSRSpeakerRecognizerPSR setVtEndInSampleCount:];
-[SSRSpeakerRecognizerPSR vtEndInSampleCount];
-[SSRSpeakerRecognizerPSR resetWithContext:];
-[SSRSpeakerRecognizerPSR lastSpeakerInfo];
-[SSRSpeakerRecognizerPSR processingEnded];
-[SSRSpeakerRecognizerPSR setPsrAnalyzer:];
-[SSRSpeakerRecognizerPSR spIdCtx];
-[SSRSpeakerRecognizerPSR _initializeWithContext:];
-[SSRSpeakerRecognizerPSR endInSampleCount];
-[SSRSpeakerRecognizerPSR getSpeakerRecognizerProcessingTime];
-[SSRSpeakerRecognizerPSR invocationStyleStr];
-[SSRSpeakerRecognizerPSR lastScoreCard];
-[SSRSpeakerRecognizerPSR processAudioData:numSamples:];
-[SSRSpeakerRecognizerPSR psrAnalyzer];
-[SSRSpeakerRecognizerPSR setEndInSampleCount:];
-[SSRSpeakerRecognizerPSR setInvocationStyleStr:];
-[SSRSpeakerRecognizerPSR setLastSpeakerInfo:];
-[SSRSpeakerRecognizerPSR setProcessingEnded:];
-[SSRSpeakerRecognizerPSR setSpIdCtx:];
-[SSRSpeakerRecognizerPSR setTotalNumSamplesReceived:];
-[SSRSpeakerRecognizerPSR totalNumSamplesReceived];
-[SSRSpeakerRecognizerPSR voiceRecognitionPSRAnalyzer:hasVoiceRecognitionInfo:];
-[SSRSpeakerRecognizerPSR voiceRecognitionPSRAnalyzerFinishedProcessing:withVoiceRecognitionInfo:];
```
