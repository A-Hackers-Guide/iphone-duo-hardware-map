# `CMVehicleConnectionData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 2 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSDate" fStartDate;
@"NSDate" fEndDate;
```

## Properties

```
@property (T@"NSDate",R,N) startDate;
@property (T@"NSDate",R,N) endDate;
```

## Class methods

```
+[CMVehicleConnectionData supportsSecureCoding];
```

## Instance methods

```
-[CMVehicleConnectionData startDate];
-[CMVehicleConnectionData dealloc];
-[CMVehicleConnectionData endDate];
-[CMVehicleConnectionData initWithStartDate:endDate:];
-[CMVehicleConnectionData encodeWithCoder:];
-[CMVehicleConnectionData description];
-[CMVehicleConnectionData initWithCoder:];
-[CMVehicleConnectionData copyWithZone:];
```
