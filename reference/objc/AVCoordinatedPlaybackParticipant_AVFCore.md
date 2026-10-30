# `AVCoordinatedPlaybackParticipant`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _suspensionReasons;
B _readyToPlay;
@"NSUUID" _identifier;
```

## Properties

```
@property (T@"NSArray",R,N,V_suspensionReasons) suspensionReasons;
@property (TB,R,N,GisReadyToPlay,V_readyToPlay) readyToPlay;
@property (T@"NSUUID",R,N,V_identifier) identifier;
```

## Instance methods

```
-[AVCoordinatedPlaybackParticipant identifier];
-[AVCoordinatedPlaybackParticipant dealloc];
-[AVCoordinatedPlaybackParticipant isReadyToPlay];
-[AVCoordinatedPlaybackParticipant suspensionReasons];
-[AVCoordinatedPlaybackParticipant hash];
-[AVCoordinatedPlaybackParticipant isEqual:];
-[AVCoordinatedPlaybackParticipant initWithParticipantIdentifier:readyToPlay:suspensionReasons:];
```
