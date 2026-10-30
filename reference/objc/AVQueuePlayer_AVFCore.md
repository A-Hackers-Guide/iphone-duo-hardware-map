# `AVQueuePlayer`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVPlayer`
- 1 instance variables, 2 properties, 21 instance methods, 3 class methods

## Instance variables

```
@"AVQueuePlayerInternal" _queuePlayer;
```

## Properties

```
@property (TB,N,GsupportsAdvanceTimeForOverlappedPlayback,SsetSupportsAdvanceTimeForOverlappedPlayback:) supportsAdvanceTimeForOverlappedPlayback;
@property (T@"NSArray",C,N) itemsToPrebuffer;
```

## Class methods

```
+[AVQueuePlayer initialize];
+[AVQueuePlayer _defaultActionAtItemEnd];
+[AVQueuePlayer queuePlayerWithItems:];
```

## Instance methods

```
-[AVQueuePlayer init];
-[AVQueuePlayer dealloc];
-[AVQueuePlayer items];
-[AVQueuePlayer removeItem:];
-[AVQueuePlayer removeAllItems];
-[AVQueuePlayer initWithItems:];
-[AVQueuePlayer advanceToNextItem];
-[AVQueuePlayer setActionAtItemEnd:];
-[AVQueuePlayer willChangeItems];
-[AVQueuePlayer _canOverlapPlaybackConditionsChangedFor:dueTo:];
-[AVQueuePlayer _canOverlapPlaybackFromPlayerItem:toPlayerItem:];
-[AVQueuePlayer _getChannelCountInFirstAudioTrackForItem:];
-[AVQueuePlayer _updateCurrentOverlapStateGiven:hasStateChanged:];
-[AVQueuePlayer canInsertItem:afterItem:];
-[AVQueuePlayer canOverlapPlaybackFromPlayerItem:toPlayerItem:];
-[AVQueuePlayer didChangeItems];
-[AVQueuePlayer insertItem:afterItem:];
-[AVQueuePlayer itemsToPrebuffer];
-[AVQueuePlayer setItemsToPrebuffer:];
-[AVQueuePlayer setSupportsAdvanceTimeForOverlappedPlayback:];
-[AVQueuePlayer supportsAdvanceTimeForOverlappedPlayback];
```
