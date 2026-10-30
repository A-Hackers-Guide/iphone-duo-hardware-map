# `AVAudioInputNode`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAudioIONode`
- Protocols: `AVAudioMixing`
- 0 instance variables, 9 properties, 13 instance methods, 0 class methods

## Properties

```
@property (TB,N,GisVoiceProcessingBypassed) voiceProcessingBypassed;
@property (TB,N,GisVoiceProcessingAGCEnabled) voiceProcessingAGCEnabled;
@property (TB,N,GisVoiceProcessingInputMuted) voiceProcessingInputMuted;
@property (T{AVAudioVoiceProcessingOtherAudioDuckingConfiguration=Bq},N) voiceProcessingOtherAudioDuckingConfiguration;
@property (Tf,D,N) volume;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AVAudioInputNode rate];
-[AVAudioInputNode voiceProcessingOtherAudioDuckingConfiguration];
-[AVAudioInputNode isVoiceProcessingInputMuted];
-[AVAudioInputNode setRate:];
-[AVAudioInputNode setRealtimeSafeManualRenderingInputPCMFormat:inputBlock:];
-[AVAudioInputNode isVoiceProcessingBypassed];
-[AVAudioInputNode setManualRenderingInputPCMFormat:inputBlock:];
-[AVAudioInputNode setMutedSpeechActivityEventListener:];
-[AVAudioInputNode setVoiceProcessingAGCEnabled:];
-[AVAudioInputNode isVoiceProcessingAGCEnabled];
-[AVAudioInputNode setVoiceProcessingInputMuted:];
-[AVAudioInputNode setVoiceProcessingBypassed:];
-[AVAudioInputNode setVoiceProcessingOtherAudioDuckingConfiguration:];
```
