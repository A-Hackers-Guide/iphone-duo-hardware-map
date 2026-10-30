# `AVExtendedNoteOnEvent`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMusicEvent`
- 1 instance variables, 6 properties, 15 instance methods, 0 class methods

## Instance variables

```
^{ExtendedNoteOnEvent=IIf{MusicDeviceNoteParams=Iff[1{NoteParamsControlValue=If}]}} _event;
```

## Properties

```
@property (T^{ExtendedNoteOnEvent=IIf{MusicDeviceNoteParams=Iff[1{NoteParamsControlValue=If}]}},R,V_event) event;
@property (Tf) midiNote;
@property (Tf) velocity;
@property (TI) instrumentID;
@property (TI) groupID;
@property (Td) duration;
```

## Instance methods

```
-[AVExtendedNoteOnEvent setGroupID:];
-[AVExtendedNoteOnEvent groupID];
-[AVExtendedNoteOnEvent dealloc];
-[AVExtendedNoteOnEvent event];
-[AVExtendedNoteOnEvent velocity];
-[AVExtendedNoteOnEvent duration];
-[AVExtendedNoteOnEvent setDuration:];
-[AVExtendedNoteOnEvent setVelocity:];
-[AVExtendedNoteOnEvent initWithMIDINote:velocity:groupID:duration:];
-[AVExtendedNoteOnEvent initWithMIDINote:velocity:instrumentID:groupID:duration:];
-[AVExtendedNoteOnEvent initWithNoteOnEvent:];
-[AVExtendedNoteOnEvent instrumentID];
-[AVExtendedNoteOnEvent midiNote];
-[AVExtendedNoteOnEvent setInstrumentID:];
-[AVExtendedNoteOnEvent setMidiNote:];
```
