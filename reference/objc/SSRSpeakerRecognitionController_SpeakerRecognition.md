# `SSRSpeakerRecognitionController`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SSRSpeakerRecognitionOrchestratorDelegate`
- 4 instance variables, 8 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"SSRSpeakerRecognitionContext" _context;
@"<SSRSpeakerRecognitionControllerDelegate>" _delegate;
@"SSRSpeakerRecognitionOrchestrator" _orchestrator;
@"NSDictionary" _lastScoreCard;
```

## Properties

```
@property (T@"SSRSpeakerRecognitionContext",&,N,V_context) context;
@property (T@"<SSRSpeakerRecognitionControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"SSRSpeakerRecognitionOrchestrator",&,N,V_orchestrator) orchestrator;
@property (T@"NSDictionary",&,N,V_lastScoreCard) lastScoreCard;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SSRSpeakerRecognitionController setDelegate:];
-[SSRSpeakerRecognitionController setContext:];
-[SSRSpeakerRecognitionController delegate];
-[SSRSpeakerRecognitionController context];
-[SSRSpeakerRecognitionController endAudio];
-[SSRSpeakerRecognitionController getLatestSpeakerInfo];
-[SSRSpeakerRecognitionController getPSRProcessingTime];
-[SSRSpeakerRecognitionController initWithContext:withDelegate:error:];
-[SSRSpeakerRecognitionController processAudio:withNumberOfSamples:];
-[SSRSpeakerRecognitionController resetWithContext:];
-[SSRSpeakerRecognitionController lastScoreCard];
-[SSRSpeakerRecognitionController orchestrator];
-[SSRSpeakerRecognitionController setLastScoreCard:];
-[SSRSpeakerRecognitionController setOrchestrator:];
-[SSRSpeakerRecognitionController voiceRecognitionOrchestrator:hasVoiceRecognitionInfo:];
-[SSRSpeakerRecognitionController voiceRecognitionOrchestratorFinishedProcessing:withFinalVoiceRecognitionInfo:];
```
