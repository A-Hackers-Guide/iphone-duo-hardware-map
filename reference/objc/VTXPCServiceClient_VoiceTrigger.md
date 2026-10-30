# `VTXPCServiceClient`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSXPCConnection" _vtxConnection;
```

## Instance methods

```
-[VTXPCServiceClient init];
-[VTXPCServiceClient dealloc];
-[VTXPCServiceClient _service];
-[VTXPCServiceClient requestCurrentBuiltInRTModelDictionary];
-[VTXPCServiceClient setCurrentBuiltInRTModelDictionary:];
-[VTXPCServiceClient resetAssertions];
-[VTXPCServiceClient clearVoiceTriggerCount];
-[VTXPCServiceClient enableVoiceTrigger:withAssertion:];
-[VTXPCServiceClient getFirstChanceAudioBuffer];
-[VTXPCServiceClient getFirstChanceTriggeredDate];
-[VTXPCServiceClient getFirstChanceVTEventInfo];
-[VTXPCServiceClient getLastTriggerType];
-[VTXPCServiceClient getVoiceTriggerCount];
-[VTXPCServiceClient isLastTriggerFollowedBySpeech];
-[VTXPCServiceClient notifySecondChanceRequest];
-[VTXPCServiceClient notifyTriggerEventRequest];
-[VTXPCServiceClient notifyVoiceTriggeredSiriSessionCancelled:];
-[VTXPCServiceClient requestAudioCapture:];
-[VTXPCServiceClient requestCurrentVoiceTriggerAssetDictionary];
-[VTXPCServiceClient requestCurrentVoiceTriggerAssetDictionaryWithReply:];
-[VTXPCServiceClient setPhraseSpotterBypassing:timeout:];
-[VTXPCServiceClient setRaiseToSpeakBypassing:timeout:];
```
