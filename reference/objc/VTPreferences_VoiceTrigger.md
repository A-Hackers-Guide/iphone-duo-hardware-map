# `VTPreferences`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 84 instance methods, 2 class methods

## Class methods

```
+[VTPreferences sharedPreferences];
+[VTPreferences deviceCategoryStringRepresentationForCategoryType:];
```

## Instance methods

```
-[VTPreferences fileLoggingIsEnabled];
-[VTPreferences isCompactVoiceTriggerAvailableForLanguageCode:forPhraseDeviceType:];
-[VTPreferences setUserPreferredVoiceTriggerPhraseType:sender:deviceType:endpointId:];
-[VTPreferences voiceTriggerEnabledWhenChargerConnected];
-[VTPreferences setVoiceTriggerEnabledWhenChargerDisconnected:];
-[VTPreferences remoteDarwinWasEverConnected];
-[VTPreferences overwritingVoiceTriggerMLock];
-[VTPreferences getPreferencesForEndpoint:fromPreferenceDomain:error:];
-[VTPreferences _getVoiceTriggerEnabledKeyWithDeviceType:];
-[VTPreferences voiceTriggerEnabled];
-[VTPreferences synchronize];
-[VTPreferences _gibraltarHasBuiltInMic];
-[VTPreferences canUseVoiceTriggerDuringPhoneCall];
-[VTPreferences init];
-[VTPreferences setVoiceTriggerEnabled:sender:];
-[VTPreferences getUserPreferredVoiceTriggerPhraseTypeForDeviceType:endpointId:error:];
-[VTPreferences gestureSubscriptionEnabled];
-[VTPreferences useSiriActivationSPIForwatchOS];
-[VTPreferences voiceTriggerEnabledForEndpointId:];
-[VTPreferences _setVoiceTriggerEnabled:sender:deviceType:];
-[VTPreferences everNotifyUserCompactTrigger];
-[VTPreferences isSATAvailable];
-[VTPreferences setEverNotifyUserCompactTrigger];
-[VTPreferences discardSATEnrollmentForLanguageCode:];
-[VTPreferences _isNonEndpointDeviceType:];
-[VTPreferences _logMetadataForVTEnabled:];
-[VTPreferences _getSATEnrollmentAudioPathForLanguageCodeForLegacyVoiceProfile:];
-[VTPreferences _setCanUseVoiceTriggerDuringPhoneCall:sender:];
-[VTPreferences _getVoiceTriggerEnabledDidChangeNotificationStringWithDeviceType:];
-[VTPreferences _setVoiceTriggerEnabled:sender:deviceType:endpointId:];
-[VTPreferences localizedCompactTriggerPhraseForLanguageCode:];
-[VTPreferences setVoiceTriggerEnabled:sender:deviceType:endpointId:];
-[VTPreferences localizedTriggerPhraseForLanguageCode:];
-[VTPreferences setVoiceTriggerEnabledWhenChargerConnected:];
-[VTPreferences setFileLoggingLevel:];
-[VTPreferences voiceTriggerWasEverUsed];
-[VTPreferences getMD5HashForSATEnrollmentAudioForLanguageCode:];
-[VTPreferences _VTSATCachePath];
-[VTPreferences markSATEnrollmentSuccessForLanguageCode:];
-[VTPreferences voiceTriggerInCoreSpeech];
-[VTPreferences isRemoteVoiceTriggerAvailable];
-[VTPreferences discardAllSATEnrollment];
-[VTPreferences isMphVTEnabled];
-[VTPreferences useSiriActivationSPIForiOS];
-[VTPreferences secondPassAudioLoggingEnabled];
-[VTPreferences _VTSATBasePath];
-[VTPreferences setPreferences:forEndpoint:inPreferenceDomain:];
-[VTPreferences _isSATMarkedForMarker:languageCode:];
-[VTPreferences _localeIdentifier];
-[VTPreferences _voiceTriggerEnabledWithDeviceType:];
-[VTPreferences onetimeRemoteAssetQueryRanSuccessfully];
-[VTPreferences _voiceTriggerEnabledWithDeviceType:endpointId:];
-[VTPreferences setCanUseVoiceTriggerDuringPhoneCall:];
-[VTPreferences fileLoggingLevel];
-[VTPreferences voiceTriggerEnabledWithDeviceType:endpointId:];
-[VTPreferences voiceTriggerEnabledWhenChargerDisconnected];
-[VTPreferences isVoiceTriggerAvailable];
-[VTPreferences setPhraseSpotterEnabled:sender:];
-[VTPreferences isSATEnrollmentMigratedForLanguageCode:];
-[VTPreferences corespeechDaemonEnabled];
-[VTPreferences shouldOverwriteVoiceTriggerMLock];
-[VTPreferences setSecondPassAudioLoggingEnabled:];
-[VTPreferences audioInjectionFilePath];
-[VTPreferences setPhraseSpotterEnabled:];
-[VTPreferences setOnetimeRemoteAssetQueryRanSuccessfully:];
-[VTPreferences _preferencesPhraseDeviceStringWithPhraseDeviceType:];
-[VTPreferences getSATEnrollmentPath];
-[VTPreferences _getCSDeviceTypeWithPhraseDeviceType:];
-[VTPreferences hasVoiceProfileIniCloudForLanguageCode:];
-[VTPreferences phraseSpotterEnabled];
-[VTPreferences enableVoiceTriggerUponVoiceProfileSyncForLanguage:];
-[VTPreferences hasExplicitlySetVoiceTriggerEnabled];
-[VTPreferences _languageCode];
-[VTPreferences canUseVoiceTriggerDuringPhoneCallWithState];
-[VTPreferences setVoiceTriggerEnabled:];
-[VTPreferences setFileLoggingIsEnabled:];
-[VTPreferences _storeModeEnabled];
-[VTPreferences setVoiceTriggerEnabled:sender:endpointId:];
-[VTPreferences localizedTriggerPhrase];
-[VTPreferences isSATEnrolledForLanguageCode:];
-[VTPreferences devicesWithVoiceProfileIniCloudForLanguage:];
-[VTPreferences _isLocalVoiceTriggerAvailable];
-[VTPreferences _getVTEnableLoggingMetadata];
-[VTPreferences isCompactVoiceTriggerAvailableForLanguageCode:];
```
