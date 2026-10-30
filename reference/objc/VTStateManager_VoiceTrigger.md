# `VTStateManager`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `VTFirstUnlockMonitorDelegate`, `VTGestureMonitorDelegate`
- 13 instance variables, 5 properties, 14 instance methods, 22 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"VTPhraseSpotter" _phraseSpotter;
@"VTBuiltInRTModel" _builtInRTModel;
@? _callbackWithMessageAndTimestamp;
@"VTPolicy" _enablePolicy;
@"VTXPCServiceServer" _xpcServer;
B _voiceTriggerIsEnabled;
B _voiceTriggerIsEnabledOnCoreSpeechDaemon;
B _rtModelDownloaded;
@"VTGestureMonitor" _gestureMonitor;
Q _wakeGestureHostTime;
@"VTRemoteDarwinHIDEventNotifier" _remoteDarwinHIDEventNotifier;
@"VTCoreSpeechKeepAliveHandler" _coreSpeechKeepAliveHandler;
```

## Properties

```
@property (T@"VTCoreSpeechKeepAliveHandler",&,N,V_coreSpeechKeepAliveHandler) coreSpeechKeepAliveHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[VTStateManager requestCurrentBuiltInRTModelDictionary];
+[VTStateManager setCurrentBuiltInRTModelDictionary:];
+[VTStateManager requestVoiceTriggerEnabled:forReason:];
+[VTStateManager _serviceClient];
+[VTStateManager clearVoiceTriggerCount];
+[VTStateManager firstChanceAudioBuffer];
+[VTStateManager firstChanceTriggeredDate];
+[VTStateManager firstChanceVTEventInfo];
+[VTStateManager getVoiceTriggerCount];
+[VTStateManager iPhoneShouldStartVoiceTriggerInCoreSpeech];
+[VTStateManager isLastTriggerForced];
+[VTStateManager isLastTriggerSecondChanceTriggered];
+[VTStateManager notifyVoiceTrigger];
+[VTStateManager notifyVoiceTriggeredSiriSessionCancelled];
+[VTStateManager notifyVoiceTriggeredSiriSessionCancelled:];
+[VTStateManager requestAudioCapture:];
+[VTStateManager requestCurrentVoiceTriggerAssetDictionary];
+[VTStateManager requestCurrentVoiceTriggerAssetDictionaryWithReply:];
+[VTStateManager requestForcedSecondChance];
+[VTStateManager requestForcedTriggerEvent];
+[VTStateManager requestPhraseSpotterBypassing:timeout:];
+[VTStateManager requestRaiseToSpeakBypassing:timeout:];
```

## Instance methods

```
-[VTStateManager getModel];
-[VTStateManager initWithProperty:callbackWithMessageAndTimestamp:];
-[VTStateManager VTFirstUnlockMonitor:didReceiveFirstUnlock:];
-[VTStateManager _initializeXPCService];
-[VTStateManager _notifyStateTransitionToState:withStartTimestamp:];
-[VTStateManager _powerlog:];
-[VTStateManager _stateTransitionDidOccur:fromCallback:];
-[VTStateManager coreSpeechKeepAliveHandler];
-[VTStateManager gestureMonitorDidReceiveSleepGesture:];
-[VTStateManager gestureMonitorDidReceiveWakeGesture:];
-[VTStateManager getPhraseSpotter];
-[VTStateManager initWithProperty:callbackWithMessage:];
-[VTStateManager initWithProperty:phraseSpotter:enablePolicy:callbackWithMessageAndTimestamp:];
-[VTStateManager setCoreSpeechKeepAliveHandler:];
```
