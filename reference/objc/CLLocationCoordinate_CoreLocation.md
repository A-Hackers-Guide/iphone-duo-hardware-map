# `CLLocationCoordinate`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 13 instance methods, 1 class methods

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
+[CLLocationCoordinate supportsSecureCoding];
```

## Instance methods

```
-[CLLocationCoordinate setLatitude:];
-[CLLocationCoordinate latitude];
-[CLLocationCoordinate longitude];
-[CLLocationCoordinate setLongitude:];
-[CLLocationCoordinate dealloc];
-[CLLocationCoordinate encodeWithCoder:];
-[CLLocationCoordinate isValid];
-[CLLocationCoordinate description];
-[CLLocationCoordinate initWithCoder:];
-[CLLocationCoordinate initWithLatitude:longitude:];
-[CLLocationCoordinate copyWithZone:];
-[CLLocationCoordinate distanceFrom:];
-[CLLocationCoordinate isEqualCoordinate:];
```
