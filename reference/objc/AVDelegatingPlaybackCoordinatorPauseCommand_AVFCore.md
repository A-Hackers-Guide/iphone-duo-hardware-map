# `AVDelegatingPlaybackCoordinatorPauseCommand`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVDelegatingPlaybackCoordinatorPlaybackControlCommand`
- 6 instance variables, 2 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"AVDelegatingPlaybackCoordinator" _coordinator;
@"AVCoordinatedPlaybackParticipant" _originator;
@"NSString" _expectedCurrentItemIdentifier;
q _commandOrderIndex;
B _shouldBufferInAnticipationOfPlayback;
f _anticipatedPlaybackRate;
```

## Properties

```
@property (TB,R,N,V_shouldBufferInAnticipationOfPlayback) shouldBufferInAnticipationOfPlayback;
@property (Tf,R,N,V_anticipatedPlaybackRate) anticipatedPlaybackRate;
```

## Instance methods

```
-[AVDelegatingPlaybackCoordinatorPauseCommand init];
-[AVDelegatingPlaybackCoordinatorPauseCommand dealloc];
-[AVDelegatingPlaybackCoordinatorPauseCommand originator];
-[AVDelegatingPlaybackCoordinatorPauseCommand anticipatedPlaybackRate];
-[AVDelegatingPlaybackCoordinatorPauseCommand expectedCurrentItemIdentifier];
-[AVDelegatingPlaybackCoordinatorPauseCommand initWithCoordinator:originator:expectedCurrentItemIdentifier:commandOrderIndex:shouldBufferInAnticipationOfPlayback:anticipatedPlaybackRate:];
-[AVDelegatingPlaybackCoordinatorPauseCommand shouldBufferInAnticipationOfPlayback];
```
