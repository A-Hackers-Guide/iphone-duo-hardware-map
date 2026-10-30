# `SSRVoiceProfileMetadataManager`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 0 instance methods, 12 class methods

## Class methods

```
+[SSRVoiceProfileMetadataManager _getBaseMetaDictionaryForUtterancePath:];
+[SSRVoiceProfileMetadataManager _writeMetaDict:forUtterancePath:];
+[SSRVoiceProfileMetadataManager isUtteranceImplicitlyTrained:];
+[SSRVoiceProfileMetadataManager recordedTimeStampOfFile:];
+[SSRVoiceProfileMetadataManager getUtteranceEnrollmentType:];
+[SSRVoiceProfileMetadataManager getUtterancePhIdFromMetaDict:];
+[SSRVoiceProfileMetadataManager isUtteranceImplicitlyTrainedFromMetaDict:];
+[SSRVoiceProfileMetadataManager loadMetadataJsonObjectFromMetadataFile:];
+[SSRVoiceProfileMetadataManager readVoiceTriggerRePromptMetadata:];
+[SSRVoiceProfileMetadataManager recordedTimeStampFromFileName:];
+[SSRVoiceProfileMetadataManager saveUtteranceMetadataForUtterance:enrollmentType:isHandheldEnrollment:triggerSource:audioInput:otherBiometricResult:containsPayload:];
+[SSRVoiceProfileMetadataManager saveVoiceTriggeRePromptMetadata:];
```
