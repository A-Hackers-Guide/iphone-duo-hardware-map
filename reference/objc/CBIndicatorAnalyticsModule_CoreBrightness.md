# `CBIndicatorAnalyticsModule`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBModule`
- Protocols: `CBContainerModuleProtocol`
- 12 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"CBHistogramBuilder3D" _stats;
@"CBIndicatorBrightnessModule" _indicatorModule;
@"NSObject<OS_dispatch_source>" _timer;
@"NSDictionary" _ddFactorEdgeMapping;
@"NSDictionary" _luxEdgeMapping;
@"NSDictionary" _nitsEdgeMapping;
B _timerIsSuspended;
d _timerIntervalMs;
f _sessionStart;
f _lastSessionDuration;
f _trustedLux;
C _displayID;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CBIndicatorAnalyticsModule startTimer];
-[CBIndicatorAnalyticsModule copyPropertyForKey:];
-[CBIndicatorAnalyticsModule setProperty:forKey:];
-[CBIndicatorAnalyticsModule stop];
-[CBIndicatorAnalyticsModule submit];
-[CBIndicatorAnalyticsModule dealloc];
-[CBIndicatorAnalyticsModule start];
-[CBIndicatorAnalyticsModule handleNotificationForKey:withProperty:];
-[CBIndicatorAnalyticsModule stopTimer];
-[CBIndicatorAnalyticsModule copyPropertyForKey:withParameter:];
-[CBIndicatorAnalyticsModule indicatorStatsTimerCallback];
-[CBIndicatorAnalyticsModule initWithQueue:andIndicatorModule:];
-[CBIndicatorAnalyticsModule initWithQueue:andIndicatorModule:andDDFactorMapping:andLuxMapping:andNitsMapping:andDDFactorEdges:andLuxEdges:andNitsEdges:andTimerIntervalMs:];
```
