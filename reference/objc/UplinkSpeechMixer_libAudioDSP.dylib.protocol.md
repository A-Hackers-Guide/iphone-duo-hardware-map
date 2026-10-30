# `UplinkSpeechMixer` (protocol)

- Image: [`/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib`](../userland/System__Library__Frameworks__AudioToolbox.framework__libAudioDSP.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 3 instance methods, 0 class methods

## Properties

```
@property (T{AudioStreamBasicDescription=dIIIIIIII},R,N) streamDescription;
@property (TI,R,N) maximumFramesPerSlice;
@property (T@?,R,N) processBlock;
```

## Instance methods

```
-[UplinkSpeechMixer streamDescription];
-[UplinkSpeechMixer processBlock];
-[UplinkSpeechMixer maximumFramesPerSlice];
```
