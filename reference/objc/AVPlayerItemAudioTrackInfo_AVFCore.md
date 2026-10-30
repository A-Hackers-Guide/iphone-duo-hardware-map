# `AVPlayerItemAudioTrackInfo`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 5 instance methods, 1 class methods

## Instance variables

```
i trackID;
i channelCount;
B isDerivedFromMultiChannelAudioTrack;
```

## Class methods

```
+[AVPlayerItemAudioTrackInfo playerItemTrackInfoForTrack:];
```

## Instance methods

```
-[AVPlayerItemAudioTrackInfo init];
-[AVPlayerItemAudioTrackInfo hash];
-[AVPlayerItemAudioTrackInfo isEqual:];
-[AVPlayerItemAudioTrackInfo servesAsMultichannelAudio];
-[AVPlayerItemAudioTrackInfo setChannelCount:isDerivedFromMultiChannelAudioTrack:];
```
