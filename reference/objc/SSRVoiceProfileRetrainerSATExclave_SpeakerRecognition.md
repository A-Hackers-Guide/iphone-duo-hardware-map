# `SSRVoiceProfileRetrainerSATExclave`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SSRVoiceProfileRetrainer`
- 19 instance variables, 25 properties, 50 instance methods, 0 class methods

## Instance variables

```
^v _novDetector;
f _bestTriggerScore;
@"SSRVoiceProfileRetrainingContext" _ctx;
@"SecureAsset" _asset;
@"SSRSpeakerRecognitionScorer" _satScorer;
@"SSRVoiceProfile" _voiceProfile;
Q _spIdType;
@"NSURL" _configFilePath;
@"NSURL" _resourceFilePath;
@"NSString" _configVersion;
@"NSURL" _satModelFilePath;
@"NSDictionary" _comparativeModels;
Q _currUttLengthInMs;
@"NSData" _speakerVector;
Q _speakerVectorSize;
Q _processedAudioDurationMs;
@"NSObject<OS_dispatch_queue>" _queue;
Q _maximumSpeakerVectors;
@"SecureSpeakerRecognitionConfig" _speakerRecognitionConfig;
```

## Properties

```
@property (T@"SSRVoiceProfileRetrainingContext",&,V_ctx) ctx;
@property (T@"SecureAsset",&,V_asset) asset;
@property (T@"SSRSpeakerRecognitionScorer",&,N,V_satScorer) satScorer;
@property (T@"SSRVoiceProfile",&,N,V_voiceProfile) voiceProfile;
@property (TQ,N,V_spIdType) spIdType;
@property (T@"NSURL",&,N,V_configFilePath) configFilePath;
@property (T@"NSURL",&,N,V_resourceFilePath) resourceFilePath;
@property (T@"NSString",&,N,V_configVersion) configVersion;
@property (T@"NSURL",&,N,V_satModelFilePath) satModelFilePath;
@property (T@"NSDictionary",&,N,V_comparativeModels) comparativeModels;
@property (TQ,N,V_currUttLengthInMs) currUttLengthInMs;
@property (T@"NSData",&,N,V_speakerVector) speakerVector;
@property (TQ,N,V_speakerVectorSize) speakerVectorSize;
@property (TQ,N,V_processedAudioDurationMs) processedAudioDurationMs;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (TQ,N,V_maximumSpeakerVectors) maximumSpeakerVectors;
@property (Tf,N,V_bestTriggerScore) bestTriggerScore;
@property (T@"SecureSpeakerRecognitionConfig",&,N,V_speakerRecognitionConfig) speakerRecognitionConfig;
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
-[SSRVoiceProfileRetrainerSATExclave asset];
-[SSRVoiceProfileRetrainerSATExclave setAsset:];
-[SSRVoiceProfileRetrainerSATExclave dealloc];
-[SSRVoiceProfileRetrainerSATExclave queue];
-[SSRVoiceProfileRetrainerSATExclave configVersion];
-[SSRVoiceProfileRetrainerSATExclave description];
-[SSRVoiceProfileRetrainerSATExclave setQueue:];
-[SSRVoiceProfileRetrainerSATExclave ctx];
-[SSRVoiceProfileRetrainerSATExclave setConfigVersion:];
-[SSRVoiceProfileRetrainerSATExclave modelFilePath];
-[SSRVoiceProfileRetrainerSATExclave setCtx:];
-[SSRVoiceProfileRetrainerSATExclave retrainerType];
-[SSRVoiceProfileRetrainerSATExclave processedAudioDurationMs];
-[SSRVoiceProfileRetrainerSATExclave setProcessedAudioDurationMs:];
-[SSRVoiceProfileRetrainerSATExclave setSpeakerVector:];
-[SSRVoiceProfileRetrainerSATExclave speakerVector];
-[SSRVoiceProfileRetrainerSATExclave initWithVoiceRetrainingContext:];
-[SSRVoiceProfileRetrainerSATExclave _processAudioFile:];
-[SSRVoiceProfileRetrainerSATExclave _processSpeakerVector:withSize:withScorers:processedAudioDurationMs:];
-[SSRVoiceProfileRetrainerSATExclave addUtterances:withPolicy:withCompletion:];
-[SSRVoiceProfileRetrainerSATExclave bestTriggerScore];
-[SSRVoiceProfileRetrainerSATExclave comparativeModels];
-[SSRVoiceProfileRetrainerSATExclave configFilePath];
-[SSRVoiceProfileRetrainerSATExclave currUttLengthInMs];
-[SSRVoiceProfileRetrainerSATExclave implicitTrainingRequired];
-[SSRVoiceProfileRetrainerSATExclave initWithVoiceRetrainingContext:secureAsset:secureSpeakerRecognitionConfig:];
-[SSRVoiceProfileRetrainerSATExclave maximumSpeakerVectors];
-[SSRVoiceProfileRetrainerSATExclave needsRetrainingWithAudioFiles:];
-[SSRVoiceProfileRetrainerSATExclave purgeConfusionInformationWithPolicy:];
-[SSRVoiceProfileRetrainerSATExclave purgeLastSpeakerEmbedding];
-[SSRVoiceProfileRetrainerSATExclave resetModelForRetraining];
-[SSRVoiceProfileRetrainerSATExclave resourceFilePath];
-[SSRVoiceProfileRetrainerSATExclave satModelFilePath];
-[SSRVoiceProfileRetrainerSATExclave satScorer];
-[SSRVoiceProfileRetrainerSATExclave setBestTriggerScore:];
-[SSRVoiceProfileRetrainerSATExclave setComparativeModels:];
-[SSRVoiceProfileRetrainerSATExclave setConfigFilePath:];
-[SSRVoiceProfileRetrainerSATExclave setCurrUttLengthInMs:];
-[SSRVoiceProfileRetrainerSATExclave setMaximumSpeakerVectors:];
-[SSRVoiceProfileRetrainerSATExclave setResourceFilePath:];
-[SSRVoiceProfileRetrainerSATExclave setSatModelFilePath:];
-[SSRVoiceProfileRetrainerSATExclave setSatScorer:];
-[SSRVoiceProfileRetrainerSATExclave setSpIdType:];
-[SSRVoiceProfileRetrainerSATExclave setSpeakerRecognitionConfig:];
-[SSRVoiceProfileRetrainerSATExclave setSpeakerVectorSize:];
-[SSRVoiceProfileRetrainerSATExclave setVoiceProfile:];
-[SSRVoiceProfileRetrainerSATExclave spIdType];
-[SSRVoiceProfileRetrainerSATExclave speakerRecognitionConfig];
-[SSRVoiceProfileRetrainerSATExclave speakerVectorSize];
-[SSRVoiceProfileRetrainerSATExclave voiceProfile];
```
