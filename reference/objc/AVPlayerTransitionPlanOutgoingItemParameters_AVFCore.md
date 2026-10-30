# `AVPlayerTransitionPlanOutgoingItemParameters`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVPlayerTransitionPlanItemParameters`
- 3 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
{?="value"q"timescale"i"flags"I"epoch"q} _overlappedPlaybackEndTime;
{?="value"q"timescale"i"flags"I"epoch"q} _advanceTimeForOverlappedPlayback;
{?="value"q"timescale"i"flags"I"epoch"q} _forwardPlaybackEndTime;
```

## Properties

```
@property (T{?=qiIq},N,V_overlappedPlaybackEndTime) overlappedPlaybackEndTime;
@property (T{?=qiIq},N,V_advanceTimeForOverlappedPlayback) advanceTimeForOverlappedPlayback;
@property (T{?=qiIq},N,V_forwardPlaybackEndTime) forwardPlaybackEndTime;
```

## Instance methods

```
-[AVPlayerTransitionPlanOutgoingItemParameters init];
-[AVPlayerTransitionPlanOutgoingItemParameters forwardPlaybackEndTime];
-[AVPlayerTransitionPlanOutgoingItemParameters setForwardPlaybackEndTime:];
-[AVPlayerTransitionPlanOutgoingItemParameters advanceTimeForOverlappedPlayback];
-[AVPlayerTransitionPlanOutgoingItemParameters applyToAVPlayerItem:];
-[AVPlayerTransitionPlanOutgoingItemParameters overlappedPlaybackEndTime];
-[AVPlayerTransitionPlanOutgoingItemParameters setAdvanceTimeForOverlappedPlayback:];
-[AVPlayerTransitionPlanOutgoingItemParameters setOverlappedPlaybackEndTime:];
```
