# `SSRVoiceProfileRetrainerPSR`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `EARSyncPSRAudioProcessorDelegate`, `SSRVoiceProfileRetrainer`
- 17 instance variables, 20 properties, 44 instance methods, 0 class methods

## Instance variables

```
Q _maximumSpeakerVectors;
f _psrScore;
f _bestTriggerScore;
B _psrTimedout;
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
```

## Properties

```
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
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSURL",R,N) modelFilePath;
@property (TB,R,N) implicitTrainingRequired;
@property (TQ,R,N) retrainerType;
```

## Instance methods

```
-[SSRVoiceProfileRetrainerPSR dealloc];
-[SSRVoiceProfileRetrainerPSR queue];
-[SSRVoiceProfileRetrainerPSR configVersion];
-[SSRVoiceProfileRetrainerPSR description];
-[SSRVoiceProfileRetrainerPSR setQueue:];
-[SSRVoiceProfileRetrainerPSR setConfigVersion:];
-[SSRVoiceProfileRetrainerPSR modelFilePath];
-[SSRVoiceProfileRetrainerPSR retrainerType];
-[SSRVoiceProfileRetrainerPSR processedAudioDurationMs];
-[SSRVoiceProfileRetrainerPSR setProcessedAudioDurationMs:];
-[SSRVoiceProfileRetrainerPSR setSpeakerVector:];
-[SSRVoiceProfileRetrainerPSR speakerVector];
-[SSRVoiceProfileRetrainerPSR initWithVoiceRetrainingContext:];
-[SSRVoiceProfileRetrainerPSR _composeSpeakerConfusionWithScores:forProfiles:];
-[SSRVoiceProfileRetrainerPSR _emitVoiceProfileOnboardedSelfLogWithExplicitScores:withProfilePitch:];
-[SSRVoiceProfileRetrainerPSR _logSpeakerConfusion:forProfileArray:withPrependString:];
-[SSRVoiceProfileRetrainerPSR _logSpeakerConfusionWithExplicitScores:withImplicitScores:withPurgeUtterances:forProfile:forConfigVersion:];
-[SSRVoiceProfileRetrainerPSR _processAudioFile:withPSRProcessor:];
-[SSRVoiceProfileRetrainerPSR _processSpeakerVector:withSize:withScorers:processedAudioDurationMs:];
-[SSRVoiceProfileRetrainerPSR _psrProcessorResetSync:];
-[SSRVoiceProfileRetrainerPSR addUtterances:withPolicy:withCompletion:];
-[SSRVoiceProfileRetrainerPSR comparativeModels];
-[SSRVoiceProfileRetrainerPSR configFilePath];
-[SSRVoiceProfileRetrainerPSR currUttLengthInMs];
-[SSRVoiceProfileRetrainerPSR implicitTrainingRequired];
-[SSRVoiceProfileRetrainerPSR needsRetrainingWithAudioFiles:];
-[SSRVoiceProfileRetrainerPSR psrModelFilePath];
-[SSRVoiceProfileRetrainerPSR psrScorer];
-[SSRVoiceProfileRetrainerPSR purgeConfusionInformationWithPolicy:];
-[SSRVoiceProfileRetrainerPSR purgeLastSpeakerEmbedding];
-[SSRVoiceProfileRetrainerPSR resetModelForRetraining];
-[SSRVoiceProfileRetrainerPSR resourceFilePath];
-[SSRVoiceProfileRetrainerPSR setComparativeModels:];
-[SSRVoiceProfileRetrainerPSR setConfigFilePath:];
-[SSRVoiceProfileRetrainerPSR setCurrUttLengthInMs:];
-[SSRVoiceProfileRetrainerPSR setPsrModelFilePath:];
-[SSRVoiceProfileRetrainerPSR setPsrScorer:];
-[SSRVoiceProfileRetrainerPSR setResourceFilePath:];
-[SSRVoiceProfileRetrainerPSR setSpIdType:];
-[SSRVoiceProfileRetrainerPSR setSpeakerVectorSize:];
-[SSRVoiceProfileRetrainerPSR setVoiceProfile:];
-[SSRVoiceProfileRetrainerPSR spIdType];
-[SSRVoiceProfileRetrainerPSR speakerVectorSize];
-[SSRVoiceProfileRetrainerPSR voiceProfile];
```
