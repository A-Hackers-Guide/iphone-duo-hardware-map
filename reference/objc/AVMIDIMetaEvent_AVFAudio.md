# `AVMIDIMetaEvent`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMusicEvent`
- 1 instance variables, 2 properties, 5 instance methods, 0 class methods

## Instance variables

```
^{MIDIMetaEvent=CCCCI[1C]} _event;
```

## Properties

```
@property (T^{MIDIMetaEvent=CCCCI[1C]},R,V_event) metaEvent;
@property (Tq,R) type;
```

## Instance methods

```
-[AVMIDIMetaEvent dealloc];
-[AVMIDIMetaEvent type];
-[AVMIDIMetaEvent initWithType:data:];
-[AVMIDIMetaEvent initWithMetaEvent:];
-[AVMIDIMetaEvent metaEvent];
```
