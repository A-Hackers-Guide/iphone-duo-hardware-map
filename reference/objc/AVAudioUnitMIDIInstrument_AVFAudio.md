# `AVAudioUnitMIDIInstrument`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAudioUnit`
- Protocols: `AVAudioMixing`
- 0 instance variables, 5 properties, 13 instance methods, 0 class methods

## Properties

```
@property (Tf,D,N) volume;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AVAudioUnitMIDIInstrument initWithAudioComponentDescription:];
-[AVAudioUnitMIDIInstrument sendController:withValue:onChannel:];
-[AVAudioUnitMIDIInstrument sendMIDIEvent:data1:];
-[AVAudioUnitMIDIInstrument sendMIDIEvent:data1:data2:];
-[AVAudioUnitMIDIInstrument sendMIDIEventList:];
-[AVAudioUnitMIDIInstrument sendMIDISysExEvent:];
-[AVAudioUnitMIDIInstrument sendPitchBend:onChannel:];
-[AVAudioUnitMIDIInstrument sendPressure:onChannel:];
-[AVAudioUnitMIDIInstrument sendPressureForKey:withValue:onChannel:];
-[AVAudioUnitMIDIInstrument sendProgramChange:bankMSB:bankLSB:onChannel:];
-[AVAudioUnitMIDIInstrument sendProgramChange:onChannel:];
-[AVAudioUnitMIDIInstrument startNote:withVelocity:onChannel:];
-[AVAudioUnitMIDIInstrument stopNote:onChannel:];
```
