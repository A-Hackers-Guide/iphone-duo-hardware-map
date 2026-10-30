# `CAFClimateControlsLocked`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- Protocols: `CAFPositioned`
- 0 instance variables, 11 properties, 16 instance methods, 3 class methods

## Properties

```
@property (T@"CAFLockStateCharacteristic",R,N) lockStateCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) vehicleLayoutKeyCharacteristic;
@property (TC,N) lockState;
@property (TB,R,N) lockStateDisabled;
@property (TB,R,N) lockStateRestricted;
@property (T@"NSString",R,N) vehicleLayoutKey;
@property (TB,R,N) hasVehicleLayoutKey;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAFClimateControlsLocked serviceIdentifier];
+[CAFClimateControlsLocked indexBy];
+[CAFClimateControlsLocked observerProtocol];
```

## Instance methods

```
-[CAFClimateControlsLocked lockState];
-[CAFClimateControlsLocked setLockState:];
-[CAFClimateControlsLocked removeObserver:];
-[CAFClimateControlsLocked addObserver:];
-[CAFClimateControlsLocked registerObserver:];
-[CAFClimateControlsLocked name];
-[CAFClimateControlsLocked unregisterObserver:];
-[CAFClimateControlsLocked registeredForLockState];
-[CAFClimateControlsLocked registeredForVehicleLayoutKey];
-[CAFClimateControlsLocked vehicleLayoutKey];
-[CAFClimateControlsLocked _characteristicDidUpdate:fromGroupUpdate:];
-[CAFClimateControlsLocked hasVehicleLayoutKey];
-[CAFClimateControlsLocked lockStateCharacteristic];
-[CAFClimateControlsLocked lockStateDisabled];
-[CAFClimateControlsLocked lockStateRestricted];
-[CAFClimateControlsLocked vehicleLayoutKeyCharacteristic];
```
