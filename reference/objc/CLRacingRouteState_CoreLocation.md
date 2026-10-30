# `CLRacingRouteState`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 11 instance variables, 11 properties, 15 instance methods, 1 class methods

## Instance variables

```
d _latitude;
d _longitude;
d _altitude;
d _odometer;
d _timestamp;
d _timeSinceStart;
d _offRouteTime;
d _distanceSinceStart;
d _offRouteDistance;
d _averagePace;
d _distanceAlongReference;
```

## Properties

```
@property (Td,R,N,V_latitude) latitude;
@property (Td,R,N,V_longitude) longitude;
@property (Td,R,N,V_altitude) altitude;
@property (Td,R,N,V_odometer) odometer;
@property (Td,R,N,V_timestamp) timestamp;
@property (Td,R,N,V_timeSinceStart) timeSinceStart;
@property (Td,R,N,V_offRouteTime) offRouteTime;
@property (Td,R,N,V_distanceSinceStart) distanceSinceStart;
@property (Td,R,N,V_offRouteDistance) offRouteDistance;
@property (Td,R,N,V_averagePace) averagePace;
@property (Td,R,N,V_distanceAlongReference) distanceAlongReference;
```

## Class methods

```
+[CLRacingRouteState supportsSecureCoding];
```

## Instance methods

```
-[CLRacingRouteState latitude];
-[CLRacingRouteState longitude];
-[CLRacingRouteState altitude];
-[CLRacingRouteState timestamp];
-[CLRacingRouteState odometer];
-[CLRacingRouteState encodeWithCoder:];
-[CLRacingRouteState initWithCoder:];
-[CLRacingRouteState copyWithZone:];
-[CLRacingRouteState timeSinceStart];
-[CLRacingRouteState averagePace];
-[CLRacingRouteState distanceAlongReference];
-[CLRacingRouteState distanceSinceStart];
-[CLRacingRouteState initWithLatitude:longitude:altitude:odometer:timestamp:timeSinceStart:offRouteTime:distanceSinceStart:offRouteDistance:averagePace:distanceAlongReference:];
-[CLRacingRouteState offRouteDistance];
-[CLRacingRouteState offRouteTime];
```
