# `CTPolygonalGeofence`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSString" _identifier;
@"NSArray" _coordinates;
```

## Properties

```
@property (T@"NSString",&,N,V_identifier) identifier;
@property (T@"NSArray",&,N,V_coordinates) coordinates;
```

## Class methods

```
+[CTPolygonalGeofence supportsSecureCoding];
```

## Instance methods

```
-[CTPolygonalGeofence identifier];
-[CTPolygonalGeofence init];
-[CTPolygonalGeofence setIdentifier:];
-[CTPolygonalGeofence encodeWithCoder:];
-[CTPolygonalGeofence initWithCoder:];
-[CTPolygonalGeofence copyWithZone:];
-[CTPolygonalGeofence setCoordinates:];
-[CTPolygonalGeofence coordinates];
-[CTPolygonalGeofence initWithCoordinates:];
```
