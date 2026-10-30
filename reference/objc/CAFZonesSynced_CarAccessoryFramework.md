# `CAFZonesSynced`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- Protocols: `CAFPositioned`
- 0 instance variables, 12 properties, 17 instance methods, 3 class methods

## Properties

```
@property (T@"CAFBoolCharacteristic",R,N) onCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) vehicleLayoutKeyCharacteristic;
@property (TB,N) on;
@property (TB,R,N) onDisabled;
@property (TB,R,N) onInvalid;
@property (TB,R,N) onRestricted;
@property (T@"NSString",R,N) vehicleLayoutKey;
@property (TB,R,N) hasVehicleLayoutKey;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAFZonesSynced serviceIdentifier];
+[CAFZonesSynced indexBy];
+[CAFZonesSynced observerProtocol];
```

## Instance methods

```
-[CAFZonesSynced on];
-[CAFZonesSynced removeObserver:];
-[CAFZonesSynced addObserver:];
-[CAFZonesSynced setOn:];
-[CAFZonesSynced registerObserver:];
-[CAFZonesSynced name];
-[CAFZonesSynced unregisterObserver:];
-[CAFZonesSynced registeredForOn];
-[CAFZonesSynced onDisabled];
-[CAFZonesSynced onInvalid];
-[CAFZonesSynced onRestricted];
-[CAFZonesSynced registeredForVehicleLayoutKey];
-[CAFZonesSynced vehicleLayoutKey];
-[CAFZonesSynced _characteristicDidUpdate:fromGroupUpdate:];
-[CAFZonesSynced hasVehicleLayoutKey];
-[CAFZonesSynced onCharacteristic];
-[CAFZonesSynced vehicleLayoutKeyCharacteristic];
```
