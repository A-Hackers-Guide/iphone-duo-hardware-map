# `MTLMetricsService` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalMetrics.framework/MetalMetrics`](../userland/System__Library__PrivateFrameworks__MetalMetrics.framework__MetalMetrics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 1 properties, 4 instance methods, 1 class methods

## Properties

```
@property (T@"CAMetalLayer",W,N) targetLayer;
```

## Class methods

```
+[MTLMetricsService sharedService];
```

## Instance methods

```
-[MTLMetricsService setTargetLayer:];
-[MTLMetricsService targetLayer];
-[MTLMetricsService registerPerFrameMetricsListener:];
-[MTLMetricsService removePerFrameMetricsListener:];
```
