# `CSVTUIAudioRecorder`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVVoiceControllerRecordDelegate`, `CSAudioSessionEventProviding`
- 10 instance variables, 8 properties, 41 instance methods, 1 class methods

## Instance variables

```
@"AVVoiceController" _voiceController;
{AudioBufferList="mNumberBuffers"I"mBuffers"[1{AudioBuffer="mNumberChannels"I"mDataByteSize"I"mData"^v}]} _interleavedABL;
^{AudioBufferList=I[1{AudioBuffer=II^v}]} _pNonInterleavedABL;
@"CSVTUIRemoteRecordClient" _remoteRecordClient;
@"NSDictionary" _latestContext;
B _waitingForDidStart;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_dispatch_queue>" _voiceControllerCreationQueue;
@"NSHashTable" _observers;
@"CSVTUIAudioRecorderRemoteDeviceContext" _remoteDeviceContext;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_voiceControllerCreationQueue) voiceControllerCreationQueue;
@property (T@"NSHashTable",&,N,V_observers) observers;
@property (T@"CSVTUIAudioRecorderRemoteDeviceContext",&,N,V_remoteDeviceContext) remoteDeviceContext;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CSVTUIAudioRecorder _convertDeactivateOption:];
```

## Instance methods

```
-[CSVTUIAudioRecorder dealloc];
-[CSVTUIAudioRecorder queue];
-[CSVTUIAudioRecorder setObservers:];
-[CSVTUIAudioRecorder observers];
-[CSVTUIAudioRecorder registerObserver:];
-[CSVTUIAudioRecorder initWithQueue:error:];
-[CSVTUIAudioRecorder unregisterObserver:];
-[CSVTUIAudioRecorder setQueue:];
-[CSVTUIAudioRecorder voiceControllerAudioCallback:forStream:buffer:];
-[CSVTUIAudioRecorder voiceControllerBeginRecordInterruption:];
-[CSVTUIAudioRecorder voiceControllerBeginRecordInterruption:withContext:];
-[CSVTUIAudioRecorder voiceControllerDidSetAudioSessionActive:isActivated:];
-[CSVTUIAudioRecorder voiceControllerDidStartRecording:forStream:successfully:error:];
-[CSVTUIAudioRecorder voiceControllerDidStopRecording:forStream:forReason:];
-[CSVTUIAudioRecorder voiceControllerEndRecordInterruption:];
-[CSVTUIAudioRecorder voiceControllerRecordHardwareConfigurationDidChange:toConfiguration:];
-[CSVTUIAudioRecorder voiceControllerWillSetAudioSessionActive:willActivate:];
-[CSVTUIAudioRecorder setContext:error:];
-[CSVTUIAudioRecorder _audioRecorderDidStartRecordingSuccessfully:streamHandleID:error:];
-[CSVTUIAudioRecorder _audioRecorderDidStopRecordingForReason:streamHandleID:];
-[CSVTUIAudioRecorder _compensateChannelDataIfNeeded:receivedNumChannels:];
-[CSVTUIAudioRecorder _destroyVoiceController];
-[CSVTUIAudioRecorder _processAudioBuffer:audioStreamHandleId:arrivalTimestampToAudioRecorder:];
-[CSVTUIAudioRecorder _processAudioChain:audioStreamHandleId:remoteVAD:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:];
-[CSVTUIAudioRecorder _shouldUseRemoteBuiltInMic:];
-[CSVTUIAudioRecorder activateAudioSessionWithReason:streamHandleId:error:];
-[CSVTUIAudioRecorder deactivateAudioSession:error:];
-[CSVTUIAudioRecorder getPlaybackRouteForStreamID:];
-[CSVTUIAudioRecorder setAudioSessionEventDelegate:];
-[CSVTUIAudioRecorder setVoiceControllerCreationQueue:];
-[CSVTUIAudioRecorder voiceControllerCreationQueue];
-[CSVTUIAudioRecorder _getRecordSettingsWithRequest];
-[CSVTUIAudioRecorder _voiceControllerWithError:];
-[CSVTUIAudioRecorder isRecordingWithStreamHandleId:];
-[CSVTUIAudioRecorder prepareAudioStreamRecordWithStreamHandleId:error:];
-[CSVTUIAudioRecorder recordRouteWithStreamHandleId:];
-[CSVTUIAudioRecorder remoteDeviceContext];
-[CSVTUIAudioRecorder setRemoteDeviceContext:];
-[CSVTUIAudioRecorder startAudioStreamWithStreamHandleId:error:];
-[CSVTUIAudioRecorder stopAudioStreamWithStreamHandleId:error:];
-[CSVTUIAudioRecorder updateAudioRecorderForTrainingDevice:deviceUUIDs:];
```
