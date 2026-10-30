# `AVAudioUnitSampler`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAudioUnitMIDIInstrument`
- 0 instance variables, 4 properties, 13 instance methods, 0 class methods

## Properties

```
@property (Tf,N) stereoPan;
@property (Tf,N) overallGain;
@property (Tf,N) masterGain;
@property (Tf,N) globalTuning;
```

## Instance methods

```
-[AVAudioUnitSampler init];
-[AVAudioUnitSampler setOverallGain:];
-[AVAudioUnitSampler globalTuning];
-[AVAudioUnitSampler initWithAudioComponentDescription:];
-[AVAudioUnitSampler loadAudioFilesAtURLs:error:];
-[AVAudioUnitSampler loadInstrumentAtURL:error:];
-[AVAudioUnitSampler loadSoundBankInstrumentAtURL:program:bankMSB:bankLSB:error:];
-[AVAudioUnitSampler masterGain];
-[AVAudioUnitSampler overallGain];
-[AVAudioUnitSampler setGlobalTuning:];
-[AVAudioUnitSampler setMasterGain:];
-[AVAudioUnitSampler setStereoPan:];
-[AVAudioUnitSampler stereoPan];
```
