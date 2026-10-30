# `CMBikeSensorData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 7 instance variables, 7 properties, 20 instance methods, 2 class methods

## Instance variables

```
d fTimestamp;
d _instantaneousSpeed;
@"NSString" _model;
@"NSString" _manufacturer;
@"NSString" _deviceIdentifier;
d _instantaneousCadence;
d _instantaneousPower;
```

## Properties

```
@property (T@"NSDate",R,N) timestamp;
@property (Td,N,V_instantaneousSpeed) instantaneousSpeed;
@property (T@"NSString",C,N,V_model) model;
@property (T@"NSString",C,N,V_manufacturer) manufacturer;
@property (T@"NSString",C,N,V_deviceIdentifier) deviceIdentifier;
@property (Td,N,V_instantaneousCadence) instantaneousCadence;
@property (Td,N,V_instantaneousPower) instantaneousPower;
```

## Class methods

```
+[CMBikeSensorData supportsSecureCoding];
+[CMBikeSensorData isAvailable];
```

## Instance methods

```
-[CMBikeSensorData model];
-[CMBikeSensorData setModel:];
-[CMBikeSensorData setDeviceIdentifier:];
-[CMBikeSensorData dealloc];
-[CMBikeSensorData timestamp];
-[CMBikeSensorData manufacturer];
-[CMBikeSensorData deviceIdentifier];
-[CMBikeSensorData initWithTimestamp:];
-[CMBikeSensorData encodeWithCoder:];
-[CMBikeSensorData description];
-[CMBikeSensorData initWithCoder:];
-[CMBikeSensorData copyWithZone:];
-[CMBikeSensorData setManufacturer:];
-[CMBikeSensorData instantaneousCadence];
-[CMBikeSensorData instantaneousPower];
-[CMBikeSensorData instantaneousSpeed];
-[CMBikeSensorData newFitnessMachineDataFromBikeSensorData];
-[CMBikeSensorData setInstantaneousCadence:];
-[CMBikeSensorData setInstantaneousPower:];
-[CMBikeSensorData setInstantaneousSpeed:];
```
