# `CSVTUIAudioSessionRecorder`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CSAudioProviderDelegate`, `CSAudioStreamProvidingDelegate`, `CSVTUIAudioSession`
- 11 instance variables, 8 properties, 37 instance methods, 0 class methods

## Instance variables

```
@"CSAudioProvider" _audioProvider;
@"CSAudioStream" _audioStream;
@"NSObject<OS_dispatch_queue>" _queue;
B _isRemoteDarwinDisplayConnected;
B _forceSupportsRemoteDarwinDisplay;
Q _startRecordingHostTime;
B _shouldUseRecordingStartHostTime;
@"<CSVTUIAudioSessionDelegate>" _delegate;
@"CSAudioPowerMeter" _powerMeter;
Q _audioStreamHandleId;
@"<CSAudioProviderSelecting>" _audioProviderSelector;
```

## Properties

```
@property (T@"CSAudioPowerMeter",&,N,V_powerMeter) powerMeter;
@property (TQ,N,V_audioStreamHandleId) audioStreamHandleId;
@property (T@"<CSAudioProviderSelecting>",&,N,V_audioProviderSelector) audioProviderSelector;
@property (T@"<CSVTUIAudioSessionDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CSVTUIAudioSessionRecorder startRecording];
-[CSVTUIAudioSessionRecorder audioStreamProvider:audioBufferAvailable:];
-[CSVTUIAudioSessionRecorder stopRecording];
-[CSVTUIAudioSessionRecorder isRecording];
-[CSVTUIAudioSessionRecorder hasAudioRoute];
-[CSVTUIAudioSessionRecorder powerMeter];
-[CSVTUIAudioSessionRecorder updateMeters];
-[CSVTUIAudioSessionRecorder setPowerMeter:];
-[CSVTUIAudioSessionRecorder setDelegate:];
-[CSVTUIAudioSessionRecorder audioStreamProvider:numSamplesAvailableInExclave:hostTime:arrivalHostTimeToAudioRecorder:exclaveSampleCount:];
-[CSVTUIAudioSessionRecorder delegate];
-[CSVTUIAudioSessionRecorder audioStreamProvider:audioChunkForTVAvailable:];
-[CSVTUIAudioSessionRecorder releaseAudioSession];
-[CSVTUIAudioSessionRecorder audioStreamProvider:didHardwareConfigurationChange:];
-[CSVTUIAudioSessionRecorder audioStreamProvider:didStopStreamUnexpectedly:];
-[CSVTUIAudioSessionRecorder averagePower];
-[CSVTUIAudioSessionRecorder audioSource];
-[CSVTUIAudioSessionRecorder getAudioSessionID];
-[CSVTUIAudioSessionRecorder setEndpointerDelegate:];
-[CSVTUIAudioSessionRecorder audioStreamHandleId];
-[CSVTUIAudioSessionRecorder setAudioStreamHandleId:];
-[CSVTUIAudioSessionRecorder audioProviderSelector];
-[CSVTUIAudioSessionRecorder initWithAudioProviderSelector:];
-[CSVTUIAudioSessionRecorder setAudioProviderSelector:];
-[CSVTUIAudioSessionRecorder resetEndPointer];
-[CSVTUIAudioSessionRecorder _forceFetchAudioProvider:recordContext:];
-[CSVTUIAudioSessionRecorder _handleDidStopWithReason:];
-[CSVTUIAudioSessionRecorder _hasCorrectInputAudioRoute];
-[CSVTUIAudioSessionRecorder _hasCorrectInputAudioRouteFromHardwareConfiguration:];
-[CSVTUIAudioSessionRecorder _hasCorrectOutputAudioRoute];
-[CSVTUIAudioSessionRecorder _updateRemoteDarwinDisplayConnectedIfNeeded];
-[CSVTUIAudioSessionRecorder convertStopReason:];
-[CSVTUIAudioSessionRecorder hasCorrectAudioRoute];
-[CSVTUIAudioSessionRecorder initWithAudioProvider:forceSupportsRemoteDarwinDisplay:];
-[CSVTUIAudioSessionRecorder prepareRecord];
-[CSVTUIAudioSessionRecorder setAudioRecordingHostTime:];
-[CSVTUIAudioSessionRecorder updateAudioRecorderForTrainingDevice:deviceUUIDs:];
```
