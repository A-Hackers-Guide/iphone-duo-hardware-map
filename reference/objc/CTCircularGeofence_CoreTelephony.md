# `CTCircularGeofence`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSString" _identifier;
@"CTGeofenceCoordinate" _coordinates;
d _radius;
```

## Properties

```
@property (T@"NSString",&,N,V_identifier) identifier;
@property (T@"CTGeofenceCoordinate",&,N,V_coordinates) coordinates;
@property (Td,N,V_radius) radius;
```

## Class methods

```
+[CTCircularGeofence supportsSecureCoding];
```

## Instance methods

```
-[CTCircularGeofence identifier];
-[CTCircularGeofence init];
-[CTCircularGeofence setRadius:];
-[CTCircularGeofence setIdentifier:];
-[CTCircularGeofence radius];
-[CTCircularGeofence encodeWithCoder:];
-[CTCircularGeofence initWithCoder:];
-[CTCircularGeofence copyWithZone:];
-[CTCircularGeofence setCoordinates:];
-[CTCircularGeofence coordinates];
-[CTCircularGeofence initWithCoordinate:radius:];
```
