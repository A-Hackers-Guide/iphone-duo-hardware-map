# `MTLMetricsService_Impl`

- Image: [`/System/Library/PrivateFrameworks/MetalMetrics.framework/MetalMetrics`](../userland/System__Library__PrivateFrameworks__MetalMetrics.framework__MetalMetrics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MTLMetricsService`, `FPMTLMetricsMetricListenerInternal`
- 2 instance variables, 1 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _listeners;
@"CAMetalLayer" _targetLayer;
```

## Properties

```
@property (T@"CAMetalLayer",W,N,V_targetLayer) targetLayer;
```

## Class methods

```
+[MTLMetricsService_Impl sharedService];
```

## Instance methods

```
-[MTLMetricsService_Impl init];
-[MTLMetricsService_Impl setTargetLayer:];
-[MTLMetricsService_Impl targetLayer];
-[MTLMetricsService_Impl metricsUpdatedForLayer:metrics:];
-[MTLMetricsService_Impl registerPerFrameMetricsListener:];
-[MTLMetricsService_Impl removePerFrameMetricsListener:];
```
