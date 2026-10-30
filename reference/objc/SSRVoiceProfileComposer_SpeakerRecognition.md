# `SSRVoiceProfileComposer`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSString" _speechId;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSString",&,N,V_speechId) speechId;
```

## Class methods

```
+[SSRVoiceProfileComposer sharedTrainer];
```

## Instance methods

```
-[SSRVoiceProfileComposer init];
-[SSRVoiceProfileComposer speechId];
-[SSRVoiceProfileComposer queue];
-[SSRVoiceProfileComposer setSpeechId:];
-[SSRVoiceProfileComposer setQueue:];
-[SSRVoiceProfileComposer _addUtteranceHelper:toProfile:withAnalyzer:withPreTriggerAudioTime:withError:];
-[SSRVoiceProfileComposer _getAnalyzerWithAsset:forProfile:];
-[SSRVoiceProfileComposer _getAnalyzerWithSecureAsset:];
-[SSRVoiceProfileComposer _getPreTriggerAudioTimeFromAsset:];
-[SSRVoiceProfileComposer _getPreTriggerAudioTimeFromSecureAsset:];
-[SSRVoiceProfileComposer _logEnrollmentUtteranceWithUtteranceId:mhUUID:locale:phId:];
-[SSRVoiceProfileComposer addUtterance:toProfile:];
-[SSRVoiceProfileComposer addUtterance:toProfile:withAsset:error:];
-[SSRVoiceProfileComposer addUtterance:toProfile:withAsset:sessionUtteranceId:sessionMHUUID:phId:];
-[SSRVoiceProfileComposer addUtterance:toProfile:withSecureAsset:error:];
-[SSRVoiceProfileComposer addUtterance:toProfile:withSecureAsset:sessionUtteranceId:sessionMHUUID:phId:];
-[SSRVoiceProfileComposer logEnrollmentUtterance:locale:utteranceId:mhUUID:phId:];
```
