# `CSSecureSiriAudioProvidingProxy`

- Image: [`/System/Library/PrivateFrameworks/CoreSpeechExclave.framework/CoreSpeechExclave`](../userland/System__Library__PrivateFrameworks__CoreSpeechExclave.framework__CoreSpeechExclave.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 44 instance methods, 0 class methods

## Instance variables

```
{corespeechexclave_sirivoicetriggerservice_s="connection"^{tb_connection_s}} _service;
^{tb_endpoint_s=(?=[96c]^v)} _tightbeamEndpoint;
@"NSString" _serviceName;
```

## Instance methods

```
-[CSSecureSiriAudioProvidingProxy initWithServiceName:];
-[CSSecureSiriAudioProvidingProxy reset];
-[CSSecureSiriAudioProvidingProxy prepare];
-[CSSecureSiriAudioProvidingProxy adBlockerMatchingInProgress:];
-[CSSecureSiriAudioProvidingProxy adBlockerReset];
-[CSSecureSiriAudioProvidingProxy configAOPVoiceTrigger];
-[CSSecureSiriAudioProvidingProxy deinitializeSecondPass];
-[CSSecureSiriAudioProvidingProxy fetchAOPVoiceTriggerResult:];
-[CSSecureSiriAudioProvidingProxy fetchAndStoreAudioBuffer];
-[CSSecureSiriAudioProvidingProxy fetchAndStoreAudioBufferWithHostTime:];
-[CSSecureSiriAudioProvidingProxy fetchIMUWithCatchup:];
-[CSSecureSiriAudioProvidingProxy fetchRaiseToSpeakResult:];
-[CSSecureSiriAudioProvidingProxy fetchSecondPassResult:completion:];
-[CSSecureSiriAudioProvidingProxy fetchVoiceTriggerAPResult:];
-[CSSecureSiriAudioProvidingProxy initializeSecondPass];
-[CSSecureSiriAudioProvidingProxy processBargeInVoiceTriggerWithResult:];
-[CSSecureSiriAudioProvidingProxy processSecondPassVoiceTriggerWithShouldFlushAudio:result:];
-[CSSecureSiriAudioProvidingProxy requestHistoricalAudioBufferWithStartSample:completion:];
-[CSSecureSiriAudioProvidingProxy resetFirstPassVoiceTrigger];
-[CSSecureSiriAudioProvidingProxy setAdBlockerAsset:];
-[CSSecureSiriAudioProvidingProxy setAssetForLocale:isOTA:completion:];
-[CSSecureSiriAudioProvidingProxy setSpeakerProfile:numEmbeddings:dimension:speakerRecognizerType:];
-[CSSecureSiriAudioProvidingProxy skipProcessingRaiseToSpeakAOE:];
-[CSSecureSiriAudioProvidingProxy skipProcessingVoiceTriggerAPModeAOE:];
-[CSSecureSiriAudioProvidingProxy startAdBlockerMatching];
-[CSSecureSiriAudioProvidingProxy startBargeInVoiceTrigger];
-[CSSecureSiriAudioProvidingProxy startBargeInVoiceTriggerWithStartOption:];
-[CSSecureSiriAudioProvidingProxy startRaiseToSpeak];
-[CSSecureSiriAudioProvidingProxy startSecondPassVoiceTriggerWithStartOption:];
-[CSSecureSiriAudioProvidingProxy startSecureAdBlockerMobileAssetLoaderService:];
-[CSSecureSiriAudioProvidingProxy startSecureMobileAssetLoaderService:completion:];
-[CSSecureSiriAudioProvidingProxy stopAdBlockerMatching];
-[CSSecureSiriAudioProvidingProxy stopBargeInVoiceTrigger];
-[CSSecureSiriAudioProvidingProxy stopRaiseToSpeak];
-[CSSecureSiriAudioProvidingProxy stopSecondPassVoiceTrigger];
-[CSSecureSiriAudioProvidingProxy stopSecureAdBlockerMobileAssetLoaderService:];
-[CSSecureSiriAudioProvidingProxy stopSecureMobileAssetLoaderService:];
-[CSSecureSiriAudioProvidingProxy convertAssetConfigurationError:];
-[CSSecureSiriAudioProvidingProxy convertSecureBargeInVoiceTriggerResultType:];
-[CSSecureSiriAudioProvidingProxy convertSecureSecondPassVoiceTriggerResultType:];
-[CSSecureSiriAudioProvidingProxy convertSecureSpeakerRecognitionType:];
-[CSSecureSiriAudioProvidingProxy convertSecureVoiceTriggerKeywordDetectionResultType:];
-[CSSecureSiriAudioProvidingProxy convertSecureVoiceTriggerSpeakerDetectionResultType:];
-[CSSecureSiriAudioProvidingProxy processBargeInVoiceTrigger];
```
