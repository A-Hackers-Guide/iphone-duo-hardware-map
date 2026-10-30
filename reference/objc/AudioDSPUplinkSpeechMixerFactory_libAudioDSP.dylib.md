# `AudioDSPUplinkSpeechMixerFactory`

- Image: [`/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib`](../userland/System__Library__Frameworks__AudioToolbox.framework__libAudioDSP.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UplinkSpeechMixerFactory`
- 1 instance variables, 6 properties, 6 instance methods, 0 class methods

## Instance variables

```
{AudioDSPUplinkSpeechMixerSettings="streamDescription"{AudioStreamBasicDescription="mSampleRate"d"mFormatID"I"mFormatFlags"I"mBytesPerPacket"I"mFramesPerPacket"I"mBytesPerFrame"I"mChannelsPerFrame"I"mBitsPerChannel"I"mReserved"I}"maximumFramesPerSlice"I} _settings;
```

## Properties

```
@property (T{AudioStreamBasicDescription=dIIIIIIII},D,N) streamDescription;
@property (TI,D,N) maximumFramesPerSlice;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AudioDSPUplinkSpeechMixerFactory init];
-[AudioDSPUplinkSpeechMixerFactory streamDescription];
-[AudioDSPUplinkSpeechMixerFactory setStreamDescription:];
-[AudioDSPUplinkSpeechMixerFactory createUplinkSpeechMixer];
-[AudioDSPUplinkSpeechMixerFactory maximumFramesPerSlice];
-[AudioDSPUplinkSpeechMixerFactory setMaximumFramesPerSlice:];
```
