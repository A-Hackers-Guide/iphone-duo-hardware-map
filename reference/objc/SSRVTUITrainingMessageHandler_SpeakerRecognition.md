# `SSRVTUITrainingMessageHandler`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SSRVTUITrainingManagerDelegate`, `SSRVTUITrainingService`
- 4 instance variables, 8 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"<SSRVTUITrainingServiceDelegate>" _remoteObjectProxy;
@"SSRVTUITrainingManager" _trainingManager;
@"NSString" _siriSharedUserId;
@"<CSAudioProviderSelecting>" _audioProviderSelector;
```

## Properties

```
@property (T@"SSRVTUITrainingManager",&,N,V_trainingManager) trainingManager;
@property (T@"NSString",&,N,V_siriSharedUserId) siriSharedUserId;
@property (T@"<CSAudioProviderSelecting>",&,N,V_audioProviderSelector) audioProviderSelector;
@property (T@"<SSRVTUITrainingServiceDelegate>",&,N,V_remoteObjectProxy) remoteObjectProxy;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SSRVTUITrainingMessageHandler setLocaleIdentifier:];
-[SSRVTUITrainingMessageHandler reset];
-[SSRVTUITrainingMessageHandler setRemoteObjectProxy:];
-[SSRVTUITrainingMessageHandler remoteObjectProxy];
-[SSRVTUITrainingMessageHandler prepareWithCompletion:];
-[SSRVTUITrainingMessageHandler audioProviderSelector];
-[SSRVTUITrainingMessageHandler setAudioProviderSelector:];
-[SSRVTUITrainingMessageHandler stopRMS];
-[SSRVTUITrainingMessageHandler initWithAudioProvidingSelector:];
-[SSRVTUITrainingMessageHandler trainingManager];
-[SSRVTUITrainingMessageHandler VTUITrainingManagerFeedLevel:];
-[SSRVTUITrainingMessageHandler VTUITrainingManagerPartialTextDetected:];
-[SSRVTUITrainingMessageHandler audioSourceWithCompletion:];
-[SSRVTUITrainingMessageHandler cancelTrainingViaXPCForID:];
-[SSRVTUITrainingMessageHandler cleanupViaXPCWithCompletion:];
-[SSRVTUITrainingMessageHandler didDetectForceEndPoint];
-[SSRVTUITrainingMessageHandler getAudioSessionID:];
-[SSRVTUITrainingMessageHandler playSoundEffectWithAudioTone:];
-[SSRVTUITrainingMessageHandler setRecordingStartHostTime:];
-[SSRVTUITrainingMessageHandler setSNRCheckEnabled:];
-[SSRVTUITrainingMessageHandler setSiriSharedUserId:];
-[SSRVTUITrainingMessageHandler setTrainingManager:];
-[SSRVTUITrainingMessageHandler setupWithLocaleID:appDomain:siriSharedUserId:];
-[SSRVTUITrainingMessageHandler siriSharedUserId];
-[SSRVTUITrainingMessageHandler startRMS];
-[SSRVTUITrainingMessageHandler trainUtteranceViaXPC:shouldUseASR:completion:];
-[SSRVTUITrainingMessageHandler trainUtteranceViaXPC:shouldUseASR:mhUUID:completionWithResult:];
-[SSRVTUITrainingMessageHandler trainUtteranceWithReferenceStringViaXPC:completionWithResult:];
-[SSRVTUITrainingMessageHandler updateTrainingManagerViaXPCForDevice:trainingDeviceUUIDList:withCompletion:];
-[SSRVTUITrainingMessageHandler voiceProfileWithCompletion:];
-[SSRVTUITrainingMessageHandler vtuiTrainingXPCDisconnected];
```
