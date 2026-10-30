# `AudioDevice`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 34 instance methods, 0 class methods

## Instance variables

```
B _isInput;
B _isRunning;
B _isDirty;
I _deviceID;
I _sourceID;
I _transType;
f _volume;
@"PLAudioAgent" _ctx;
@? _audioPropertyHandlerBlock;
@"NSDate" _lastUpdateTime;
```

## Properties

```
@property (T@"PLAudioAgent",W,N,V_ctx) ctx;
@property (TI,N,V_deviceID) deviceID;
@property (TI,N,V_sourceID) sourceID;
@property (TI,N,V_transType) transType;
@property (TB,N,V_isInput) isInput;
@property (TB,N,V_isRunning) isRunning;
@property (Tf,N,V_volume) volume;
@property (T@?,C,N,V_audioPropertyHandlerBlock) audioPropertyHandlerBlock;
@property (TB,N,V_isDirty) isDirty;
@property (T@"NSDate",&,V_lastUpdateTime) lastUpdateTime;
```

## Instance methods

```
-[AudioDevice lastUpdateTime];
-[AudioDevice isRunning];
-[AudioDevice isInput];
-[AudioDevice volume];
-[AudioDevice deviceID];
-[AudioDevice setLastUpdateTime:];
-[AudioDevice setSourceID:];
-[AudioDevice setVolume:];
-[AudioDevice sourceID];
-[AudioDevice setDeviceID:];
-[AudioDevice setIsDirty:];
-[AudioDevice isDirty];
-[AudioDevice setIsRunning:];
-[AudioDevice ctx];
-[AudioDevice setCtx:];
-[AudioDevice setIsInput:];
-[AudioDevice addAudioDeviceListener];
-[AudioDevice audioPropertyHandlerBlock];
-[AudioDevice cleanAndUpdateDeviceInfo];
-[AudioDevice flushAndUpdateDeviceInfoWithBlock:];
-[AudioDevice getAudioDeviceIsMute];
-[AudioDevice getAudioDeviceIsRunningSomewhere];
-[AudioDevice getAudioDeviceSource];
-[AudioDevice getAudioDeviceTransportType];
-[AudioDevice getAudioDeviceVolume];
-[AudioDevice handleAudioDevicePropertyChange:addresses:];
-[AudioDevice initAudioPropertyHandler];
-[AudioDevice initInputDeviceWithCtx:];
-[AudioDevice initOutputDeviceWithCtx:];
-[AudioDevice removeAudioDeviceListener];
-[AudioDevice setAudioPropertyHandlerBlock:];
-[AudioDevice setTransType:];
-[AudioDevice transType];
-[AudioDevice updateDefaultAudioDeviceInfo];
```
