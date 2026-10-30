# `SSRVTUITrainingServiceClient`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SSRVTUITrainingServiceDelegate`, `SSRVTUITrainingService`
- 12 instance variables, 13 properties, 46 instance methods, 0 class methods

## Instance variables

```
@"NSString" _localeIdentifier;
@"NSString" _appDomain;
@"NSString" _siriSharedUserId;
B _requireResetup;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSXPCConnection" _xpcConnection;
@ _remoteObjectProxy;
@"<SSRVTUITrainingServiceDelegate>" _delegate;
@? _prepareCompletion;
@? _cleanupCompletion;
@? _trainCompletion;
@? _trainCompletionWithResult;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSXPCConnection",&,N,V_xpcConnection) xpcConnection;
@property (T@,&,N,V_remoteObjectProxy) remoteObjectProxy;
@property (T@"<SSRVTUITrainingServiceDelegate>",W,N,V_delegate) delegate;
@property (T@?,C,N,V_prepareCompletion) prepareCompletion;
@property (T@?,C,N,V_cleanupCompletion) cleanupCompletion;
@property (T@?,C,N,V_trainCompletion) trainCompletion;
@property (T@?,C,N,V_trainCompletionWithResult) trainCompletionWithResult;
@property (TB,N,V_requireResetup) requireResetup;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SSRVTUITrainingServiceClient setLocaleIdentifier:];
-[SSRVTUITrainingServiceClient _connection];
-[SSRVTUITrainingServiceClient initWithDelegate:];
-[SSRVTUITrainingServiceClient setXpcConnection:];
-[SSRVTUITrainingServiceClient reset];
-[SSRVTUITrainingServiceClient queue];
-[SSRVTUITrainingServiceClient setRemoteObjectProxy:];
-[SSRVTUITrainingServiceClient xpcConnection];
-[SSRVTUITrainingServiceClient invalidate];
-[SSRVTUITrainingServiceClient setDelegate:];
-[SSRVTUITrainingServiceClient delegate];
-[SSRVTUITrainingServiceClient _newConnection];
-[SSRVTUITrainingServiceClient remoteObjectProxy];
-[SSRVTUITrainingServiceClient setQueue:];
-[SSRVTUITrainingServiceClient prepareWithCompletion:];
-[SSRVTUITrainingServiceClient _service];
-[SSRVTUITrainingServiceClient CSVTUIRemoteDetectedPartialTranscriptionResult:];
-[SSRVTUITrainingServiceClient stopRMS];
-[SSRVTUITrainingServiceClient trainCompletion];
-[SSRVTUITrainingServiceClient CSVTUIRemoteTrainingSessionRMSAvailable:];
-[SSRVTUITrainingServiceClient _handleXPCDisconnectedUnexpectedlyWithError:];
-[SSRVTUITrainingServiceClient _resetupIfNeeded];
-[SSRVTUITrainingServiceClient audioSourceWithCompletion:];
-[SSRVTUITrainingServiceClient cancelTrainingViaXPCForID:];
-[SSRVTUITrainingServiceClient cleanupCompletion];
-[SSRVTUITrainingServiceClient cleanupViaXPCWithCompletion:];
-[SSRVTUITrainingServiceClient didDetectForceEndPoint];
-[SSRVTUITrainingServiceClient getAudioSessionID:];
-[SSRVTUITrainingServiceClient playSoundEffectWithAudioTone:];
-[SSRVTUITrainingServiceClient prepareCompletion];
-[SSRVTUITrainingServiceClient requireResetup];
-[SSRVTUITrainingServiceClient setCleanupCompletion:];
-[SSRVTUITrainingServiceClient setPrepareCompletion:];
-[SSRVTUITrainingServiceClient setRecordingStartHostTime:];
-[SSRVTUITrainingServiceClient setRequireResetup:];
-[SSRVTUITrainingServiceClient setSNRCheckEnabled:];
-[SSRVTUITrainingServiceClient setTrainCompletion:];
-[SSRVTUITrainingServiceClient setTrainCompletionWithResult:];
-[SSRVTUITrainingServiceClient setupWithLocaleID:appDomain:siriSharedUserId:];
-[SSRVTUITrainingServiceClient startRMS];
-[SSRVTUITrainingServiceClient trainCompletionWithResult];
-[SSRVTUITrainingServiceClient trainUtteranceViaXPC:shouldUseASR:completion:];
-[SSRVTUITrainingServiceClient trainUtteranceViaXPC:shouldUseASR:mhUUID:completionWithResult:];
-[SSRVTUITrainingServiceClient trainUtteranceWithReferenceStringViaXPC:completionWithResult:];
-[SSRVTUITrainingServiceClient updateTrainingManagerViaXPCForDevice:trainingDeviceUUIDList:withCompletion:];
-[SSRVTUITrainingServiceClient voiceProfileWithCompletion:];
```
