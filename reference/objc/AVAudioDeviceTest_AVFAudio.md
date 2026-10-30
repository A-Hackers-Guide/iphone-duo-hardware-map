# `AVAudioDeviceTest`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 24 instance methods, 0 class methods

## Instance variables

```
B _processSequenceAsynchronously;
@"NSXPCConnection" _connection;
@"<AVAudioDeviceTestServiceProtocol>" _serviceDelegateAsync;
@"<AVAudioDeviceTestServiceProtocol>" _serviceDelegateSync;
@"AVAudioDeviceTestService" _service;
```

## Properties

```
@property (T@"NSXPCConnection",&,N,V_connection) connection;
@property (T@"<AVAudioDeviceTestServiceProtocol>",&,N,V_serviceDelegateAsync) serviceDelegateAsync;
@property (T@"<AVAudioDeviceTestServiceProtocol>",&,N,V_serviceDelegateSync) serviceDelegateSync;
@property (T@"AVAudioDeviceTestService",&,N,V_service) service;
@property (TB,V_processSequenceAsynchronously) processSequenceAsynchronously;
```

## Instance methods

```
-[AVAudioDeviceTest setService:];
-[AVAudioDeviceTest init];
-[AVAudioDeviceTest dealloc];
-[AVAudioDeviceTest service];
-[AVAudioDeviceTest stopPlayback];
-[AVAudioDeviceTest connection];
-[AVAudioDeviceTest setConnection:];
-[AVAudioDeviceTest cancel];
-[AVAudioDeviceTest stopRecording:];
-[AVAudioDeviceTest initInProcess:];
-[AVAudioDeviceTest initWithXPCEndPoint:];
-[AVAudioDeviceTest playback:filePath:completion:];
-[AVAudioDeviceTest playbackTone:completion:];
-[AVAudioDeviceTest processSequenceAsynchronously];
-[AVAudioDeviceTest serviceDelegateAsync];
-[AVAudioDeviceTest serviceDelegateSync];
-[AVAudioDeviceTest setProcessSequenceAsynchronously:];
-[AVAudioDeviceTest setServiceDelegateAsync:];
-[AVAudioDeviceTest setServiceDelegateSync:];
-[AVAudioDeviceTest setupAudioSessionForHearingTest:];
-[AVAudioDeviceTest setupAudioSessionForHearingTestWithStatus:success:];
-[AVAudioDeviceTest startRecording:filePath:completion:];
-[AVAudioDeviceTest startWithSequence:completion:];
-[AVAudioDeviceTest stopAudioSession:];
```
