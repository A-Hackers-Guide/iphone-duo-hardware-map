# `CLRacingRoutePerformanceResults`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 7 instance methods, 0 class methods

## Instance variables

```
d _timeAhead_s;
d _currentDistance_m;
d _referenceDistance_m;
d _currentAveragePace_s_per_m;
d _totalOverlapDistance_m;
Q _state;
```

## Properties

```
@property (Td,R,N,V_timeAhead_s) timeAhead_s;
@property (Td,R,N,V_currentDistance_m) currentDistance_m;
@property (Td,R,N,V_referenceDistance_m) referenceDistance_m;
@property (Td,R,N,V_currentAveragePace_s_per_m) currentAveragePace_s_per_m;
@property (Td,R,N,V_totalOverlapDistance_m) totalOverlapDistance_m;
@property (TQ,R,N,V_state) state;
```

## Instance methods

```
-[CLRacingRoutePerformanceResults state];
-[CLRacingRoutePerformanceResults currentAveragePace_s_per_m];
-[CLRacingRoutePerformanceResults currentDistance_m];
-[CLRacingRoutePerformanceResults initWithTimeAhead:currentDistance:referenceDistance:currentAveragePace:totalOverlapDistance:state:];
-[CLRacingRoutePerformanceResults referenceDistance_m];
-[CLRacingRoutePerformanceResults timeAhead_s];
-[CLRacingRoutePerformanceResults totalOverlapDistance_m];
```
