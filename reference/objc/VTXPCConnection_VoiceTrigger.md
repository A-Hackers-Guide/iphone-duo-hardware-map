# `VTXPCConnection`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `VTXPCService`
- 3 instance variables, 4 properties, 24 instance methods, 1 class methods

## Instance variables

```
@"NSMutableSet" _activationAssertions;
B _isPhraseSpotterBypassed;
B _isRecording;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[VTXPCConnection initialize];
```

## Instance methods

```
-[VTXPCConnection init];
-[VTXPCConnection setCurrentBuiltInRTModelDictionary:];
-[VTXPCConnection resetAssertions];
-[VTXPCConnection _setPhraseSpotterBypassing:];
-[VTXPCConnection _setRaiseToSpeakBypassing:];
-[VTXPCConnection clearVoiceTriggerCount];
-[VTXPCConnection enableTriggerEventXPCNotification:];
-[VTXPCConnection enableVoiceTrigger:withAssertion:timestamp:];
-[VTXPCConnection getFirstChanceAudioBufferWithReply:];
-[VTXPCConnection getFirstChanceTriggeredDateWithReply:];
-[VTXPCConnection getFirstChanceVTEventInfoWithReply:];
-[VTXPCConnection getTestResponse:];
-[VTXPCConnection getVoiceTriggerCountWithReply:];
-[VTXPCConnection handleDisconnect];
-[VTXPCConnection isLastTriggerFollowedBySpeechWithReply:];
-[VTXPCConnection notifySecondChanceRequest];
-[VTXPCConnection notifyTriggerEventRequest];
-[VTXPCConnection notifyVoiceTriggeredSiriSessionCancelled:];
-[VTXPCConnection queryLastTriggerEventTypeWithReply:];
-[VTXPCConnection requestAudioCapture:];
-[VTXPCConnection requestCurrentBuiltInRTModelDictionaryWithReply:];
-[VTXPCConnection requestCurrentVoiceTriggerAssetDictionaryWithReply:];
-[VTXPCConnection setPhraseSpotterBypassing:timeout:timestamp:];
-[VTXPCConnection setRaiseToSpeakBypassing:timeout:timestamp:];
```
