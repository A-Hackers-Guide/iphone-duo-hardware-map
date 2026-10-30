# `SSRVoiceProfileStoreCleaner`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 14 instance methods, 0 class methods

## Instance methods

```
-[SSRVoiceProfileStoreCleaner _cleanupOrphanedMetafilesAtURL:];
-[SSRVoiceProfileStoreCleaner _cleanupAppDomain:];
-[SSRVoiceProfileStoreCleaner _cleanupContentsOfSatFolder:];
-[SSRVoiceProfileStoreCleaner _cleanupImplicitUtteranceCacheForProfile:];
-[SSRVoiceProfileStoreCleaner _cleanupInvalidAudioFiles:];
-[SSRVoiceProfileStoreCleaner _cleanupModelFilesAtDir:forAssetArray:];
-[SSRVoiceProfileStoreCleaner _cleanupOrphanedMetafilesForProfile:payloadUtteranceLifeTimeInDays:];
-[SSRVoiceProfileStoreCleaner _cleanupPayloadUtterancesFromProfile:forModelType:exceedingLifeTimeInDays:];
-[SSRVoiceProfileStoreCleaner _cleanuplanguageCodePath:forAppDomain:];
-[SSRVoiceProfileStoreCleaner cleanupInvalidModelsForProfile:withAssetArray:];
-[SSRVoiceProfileStoreCleaner cleanupProfileStore];
-[SSRVoiceProfileStoreCleaner deleteInvalidSiriProfilesFromPersonalDevicesForLanguage:appDomain:];
-[SSRVoiceProfileStoreCleaner filterDuplicatedSiriProfilesFrom:];
-[SSRVoiceProfileStoreCleaner filterInvalidSiriProfilesFrom:];
```
