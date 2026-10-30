# `SSRVTUITrainingService` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 19 instance methods, 0 class methods

## Instance methods

```
-[SSRVTUITrainingService setLocaleIdentifier:];
-[SSRVTUITrainingService reset];
-[SSRVTUITrainingService prepareWithCompletion:];
-[SSRVTUITrainingService stopRMS];
-[SSRVTUITrainingService didDetectForceEndPoint];
-[SSRVTUITrainingService startRMS];
-[SSRVTUITrainingService audioSourceWithCompletion:];
-[SSRVTUITrainingService cancelTrainingViaXPCForID:];
-[SSRVTUITrainingService cleanupViaXPCWithCompletion:];
-[SSRVTUITrainingService getAudioSessionID:];
-[SSRVTUITrainingService playSoundEffectWithAudioTone:];
-[SSRVTUITrainingService setRecordingStartHostTime:];
-[SSRVTUITrainingService setSNRCheckEnabled:];
-[SSRVTUITrainingService setupWithLocaleID:appDomain:siriSharedUserId:];
-[SSRVTUITrainingService trainUtteranceViaXPC:shouldUseASR:completion:];
-[SSRVTUITrainingService trainUtteranceViaXPC:shouldUseASR:mhUUID:completionWithResult:];
-[SSRVTUITrainingService trainUtteranceWithReferenceStringViaXPC:completionWithResult:];
-[SSRVTUITrainingService updateTrainingManagerViaXPCForDevice:trainingDeviceUUIDList:withCompletion:];
-[SSRVTUITrainingService voiceProfileWithCompletion:];
```
