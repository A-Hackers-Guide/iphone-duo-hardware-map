# `AVVoiceController`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVAudioRemoteInputPlugin_PrivateTest`
- 3 instance variables, 13 properties, 101 instance methods, 0 class methods

## Instance variables

```
^v _impl;
B mClientAPIClutch;
Q _alertStartTime;
```

## Properties

```
@property (T@"<Endpointer>",&) endpointerDelegate;
@property (Ti) recordEndpointMode;
@property (Td) recordStartWaitTime;
@property (Td) recordInterspeechWaitTime;
@property (Td) recordEndWaitTime;
@property (T@"<AVVoiceControllerRecordDelegate>",D) recordDelegate;
@property (Tf) alertVolume;
@property (TQ,R,V_alertStartTime) alertStartTime;
@property (T@"NSDictionary",R) metrics;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AVVoiceController finalize];
-[AVVoiceController impl];
-[AVVoiceController alertStartTime];
-[AVVoiceController dealloc];
-[AVVoiceController initWithError:];
-[AVVoiceController handleMediaServerDeath:];
-[AVVoiceController metrics];
-[AVVoiceController sessionCleanup];
-[AVVoiceController activateAudioSessionForStream:isPrewarm:recordMode:error:];
-[AVVoiceController configureAlertBehaviorForStream:error:];
-[AVVoiceController deactivateAudioSessionForStream:withOptions:error:];
-[AVVoiceController getAveragePowerForStream:forChannel:];
-[AVVoiceController initVoiceControllerForClient:withError:];
-[AVVoiceController playAlertSoundForType:overrideMode:];
-[AVVoiceController prepareRecordForStream:error:];
-[AVVoiceController setAlertSoundFromURL:forType:];
-[AVVoiceController setContext:streamType:error:];
-[AVVoiceController setRecordDelegate:];
-[AVVoiceController startRecordForStream:error:];
-[AVVoiceController stopRecordForStream:error:];
-[AVVoiceController teardownWithError:];
-[AVVoiceController updateMeterForStream:];
-[AVVoiceController handleInterruption:];
-[AVVoiceController handleRouteChange:];
-[AVVoiceController IsDeviceAvailableInLocalRoute:error:];
-[AVVoiceController interspeechPointDetectedAtTime:];
-[AVVoiceController setAlertVolume:];
-[AVVoiceController stopRecordForStream:completion:];
-[AVVoiceController _bringUp:withError:];
-[AVVoiceController _teardownWithError:];
-[AVVoiceController activateAudioSessionForStream:isPrewarm:error:];
-[AVVoiceController alertPlaybackFinishedWithSettings:];
-[AVVoiceController alertVolume];
-[AVVoiceController beganRecording:status:];
-[AVVoiceController beginAudioSessionActivate:];
-[AVVoiceController beginRecordInterruptionWithContext:];
-[AVVoiceController cleanSlateWithError:];
-[AVVoiceController configureAlertBehaviorForStream:completion:];
-[AVVoiceController configureVoiceTriggerClientCompletionBlocks];
-[AVVoiceController deactivateAudioSessionForStream:withOptions:completion:];
-[AVVoiceController deactivateAudioSessionWithOptions:];
-[AVVoiceController enableMiniDucking:];
-[AVVoiceController enableSmartRoutingConsiderationForStream:enable:error:];
-[AVVoiceController enableTriangleModeForStream:enable:withCompletion:];
-[AVVoiceController encodeError:];
-[AVVoiceController endAudioSessionActivate:];
-[AVVoiceController endRecordInterruption];
-[AVVoiceController endpointDetectedAtTime:];
-[AVVoiceController endpointerDelegate];
-[AVVoiceController finishedRecording:status:];
-[AVVoiceController getAlertStartTime];
-[AVVoiceController getCurrentSessionState];
-[AVVoiceController getCurrentSessionStateForStream:];
-[AVVoiceController getCurrentStreamState:];
-[AVVoiceController getDeviceLatenciesForStream:withCompletion:];
-[AVVoiceController getInputChannelInfoForStream:completion:];
-[AVVoiceController getPeakPowerForStream:forChannel:];
-[AVVoiceController getPlaybackRouteForStream:withCompletion:];
-[AVVoiceController getPlaybackRouteForStream:withError:];
-[AVVoiceController getRecordBufferDurationForStream:];
-[AVVoiceController getRecordDeviceInfoForStream:];
-[AVVoiceController getRecordModeForStream:];
-[AVVoiceController getRecordSettingsForStream:];
-[AVVoiceController handleMediaServerReset:];
-[AVVoiceController handlePluginDidPublishDevice:withDevice:];
-[AVVoiceController handlePluginDidUnpublishDevice:withDevice:];
-[AVVoiceController hardwareConfigChanged:];
-[AVVoiceController isDuckingSupportedOnPickedRouteForStream:error:];
-[AVVoiceController isMeteringEnabledForStream:];
-[AVVoiceController mockPluginEndpoint];
-[AVVoiceController notifyEventOccured:error:];
-[AVVoiceController notifyStreamInvalidated:];
-[AVVoiceController playAlert:withOverride:completion:];
-[AVVoiceController prepareRecordForStream:completion:];
-[AVVoiceController recordDelegate];
-[AVVoiceController recordEndWaitTime];
-[AVVoiceController recordEndpointMode];
-[AVVoiceController recordInterspeechWaitTime];
-[AVVoiceController recordStartWaitTime];
-[AVVoiceController removeSessionNotifications:];
-[AVVoiceController removeStream:completion:];
-[AVVoiceController sessionSetup];
-[AVVoiceController setAnnounceCallsEnabledForStream:enable:];
-[AVVoiceController setContext:completion:];
-[AVVoiceController setContext:error:];
-[AVVoiceController setContextForStream:forStream:error:];
-[AVVoiceController setDuckOthersForStream:withSettings:error:];
-[AVVoiceController setEnableInterruptionByRecordingClientsForStream:enable:error:];
-[AVVoiceController setEndpointerDelegate:];
-[AVVoiceController setRecordEndWaitTime:];
-[AVVoiceController setRecordEndpointMode:];
-[AVVoiceController setRecordInterspeechWaitTime:];
-[AVVoiceController setRecordModeForStream:recordMode:error:];
-[AVVoiceController setRecordStartWaitTime:];
-[AVVoiceController setRecordStatusChangeBlock:];
-[AVVoiceController setSessionNotifications:];
-[AVVoiceController startKeepAliveQueueForStream:completion:];
-[AVVoiceController startRecordForStream:completion:];
-[AVVoiceController startRecordWithSettings:completion:alertCompletion:audioCallback:];
-[AVVoiceController startpointDetected];
-[AVVoiceController stopKeepAliveQueueForStream:completion:];
```
