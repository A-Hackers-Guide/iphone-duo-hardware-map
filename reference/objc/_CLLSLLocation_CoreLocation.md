# `_CLLSLLocation`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"_CLLSLLocationCoordinate" _coordinate;
d _altitude;
d _timestamp;
```

## Properties

```
@property (T@"_CLLSLLocationCoordinate",C,N,V_coordinate) coordinate;
@property (Td,N,V_altitude) altitude;
@property (Td,N,V_timestamp) timestamp;
```

## Class methods

```
+[_CLLSLLocation supportsSecureCoding];
```

## Instance methods

```
-[_CLLSLLocation setTimestamp:];
-[_CLLSLLocation coordinate];
-[_CLLSLLocation initWithCoordinate:];
-[_CLLSLLocation altitude];
-[_CLLSLLocation dealloc];
-[_CLLSLLocation timestamp];
-[_CLLSLLocation setAltitude:];
-[_CLLSLLocation setCoordinate:];
-[_CLLSLLocation encodeWithCoder:];
-[_CLLSLLocation description];
-[_CLLSLLocation initWithCoder:];
-[_CLLSLLocation initWithLatitude:longitude:];
-[_CLLSLLocation copyWithZone:];
-[_CLLSLLocation descriptionWithMemberIndent:endIndent:];
-[_CLLSLLocation initWithCoordinate:altitude:timetamp:];
-[_CLLSLLocation initWithLatitude:longitude:altitude:timetamp:];
```
