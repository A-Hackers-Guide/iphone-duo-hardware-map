# `CAFDefrost`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- Protocols: `CAFPositionedRequired`
- 0 instance variables, 16 properties, 22 instance methods, 3 class methods

## Properties

```
@property (T@"CAFDefrostTypesCharacteristic",R,N) typesCharacteristic;
@property (T@"CAFUInt8Characteristic",R,N) levelCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) vehicleLayoutKeyCharacteristic;
@property (TQ,R,N) types;
@property (TB,R,N) hasBlownAir;
@property (TB,R,N) hasFilament;
@property (TC,N) level;
@property (T@"CAFUInt8Range",R,N) levelRange;
@property (TB,R,N) levelInvalid;
@property (TB,R,N) levelDisabled;
@property (T@"NSString",R,N) vehicleLayoutKey;
@property (T@"NSString",R,N) positionKey;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAFDefrost serviceIdentifier];
+[CAFDefrost indexBy];
+[CAFDefrost observerProtocol];
```

## Instance methods

```
-[CAFDefrost removeObserver:];
-[CAFDefrost types];
-[CAFDefrost level];
-[CAFDefrost addObserver:];
-[CAFDefrost setLevel:];
-[CAFDefrost registerObserver:];
-[CAFDefrost name];
-[CAFDefrost unregisterObserver:];
-[CAFDefrost levelRange];
-[CAFDefrost positionKey];
-[CAFDefrost levelDisabled];
-[CAFDefrost levelInvalid];
-[CAFDefrost registeredForDefrostTypes];
-[CAFDefrost registeredForLevel];
-[CAFDefrost registeredForVehicleLayoutKey];
-[CAFDefrost vehicleLayoutKey];
-[CAFDefrost hasBlownAir];
-[CAFDefrost _characteristicDidUpdate:fromGroupUpdate:];
-[CAFDefrost hasFilament];
-[CAFDefrost levelCharacteristic];
-[CAFDefrost typesCharacteristic];
-[CAFDefrost vehicleLayoutKeyCharacteristic];
```
