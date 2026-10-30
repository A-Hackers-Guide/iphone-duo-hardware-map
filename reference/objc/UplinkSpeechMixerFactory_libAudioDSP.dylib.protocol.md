# `UplinkSpeechMixerFactory` (protocol)

- Image: [`/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib`](../userland/System__Library__Frameworks__AudioToolbox.framework__libAudioDSP.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 5 instance methods, 0 class methods

## Properties

```
@property (T{AudioStreamBasicDescription=dIIIIIIII},N) streamDescription;
@property (TI,N) maximumFramesPerSlice;
```

## Instance methods

```
-[UplinkSpeechMixerFactory streamDescription];
-[UplinkSpeechMixerFactory setStreamDescription:];
-[UplinkSpeechMixerFactory createUplinkSpeechMixer];
-[UplinkSpeechMixerFactory maximumFramesPerSlice];
-[UplinkSpeechMixerFactory setMaximumFramesPerSlice:];
```
