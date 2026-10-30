# `AVAudioSessionChannelDescription`

- Image: [`/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`](../userland/System__Library__PrivateFrameworks__AudioSession.framework__AudioSession.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 4 properties, 11 instance methods, 2 class methods

## Instance variables

```
^v _impl;
```

## Properties

```
@property (T@"NSString",R,N) channelName;
@property (T@"NSString",R,N) owningPortUID;
@property (TQ,R,N) channelNumber;
@property (TI,R,N) channelLabel;
```

## Class methods

```
+[AVAudioSessionChannelDescription privateCreate:portUID:channelNumber:];
+[AVAudioSessionChannelDescription privateCreateArray:portUID:];
```

## Instance methods

```
-[AVAudioSessionChannelDescription channelName];
-[AVAudioSessionChannelDescription init];
-[AVAudioSessionChannelDescription dealloc];
-[AVAudioSessionChannelDescription owningPortUID];
-[AVAudioSessionChannelDescription channelLabel];
-[AVAudioSessionChannelDescription isEqualToChannel:];
-[AVAudioSessionChannelDescription hash];
-[AVAudioSessionChannelDescription description];
-[AVAudioSessionChannelDescription privateGetImplementation];
-[AVAudioSessionChannelDescription isEqual:];
-[AVAudioSessionChannelDescription channelNumber];
```
