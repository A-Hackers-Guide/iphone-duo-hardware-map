# `SSRUtils`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 0 instance methods, 59 class methods

## Class methods

```
+[SSRUtils baseDir];
+[SSRUtils deviceCategoryForDeviceProductType:];
+[SSRUtils deviceCategoryStringRepresentationForCategoryType:];
+[SSRUtils timeStampString];
+[SSRUtils streamAudioFromFileUrl:audioStreamBasicDescriptor:samplesPerStreamChunk:audioDataAvailableHandler:];
+[SSRUtils ssrAudioLogsDir];
+[SSRUtils platformSupportsProfileDownload];
+[SSRUtils psrConfigFileNameForCSSpIdType:];
+[SSRUtils satConfigFileNameForCSSpIdType:];
+[SSRUtils stringForSpeakerRecognizerType:];
+[SSRUtils _getUtterancesFromDirectory:];
+[SSRUtils cleanupOrphanedVoiceIdGradingFiles];
+[SSRUtils combineScoreFromPSR:fromSAT:withCombinedWt:];
+[SSRUtils concatenateDonationId:triggerPhraseId:];
+[SSRUtils convertSchemaTypeWithLocale:];
+[SSRUtils convertToEnrollmentTriggerPhraseWithPhId:];
+[SSRUtils convertToSchemaEnumWithPhId:];
+[SSRUtils convertToUtteranceDataWithDonationString:];
+[SSRUtils createAVAudioPCMBufferWithNSData:audioFormat:sampleRate:numOfChannel:isInterleaved:];
+[SSRUtils createDirectoryIfDoesNotExist:];
+[SSRUtils deviceCategoryFromString:];
+[SSRUtils dumpFilesInDirectory:];
+[SSRUtils encryptFileAt:andSaveTo:error:];
+[SSRUtils explicitSpIdTypeForSpId:];
+[SSRUtils generateEnrollmentId];
+[SSRUtils getContentsOfDirectory:];
+[SSRUtils getCurrentDeviceCategoryType];
+[SSRUtils getEmbeddingFileName:];
+[SSRUtils getEnrollmentUtterancesCountFromDirectory:withCountBlock:];
+[SSRUtils getEnrollmentUtterancesFromDirectory:];
+[SSRUtils getExplicitEnrollmentUtterancesFromDirectory:];
+[SSRUtils getExplicitMarkedEnrollmentUtterancesFromDirectory:];
+[SSRUtils getHomeUserIdForVoiceProfile:withCompletion:];
+[SSRUtils getImplicitEnrollmentUtterancesFromDirectory:];
+[SSRUtils getImplicitUtteranceCacheDirectory];
+[SSRUtils getNumberOfAudioFilesInDirectory:];
+[SSRUtils getVoiceEnrollmentDownloadBaseDir];
+[SSRUtils getVoiceProfileForSiriProfileId:forLanguageCode:];
+[SSRUtils getVoiceProfileIdentityFromVersionFilePath:];
+[SSRUtils getVoiceProfileProductCategoryFromVersionFilePath:];
+[SSRUtils getVoiceProfilesForSiriProfileId:];
+[SSRUtils isCurrentDeviceCompatibleWithNewerVoiceProfileAt:];
+[SSRUtils isCurrentDeviceCompatibleWithVoiceProfileAt:];
+[SSRUtils isMphVTUIKeywordDetectorSupportedPlatform];
+[SSRUtils isSpeakerRecognitionSupportedInLocale:];
+[SSRUtils logSpeakerRecognitionGradingMetadataAtFilepath:withScoreInfo:];
+[SSRUtils moveContentsOfSrcDirectory:toDestDirectory:];
+[SSRUtils platformSupportsProfileUpdate];
+[SSRUtils readJsonFileAtPath:];
+[SSRUtils removeItemAtPath:];
+[SSRUtils satConfigFileNameForCSSpIdType:forModelType:forAssetType:];
+[SSRUtils segmentVoiceTriggerFromAudioFile:withVTEventInfo:withStorePayloadPortion:withCompletion:];
+[SSRUtils spIdTypeForString:];
+[SSRUtils spIdVoiceProfileImportRootDir];
+[SSRUtils spidAudioTrainUtterancesDir];
+[SSRUtils ssrAudioLogsCountWithinPrivacyLimit];
+[SSRUtils stringForCSSpIdType:];
+[SSRUtils stringForInvocationStyle:];
+[SSRUtils stringForVoiceProfileRetrainerType:];
```
