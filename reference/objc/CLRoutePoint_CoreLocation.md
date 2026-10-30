# `CLRoutePoint`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 6 properties, 13 instance methods, 1 class methods

## Instance variables

```
i _signalEnvironmentType;
d _latitude_deg;
d _longitude_deg;
d _altitude_m;
d _odometer_m;
d _timestamp_s;
```

## Properties

```
@property (Td,R,N,V_latitude_deg) latitude_deg;
@property (Td,R,N,V_longitude_deg) longitude_deg;
@property (Td,R,N,V_altitude_m) altitude_m;
@property (Td,R,N,V_odometer_m) odometer_m;
@property (Td,R,N,V_timestamp_s) timestamp_s;
@property (Ti,R,N,V_signalEnvironmentType) signalEnvironmentType;
```

## Class methods

```
+[CLRoutePoint supportsSecureCoding];
```

## Instance methods

```
-[CLRoutePoint encodeWithCoder:];
-[CLRoutePoint hash];
-[CLRoutePoint description];
-[CLRoutePoint initWithCoder:];
-[CLRoutePoint copyWithZone:];
-[CLRoutePoint isEqual:];
-[CLRoutePoint altitude_m];
-[CLRoutePoint initWithLatitude:longitude:altitude:odometer:timestamp:signalEnvironmentType:];
-[CLRoutePoint latitude_deg];
-[CLRoutePoint longitude_deg];
-[CLRoutePoint odometer_m];
-[CLRoutePoint signalEnvironmentType];
-[CLRoutePoint timestamp_s];
```
