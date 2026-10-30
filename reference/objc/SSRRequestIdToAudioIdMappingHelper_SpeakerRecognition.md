# `SSRRequestIdToAudioIdMappingHelper`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 2 instance methods, 11 class methods

## Instance variables

```
@"SSRVoiceProfileStorePrefs" _storePrefs;
```

## Properties

```
@property (T@"SSRVoiceProfileStorePrefs",&,N,V_storePrefs) storePrefs;
```

## Class methods

```
+[SSRRequestIdToAudioIdMappingHelper _convertNestedDictionaryToMutable:];
+[SSRRequestIdToAudioIdMappingHelper _loadRequestIdToAudioIdMappingFromPlist];
+[SSRRequestIdToAudioIdMappingHelper _writeMappingIntoPlist:];
+[SSRRequestIdToAudioIdMappingHelper getAudioIdWithRequestId:languageCode:date:error:];
+[SSRRequestIdToAudioIdMappingHelper getRequestIdsForLocale:date:error:];
+[SSRRequestIdToAudioIdMappingHelper purgeAllEntriesInSpkeakerIdBiome];
+[SSRRequestIdToAudioIdMappingHelper removeMapping];
+[SSRRequestIdToAudioIdMappingHelper removeMappingOnAndBefore:completion:];
+[SSRRequestIdToAudioIdMappingHelper removeMappingWithLocale:completion:];
+[SSRRequestIdToAudioIdMappingHelper removeMappingWithLocale:date:completion:];
+[SSRRequestIdToAudioIdMappingHelper writeIntoMappingWithRequestId:audioId:date:locale:completion:];
```

## Instance methods

```
-[SSRRequestIdToAudioIdMappingHelper setStorePrefs:];
-[SSRRequestIdToAudioIdMappingHelper storePrefs];
```
