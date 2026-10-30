# `SSRSpeakerRecognizerSAT`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SSRSpeakerAnalyzerSATDelegate`, `SSRSpeakerRecognizer`
- 11 instance variables, 16 properties, 31 instance methods, 0 class methods

## Instance variables

```
B _processingEnded;
@"SSRSpeakerRecognitionContext" _spIdCtx;
@"NSString" _sessionId;
@"NSDictionary" _lastSpeakerInfo;
@"<SSRSpeakerRecognizerDelegate>" _delegate;
@"NSString" _invocationStyleStr;
Q _extraSamplesAtStart;
Q _tdEndInSampleCount;
Q _totalNumSamplesReceived;
Q _numTdTiSamplesProcessed;
@"SSRSpeakerAnalyzerSAT" _satAnalyzer;
```

## Properties

```
@property (T@"SSRSpeakerRecognitionContext",&,N,V_spIdCtx) spIdCtx;
@property (T@"NSString",&,N,V_sessionId) sessionId;
@property (T@"NSDictionary",&,N,V_lastSpeakerInfo) lastSpeakerInfo;
@property (T@"<SSRSpeakerRecognizerDelegate>",W,N,V_delegate) delegate;
@property (T@"NSString",&,N,V_invocationStyleStr) invocationStyleStr;
@property (TQ,N,V_extraSamplesAtStart) extraSamplesAtStart;
@property (TQ,N,V_tdEndInSampleCount) tdEndInSampleCount;
@property (TQ,N,V_totalNumSamplesReceived) totalNumSamplesReceived;
@property (TQ,N,V_numTdTiSamplesProcessed) numTdTiSamplesProcessed;
@property (TB,N,V_processingEnded) processingEnded;
@property (T@"SSRSpeakerAnalyzerSAT",&,N,V_satAnalyzer) satAnalyzer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSDictionary",R,N) lastScoreCard;
```

## Instance methods

```
-[SSRSpeakerRecognizerSAT sessionId];
-[SSRSpeakerRecognizerSAT setSessionId:];
-[SSRSpeakerRecognizerSAT dealloc];
-[SSRSpeakerRecognizerSAT initWithContext:delegate:];
-[SSRSpeakerRecognizerSAT setDelegate:];
-[SSRSpeakerRecognizerSAT delegate];
-[SSRSpeakerRecognizerSAT endAudio];
-[SSRSpeakerRecognizerSAT extraSamplesAtStart];
-[SSRSpeakerRecognizerSAT setExtraSamplesAtStart:];
-[SSRSpeakerRecognizerSAT resetWithContext:];
-[SSRSpeakerRecognizerSAT lastSpeakerInfo];
-[SSRSpeakerRecognizerSAT processingEnded];
-[SSRSpeakerRecognizerSAT setSatAnalyzer:];
-[SSRSpeakerRecognizerSAT spIdCtx];
-[SSRSpeakerRecognizerSAT _initializeWithContext:];
-[SSRSpeakerRecognizerSAT invocationStyleStr];
-[SSRSpeakerRecognizerSAT lastScoreCard];
-[SSRSpeakerRecognizerSAT numTdTiSamplesProcessed];
-[SSRSpeakerRecognizerSAT processAudioData:numSamples:];
-[SSRSpeakerRecognizerSAT satAnalyzer];
-[SSRSpeakerRecognizerSAT setInvocationStyleStr:];
-[SSRSpeakerRecognizerSAT setLastSpeakerInfo:];
-[SSRSpeakerRecognizerSAT setNumTdTiSamplesProcessed:];
-[SSRSpeakerRecognizerSAT setProcessingEnded:];
-[SSRSpeakerRecognizerSAT setSpIdCtx:];
-[SSRSpeakerRecognizerSAT setTdEndInSampleCount:];
-[SSRSpeakerRecognizerSAT setTotalNumSamplesReceived:];
-[SSRSpeakerRecognizerSAT tdEndInSampleCount];
-[SSRSpeakerRecognizerSAT totalNumSamplesReceived];
-[SSRSpeakerRecognizerSAT voiceRecognitionSATAnalyzer:hasVoiceRecognitionInfo:];
-[SSRSpeakerRecognizerSAT voiceRecognitionSATAnalyzerFinishedProcessing:withVoiceRecognitionInfo:];
```
