# `_CLLSLLocationCoordinate`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 10 instance methods, 1 class methods

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
+[_CLLSLLocationCoordinate supportsSecureCoding];
```

## Instance methods

```
-[_CLLSLLocationCoordinate setLatitude:];
-[_CLLSLLocationCoordinate latitude];
-[_CLLSLLocationCoordinate initWithCoordinate:];
-[_CLLSLLocationCoordinate longitude];
-[_CLLSLLocationCoordinate setLongitude:];
-[_CLLSLLocationCoordinate encodeWithCoder:];
-[_CLLSLLocationCoordinate description];
-[_CLLSLLocationCoordinate initWithCoder:];
-[_CLLSLLocationCoordinate initWithLatitude:longitude:];
-[_CLLSLLocationCoordinate copyWithZone:];
```
