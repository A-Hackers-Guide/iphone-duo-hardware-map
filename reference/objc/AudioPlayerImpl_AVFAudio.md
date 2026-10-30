# `AudioPlayerImpl`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
@"<AVAudioPlayerDelegate>" _delegate;
@"NSData" _data;
@"NSURL" _url;
@"NSDictionary" _actualSettings;
@"AVAudioFormat" _format;
B _playRetain;
@"NSArray" _channelAssignments;
@"AVAudioSession" _audioSession;
B _sessionListenerWasSet;
Q _endInterruptionFlags;
^v _localPlayer;
{unfair_lock="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} _mutex;
```

## Instance methods

```
-[AudioPlayerImpl init];
-[AudioPlayerImpl dealloc];
```
