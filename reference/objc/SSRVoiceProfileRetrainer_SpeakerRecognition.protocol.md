# `SSRVoiceProfileRetrainer` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 9 instance methods, 0 class methods

## Properties

```
@property (T@"NSURL",R,N) modelFilePath;
@property (TB,R,N) implicitTrainingRequired;
@property (TQ,R,N) retrainerType;
```

## Instance methods

```
-[SSRVoiceProfileRetrainer modelFilePath];
-[SSRVoiceProfileRetrainer retrainerType];
-[SSRVoiceProfileRetrainer initWithVoiceRetrainingContext:];
-[SSRVoiceProfileRetrainer addUtterances:withPolicy:withCompletion:];
-[SSRVoiceProfileRetrainer implicitTrainingRequired];
-[SSRVoiceProfileRetrainer needsRetrainingWithAudioFiles:];
-[SSRVoiceProfileRetrainer purgeConfusionInformationWithPolicy:];
-[SSRVoiceProfileRetrainer purgeLastSpeakerEmbedding];
-[SSRVoiceProfileRetrainer resetModelForRetraining];
```
