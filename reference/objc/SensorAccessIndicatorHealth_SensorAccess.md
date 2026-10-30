# `SensorAccessIndicatorHealth`

- Image: [`/System/Library/PrivateFrameworks/SensorAccess.framework/SensorAccess`](../userland/System__Library__PrivateFrameworks__SensorAccess.framework__SensorAccess.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
i indicatorType;
i healthCheckType;
B indicatorHealthy;
```

## Properties

```
@property (Ti,N,VindicatorType) indicatorType;
@property (Ti,N,VhealthCheckType) healthCheckType;
@property (TB,N,VindicatorHealthy) indicatorHealthy;
@property (T@"NSString",N,R) description;
```

## Instance methods

```
-[SensorAccessIndicatorHealth init];
-[SensorAccessIndicatorHealth setIndicatorType:];
-[SensorAccessIndicatorHealth description];
-[SensorAccessIndicatorHealth indicatorType];
-[SensorAccessIndicatorHealth healthCheckType];
-[SensorAccessIndicatorHealth healthCheckTypeDescriptionWithHealthCheckType:];
-[SensorAccessIndicatorHealth indicatorHealthy];
-[SensorAccessIndicatorHealth indicatorTypeDescriptionWithIndicatorType:];
-[SensorAccessIndicatorHealth initWithIndicatorType:healthCheckType:];
-[SensorAccessIndicatorHealth setHealthCheckType:];
-[SensorAccessIndicatorHealth setIndicatorHealthy:];
```
