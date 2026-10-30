# `AVVideoPerformanceMetrics`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 11 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"AVVideoPerformanceMetricsInternal" _performanceMetricsInternal;
```

## Properties

```
@property (Tq,R,N) totalNumberOfFrames;
@property (Tq,R,N) numberOfDroppedFrames;
@property (Tq,R,N) numberOfCorruptedFrames;
@property (Tq,R,N) numberOfFramesDisplayedUsingOptimizedCompositing;
@property (Td,R,N) totalAccumulatedFrameDelay;
@property (TQ,R,N) totalNumberOfVideoFrames;
@property (TQ,R,N) numberOfDroppedVideoFrames;
@property (TQ,R,N) numberOfCorruptedVideoFrames;
@property (TQ,R,N) numberOfDisplayCompositedVideoFrames;
@property (TQ,R,N) numberOfNonDisplayCompositedVideoFrames;
@property (Td,R,N) totalFrameDelay;
```

## Instance methods

```
-[AVVideoPerformanceMetrics initWithDictionary:];
-[AVVideoPerformanceMetrics init];
-[AVVideoPerformanceMetrics dealloc];
-[AVVideoPerformanceMetrics totalFrameDelay];
-[AVVideoPerformanceMetrics numberOfCorruptedFrames];
-[AVVideoPerformanceMetrics numberOfCorruptedVideoFrames];
-[AVVideoPerformanceMetrics numberOfDisplayCompositedVideoFrames];
-[AVVideoPerformanceMetrics numberOfDroppedFrames];
-[AVVideoPerformanceMetrics numberOfDroppedVideoFrames];
-[AVVideoPerformanceMetrics numberOfFramesDisplayedUsingOptimizedCompositing];
-[AVVideoPerformanceMetrics numberOfNonDisplayCompositedVideoFrames];
-[AVVideoPerformanceMetrics totalAccumulatedFrameDelay];
-[AVVideoPerformanceMetrics totalNumberOfFrames];
-[AVVideoPerformanceMetrics totalNumberOfVideoFrames];
```
