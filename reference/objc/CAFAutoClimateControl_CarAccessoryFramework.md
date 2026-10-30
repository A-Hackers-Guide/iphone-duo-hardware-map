# `CAFAutoClimateControl`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- Protocols: `CAFPositioned`
- 0 instance variables, 30 properties, 41 instance methods, 3 class methods

## Properties

```
@property (T@"CAFUInt8Characteristic",R,N) levelCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) onCharacteristic;
@property (T@"CAFArrayCharacteristic",R,N) intensitiesCharacteristic;
@property (T@"CAFUInt32Characteristic",R,N) autoModeIntensityIndexCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) vehicleLayoutKeyCharacteristic;
@property (TC,N) level;
@property (T@"CAFUInt8Range",R,N) levelRange;
@property (TB,R,N) hasLevel;
@property (TB,R,N) levelInvalid;
@property (TB,R,N) levelDisabled;
@property (TB,R,N) levelRestricted;
@property (TB,N) on;
@property (TB,R,N) hasOn;
@property (TB,R,N) onDisabled;
@property (TB,R,N) onInvalid;
@property (TB,R,N) onRestricted;
@property (T@"NSArray",C,N) intensities;
@property (TB,R,N) hasIntensities;
@property (TI,N) autoModeIntensityIndex;
@property (T@"CAFUInt32Range",R,N) autoModeIntensityIndexRange;
@property (TB,R,N) hasAutoModeIntensityIndex;
@property (TB,R,N) autoModeIntensityIndexDisabled;
@property (TB,R,N) autoModeIntensityIndexInvalid;
@property (TB,R,N) autoModeIntensityIndexRestricted;
@property (T@"NSString",R,N) vehicleLayoutKey;
@property (TB,R,N) hasVehicleLayoutKey;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAFAutoClimateControl serviceIdentifier];
+[CAFAutoClimateControl indexBy];
+[CAFAutoClimateControl observerProtocol];
```

## Instance methods

```
-[CAFAutoClimateControl on];
-[CAFAutoClimateControl removeObserver:];
-[CAFAutoClimateControl level];
-[CAFAutoClimateControl addObserver:];
-[CAFAutoClimateControl setLevel:];
-[CAFAutoClimateControl setOn:];
-[CAFAutoClimateControl registerObserver:];
-[CAFAutoClimateControl name];
-[CAFAutoClimateControl unregisterObserver:];
-[CAFAutoClimateControl hasLevel];
-[CAFAutoClimateControl intensities];
-[CAFAutoClimateControl levelRange];
-[CAFAutoClimateControl registeredForOn];
-[CAFAutoClimateControl setIntensities:];
-[CAFAutoClimateControl autoModeIntensityIndex];
-[CAFAutoClimateControl hasAutoModeIntensityIndex];
-[CAFAutoClimateControl hasOn];
-[CAFAutoClimateControl levelDisabled];
-[CAFAutoClimateControl levelInvalid];
-[CAFAutoClimateControl onDisabled];
-[CAFAutoClimateControl onInvalid];
-[CAFAutoClimateControl onRestricted];
-[CAFAutoClimateControl registeredForAutoModeIntensities];
-[CAFAutoClimateControl registeredForAutoModeIntensityIndex];
-[CAFAutoClimateControl registeredForAutoModeLevel];
-[CAFAutoClimateControl registeredForVehicleLayoutKey];
-[CAFAutoClimateControl setAutoModeIntensityIndex:];
-[CAFAutoClimateControl vehicleLayoutKey];
-[CAFAutoClimateControl autoModeIntensityIndexDisabled];
-[CAFAutoClimateControl levelRestricted];
-[CAFAutoClimateControl _characteristicDidUpdate:fromGroupUpdate:];
-[CAFAutoClimateControl autoModeIntensityIndexCharacteristic];
-[CAFAutoClimateControl autoModeIntensityIndexInvalid];
-[CAFAutoClimateControl autoModeIntensityIndexRange];
-[CAFAutoClimateControl autoModeIntensityIndexRestricted];
-[CAFAutoClimateControl hasIntensities];
-[CAFAutoClimateControl hasVehicleLayoutKey];
-[CAFAutoClimateControl intensitiesCharacteristic];
-[CAFAutoClimateControl levelCharacteristic];
-[CAFAutoClimateControl onCharacteristic];
-[CAFAutoClimateControl vehicleLayoutKeyCharacteristic];
```
