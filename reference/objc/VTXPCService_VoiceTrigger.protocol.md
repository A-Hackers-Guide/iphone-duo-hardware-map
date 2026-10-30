# `VTXPCService` (protocol)

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 20 instance methods, 0 class methods

## Instance methods

```
-[VTXPCService setCurrentBuiltInRTModelDictionary:];
-[VTXPCService resetAssertions];
-[VTXPCService clearVoiceTriggerCount];
-[VTXPCService enableTriggerEventXPCNotification:];
-[VTXPCService enableVoiceTrigger:withAssertion:timestamp:];
-[VTXPCService getFirstChanceAudioBufferWithReply:];
-[VTXPCService getFirstChanceTriggeredDateWithReply:];
-[VTXPCService getFirstChanceVTEventInfoWithReply:];
-[VTXPCService getTestResponse:];
-[VTXPCService getVoiceTriggerCountWithReply:];
-[VTXPCService isLastTriggerFollowedBySpeechWithReply:];
-[VTXPCService notifySecondChanceRequest];
-[VTXPCService notifyTriggerEventRequest];
-[VTXPCService notifyVoiceTriggeredSiriSessionCancelled:];
-[VTXPCService queryLastTriggerEventTypeWithReply:];
-[VTXPCService requestAudioCapture:];
-[VTXPCService requestCurrentBuiltInRTModelDictionaryWithReply:];
-[VTXPCService requestCurrentVoiceTriggerAssetDictionaryWithReply:];
-[VTXPCService setPhraseSpotterBypassing:timeout:timestamp:];
-[VTXPCService setRaiseToSpeakBypassing:timeout:timestamp:];
```
