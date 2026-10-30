# `AVMIDIChannelEvent`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMusicEvent`
- 1 instance variables, 2 properties, 10 instance methods, 0 class methods

## Instance variables

```
{MIDIChannelMessage="status"C"data1"C"data2"C"reserved"C} _msg;
```

## Properties

```
@property (T^{MIDIChannelMessage=CCCC},R) message;
@property (TI) channel;
```

## Instance methods

```
-[AVMIDIChannelEvent setChannel:];
-[AVMIDIChannelEvent channel];
-[AVMIDIChannelEvent initWithMessage:];
-[AVMIDIChannelEvent message];
-[AVMIDIChannelEvent isEqualTo:];
-[AVMIDIChannelEvent data1];
-[AVMIDIChannelEvent data2];
-[AVMIDIChannelEvent initWithChannel:status:data1:data2:];
-[AVMIDIChannelEvent setData1:];
-[AVMIDIChannelEvent setData2:];
```
