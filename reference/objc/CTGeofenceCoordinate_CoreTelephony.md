# `CTGeofenceCoordinate`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 9 instance methods, 1 class methods

## Instance variables

```
d _latitude;
d _longitude;
```

## Properties

```
@property (Td,N,V_latitude) latitude;
@property (Td,N,V_longitude) longitude;
```

## Class methods

```
+[CTGeofenceCoordinate supportsSecureCoding];
```

## Instance methods

```
-[CTGeofenceCoordinate init];
-[CTGeofenceCoordinate setLatitude:];
-[CTGeofenceCoordinate latitude];
-[CTGeofenceCoordinate longitude];
-[CTGeofenceCoordinate setLongitude:];
-[CTGeofenceCoordinate encodeWithCoder:];
-[CTGeofenceCoordinate initWithCoder:];
-[CTGeofenceCoordinate initWithLatitude:longitude:];
-[CTGeofenceCoordinate copyWithZone:];
```
