# `CLVehicleHeading`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 1 instance variables, 2 properties, 9 instance methods, 1 class methods

## Instance variables

```
@ _internal;
```

## Properties

```
@property (Td,R,N) trueHeading;
@property (T@"NSDate",R,N) timestamp;
```

## Class methods

```
+[CLVehicleHeading supportsSecureCoding];
```

## Instance methods

```
-[CLVehicleHeading dealloc];
-[CLVehicleHeading timestamp];
-[CLVehicleHeading shortDescription];
-[CLVehicleHeading encodeWithCoder:];
-[CLVehicleHeading description];
-[CLVehicleHeading initWithCoder:];
-[CLVehicleHeading copyWithZone:];
-[CLVehicleHeading trueHeading];
-[CLVehicleHeading initWithClientVehicleHeading:];
```
