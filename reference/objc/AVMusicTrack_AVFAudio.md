# `AVMusicTrack`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 12 properties, 46 instance methods, 0 class methods

## Instance variables

```
^v _impl;
```

## Properties

```
@property (TB) usesAutomatedParameters;
@property (T@"AVAudioUnit",&,N) destinationAudioUnit;
@property (TI,N) destinationMIDIEndpoint;
@property (T{_AVBeatRange=dd},N) loopRange;
@property (TB,N,GisLoopingEnabled) loopingEnabled;
@property (Tq,N) numberOfLoops;
@property (Td,N) offsetTime;
@property (TB,N,GisMuted) muted;
@property (TB,N,GisSoloed) soloed;
@property (Td,N) lengthInBeats;
@property (Td,N) lengthInSeconds;
@property (TQ,R,N) timeResolution;
```

## Instance methods

```
-[AVMusicTrack setMuted:];
-[AVMusicTrack isMuted];
-[AVMusicTrack initWithImpl:];
-[AVMusicTrack isLoopingEnabled];
-[AVMusicTrack setLoopingEnabled:];
-[AVMusicTrack dealloc];
-[AVMusicTrack index];
-[AVMusicTrack track];
-[AVMusicTrack setNumberOfLoops:];
-[AVMusicTrack timeResolution];
-[AVMusicTrack numberOfLoops];
-[AVMusicTrack doAddExtendedTempoEvent:atBeat:];
-[AVMusicTrack lengthInSeconds];
-[AVMusicTrack addEvent:atBeat:];
-[AVMusicTrack clearEventsInRange:];
-[AVMusicTrack copyAndMergeEventsInRange:fromTrack:mergeAtBeat:];
-[AVMusicTrack copyEventsInRange:fromTrack:insertAtBeat:];
-[AVMusicTrack createEventIterator];
-[AVMusicTrack cutEventsInRange:];
-[AVMusicTrack destinationAudioUnit];
-[AVMusicTrack destinationMIDIEndpoint];
-[AVMusicTrack doAddAUPresetEvent:atBeat:];
-[AVMusicTrack doAddExtendedNoteOnEvent:atBeat:];
-[AVMusicTrack doAddMIDIChannelEvent:atBeat:];
-[AVMusicTrack doAddMIDIMetaEvent:atBeat:];
-[AVMusicTrack doAddMIDINoteEvent:atBeat:];
-[AVMusicTrack doAddMIDISysexEvent:atBeat:];
-[AVMusicTrack doAddParameterEvent:atBeat:];
-[AVMusicTrack doAddUserEvent:atBeat:];
-[AVMusicTrack enumerateEventsInRange:usingBlock:];
-[AVMusicTrack isSoloed];
-[AVMusicTrack lengthInBeats];
-[AVMusicTrack loopRange];
-[AVMusicTrack moveEventsInRange:byAmount:];
-[AVMusicTrack offsetTime];
-[AVMusicTrack setDestinationAudioUnit:];
-[AVMusicTrack setDestinationMIDIEndpoint:];
-[AVMusicTrack setLengthInBeats:];
-[AVMusicTrack setLengthInSeconds:];
-[AVMusicTrack setLoopRange:];
-[AVMusicTrack setOffsetTime:];
-[AVMusicTrack setSoloed:];
-[AVMusicTrack setUsesAutomatedParameters:];
-[AVMusicTrack setUsesAutomatedParameters:];
-[AVMusicTrack usesAutomatedParameters];
-[AVMusicTrack usesAutomatedParameters];
```
