# `AVMusicTrackEventIterator`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 11 instance methods, 0 class methods

## Instance variables

```
^{MusicTrackEventIteratorImpl=^{OpaqueMusicEventIterator}} _impl;
```

## Instance methods

```
-[AVMusicTrackEventIterator nextEvent];
-[AVMusicTrackEventIterator initWithImpl:];
-[AVMusicTrackEventIterator setEventTime:];
-[AVMusicTrackEventIterator deleteEvent];
-[AVMusicTrackEventIterator previousEvent];
-[AVMusicTrackEventIterator hasCurrentEvent];
-[AVMusicTrackEventIterator getEventInfo:outEventType:eventData:dataSize:];
-[AVMusicTrackEventIterator hasNextEvent];
-[AVMusicTrackEventIterator hasPreviousEvent];
-[AVMusicTrackEventIterator seek:];
-[AVMusicTrackEventIterator setEventInfo:data:];
```
