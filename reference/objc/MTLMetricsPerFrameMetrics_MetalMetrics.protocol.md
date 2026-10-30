# `MTLMetricsPerFrameMetrics` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalMetrics.framework/MetalMetrics`](../userland/System__Library__PrivateFrameworks__MetalMetrics.framework__MetalMetrics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 20 properties, 20 instance methods, 0 class methods

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
```

## Instance methods

```
-[MTLMetricsPerFrameMetrics lastUpdateTime];
-[MTLMetricsPerFrameMetrics detached];
-[MTLMetricsPerFrameMetrics isMainLayer];
-[MTLMetricsPerFrameMetrics presented];
-[MTLMetricsPerFrameMetrics frameNumber];
-[MTLMetricsPerFrameMetrics numberOfCommandBuffers];
-[MTLMetricsPerFrameMetrics cpuClientPresentationLateness];
-[MTLMetricsPerFrameMetrics cpuCommandBufferActive];
-[MTLMetricsPerFrameMetrics cpuDrawableAcquireToPresent];
-[MTLMetricsPerFrameMetrics cpuDrawableOnScreenDuration];
-[MTLMetricsPerFrameMetrics cpuDrawableOnScreenTime];
-[MTLMetricsPerFrameMetrics cpuFirstCommandBufferBegin];
-[MTLMetricsPerFrameMetrics cpuLastCommandBufferEnd];
-[MTLMetricsPerFrameMetrics cpuNextDrawableAcquiredTime];
-[MTLMetricsPerFrameMetrics cpuNextDrawableRequestTime];
-[MTLMetricsPerFrameMetrics cpuOnGlassPresentationLateness];
-[MTLMetricsPerFrameMetrics cpuPresentInterval];
-[MTLMetricsPerFrameMetrics gpuCommandBufferActive];
-[MTLMetricsPerFrameMetrics gpuFirstCommandBufferBegin];
-[MTLMetricsPerFrameMetrics gpuLastCommandBufferEnd];
```
