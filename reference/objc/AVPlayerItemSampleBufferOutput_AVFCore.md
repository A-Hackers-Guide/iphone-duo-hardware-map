# `AVPlayerItemSampleBufferOutput`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVPlayerItemOutput`
- 17 instance variables, 2 properties, 36 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _stateQueue;
@"AVWeakReference" _weakReference;
@"AVWeakReferencingDelegateStorage" _delegateStorage;
^{OpaqueFigPlaybackItem=} _figPlaybackItem;
d _advanceInterval;
^{opaqueCMFormatDescription=} _requestedAudioFormat;
B _hasFigPlaybackItemListeners;
I _flags;
@? _sampleBufferBecameAvailable;
@"AVWeakReference" _weakReferenceToPlayerItemTrack;
i _trackID;
i _extractionID;
@"AVWeakReference" _weakReferenceToPlayerItem;
^{OpaqueFigSampleBufferProvider=} _provider;
B _hasSampleBufferProviderListeners;
{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}} _pendingTimeRange;
B _hasPendingTimeRange;
```

## Properties

```
@property (T@"<AVPlayerItemSampleBufferOutputDelegate>",R,W) delegate;
@property (T@"NSObject<OS_dispatch_queue>",R,N) delegateQueue;
```

## Class methods

```
+[AVPlayerItemSampleBufferOutput initialize];
```

## Instance methods

```
-[AVPlayerItemSampleBufferOutput setDelegate:queue:];
-[AVPlayerItemSampleBufferOutput init];
-[AVPlayerItemSampleBufferOutput dealloc];
-[AVPlayerItemSampleBufferOutput initWithConfiguration:];
-[AVPlayerItemSampleBufferOutput _weakReference];
-[AVPlayerItemSampleBufferOutput copyNextSampleBuffer];
-[AVPlayerItemSampleBufferOutput delegate];
-[AVPlayerItemSampleBufferOutput delegateQueue];
-[AVPlayerItemSampleBufferOutput _removeFigPlaybackItemListeners];
-[AVPlayerItemSampleBufferOutput _weakReferenceToPlayerItemTrack];
-[AVPlayerItemSampleBufferOutput _addFigPlaybackItemListeners];
-[AVPlayerItemSampleBufferOutput _addFigSampleBufferProviderListeners];
-[AVPlayerItemSampleBufferOutput _advanceInterval];
-[AVPlayerItemSampleBufferOutput _attachToPlayerItem:];
-[AVPlayerItemSampleBufferOutput _attachToPlayerItemTrack:figPlaybackItem:];
-[AVPlayerItemSampleBufferOutput _detachFromPlayerItem];
-[AVPlayerItemSampleBufferOutput _detachFromPlayerItemTrack];
-[AVPlayerItemSampleBufferOutput _extractionID];
-[AVPlayerItemSampleBufferOutput _figPlaybackItem];
-[AVPlayerItemSampleBufferOutput _figPlaybackItemDidBecomeAvailable:];
-[AVPlayerItemSampleBufferOutput _figPlaybackItemSampleBufferProviderDataDidBecomeAvailableForItem];
-[AVPlayerItemSampleBufferOutput _figPlaybackItemSampleBufferProviderDidBecomeAvailableForItem:];
-[AVPlayerItemSampleBufferOutput _figPlaybackItemSampleBufferProviderResetOutput:];
-[AVPlayerItemSampleBufferOutput _figPlaybackItemTrackOutputSequenceWasFlushedForTrackID:extractionID:];
-[AVPlayerItemSampleBufferOutput _figPlaybackItemTrackSampleBufferDidBecomeAvailableForTrackID:extractionID:];
-[AVPlayerItemSampleBufferOutput _notifyOutputMediaDataAvailableForTrackID:];
-[AVPlayerItemSampleBufferOutput _removeFigSampleBufferProviderListeners];
-[AVPlayerItemSampleBufferOutput _requestedAudioFormat];
-[AVPlayerItemSampleBufferOutput _setExtractionID:];
-[AVPlayerItemSampleBufferOutput _setFigPlaybackItem:];
-[AVPlayerItemSampleBufferOutput _setTrackID:];
-[AVPlayerItemSampleBufferOutput _trackID];
-[AVPlayerItemSampleBufferOutput copyNextSampleBufferForTrackID:flags:];
-[AVPlayerItemSampleBufferOutput copyNextSampleBufferWithFlags:];
-[AVPlayerItemSampleBufferOutput requestMediaDataForTimeRange:];
-[AVPlayerItemSampleBufferOutput whenNextSampleBufferIsAvailable:];
```
