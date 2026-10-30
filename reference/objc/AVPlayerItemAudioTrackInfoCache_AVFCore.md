# `AVPlayerItemAudioTrackInfoCache`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" availableTracks;
^{OpaqueFigSimpleMutex=} mutex;
B hasMultiChannelTracks;
```

## Instance methods

```
-[AVPlayerItemAudioTrackInfoCache init];
-[AVPlayerItemAudioTrackInfoCache dealloc];
-[AVPlayerItemAudioTrackInfoCache contains:];
-[AVPlayerItemAudioTrackInfoCache channelCountForTrack:];
-[AVPlayerItemAudioTrackInfoCache isAudioOfMultiChannelFamily];
-[AVPlayerItemAudioTrackInfoCache store:];
```
