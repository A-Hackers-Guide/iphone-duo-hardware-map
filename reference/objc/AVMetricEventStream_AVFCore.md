# `AVMetricEventStream`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 0 properties, 10 instance methods, 18 class methods

## Instance variables

```
^{__CFDictionary=} _publisherByEventTimeline;
^{__CFArray=} _eventTimelines;
@"AVWeakReferencingDelegateStorage" _delegateStorage;
@"NSMutableArray" _metricEventClassesToSubscribe;
B _shouldSubscribeToAllMetricEventClasses;
@"AVWeakReference" _weakSelf;
@"NSObject<OS_dispatch_queue>" _internalQueue;
```

## Class methods

```
+[AVMetricEventStream eventStream];
+[AVMetricEventStream contentKeyRequestEventWithFigMetricEvent:];
+[AVMetricEventStream downloadSummaryEventWithFigMetricEvent:];
+[AVMetricEventStream errorEventWithFigMetricEvent:];
+[AVMetricEventStream initialLikelyToKeepUpEventWithFigMetricEvent:];
+[AVMetricEventStream likelyToKeepUpEventWithFigMetricEvent:];
+[AVMetricEventStream mediaSegmentRequestEventWithFigMetricEvent:];
+[AVMetricEventStream metricEventForFigMetricEvent:];
+[AVMetricEventStream playbackModeSwitchEventWithFigMetricEvent:];
+[AVMetricEventStream playbackSummaryEventWithFigMetricEvent:];
+[AVMetricEventStream playlistRequestEventWithFigMetricEvent:];
+[AVMetricEventStream rateChangeEventWithFigMetricEvent:];
+[AVMetricEventStream resourceRequestEventWithFigMetricEvent:];
+[AVMetricEventStream seekDidCompleteEventWithFigMetricEvent:];
+[AVMetricEventStream seekEventWithFigMetricEvent:];
+[AVMetricEventStream stallEventWithFigMetricEvent:];
+[AVMetricEventStream variantChangeEventWithFigMetricEvent:];
+[AVMetricEventStream variantChangeStartEventWithFigMetricEvent:];
```

## Instance methods

```
-[AVMetricEventStream init];
-[AVMetricEventStream dealloc];
-[AVMetricEventStream addPublisher:];
-[AVMetricEventStream addPublisher:eventTimeline:];
-[AVMetricEventStream didReceiveEventForMetricEventTimeline:event:];
-[AVMetricEventStream getFigMetricEventIDForAVMetricClass:];
-[AVMetricEventStream setSubscriber:queue:];
-[AVMetricEventStream subscribeToAllMetricEvents];
-[AVMetricEventStream subscribeToMetricEvent:];
-[AVMetricEventStream subscribeToMetricEvents:];
```
