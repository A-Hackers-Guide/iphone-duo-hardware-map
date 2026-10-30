# `CMVehicleStateData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 6 instance variables, 7 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"CMMotionTimeRange" fTimeRange;
@"NSString" fVehicleName;
@"NSString" fVehicleModelName;
@"NSString" fVehicleBluetoothAddress;
Q fVehicularState;
Q fVehicularHints;
```

## Properties

```
@property (T@"CMMotionTimeRange",R,N) timeRange;
@property (T@"NSString",R,N) deviceId;
@property (T@"NSString",R,N) vehicleName;
@property (T@"NSString",R,N) vehicleModelName;
@property (T@"NSString",R,N) vehicleBluetoothAddress;
@property (TQ,R,N) vehicularState;
@property (TQ,R,N) vehicularHints;
```

## Class methods

```
+[CMVehicleStateData supportsSecureCoding];
```

## Instance methods

```
-[CMVehicleStateData deviceId];
-[CMVehicleStateData timeRange];
-[CMVehicleStateData dealloc];
-[CMVehicleStateData vehicularHints];
-[CMVehicleStateData vehicularState];
-[CMVehicleStateData encodeWithCoder:];
-[CMVehicleStateData description];
-[CMVehicleStateData initWithCoder:];
-[CMVehicleStateData copyWithZone:];
-[CMVehicleStateData vehicleName];
-[CMVehicleStateData initWithTimeRange:vehicleName:vehicleModelName:vehicleBluetoothAddress:];
-[CMVehicleStateData initWithTimestamp:state:hints:];
-[CMVehicleStateData vehicleBluetoothAddress];
-[CMVehicleStateData vehicleModelName];
```
