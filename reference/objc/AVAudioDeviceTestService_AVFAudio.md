# `AVAudioDeviceTestService`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVAudioDeviceTestServiceProtocol`
- 21 instance variables, 20 properties, 76 instance methods, 0 class methods

## Instance variables

```
{unique_ptr<PulseTone, std::default_delete<PulseTone>>=""{?="__ptr_"^{PulseTone}}} mPulseToneHandler;
B _testServiceSupportedOnHardware;
@"AVAudioEngine" _engine;
@"AVAudioPlayerNode" _player;
@"AVAudioUnitEQ" _inputFilter;
@"AVAudioUnitEQ" _outputFilter;
@"AVAudioUnit" _multichannelMixer;
@"AVAudioSession" _currentSession;
@"AVAudioNode" _nodeToCaptureData;
@"AVAudioFile" _inputTapFile;
@ _routeChangeObserver;
@ _interruptionObserver;
@ _mediaservicesLostObserver;
@ _mediaservicesResetObserver;
@ _systemVolumeObserver;
q _extensionHandle;
@"AVAudioSourceNode" _sourceNode;
@"NSObject<OS_dispatch_queue>" _toneQueue;
@"NSNumber" _userVolumeBeforeHearingTest;
@"AVAudioSession" _hearingTestSession;
@"NSObject<OS_os_transaction>" _transaction;
```

## Properties

```
@property (T@"AVAudioEngine",&,V_engine) engine;
@property (T@"AVAudioPlayerNode",&,V_player) player;
@property (T@"AVAudioUnitEQ",&,V_inputFilter) inputFilter;
@property (T@"AVAudioUnitEQ",&,V_outputFilter) outputFilter;
@property (T@"AVAudioUnit",&,V_multichannelMixer) multichannelMixer;
@property (T@"AVAudioSession",&,V_currentSession) currentSession;
@property (T@"AVAudioNode",&,V_nodeToCaptureData) nodeToCaptureData;
@property (T@"AVAudioFile",&,V_inputTapFile) inputTapFile;
@property (T@,&,V_routeChangeObserver) routeChangeObserver;
@property (T@,&,V_interruptionObserver) interruptionObserver;
@property (T@,&,V_mediaservicesLostObserver) mediaservicesLostObserver;
@property (T@,&,V_mediaservicesResetObserver) mediaservicesResetObserver;
@property (T@,&,V_systemVolumeObserver) systemVolumeObserver;
@property (TB,V_testServiceSupportedOnHardware) testServiceSupportedOnHardware;
@property (Tq,V_extensionHandle) extensionHandle;
@property (T@"AVAudioSourceNode",&,N,V_sourceNode) sourceNode;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_toneQueue) toneQueue;
@property (T@"NSNumber",&,N,V_userVolumeBeforeHearingTest) userVolumeBeforeHearingTest;
@property (T@"AVAudioSession",&,N,V_hearingTestSession) hearingTestSession;
@property (T@"NSObject<OS_os_transaction>",&,N,V_transaction) transaction;
```

## Instance methods

