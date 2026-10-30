# `NILocation`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 14 instance variables, 14 properties, 36 instance methods, 1 class methods

## Instance variables

```
@"NSDate" _timestamp;
d _latitude;
d _longitude;
d _altitude;
d _ellipsoidalAltitude;
d _horizontalAccuracy;
d _verticalAccuracy;
d _speed;
d _speedAccuracy;
d _course;
d _courseAccuracy;
q _floor;
q _locationType;
q _signalEnvironment;
```

## Properties

```
@property (T@"NSDate",C,N,V_timestamp) timestamp;
@property (Td,N,V_latitude) latitude;
@property (Td,N,V_longitude) longitude;
@property (Td,N,V_altitude) altitude;
@property (Td,N,V_ellipsoidalAltitude) ellipsoidalAltitude;
@property (Td,N,V_horizontalAccuracy) horizontalAccuracy;
@property (Td,N,V_verticalAccuracy) verticalAccuracy;
@property (Td,N,V_speed) speed;
@property (Td,N,V_speedAccuracy) speedAccuracy;
@property (Td,N,V_course) course;
@property (Td,N,V_courseAccuracy) courseAccuracy;
@property (Tq,N,V_floor) floor;
@property (Tq,N,V_locationType) locationType;
@property (Tq,N,V_signalEnvironment) signalEnvironment;
```

## Class methods

```
+[NILocation supportsSecureCoding];
```

## Instance methods

```
-[NILocation setTimestamp:];
-[NILocation setSpeed:];
-[NILocation setLocationType:];
-[NILocation speed];
-[NILocation descriptionInternal];
-[NILocation setLatitude:];
-[NILocation latitude];
-[NILocation longitude];
-[NILocation altitude];
-[NILocation setLongitude:];
-[NILocation timestamp];
-[NILocation horizontalAccuracy];
-[NILocation setHorizontalAccuracy:];
-[NILocation setAltitude:];
-[NILocation setVerticalAccuracy:];
-[NILocation verticalAccuracy];
-[NILocation encodeWithCoder:];
-[NILocation hash];
-[NILocation speedAccuracy];
-[NILocation description];
-[NILocation initWithCoder:];
-[NILocation courseAccuracy];
-[NILocation copyWithZone:];
-[NILocation isEqual:];
-[NILocation course];
-[NILocation locationType];
-[NILocation setCourse:];
-[NILocation floor];
-[NILocation setCourseAccuracy:];
-[NILocation setSpeedAccuracy:];
-[NILocation ellipsoidalAltitude];
-[NILocation setFloor:];
-[NILocation setSignalEnvironment:];
-[NILocation signalEnvironment];
-[NILocation initWithTimestamp:latitude:longitude:altitude:ellipsoidalAltitude:horizontalAccuracy:verticalAccuracy:speed:speedAccuracy:course:courseAccuracy:floor:locationType:signalEnvironment:];
-[NILocation setEllipsoidalAltitude:];
```
