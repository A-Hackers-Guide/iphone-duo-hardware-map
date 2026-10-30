# `CLLocationExtendedTimestamps`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"CLLocation" _location;
@"NSDate" _systemTimeNotUserTime;
d _machContinuousTimeSec;
```

## Properties

```
@property (T@"CLLocation",C,N,V_location) location;
@property (T@"NSDate",C,N,V_systemTimeNotUserTime) systemTimeNotUserTime;
@property (Td,N,V_machContinuousTimeSec) machContinuousTimeSec;
```

## Class methods

```
+[CLLocationExtendedTimestamps supportsSecureCoding];
```

## Instance methods

```
-[CLLocationExtendedTimestamps location];
-[CLLocationExtendedTimestamps dealloc];
-[CLLocationExtendedTimestamps setLocation:];
-[CLLocationExtendedTimestamps encodeWithCoder:];
-[CLLocationExtendedTimestamps initWithCoder:];
-[CLLocationExtendedTimestamps copyWithZone:];
-[CLLocationExtendedTimestamps initWithCLLocation:systemTime:machContinuousTimeSec:];
-[CLLocationExtendedTimestamps machContinuousTimeSec];
-[CLLocationExtendedTimestamps setMachContinuousTimeSec:];
-[CLLocationExtendedTimestamps setSystemTimeNotUserTime:];
-[CLLocationExtendedTimestamps systemTimeNotUserTime];
```
