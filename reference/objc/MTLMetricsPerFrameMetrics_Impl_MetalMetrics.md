# `MTLMetricsPerFrameMetrics_Impl`

- Image: [`/System/Library/PrivateFrameworks/MetalMetrics.framework/MetalMetrics`](../userland/System__Library__PrivateFrameworks__MetalMetrics.framework__MetalMetrics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MTLMetricsPerFrameMetrics`
- 1 instance variables, 24 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"FPMTLMetricsMetricsBundleInternal" _bundle;
```

## Properties

```
@property (Td,R,N) cpuNextDrawableRequestTime;
@property (Td,R,N) cpuNextDrawableAcquiredTime;
@property (Td,R,N) cpuPresentInterval;
@property (Td,R,N) cpuClientPresentationLateness;
@property (Td,R,N) cpuOnGlassPresentationLateness;
@property (Td,R,N) cpuDrawableOnScreenTime;
@property (Td,R,N) cpuDrawableAcquireToPresent;
@property (Td,R,N) cpuDrawableOnScreenDuration;
@property (Td,R,N) cpuFirstCommandBufferBegin;
@property (Td,R,N) cpuLastCommandBufferEnd;
@property (Td,R,N) cpuCommandBufferActive;
@property (Td,R,N) gpuFirstCommandBufferBegin;
@property (Td,R,N) gpuLastCommandBufferEnd;
@property (Td,R,N) gpuCommandBufferActive;
@property (TQ,R,N) numberOfCommandBuffers;
@property (TQ,R,N) frameNumber;
@property (TB,R,N) detached;
@property (TB,R,N) presented;
@property (TB,R,N) isMainLayer;
@property (Td,R,N) lastUpdateTime;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLMetricsPerFrameMetrics_Impl lastUpdateTime];
-[MTLMetricsPerFrameMetrics_Impl surfaceID];
-[MTLMetricsPerFrameMetrics_Impl drawableID];
-[MTLMetricsPerFrameMetrics_Impl detached];
-[MTLMetricsPerFrameMetrics_Impl initWithBundle:];
-[MTLMetricsPerFrameMetrics_Impl isMainLayer];
-[MTLMetricsPerFrameMetrics_Impl presented];
-[MTLMetricsPerFrameMetrics_Impl frameNumber];
-[MTLMetricsPerFrameMetrics_Impl numberOfCommandBuffers];
-[MTLMetricsPerFrameMetrics_Impl cpuClientPresentationLateness];
-[MTLMetricsPerFrameMetrics_Impl cpuCommandBufferActive];
-[MTLMetricsPerFrameMetrics_Impl cpuDrawableAcquireToPresent];
-[MTLMetricsPerFrameMetrics_Impl cpuDrawableOnScreen];
-[MTLMetricsPerFrameMetrics_Impl cpuDrawableOnScreenDuration];
-[MTLMetricsPerFrameMetrics_Impl cpuDrawableOnScreenTime];
-[MTLMetricsPerFrameMetrics_Impl cpuFirstCommandBufferBegin];
-[MTLMetricsPerFrameMetrics_Impl cpuLastCommandBufferEnd];
-[MTLMetricsPerFrameMetrics_Impl cpuNextDrawableAcquiredTime];
-[MTLMetricsPerFrameMetrics_Impl cpuNextDrawableRequestTime];
-[MTLMetricsPerFrameMetrics_Impl cpuOnGlassPresentationLateness];
-[MTLMetricsPerFrameMetrics_Impl cpuPresentInterval];
-[MTLMetricsPerFrameMetrics_Impl gpuCommandBufferActive];
-[MTLMetricsPerFrameMetrics_Impl gpuFirstCommandBufferBegin];
-[MTLMetricsPerFrameMetrics_Impl gpuLastCommandBufferEnd];
-[MTLMetricsPerFrameMetrics_Impl imageQueueId];
```
