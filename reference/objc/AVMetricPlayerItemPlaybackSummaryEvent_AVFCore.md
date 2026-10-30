# `AVMetricPlayerItemPlaybackSummaryEvent`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetricEvent`
- 10 instance variables, 10 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"AVMetricErrorEvent" _errorEvent;
q _recoverableErrorCount;
q _stallCount;
q _variantSwitchCount;
q _playbackDuration;
q _mediaResourceRequestCount;
d _timeSpentRecoveringFromStall;
d _timeSpentInInitialStartup;
q _timeWeightedAverageBitrate;
q _timeWeightedPeakBitrate;
```

## Properties

```
@property (T@"AVMetricErrorEvent",R) errorEvent;
@property (Tq,R) recoverableErrorCount;
@property (Tq,R) stallCount;
@property (Tq,R) variantSwitchCount;
@property (Tq,R) playbackDuration;
@property (Tq,R) mediaResourceRequestCount;
@property (Td,R) timeSpentRecoveringFromStall;
@property (Td,R) timeSpentInInitialStartup;
@property (Tq,R) timeWeightedAverageBitrate;
@property (Tq,R) timeWeightedPeakBitrate;
```

## Class methods

```
+[AVMetricPlayerItemPlaybackSummaryEvent supportsSecureCoding];
```

## Instance methods

```
-[AVMetricPlayerItemPlaybackSummaryEvent debugDescription];
-[AVMetricPlayerItemPlaybackSummaryEvent dealloc];
-[AVMetricPlayerItemPlaybackSummaryEvent encodeWithCoder:];
-[AVMetricPlayerItemPlaybackSummaryEvent initWithCoder:];
-[AVMetricPlayerItemPlaybackSummaryEvent playbackDuration];
-[AVMetricPlayerItemPlaybackSummaryEvent errorEvent];
-[AVMetricPlayerItemPlaybackSummaryEvent initWithDate:mediaTime:sessionID:figMetricEvent:errorEvent:recoverableErrorCount:stallCount:variantSwitchCount:playbackDuration:mediaResourceRequestCount:timeSpentRecoveringFromStall:timeSpentInInitialStartup:timeWeightedAverageBitrate:timeWeightedPeakBitrate:];
-[AVMetricPlayerItemPlaybackSummaryEvent mediaResourceRequestCount];
-[AVMetricPlayerItemPlaybackSummaryEvent recoverableErrorCount];
-[AVMetricPlayerItemPlaybackSummaryEvent stallCount];
-[AVMetricPlayerItemPlaybackSummaryEvent timeSpentInInitialStartup];
-[AVMetricPlayerItemPlaybackSummaryEvent timeSpentRecoveringFromStall];
-[AVMetricPlayerItemPlaybackSummaryEvent timeWeightedAverageBitrate];
-[AVMetricPlayerItemPlaybackSummaryEvent timeWeightedPeakBitrate];
-[AVMetricPlayerItemPlaybackSummaryEvent variantSwitchCount];
```
