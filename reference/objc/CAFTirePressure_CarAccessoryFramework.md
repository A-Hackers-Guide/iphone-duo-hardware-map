# `CAFTirePressure`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- Protocols: `CAFPositionedRequired`
- 0 instance variables, 16 properties, 22 instance methods, 3 class methods

## Properties

```
@property (T@"CAFSensorStateCharacteristic",R,N) sensorStateCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) pressureCharacteristic;
@property (T@"CAFPressureStateCharacteristic",R,N) pressureStateCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) vehicleLayoutKeyCharacteristic;
@property (TC,R,N) sensorState;
@property (TB,R,N) hasSensorState;
@property (T@"NSMeasurement",R,N) pressure;
@property (T@"CAFUInt32Range",R,N) pressureRange;
@property (T@"CAFMeasurementRange",R,N) pressureMeasurementRange;
@property (TB,R,N) hasPressure;
@property (TC,R,N) pressureState;
@property (T@"NSString",R,N) vehicleLayoutKey;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAFTirePressure serviceIdentifier];
+[CAFTirePressure indexBy];
+[CAFTirePressure observerProtocol];
```

## Instance methods

```
-[CAFTirePressure removeObserver:];
-[CAFTirePressure addObserver:];
-[CAFTirePressure pressure];
-[CAFTirePressure registerObserver:];
-[CAFTirePressure name];
-[CAFTirePressure unregisterObserver:];
-[CAFTirePressure pressureState];
-[CAFTirePressure hasSensorState];
-[CAFTirePressure registeredForPressure];
-[CAFTirePressure registeredForPressureState];
-[CAFTirePressure registeredForSensorState];
-[CAFTirePressure registeredForVehicleLayoutKey];
-[CAFTirePressure sensorState];
-[CAFTirePressure vehicleLayoutKey];
-[CAFTirePressure _characteristicDidUpdate:fromGroupUpdate:];
-[CAFTirePressure hasPressure];
-[CAFTirePressure pressureCharacteristic];
-[CAFTirePressure pressureMeasurementRange];
-[CAFTirePressure pressureRange];
-[CAFTirePressure pressureStateCharacteristic];
-[CAFTirePressure sensorStateCharacteristic];
-[CAFTirePressure vehicleLayoutKeyCharacteristic];
```
