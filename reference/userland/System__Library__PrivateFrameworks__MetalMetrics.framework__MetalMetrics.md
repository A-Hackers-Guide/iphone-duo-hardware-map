# `/System/Library/PrivateFrameworks/MetalMetrics.framework/MetalMetrics`

iOS 27.2 dyld shared cache image. Version `5.0.26.0.0`. **[DSC]**

## Linked libraries (6)

- `/System/Library/Frameworks/Metal.framework/Metal`
- `/System/Library/Frameworks/QuartzCore.framework/QuartzCore`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 3 classes, 4 protocols, 83 methods, 52 properties

### Class pages

Every class and protocol, with its methods: [`FPMTLMetricsMetricListenerInternal`](../objc/FPMTLMetricsMetricListenerInternal_MetalMetrics.protocol.md), [`MTLMetricsMetricListenerObject`](../objc/MTLMetricsMetricListenerObject_MetalMetrics.md), [`MTLMetricsPerFrameMetrics`](../objc/MTLMetricsPerFrameMetrics_MetalMetrics.protocol.md), [`MTLMetricsPerFrameMetrics_Impl`](../objc/MTLMetricsPerFrameMetrics_Impl_MetalMetrics.md), [`MTLMetricsService`](../objc/MTLMetricsService_MetalMetrics.protocol.md), [`MTLMetricsService_Impl`](../objc/MTLMetricsService_Impl_MetalMetrics.md), [`NSObject`](../objc/NSObject_MetalMetrics.protocol.md)

### Classes

`MTLMetricsMetricListenerObject`, `MTLMetricsPerFrameMetrics_Impl`, `MTLMetricsService_Impl`

### Protocols

`FPMTLMetricsMetricListenerInternal`, `MTLMetricsPerFrameMetrics`, `MTLMetricsService`, `NSObject`

### Properties

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
@property (T@"CAMetalLayer",W,N) targetLayer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<MTLMetricsPerFrameMetricListener>",W,N,V_listener) listener;
@property (T@"CAMetalLayer",W,N,V_layer) layer;
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
@property (T@"CAMetalLayer",W,N,V_targetLayer) targetLayer;
```

## Strings (3)

```
v8@?0
instance
_CADeveloperHUDProperties
```
