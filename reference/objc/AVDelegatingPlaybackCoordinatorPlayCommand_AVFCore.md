# `AVDelegatingPlaybackCoordinatorPlayCommand`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVDelegatingPlaybackCoordinatorPlaybackControlCommand`
- 7 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"AVDelegatingPlaybackCoordinator" _coordinator;
@"AVCoordinatedPlaybackParticipant" _originator;
@"NSString" _expectedCurrentItemIdentifier;
q _commandOrderIndex;
f _rate;
{?="value"q"timescale"i"flags"I"epoch"q} _itemTime;
{?="value"q"timescale"i"flags"I"epoch"q} _hostClockTime;
```

## Properties

```
@property (Tf,R,N,V_rate) rate;
@property (T{?=qiIq},R,N,V_itemTime) itemTime;
@property (T{?=qiIq},R,N,V_hostClockTime) hostClockTime;
```

## Instance methods

```
-[AVDelegatingPlaybackCoordinatorPlayCommand rate];
-[AVDelegatingPlaybackCoordinatorPlayCommand init];
-[AVDelegatingPlaybackCoordinatorPlayCommand dealloc];
-[AVDelegatingPlaybackCoordinatorPlayCommand originator];
-[AVDelegatingPlaybackCoordinatorPlayCommand expectedCurrentItemIdentifier];
-[AVDelegatingPlaybackCoordinatorPlayCommand hostClockTime];
-[AVDelegatingPlaybackCoordinatorPlayCommand initWithCoordinator:originator:expectedCurrentItemIdentifier:commandOrderIndex:rate:itemTime:hostClockTime:];
-[AVDelegatingPlaybackCoordinatorPlayCommand itemTime];
```
