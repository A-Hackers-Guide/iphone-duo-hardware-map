# `SSRSpeakerAnalyzerSAT`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 9 properties, 28 instance methods, 0 class methods

## Instance variables

```
^v _novDetect;
Q _numSamplesProcessed;
B _triggerPhraseDetectedOnTap;
@"<SSRSpeakerAnalyzerSATDelegate>" _delegate;
@"NSURL" _configFilePath;
@"NSURL" _resourceFilePath;
@"SSRSpeakerRecognitionContext" _context;
@"NSDictionary" _voiceProfilesModelFilePaths;
@"NSDictionary" _voiceProfilesExpModelFilePaths;
@"NSArray" _satScorers;
@"NSDictionary" _scoreCard;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"<SSRSpeakerAnalyzerSATDelegate>",W,N,V_delegate) delegate;
@property (T@"NSURL",&,N,V_configFilePath) configFilePath;
@property (T@"NSURL",&,N,V_resourceFilePath) resourceFilePath;
@property (T@"SSRSpeakerRecognitionContext",&,N,V_context) context;
@property (T@"NSDictionary",&,N,V_voiceProfilesModelFilePaths) voiceProfilesModelFilePaths;
@property (T@"NSDictionary",&,N,V_voiceProfilesExpModelFilePaths) voiceProfilesExpModelFilePaths;
@property (T@"NSArray",&,N,V_satScorers) satScorers;
@property (T@"NSDictionary",&,N,V_scoreCard) scoreCard;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
```

## Instance methods

```
-[SSRSpeakerAnalyzerSAT dealloc];
-[SSRSpeakerAnalyzerSAT queue];
-[SSRSpeakerAnalyzerSAT setDelegate:];
-[SSRSpeakerAnalyzerSAT setContext:];
-[SSRSpeakerAnalyzerSAT delegate];
-[SSRSpeakerAnalyzerSAT context];
-[SSRSpeakerAnalyzerSAT setQueue:];
-[SSRSpeakerAnalyzerSAT endAudio];
-[SSRSpeakerAnalyzerSAT resetForNewRequest];
-[SSRSpeakerAnalyzerSAT setVoiceProfilesModelFilePaths:];
-[SSRSpeakerAnalyzerSAT _updateScoreCardForFinalResult:];
-[SSRSpeakerAnalyzerSAT _getAnalyzedResult];
-[SSRSpeakerAnalyzerSAT _getSuperVectorWithEndPoint:];
-[SSRSpeakerAnalyzerSAT _processSuperVector:withSize:processedAudioDurationMs:isFinal:];
-[SSRSpeakerAnalyzerSAT configFilePath];
-[SSRSpeakerAnalyzerSAT getVoiceRecognizerResults];
-[SSRSpeakerAnalyzerSAT initWithVoiceRecognitionContext:delegate:];
-[SSRSpeakerAnalyzerSAT processAudioData:numSamples:];
-[SSRSpeakerAnalyzerSAT resourceFilePath];
-[SSRSpeakerAnalyzerSAT satScorers];
-[SSRSpeakerAnalyzerSAT scoreCard];
-[SSRSpeakerAnalyzerSAT setConfigFilePath:];
-[SSRSpeakerAnalyzerSAT setResourceFilePath:];
-[SSRSpeakerAnalyzerSAT setSatScorers:];
-[SSRSpeakerAnalyzerSAT setScoreCard:];
-[SSRSpeakerAnalyzerSAT setVoiceProfilesExpModelFilePaths:];
-[SSRSpeakerAnalyzerSAT voiceProfilesExpModelFilePaths];
-[SSRSpeakerAnalyzerSAT voiceProfilesModelFilePaths];
```
