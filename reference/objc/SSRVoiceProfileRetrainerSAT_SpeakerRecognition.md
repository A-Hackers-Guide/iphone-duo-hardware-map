# `SSRVoiceProfileRetrainerSAT`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SSRVoiceProfileRetrainer`
- 13 instance variables, 18 properties, 34 instance methods, 0 class methods

## Instance variables

```
Q _maximumSpeakerVectors;
f _bestTriggerScore;
@"SSRSpeakerRecognitionScorer" _satScorer;
@"SSRVoiceProfile" _voiceProfile;
@"NSURL" _configFilePath;
@"NSURL" _resourceFilePath;
@"NSURL" _satModelFilePath;
Q _spIdType;
@"NSDictionary" _comparativeModels;
@"NSData" _superVector;
Q _superVectorSize;
Q _processedAudioDurationMs;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"SSRSpeakerRecognitionScorer",&,N,V_satScorer) satScorer;
@property (T@"SSRVoiceProfile",&,N,V_voiceProfile) voiceProfile;
@property (T@"NSURL",&,N,V_configFilePath) configFilePath;
@property (T@"NSURL",&,N,V_resourceFilePath) resourceFilePath;
@property (T@"NSURL",&,N,V_satModelFilePath) satModelFilePath;
@property (TQ,N,V_spIdType) spIdType;
@property (T@"NSDictionary",&,N,V_comparativeModels) comparativeModels;
@property (T@"NSData",&,N,V_superVector) superVector;
@property (TQ,N,V_superVectorSize) superVectorSize;
@property (TQ,N,V_processedAudioDurationMs) processedAudioDurationMs;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSURL",R,N) modelFilePath;
@property (TB,R,N) implicitTrainingRequired;
@property (TQ,R,N) retrainerType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SSRVoiceProfileRetrainerSAT queue];
-[SSRVoiceProfileRetrainerSAT description];
-[SSRVoiceProfileRetrainerSAT setQueue:];
-[SSRVoiceProfileRetrainerSAT modelFilePath];
-[SSRVoiceProfileRetrainerSAT retrainerType];
-[SSRVoiceProfileRetrainerSAT processedAudioDurationMs];
-[SSRVoiceProfileRetrainerSAT setProcessedAudioDurationMs:];
-[SSRVoiceProfileRetrainerSAT initWithVoiceRetrainingContext:];
-[SSRVoiceProfileRetrainerSAT setSuperVector:];
-[SSRVoiceProfileRetrainerSAT superVectorSize];
-[SSRVoiceProfileRetrainerSAT _processAudioFile:withSATProcessor:];
-[SSRVoiceProfileRetrainerSAT _processSuperVector:withSize:withScorers:processedAudioDurationMs:];
-[SSRVoiceProfileRetrainerSAT addUtterances:withPolicy:withCompletion:];
-[SSRVoiceProfileRetrainerSAT comparativeModels];
-[SSRVoiceProfileRetrainerSAT configFilePath];
-[SSRVoiceProfileRetrainerSAT implicitTrainingRequired];
-[SSRVoiceProfileRetrainerSAT needsRetrainingWithAudioFiles:];
-[SSRVoiceProfileRetrainerSAT purgeConfusionInformationWithPolicy:];
-[SSRVoiceProfileRetrainerSAT purgeLastSpeakerEmbedding];
-[SSRVoiceProfileRetrainerSAT resetModelForRetraining];
-[SSRVoiceProfileRetrainerSAT resourceFilePath];
-[SSRVoiceProfileRetrainerSAT satModelFilePath];
-[SSRVoiceProfileRetrainerSAT satScorer];
-[SSRVoiceProfileRetrainerSAT setComparativeModels:];
-[SSRVoiceProfileRetrainerSAT setConfigFilePath:];
-[SSRVoiceProfileRetrainerSAT setResourceFilePath:];
-[SSRVoiceProfileRetrainerSAT setSatModelFilePath:];
-[SSRVoiceProfileRetrainerSAT setSatScorer:];
-[SSRVoiceProfileRetrainerSAT setSpIdType:];
-[SSRVoiceProfileRetrainerSAT setSuperVectorSize:];
-[SSRVoiceProfileRetrainerSAT setVoiceProfile:];
-[SSRVoiceProfileRetrainerSAT spIdType];
-[SSRVoiceProfileRetrainerSAT superVector];
-[SSRVoiceProfileRetrainerSAT voiceProfile];
```
