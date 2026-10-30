# `AVAudioSessionPortDescription`

- Image: [`/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`](../userland/System__Library__PrivateFrameworks__AudioSession.framework__AudioSession.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 9 properties, 26 instance methods, 1 class methods

## Instance variables

```
^v _impl;
```

## Properties

```
@property (T@"NSString",R,N) portType;
@property (T@"NSString",R,N) portName;
@property (T@"NSString",R,N) UID;
@property (TB,R) hasHardwareVoiceCallProcessing;
@property (TB,R,GisSpatialAudioEnabled) spatialAudioEnabled;
@property (T@"NSArray",R,N) channels;
@property (T@"NSArray",R,N) dataSources;
@property (T@"AVAudioSessionDataSourceDescription",R,N) selectedDataSource;
@property (T@"AVAudioSessionDataSourceDescription",R,N) preferredDataSource;
```

## Class methods

```
+[AVAudioSessionPortDescription privateCreateArray:owningSession:];
```

## Instance methods

```
-[AVAudioSessionPortDescription UID];
-[AVAudioSessionPortDescription endpointType];
-[AVAudioSessionPortDescription channels];
-[AVAudioSessionPortDescription dataSources];
-[AVAudioSessionPortDescription portType];
-[AVAudioSessionPortDescription preferredDataSource];
-[AVAudioSessionPortDescription portName];
-[AVAudioSessionPortDescription configureChannelsAndDataSources:];
-[AVAudioSessionPortDescription hasHardwareVoiceCallProcessing];
-[AVAudioSessionPortDescription bluetoothMicrophoneExtension];
-[AVAudioSessionPortDescription dealloc];
-[AVAudioSessionPortDescription setPreferredDataSource:error:];
-[AVAudioSessionPortDescription initWithRawPortDescriptionXPC:owningSession:];
-[AVAudioSessionPortDescription isLiveListenSupported];
-[AVAudioSessionPortDescription portSubType];
-[AVAudioSessionPortDescription isLowLatencyAirPlay];
-[AVAudioSessionPortDescription hash];
-[AVAudioSessionPortDescription privateGetID];
-[AVAudioSessionPortDescription description];
-[AVAudioSessionPortDescription privateGetImplementation];
-[AVAudioSessionPortDescription isHeadphones];
-[AVAudioSessionPortDescription isEqualToPort:compareStrict:];
-[AVAudioSessionPortDescription isSpatialAudioEnabled];
-[AVAudioSessionPortDescription isEqual:];
-[AVAudioSessionPortDescription selectedDataSource];
-[AVAudioSessionPortDescription setSupportsSpatialAudio:];
```
