# `SSRVoiceProfilePruner`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SSRSpeakerRecognitionControllerDelegate`
- 0 instance variables, 4 properties, 4 instance methods, 0 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SSRVoiceProfilePruner _deleteUtterances:];
-[SSRVoiceProfilePruner _retrainVoiceProfile:withAsset:];
-[SSRVoiceProfilePruner _getScoresForAudio:withController:withDetector:forProfile:withCompletion:];
-[SSRVoiceProfilePruner pruneVoiceProfile:forSpIdType:withAsset:];
```
