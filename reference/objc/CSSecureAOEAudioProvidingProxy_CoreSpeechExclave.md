# `CSSecureAOEAudioProvidingProxy`

- Image: [`/System/Library/PrivateFrameworks/CoreSpeechExclave.framework/CoreSpeechExclave`](../userland/System__Library__PrivateFrameworks__CoreSpeechExclave.framework__CoreSpeechExclave.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CSSecureSiriAudioProvidingProxy`
- 6 instance variables, 0 properties, 45 instance methods, 0 class methods

## Instance variables

```
alwaysOnExclaveClient;
siriVoiceTriggerService;
serverQueue;
lock;
delegate;
serviceName;
```

## Instance methods

```
-[CSSecureAOEAudioProvidingProxy init];
-[CSSecureAOEAudioProvidingProxy dealloc];
-[CSSecureAOEAudioProvidingProxy initWithServiceName:];
-[CSSecureAOEAudioProvidingProxy reset];
-[CSSecureAOEAudioProvidingProxy prepare];
-[CSSecureAOEAudioProvidingProxy adBlockerMatchingInProgress:];
-[CSSecureAOEAudioProvidingProxy adBlockerReset];
-[CSSecureAOEAudioProvidingProxy configAOPVoiceTrigger];
-[CSSecureAOEAudioProvidingProxy deinitializeSecondPass];
-[CSSecureAOEAudioProvidingProxy fetchAOPVoiceTriggerResult:];
-[CSSecureAOEAudioProvidingProxy fetchAndStoreAudioBuffer];
-[CSSecureAOEAudioProvidingProxy fetchAndStoreAudioBufferWithHostTime:];
-[CSSecureAOEAudioProvidingProxy fetchIMUWithCatchup:];
-[CSSecureAOEAudioProvidingProxy fetchRaiseToSpeakResult:];
-[CSSecureAOEAudioProvidingProxy fetchSecondPassResult:completion:];
-[CSSecureAOEAudioProvidingProxy fetchVoiceTriggerAPResult:];
-[CSSecureAOEAudioProvidingProxy initWithDelegate:serviceName:];
-[CSSecureAOEAudioProvidingProxy initializeSecondPass];
-[CSSecureAOEAudioProvidingProxy processBargeInVoiceTriggerWithResult:];
-[CSSecureAOEAudioProvidingProxy processSecondPassVoiceTriggerWithShouldFlushAudio:result:];
-[CSSecureAOEAudioProvidingProxy requestHistoricalAudioBufferWithStartSample:completion:];
-[CSSecureAOEAudioProvidingProxy resetFirstPassVoiceTrigger];
-[CSSecureAOEAudioProvidingProxy setAdBlockerAsset:];
-[CSSecureAOEAudioProvidingProxy setAssetForLocale:isOTA:completion:];
-[CSSecureAOEAudioProvidingProxy setSpeakerProfile:numEmbeddings:dimension:speakerRecognizerType:];
-[CSSecureAOEAudioProvidingProxy skipProcessingRaiseToSpeakAOE:];
-[CSSecureAOEAudioProvidingProxy skipProcessingVoiceTriggerAPModeAOE:];
-[CSSecureAOEAudioProvidingProxy startAdBlockerMatching];
-[CSSecureAOEAudioProvidingProxy startBargeInVoiceTrigger];
-[CSSecureAOEAudioProvidingProxy startBargeInVoiceTriggerWithStartOption:];
-[CSSecureAOEAudioProvidingProxy startRaiseToSpeak];
-[CSSecureAOEAudioProvidingProxy startSecondPassVoiceTriggerWithStartOption:];
-[CSSecureAOEAudioProvidingProxy startSecureAdBlockerMobileAssetLoaderService:];
-[CSSecureAOEAudioProvidingProxy startSecureMobileAssetLoaderService:completion:];
-[CSSecureAOEAudioProvidingProxy stopAdBlockerMatching];
-[CSSecureAOEAudioProvidingProxy stopBargeInVoiceTrigger];
-[CSSecureAOEAudioProvidingProxy stopRaiseToSpeak];
-[CSSecureAOEAudioProvidingProxy stopSecondPassVoiceTrigger];
-[CSSecureAOEAudioProvidingProxy stopSecureAdBlockerMobileAssetLoaderService:];
-[CSSecureAOEAudioProvidingProxy stopSecureMobileAssetLoaderService:];
-[CSSecureAOEAudioProvidingProxy _resetServerState];
-[CSSecureAOEAudioProvidingProxy _handleServerInterruption];
-[CSSecureAOEAudioProvidingProxy _setupXPCConnectionToServer];
-[CSSecureAOEAudioProvidingProxy connectExclaveServerEP];
-[CSSecureAOEAudioProvidingProxy disconnectExclaveServerEP];
```
