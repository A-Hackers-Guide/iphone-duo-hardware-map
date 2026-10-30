# `AVMetricDownloadSummaryEvent`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetricEvent`
- 6 instance variables, 6 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"AVMetricErrorEvent" _errorEvent;
q _recoverableErrorCount;
q _mediaResourceRequestCount;
q _bytesDownloadedCount;
d _downloadDuration;
@"NSArray" _variants;
```

## Properties

```
@property (T@"AVMetricErrorEvent",R) errorEvent;
@property (Tq,R) recoverableErrorCount;
@property (Tq,R) mediaResourceRequestCount;
@property (Tq,R) bytesDownloadedCount;
@property (Td,R) downloadDuration;
@property (T@"NSArray",R) variants;
```

## Class methods

```
+[AVMetricDownloadSummaryEvent supportsSecureCoding];
```

## Instance methods

```
-[AVMetricDownloadSummaryEvent debugDescription];
-[AVMetricDownloadSummaryEvent dealloc];
-[AVMetricDownloadSummaryEvent variants];
-[AVMetricDownloadSummaryEvent encodeWithCoder:];
-[AVMetricDownloadSummaryEvent initWithCoder:];
-[AVMetricDownloadSummaryEvent bytesDownloadedCount];
-[AVMetricDownloadSummaryEvent downloadDuration];
-[AVMetricDownloadSummaryEvent errorEvent];
-[AVMetricDownloadSummaryEvent initWithDate:mediaTime:sessionID:figMetricEvent:errorEvent:recoverableErrorCount:mediaResourceRequestCount:bytesDownloadedCount:downloadDuration:variants:];
-[AVMetricDownloadSummaryEvent mediaResourceRequestCount];
-[AVMetricDownloadSummaryEvent recoverableErrorCount];
```