```
-[AVAudioDeviceTestService setEngine:];
-[AVAudioDeviceTestService cleanUp];
-[AVAudioDeviceTestService setTransaction:];
-[AVAudioDeviceTestService engine];
-[AVAudioDeviceTestService player];
-[AVAudioDeviceTestService transaction];
-[AVAudioDeviceTestService setExtensionHandle:];
-[AVAudioDeviceTestService setSourceNode:];
-[AVAudioDeviceTestService init];
-[AVAudioDeviceTestService extensionHandle];
-[AVAudioDeviceTestService setCurrentSession:];
-[AVAudioDeviceTestService dealloc];
-[AVAudioDeviceTestService setVolume:];
-[AVAudioDeviceTestService setPlayer:];
-[AVAudioDeviceTestService sourceNode];
-[AVAudioDeviceTestService stopPlayback];
-[AVAudioDeviceTestService currentSession];
-[AVAudioDeviceTestService cancel];
-[AVAudioDeviceTestService stopRecording:];
-[AVAudioDeviceTestService setInputFilter:];
-[AVAudioDeviceTestService setupObservers:];
-[AVAudioDeviceTestService isOutputRouteBluetooth:session:];
-[AVAudioDeviceTestService setUserVolumeBeforeHearingTest:];
-[AVAudioDeviceTestService calculateCrossCorrelationPeakRelativeToSource:capture:];
-[AVAudioDeviceTestService checkSequenceValidity:completion:];
-[AVAudioDeviceTestService cleanUpObservers];
-[AVAudioDeviceTestService configureDataSources:session:];
-[AVAudioDeviceTestService configureMultiChannelMixerForOutputChannel:totalChannels:];
-[AVAudioDeviceTestService convertBufferFor:sourceBuffer:];
-[AVAudioDeviceTestService createAudioEngineAndProcessingChain:session:sourceNodeBlock:];
-[AVAudioDeviceTestService createAudioEngineAndPulseToneHandlerFor:];
-[AVAudioDeviceTestService hearingTestSession];
-[AVAudioDeviceTestService inputFilter];
-[AVAudioDeviceTestService inputTapFile];
-[AVAudioDeviceTestService interruptionObserver];
-[AVAudioDeviceTestService isMixerOutputEnabled];
-[AVAudioDeviceTestService isPlaybackForTestEnabled];
-[AVAudioDeviceTestService mediaservicesLostObserver];
-[AVAudioDeviceTestService mediaservicesResetObserver];
-[AVAudioDeviceTestService multichannelMixer];
-[AVAudioDeviceTestService nodeToCaptureData];
-[AVAudioDeviceTestService outputFilter];
-[AVAudioDeviceTestService passExtensionToken:];
-[AVAudioDeviceTestService playback:filePath:completion:];
-[AVAudioDeviceTestService playbackTone:completion:];
-[AVAudioDeviceTestService removeSystemVolumeObserver];
-[AVAudioDeviceTestService resetVolume:];
-[AVAudioDeviceTestService routeChangeObserver];
-[AVAudioDeviceTestService setHearingTestSession:];
-[AVAudioDeviceTestService setInputTapFile:];
-[AVAudioDeviceTestService setInterruptionObserver:];
-[AVAudioDeviceTestService setMediaservicesLostObserver:];
-[AVAudioDeviceTestService setMediaservicesResetObserver:];
-[AVAudioDeviceTestService setMultichannelMixer:];
-[AVAudioDeviceTestService setNodeToCaptureData:];
-[AVAudioDeviceTestService setOutputFilter:];
-[AVAudioDeviceTestService setRouteChangeObserver:];
-[AVAudioDeviceTestService setSystemVolumeObserver:];
-[AVAudioDeviceTestService setTestServiceSupportedOnHardware:];
-[AVAudioDeviceTestService setToneQueue:];
-[AVAudioDeviceTestService setVolume:session:];
-[AVAudioDeviceTestService setupAudioEngineFor:sourceNodeBlock:];
-[AVAudioDeviceTestService setupAudioSessionFor:playbackOnly:completion:];
-[AVAudioDeviceTestService setupAudioSessionForHearingTest:];
-[AVAudioDeviceTestService setupAudioSessionForHearingTestWithStatus:success:];
-[AVAudioDeviceTestService setupMultiChannelMixerForOutputChannel:completion:];
-[AVAudioDeviceTestService setupVolumeObserverForVolume:completion:];
-[AVAudioDeviceTestService startRecording:filePath:completion:];
-[AVAudioDeviceTestService startWithSequence:completion:];
-[AVAudioDeviceTestService stopAudioSession:];
-[AVAudioDeviceTestService stringForInterruptionReason:];
-[AVAudioDeviceTestService stringForRouteChangeReason:];
-[AVAudioDeviceTestService systemVolumeObserver];
-[AVAudioDeviceTestService testServiceSupportedOnHardware];
-[AVAudioDeviceTestService toneQueue];
-[AVAudioDeviceTestService userVolumeBeforeHearingTest];
```
