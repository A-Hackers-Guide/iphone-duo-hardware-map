# `AVAudioIONode`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAudioNode`
- 0 instance variables, 3 properties, 11 instance methods, 0 class methods

## Properties

```
@property (Td,R,N) presentationLatency;
@property (T^{OpaqueAudioComponentInstance=},R,N) audioUnit;
@property (TB,R,N,GisVoiceProcessingEnabled) voiceProcessingEnabled;
```

## Instance methods

```
-[AVAudioIONode audioUnit];
-[AVAudioIONode enableRealtimeRenderingModeWithIOUnit:isInput:forceIOUnitReset:];
-[AVAudioIONode didAttachToEngine:];
-[AVAudioIONode didDetachFromEngine:error:];
-[AVAudioIONode enableManualRenderingMode:isInput:];
-[AVAudioIONode initWithIOUnit:isInput:];
-[AVAudioIONode isInManualRenderingMode];
-[AVAudioIONode isVoiceProcessingEnabled];
-[AVAudioIONode manualRenderingMode];
-[AVAudioIONode presentationLatency];
-[AVAudioIONode setVoiceProcessingEnabled:error:];
```
