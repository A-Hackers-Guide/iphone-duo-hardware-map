# `SSRVoiceProfileManager`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 96 instance methods, 3 class methods

## Instance variables

```
Q _currentDeviceCategory;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSUUID" _endpointUUID;
@"SSRRemoteControlClient" _remoteControlClient;
@"NSString" _lastRepromptedDate;
@"<SSRVoiceProfileManagerDelegate>" _delegate;
```

## Properties

```
@property (TQ,N,V_currentDeviceCategory) currentDeviceCategory;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSUUID",&,N,V_endpointUUID) endpointUUID;
@property (T@"SSRRemoteControlClient",&,N,V_remoteControlClient) remoteControlClient;
@property (T@"NSString",C,V_lastRepromptedDate) lastRepromptedDate;
@property (T@"<SSRVoiceProfileManagerDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[SSRVoiceProfileManager sharedInstance];
+[SSRVoiceProfileManager sharedInstanceWithEndpointId:];
+[SSRVoiceProfileManager clearVTEnableAfterProfileSyncFlag];
```

## Instance methods

```
-[SSRVoiceProfileManager _isDirectory:];
-[SSRVoiceProfileManager initWithEndpointId:];
-[SSRVoiceProfileManager init];
-[SSRVoiceProfileManager queue];
-[SSRVoiceProfileManager setDelegate:];
-[SSRVoiceProfileManager setEndpointUUID:];
-[SSRVoiceProfileManager endpointUUID];
-[SSRVoiceProfileManager delegate];
-[SSRVoiceProfileManager isSpeakerRecognitionAvailable];
-[SSRVoiceProfileManager getSATEnrollmentPath];
-[SSRVoiceProfileManager hasVoiceProfileIniCloudForLanguageCode:];
-[SSRVoiceProfileManager enableVoiceTriggerUponVoiceProfileSyncForLanguage:];
-[SSRVoiceProfileManager _isRemoteVoiceTriggerAvailable];
-[SSRVoiceProfileManager setQueue:];
-[SSRVoiceProfileManager devicesWithVoiceProfileIniCloudForLanguage:];
-[SSRVoiceProfileManager SSRSpeakerProfilesBasePath];
-[SSRVoiceProfileManager isSATEnrolledForSiriProfileId:forLanguageCode:];
-[SSRVoiceProfileManager isVoiceTriggerRepromptRequired];
-[SSRVoiceProfileManager voiceTriggerRepromptFinished];
-[SSRVoiceProfileManager addUtterances:toProfile:withContext:withCompletion:];
-[SSRVoiceProfileManager cleanupVoiceProfileModelFilesForLocale:withAssets:];
-[SSRVoiceProfileManager deleteUserVoiceProfile:];
-[SSRVoiceProfileManager getVoiceProfileAnalyticsForAppDomain:withLocale:];
-[SSRVoiceProfileManager migrateTDVoiceProfilesToTDTI];
-[SSRVoiceProfileManager modelDirectoryPathForProfile:];
-[SSRVoiceProfileManager newVoiceProfileWithLocale:withAppDomain:];
-[SSRVoiceProfileManager notifyImplicitTrainingUtteranceAvailable:forVoiceProfileId:withRecordDeviceInfo:withRecordCtxt:withVoiceTriggerCtxt:withOtherCtxt:assetToUse:withCompletion:];
-[SSRVoiceProfileManager provisionedVoiceProfilesForAppDomain:withLocale:];
-[SSRVoiceProfileManager provisionedVoiceProfilesForLocale:];
-[SSRVoiceProfileManager pruneImplicitUtterancesOfProfile:withAsset:];
-[SSRVoiceProfileManager triggerInvalidSiriProfileCleanupFromPersonalDevicesForLanguage:appDomain:];
-[SSRVoiceProfileManager triggerRetrainingVoiceProfile:withContext:withCompletion:];
-[SSRVoiceProfileManager triggerVoiceProfileCleanupWithCompletion:];
-[SSRVoiceProfileManager triggerVoiceProfileDownload];
-[SSRVoiceProfileManager triggerVoiceProfileDuplicatesCleanup];
-[SSRVoiceProfileManager triggerVoiceProfileMigrationWithCompletion:];
-[SSRVoiceProfileManager updateVoiceProfile:withUserName:];
-[SSRVoiceProfileManager voiceProfileForId:];
-[SSRVoiceProfileManager _CSSATCachePath];
-[SSRVoiceProfileManager _copyVoiceProfileAtPath:toPath:];
-[SSRVoiceProfileManager SSRBasePathForAppDomain:];
-[SSRVoiceProfileManager notifyUserVoiceProfileUploadCompleteForSiriProfileId:withError:];
-[SSRVoiceProfileManager _CSSATCachePathForAppDomain:];
-[SSRVoiceProfileManager _CSSATDownloadPath];
-[SSRVoiceProfileManager _CSSATLegacyUploadPath];
-[SSRVoiceProfileManager _CSSATUploadPathForSiriProfileId:];
-[SSRVoiceProfileManager _checkIfDownloadRequiredForProfileId:];
-[SSRVoiceProfileManager _copyExplicitEnrollmentFilesFromPath:toPath:withCompletion:];
-[SSRVoiceProfileManager _createAndSetNewEnrollmentId];
-[SSRVoiceProfileManager _downloadAndEnrollVoiceProfileForProfileId:withDownloadTriggerBlock:];
-[SSRVoiceProfileManager _downloadVoiceProfileForProfileId:forDeviceCategory:withDownloadTriggerBlock:withCompletion:];
-[SSRVoiceProfileManager _enableVoiceTriggerIfLanguageMatches:];
-[SSRVoiceProfileManager _enrollVoiceProfileForSiriProfileId:fromCacheDirectoryPath:withCategoryType:];
-[SSRVoiceProfileManager _getUserVoiceProfileDownloadCacheDirectoryForProfileId:forDeviceCategory:forVoiceProfileVersion:];
-[SSRVoiceProfileManager _getUserVoiceProfileDownloadCacheDirectoryWithUpdatePath:];
-[SSRVoiceProfileManager _getVoiceProfilePathsToBeUploadedForSiriProfileId:];
-[SSRVoiceProfileManager _getVoiceProfilesForSiriProfileId:withLanguageCode:];
-[SSRVoiceProfileManager _isLegacyEnrollmentMarkedWith:forLanguageCode:];
-[SSRVoiceProfileManager _isMarkedForVoiceProfileTrainingSyncForLanguage:];
-[SSRVoiceProfileManager _markVoiceProfileTrainingSyncForLanguage:];
-[SSRVoiceProfileManager _prepareVoiceProfileWithSiriProfileId:withUploadBlock:];
-[SSRVoiceProfileManager addUtterances:toProfile:withContext:doUtteranceDonation:withCompletion:];
-[SSRVoiceProfileManager applyContentsToVoiceProfileStore:];
-[SSRVoiceProfileManager cleanupVoiceProfileModelFilesForLocale:withAsset:];
-[SSRVoiceProfileManager createEnrollmentId];
-[SSRVoiceProfileManager currentDeviceCategory];
-[SSRVoiceProfileManager deleteAllVoiceProfilesForAppDomain:];
-[SSRVoiceProfileManager discardSiriEnrollmentForLanguageCode:];
-[SSRVoiceProfileManager discardSiriEnrollmentForProfileId:forLanguageCode:];
-[SSRVoiceProfileManager emitMetricEnrollmentId:isVoiceProfileiCloudSyncSuccess:failureReasonIfAny:forLocale:];
-[SSRVoiceProfileManager getAllContentsOfVoiceProfileStore];
-[SSRVoiceProfileManager getCacheDirectoryForAppDomain:];
-[SSRVoiceProfileManager getCachedVoiceProfileAvailabilityMetaBlob];
-[SSRVoiceProfileManager getDonationIdsFromLanguageCode:error:];
-[SSRVoiceProfileManager getUserVoiceProfileUpdateDirectory];
-[SSRVoiceProfileManager getUserVoiceProfileUploadPathWithEnrolledLanguageList:];
-[SSRVoiceProfileManager hasVoiceProfileIniCloudForLanguageCode:withBackupMetaBlob:];
-[SSRVoiceProfileManager importVoiceProfile:appDomain:withSharedUserId:withLocale:withAsset:withCompletion:];
-[SSRVoiceProfileManager importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:];
-[SSRVoiceProfileManager isImplicitTrainingRequiredForVoiceProfileId:locale:completion:];
-[SSRVoiceProfileManager isSATEnrolledForSiriProfileId:forLanguageCode:completion:];
-[SSRVoiceProfileManager isSATEnrollmentMigratedForSiriProfileId:forLanguageCode:];
-[SSRVoiceProfileManager isVoiceProfileUploadedToiCloudForLanguageCode:withCompletionBlock:];
-[SSRVoiceProfileManager isVoiceTriggerRepromptRequiredWithCompletion:];
-[SSRVoiceProfileManager lastRepromptedDate];
-[SSRVoiceProfileManager markSATEnrollmentSuccessForVoiceProfile:];
-[SSRVoiceProfileManager markSATEnrollmentSuccessForVoiceProfile:completion:];
-[SSRVoiceProfileManager notifyUserVoiceProfileDownloadReadyForUser:getData:completion:];
-[SSRVoiceProfileManager notifyUserVoiceProfileUpdateReady];
-[SSRVoiceProfileManager notifyUserVoiceProfileUploadComplete];
-[SSRVoiceProfileManager remoteControlClient];
-[SSRVoiceProfileManager setCurrentDeviceCategory:];
-[SSRVoiceProfileManager setLastRepromptedDate:];
-[SSRVoiceProfileManager setRemoteControlClient:];
-[SSRVoiceProfileManager uploadUserVoiceProfileForSiriProfileId:withUploadTrigger:completion:];
-[SSRVoiceProfileManager voiceTriggerRepromptFinishedWithCompletion:];
```
