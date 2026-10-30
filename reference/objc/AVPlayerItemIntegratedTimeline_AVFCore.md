# `AVPlayerItemIntegratedTimeline`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 4 properties, 43 instance methods, 1 class methods

## Instance variables

```
^{OpaqueFigItemIntegratedTimeline=} _figTimeline;
@"AVWeakReference" _weakReference;
@"AVWeakReference" _weakReferenceToPrimaryItem;
@"AVWeakReference" _weakReferenceToInterstitialPlayer;
^{OpaqueFigSimpleMutex=} _seekIDMutex;
i _nextSeekIDToGenerate;
i _pendingSeekID;
{?="value"q"timescale"i"flags"I"epoch"q} _pendingSeekTime;
@? _seekCompletionHandler;
i _initialSeekID;
{?="value"q"timescale"i"flags"I"epoch"q} _initialTime;
@"NSDate" _initialDate;
{?="value"q"timescale"i"flags"I"epoch"q} _initialToleranceBefore;
{?="value"q"timescale"i"flags"I"epoch"q} _initialToleranceAfter;
^{__CFDictionary=} _initialOptions;
@"NSObject<OS_dispatch_queue>" _stateQueue;
@"NSMutableArray" _observers;
@"<AVPlayerItemIntegratedTimelineSeekDelegate>" _seekDelegate;
```

## Properties

```
@property (T@"<AVPlayerItemIntegratedTimelineSeekDelegate>",W,N) seekDelegate;
@property (T@"AVPlayerItemIntegratedTimelineSnapshot",R) currentSnapshot;
@property (T{?=qiIq},R) currentTime;
@property (T@"NSDate",R) currentDate;
```

## Class methods

```
+[AVPlayerItemIntegratedTimeline initialize];
```

## Instance methods

```
-[AVPlayerItemIntegratedTimeline currentDate];
-[AVPlayerItemIntegratedTimeline seekToTime:toleranceBefore:toleranceAfter:completionHandler:];
-[AVPlayerItemIntegratedTimeline currentSnapshot];
-[AVPlayerItemIntegratedTimeline removeTimeObserver:];
-[AVPlayerItemIntegratedTimeline dealloc];
-[AVPlayerItemIntegratedTimeline currentTime];
-[AVPlayerItemIntegratedTimeline addPeriodicTimeObserverForInterval:queue:usingBlock:];
-[AVPlayerItemIntegratedTimeline _initInternal];
-[AVPlayerItemIntegratedTimeline _addInterstitialPlayerListeners];
-[AVPlayerItemIntegratedTimeline _addListener];
-[AVPlayerItemIntegratedTimeline _attachCoordinator:];
-[AVPlayerItemIntegratedTimeline _attachInterstitialPlayer:];
-[AVPlayerItemIntegratedTimeline _attachToItem:];
-[AVPlayerItemIntegratedTimeline _cancelPendingSeekAndRegisterSeekID:seekTime:withCompletionHandler:];
-[AVPlayerItemIntegratedTimeline _cancelPendingSeeks];
-[AVPlayerItemIntegratedTimeline _clearCachedSeekWithLock];
-[AVPlayerItemIntegratedTimeline _createSeekID];
-[AVPlayerItemIntegratedTimeline _currentItemForCurrentSegment];
-[AVPlayerItemIntegratedTimeline _currentItemForSegmentType:];
-[AVPlayerItemIntegratedTimeline _currentSegmentTypeOfCurrentSnapshot];
-[AVPlayerItemIntegratedTimeline _deferOrIssueSeekOnFigTimelineForID:time:toleranceBefore:toleranceAfter:options:];
-[AVPlayerItemIntegratedTimeline _ensureObserversAreScheduledForItem:];
-[AVPlayerItemIntegratedTimeline _ensureObserversHandleSnapshotSegmentsChanged];
-[AVPlayerItemIntegratedTimeline _getPendingSeekID];
-[AVPlayerItemIntegratedTimeline _getPendingSeekTime];
-[AVPlayerItemIntegratedTimeline _informDelegateOfSeekForTimeIfNecessary:];
-[AVPlayerItemIntegratedTimeline _interstitialPlayer];
-[AVPlayerItemIntegratedTimeline _issueCachedSeekIfNecessary];
-[AVPlayerItemIntegratedTimeline _primaryItem];
-[AVPlayerItemIntegratedTimeline _removeInterstitialPlayerListeners];
-[AVPlayerItemIntegratedTimeline _removeListeners];
-[AVPlayerItemIntegratedTimeline _resetPlaybackCoordinatorTimelineExpectations:];
-[AVPlayerItemIntegratedTimeline _seekToDate:options:completionHandler:];
-[AVPlayerItemIntegratedTimeline _seekToTime:toleranceBefore:toleranceAfter:options:completionHandler:];
-[AVPlayerItemIntegratedTimeline _setInitialSeekState:time:date:toleranceBefore:toleranceAfter:options:];
-[AVPlayerItemIntegratedTimeline _shouldDeferSeekToDelegate];
-[AVPlayerItemIntegratedTimeline _shouldIssueCachedSeek:];
-[AVPlayerItemIntegratedTimeline _unregisterInvokeAndReleasePendingSeekCompletionHandlerForSeekID:finished:];
-[AVPlayerItemIntegratedTimeline addBoundaryTimeObserverForSegment:offsetsIntoSegment:queue:usingBlock:];
-[AVPlayerItemIntegratedTimeline noteSeekID:didFinish:];
-[AVPlayerItemIntegratedTimeline seekDelegate];
-[AVPlayerItemIntegratedTimeline seekToDate:completionHandler:];
-[AVPlayerItemIntegratedTimeline setSeekDelegate:];
```
