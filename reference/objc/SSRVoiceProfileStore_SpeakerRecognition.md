# `SSRVoiceProfileStore`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 41 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"SSRVoiceProfileStorePrefs" _storePrefs;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"SSRVoiceProfileStorePrefs",&,N,V_storePrefs) storePrefs;
```

## Class methods

```
+[SSRVoiceProfileStore sharedInstance];
```

## Instance methods

```
-[SSRVoiceProfileStore queue];
-[SSRVoiceProfileStore setQueue:];
-[SSRVoiceProfileStore cleanupVoiceProfileModelFilesForLocale:withAssets:];
-[SSRVoiceProfileStore deleteUserVoiceProfile:];
-[SSRVoiceProfileStore updateVoiceProfile:withUserName:];
-[SSRVoiceProfileStore _checkIfRetrainingRequiredForProfile:];
-[SSRVoiceProfileStore _deleteUserVoiceProfile:];
-[SSRVoiceProfileStore _enrolledVoiceProfiles];
-[SSRVoiceProfileStore _getTopScoringProfileIdFromScores:];
-[SSRVoiceProfileStore _logVoiceProfileConfusionWithCleanup:];
-[SSRVoiceProfileStore _retrainLiveOnOnboardedProfilesForLanguage:withForceRetrain:withCompletion:];
-[SSRVoiceProfileStore _retrainVoiceProfile:withContext:];
-[SSRVoiceProfileStore _retrainVoiceProfile:withContext:withUtterances:];
-[SSRVoiceProfileStore _saveTrainedUsers:];
-[SSRVoiceProfileStore _synchronizeSiriVoiceProfilesWithAssistant];
-[SSRVoiceProfileStore _updateTrainedUsersWithAction:UserVoiceProfile:];
-[SSRVoiceProfileStore addImplicitUtterance:toVoiceProfile:withAsset:withTriggerSource:withAudioInput:withCompletion:];
-[SSRVoiceProfileStore addUserVoiceProfile:withContext:withCompletion:];
-[SSRVoiceProfileStore checkIfVoiceProfile:needsUpdatedWith:withCategory:];
-[SSRVoiceProfileStore cleanupDuplicatedProfiles];
-[SSRVoiceProfileStore cleanupDuplicatesForProfile:];
-[SSRVoiceProfileStore cleanupInvalidSiriProfilesFromPersonalDevicesForLanguage:appDomain:];
-[SSRVoiceProfileStore cleanupVoiceProfileModelFilesForLocale:withAsset:];
-[SSRVoiceProfileStore cleanupVoiceProfileStore:];
-[SSRVoiceProfileStore copyAudioFiles:toProfile:forModelType:];
-[SSRVoiceProfileStore evaluateImplicitAdditionPolicyWithScores:forProfile:withImplicitThreshold:withDeltaThreshold:];
-[SSRVoiceProfileStore initStore];
-[SSRVoiceProfileStore isImplicitTrainingRequiredToVoiceProfile:withAsset:completion:];
-[SSRVoiceProfileStore loadCurrentVoiceProfiles];
-[SSRVoiceProfileStore logVoiceProfileConfusionWithCleanup:];
-[SSRVoiceProfileStore migrateVoiceProfilesIfNeededWithCompletionBlock:];
-[SSRVoiceProfileStore retrainVoiceProfile:withContext:withCompletion:];
-[SSRVoiceProfileStore saveVoiceProfiles:completion:];
-[SSRVoiceProfileStore setStorePrefs:];
-[SSRVoiceProfileStore storePrefs];
-[SSRVoiceProfileStore updateVoiceProfile:withEnrollmentQualityMetrics:];
-[SSRVoiceProfileStore updateVoiceProfile:withUserName:withBasePathExclave:];
-[SSRVoiceProfileStore userVoiceProfileForVoiceProfileID:];
-[SSRVoiceProfileStore userVoiceProfilesForAppDomain:];
-[SSRVoiceProfileStore userVoiceProfilesForAppDomain:forLocale:];
-[SSRVoiceProfileStore userVoiceProfilesForLocale:];
```
