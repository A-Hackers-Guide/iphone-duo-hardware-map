# `AVDelegatingPlaybackCoordinatorSeekCommand`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVDelegatingPlaybackCoordinatorPlaybackControlCommand`
- 9 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"AVDelegatingPlaybackCoordinator" _coordinator;
@"AVCoordinatedPlaybackParticipant" _originator;
@"NSString" _expectedCurrentItemIdentifier;
q _commandOrderIndex;
{?="value"q"timescale"i"flags"I"epoch"q} _itemTime;
B _shouldPause;
B _shouldBufferInAnticipationOfPlayback;
f _anticipatedPlaybackRate;
@"NSDate" _completionDueDate;
```

## Properties

```
@property (T{?=qiIq},R,N,V_itemTime) itemTime;
@property (TB,R,N,V_shouldBufferInAnticipationOfPlayback) shouldBufferInAnticipationOfPlayback;
@property (Tf,R,N,V_anticipatedPlaybackRate) anticipatedPlaybackRate;
@property (T@"NSDate",R,N,V_completionDueDate) completionDueDate;
```

## Instance methods

```
-[AVDelegatingPlaybackCoordinatorSeekCommand init];
-[AVDelegatingPlaybackCoordinatorSeekCommand dealloc];
-[AVDelegatingPlaybackCoordinatorSeekCommand originator];
-[AVDelegatingPlaybackCoordinatorSeekCommand anticipatedPlaybackRate];
-[AVDelegatingPlaybackCoordinatorSeekCommand completionDueDate];
-[AVDelegatingPlaybackCoordinatorSeekCommand expectedCurrentItemIdentifier];
-[AVDelegatingPlaybackCoordinatorSeekCommand initWithCoordinator:originator:expectedCurrentItemIdentifier:commandOrderIndex:itemTime:shouldPause:shouldBufferInAnticipationOfPlayback:anticipatedPlaybackRate:completionDueDate:];
-[AVDelegatingPlaybackCoordinatorSeekCommand itemTime];
-[AVDelegatingPlaybackCoordinatorSeekCommand shouldBufferInAnticipationOfPlayback];
```
