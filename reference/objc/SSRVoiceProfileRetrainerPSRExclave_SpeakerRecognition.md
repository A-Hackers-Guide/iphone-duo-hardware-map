# `SSRVoiceProfileRetrainerPSRExclave`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SSRVoiceProfileRetrainer`
- 19 instance variables, 25 properties, 53 instance methods, 0 class methods

## Instance variables

```
^v _novDetector;
f _bestTriggerScore;
@"SSRVoiceProfileRetrainingContext" _ctx;
@"SecureAsset" _asset;
@"SSRSpeakerRecognitionScorer" _psrScorer;
@"SSRVoiceProfile" _voiceProfile;
Q _spIdType;
@"NSURL" _configFilePath;
@"NSURL" _resourceFilePath;
@"NSString" _configVersion;
@"NSURL" _psrModelFilePath;
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
@property (T@"SSRSpeakerRecognitionScorer",&,N,V_psrScorer) psrScorer;
@property (T@"SSRVoiceProfile",&,N,V_voiceProfile) voiceProfile;
@property (TQ,N,V_spIdType) spIdType;
@property (T@"NSURL",&,N,V_configFilePath) configFilePath;
@property (T@"NSURL",&,N,V_resourceFilePath) resourceFilePath;
@property (T@"NSString",&,N,V_configVersion) configVersion;
@property (T@"NSURL",&,N,V_psrModelFilePath) psrModelFilePath;
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
-[SSRVoiceProfileRetrainerPSRExclave asset];
-[SSRVoiceProfileRetrainerPSRExclave setAsset:];
-[SSRVoiceProfileRetrainerPSRExclave dealloc];
-[SSRVoiceProfileRetrainerPSRExclave queue];
-[SSRVoiceProfileRetrainerPSRExclave configVersion];
-[SSRVoiceProfileRetrainerPSRExclave description];
-[SSRVoiceProfileRetrainerPSRExclave setQueue:];
-[SSRVoiceProfileRetrainerPSRExclave ctx];
-[SSRVoiceProfileRetrainerPSRExclave setConfigVersion:];
-[SSRVoiceProfileRetrainerPSRExclave modelFilePath];
-[SSRVoiceProfileRetrainerPSRExclave setCtx:];
-[SSRVoiceProfileRetrainerPSRExclave retrainerType];
-[SSRVoiceProfileRetrainerPSRExclave processedAudioDurationMs];
-[SSRVoiceProfileRetrainerPSRExclave setProcessedAudioDurationMs:];
-[SSRVoiceProfileRetrainerPSRExclave setSpeakerVector:];
-[SSRVoiceProfileRetrainerPSRExclave speakerVector];
-[SSRVoiceProfileRetrainerPSRExclave initWithVoiceRetrainingContext:];
-[SSRVoiceProfileRetrainerPSRExclave _composeSpeakerConfusionWithScores:forProfiles:];
-[SSRVoiceProfileRetrainerPSRExclave _logSpeakerConfusion:forProfileArray:withPrependString:];
-[SSRVoiceProfileRetrainerPSRExclave _logSpeakerConfusionWithExplicitScores:withImplicitScores:withPurgeUtterances:forProfile:forConfigVersion:];
-[SSRVoiceProfileRetrainerPSRExclave _processAudioFile:];
-[SSRVoiceProfileRetrainerPSRExclave _processSpeakerVector:withSize:withScorers:processedAudioDurationMs:];
-[SSRVoiceProfileRetrainerPSRExclave addUtterances:withPolicy:withCompletion:];
-[SSRVoiceProfileRetrainerPSRExclave bestTriggerScore];
-[SSRVoiceProfileRetrainerPSRExclave comparativeModels];
-[SSRVoiceProfileRetrainerPSRExclave configFilePath];
-[SSRVoiceProfileRetrainerPSRExclave currUttLengthInMs];
-[SSRVoiceProfileRetrainerPSRExclave implicitTrainingRequired];
-[SSRVoiceProfileRetrainerPSRExclave initWithVoiceRetrainingContext:secureAsset:secureSpeakerRecognitionConfig:];
-[SSRVoiceProfileRetrainerPSRExclave maximumSpeakerVectors];
-[SSRVoiceProfileRetrainerPSRExclave needsRetrainingWithAudioFiles:];
-[SSRVoiceProfileRetrainerPSRExclave psrModelFilePath];
-[SSRVoiceProfileRetrainerPSRExclave psrScorer];
-[SSRVoiceProfileRetrainerPSRExclave purgeConfusionInformationWithPolicy:];
-[SSRVoiceProfileRetrainerPSRExclave purgeLastSpeakerEmbedding];
-[SSRVoiceProfileRetrainerPSRExclave resetModelForRetraining];
-[SSRVoiceProfileRetrainerPSRExclave resourceFilePath];
-[SSRVoiceProfileRetrainerPSRExclave setBestTriggerScore:];
-[SSRVoiceProfileRetrainerPSRExclave setComparativeModels:];
-[SSRVoiceProfileRetrainerPSRExclave setConfigFilePath:];
-[SSRVoiceProfileRetrainerPSRExclave setCurrUttLengthInMs:];
-[SSRVoiceProfileRetrainerPSRExclave setMaximumSpeakerVectors:];
-[SSRVoiceProfileRetrainerPSRExclave setPsrModelFilePath:];
-[SSRVoiceProfileRetrainerPSRExclave setPsrScorer:];
-[SSRVoiceProfileRetrainerPSRExclave setResourceFilePath:];
-[SSRVoiceProfileRetrainerPSRExclave setSpIdType:];
-[SSRVoiceProfileRetrainerPSRExclave setSpeakerRecognitionConfig:];
-[SSRVoiceProfileRetrainerPSRExclave setSpeakerVectorSize:];
-[SSRVoiceProfileRetrainerPSRExclave setVoiceProfile:];
-[SSRVoiceProfileRetrainerPSRExclave spIdType];
-[SSRVoiceProfileRetrainerPSRExclave speakerRecognitionConfig];
-[SSRVoiceProfileRetrainerPSRExclave speakerVectorSize];
-[SSRVoiceProfileRetrainerPSRExclave voiceProfile];
```
