# `AVMetricPlayerItemInitialLikelyToKeepUpEvent`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetricPlayerItemLikelyToKeepUpEvent`
- 3 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _playlistRequestEvents;
@"NSArray" _mediaSegmentRequestEvents;
@"NSArray" _contentKeyRequestEvents;
```

## Properties

```
@property (T@"NSArray",R) playlistRequestEvents;
@property (T@"NSArray",R) mediaSegmentRequestEvents;
@property (T@"NSArray",R) contentKeyRequestEvents;
```

## Class methods

```
+[AVMetricPlayerItemInitialLikelyToKeepUpEvent supportsSecureCoding];
```

## Instance methods

```
-[AVMetricPlayerItemInitialLikelyToKeepUpEvent debugDescription];
-[AVMetricPlayerItemInitialLikelyToKeepUpEvent dealloc];
-[AVMetricPlayerItemInitialLikelyToKeepUpEvent encodeWithCoder:];
-[AVMetricPlayerItemInitialLikelyToKeepUpEvent initWithCoder:];
-[AVMetricPlayerItemInitialLikelyToKeepUpEvent contentKeyRequestEvents];
-[AVMetricPlayerItemInitialLikelyToKeepUpEvent initWithDate:mediaTime:sessionID:figMetricEvent:variant:timeTaken:loadedTimeRanges:playlistRequestEvents:mediaSegmentRequestEvents:contentKeyRequestEvents:];
-[AVMetricPlayerItemInitialLikelyToKeepUpEvent mediaSegmentRequestEvents];
-[AVMetricPlayerItemInitialLikelyToKeepUpEvent playlistRequestEvents];
```
