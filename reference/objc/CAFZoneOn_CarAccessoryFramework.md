# `CAFZoneOn`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- Protocols: `CAFPositionedRequired`
- 0 instance variables, 11 properties, 16 instance methods, 3 class methods

## Properties

```
@property (T@"CAFBoolCharacteristic",R,N) onCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) vehicleLayoutKeyCharacteristic;
@property (TB,N) on;
@property (TB,R,N) onDisabled;
@property (TB,R,N) onInvalid;
@property (TB,R,N) onRestricted;
@property (T@"NSString",R,N) vehicleLayoutKey;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAFZoneOn serviceIdentifier];
+[CAFZoneOn indexBy];
+[CAFZoneOn observerProtocol];
```

## Instance methods

```
-[CAFZoneOn on];
-[CAFZoneOn removeObserver:];
-[CAFZoneOn addObserver:];
-[CAFZoneOn setOn:];
-[CAFZoneOn registerObserver:];
-[CAFZoneOn name];
-[CAFZoneOn unregisterObserver:];
-[CAFZoneOn registeredForOn];
-[CAFZoneOn onDisabled];
-[CAFZoneOn onInvalid];
-[CAFZoneOn onRestricted];
-[CAFZoneOn registeredForVehicleLayoutKey];
-[CAFZoneOn vehicleLayoutKey];
-[CAFZoneOn _characteristicDidUpdate:fromGroupUpdate:];
-[CAFZoneOn onCharacteristic];
-[CAFZoneOn vehicleLayoutKeyCharacteristic];
```
