# `BLSHFlipbookRequestDatesTelemetryData`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 12 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _didReset;
d _timestamp;
@"NSArray" _environmentIdentifiers;
d _shortestInterval;
d _averageInterval;
d _longestInterval;
d _completionDuration;
Q _timedOutCount;
```

## Properties

```
@property (T@"NSString",R,N) blsh_analyticsEventName;
@property (T@"NSDictionary",R,N) blsh_analyticsPayload;
@property (Td,R,N,V_timestamp) timestamp;
@property (T@"NSArray",R,N,V_environmentIdentifiers) environmentIdentifiers;
@property (Td,R,N,V_shortestInterval) shortestInterval;
@property (Td,R,N,V_averageInterval) averageInterval;
@property (Td,R,N,V_longestInterval) longestInterval;
@property (Td,R,N,V_completionDuration) completionDuration;
@property (TB,R,N,V_didReset) didReset;
@property (TQ,R,N,V_timedOutCount) timedOutCount;
@property (T@"NSString",R,N) firstEnvironmentIdentifier;
@property (TI,R,N) environmentCount;
```

## Instance methods

```
-[BLSHFlipbookRequestDatesTelemetryData timestamp];
-[BLSHFlipbookRequestDatesTelemetryData description];
-[BLSHFlipbookRequestDatesTelemetryData didReset];
-[BLSHFlipbookRequestDatesTelemetryData averageInterval];
-[BLSHFlipbookRequestDatesTelemetryData longestInterval];
-[BLSHFlipbookRequestDatesTelemetryData completionDuration];
-[BLSHFlipbookRequestDatesTelemetryData environmentIdentifiers];
-[BLSHFlipbookRequestDatesTelemetryData shortestInterval];
-[BLSHFlipbookRequestDatesTelemetryData timedOutCount];
-[BLSHFlipbookRequestDatesTelemetryData blsh_analyticsEventName];
-[BLSHFlipbookRequestDatesTelemetryData blsh_analyticsPayload];
-[BLSHFlipbookRequestDatesTelemetryData environmentCount];
-[BLSHFlipbookRequestDatesTelemetryData firstEnvironmentIdentifier];
-[BLSHFlipbookRequestDatesTelemetryData initWithTimestamp:environmentIdentifiers:shortestInterval:averageInterval:longestInterval:completionDuration:didReset:timedOutCount:];
```
