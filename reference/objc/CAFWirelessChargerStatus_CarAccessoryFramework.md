# `CAFWirelessChargerStatus`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- Protocols: `CAFPositioned`
- 0 instance variables, 28 properties, 39 instance methods, 2 class methods

## Properties

```
@property (T@"CAFChargerStatusCharacteristic",R,N) chargerStatusCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) batteryLevelCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) contentURLActionCharacteristic;
@property (T@"CAFButtonActionCharacteristic",R,N) buttonActionCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) vehicleLayoutKeyCharacteristic;
@property (T@"CAFUInt8Characteristic",R,N) sortOrderCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) disabledCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) hiddenCharacteristic;
@property (TC,R,N) chargerStatus;
@property (T@"NSMeasurement",R,N) batteryLevel;
@property (T@"CAFUInt8Range",R,N) batteryLevelRange;
@property (T@"CAFMeasurementRange",R,N) batteryLevelMeasurementRange;
@property (TB,R,N) hasBatteryLevel;
@property (T@"NSString",R,N) contentURLAction;
@property (TB,R,N) hasContentURLAction;
@property (TC,N) buttonAction;
@property (TB,R,N) hasButtonAction;
@property (T@"NSString",R,N) vehicleLayoutKey;
@property (TB,R,N) hasVehicleLayoutKey;
@property (TC,R,N) sortOrder;
@property (TB,R,N) disabled;
@property (TB,R,N) hasDisabled;
@property (TB,R,N) hidden;
@property (TB,R,N) hasHidden;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAFWirelessChargerStatus serviceIdentifier];
+[CAFWirelessChargerStatus observerProtocol];
```

## Instance methods

```
-[CAFWirelessChargerStatus sortOrder];
-[CAFWirelessChargerStatus disabled];
-[CAFWirelessChargerStatus batteryLevel];
-[CAFWirelessChargerStatus hasBatteryLevel];
-[CAFWirelessChargerStatus removeObserver:];
-[CAFWirelessChargerStatus addObserver:];
-[CAFWirelessChargerStatus registerObserver:];
-[CAFWirelessChargerStatus hasDisabled];
-[CAFWirelessChargerStatus name];
-[CAFWirelessChargerStatus unregisterObserver:];
-[CAFWirelessChargerStatus hidden];
-[CAFWirelessChargerStatus buttonAction];
-[CAFWirelessChargerStatus setButtonAction:];
-[CAFWirelessChargerStatus hasButtonAction];
-[CAFWirelessChargerStatus hasHidden];
-[CAFWirelessChargerStatus chargerStatus];
-[CAFWirelessChargerStatus contentURLAction];
-[CAFWirelessChargerStatus registeredForBatteryLevel];
-[CAFWirelessChargerStatus registeredForButtonAction];
-[CAFWirelessChargerStatus registeredForChargerStatus];
-[CAFWirelessChargerStatus registeredForContentURLAction];
-[CAFWirelessChargerStatus registeredForDisabled];
-[CAFWirelessChargerStatus registeredForHidden];
-[CAFWirelessChargerStatus registeredForSortOrder];
-[CAFWirelessChargerStatus registeredForVehicleLayoutKey];
-[CAFWirelessChargerStatus vehicleLayoutKey];
-[CAFWirelessChargerStatus _characteristicDidUpdate:fromGroupUpdate:];
-[CAFWirelessChargerStatus batteryLevelCharacteristic];
-[CAFWirelessChargerStatus batteryLevelMeasurementRange];
-[CAFWirelessChargerStatus batteryLevelRange];
-[CAFWirelessChargerStatus buttonActionCharacteristic];
-[CAFWirelessChargerStatus chargerStatusCharacteristic];
-[CAFWirelessChargerStatus contentURLActionCharacteristic];
-[CAFWirelessChargerStatus disabledCharacteristic];
-[CAFWirelessChargerStatus hasContentURLAction];
-[CAFWirelessChargerStatus hasVehicleLayoutKey];
-[CAFWirelessChargerStatus hiddenCharacteristic];
-[CAFWirelessChargerStatus sortOrderCharacteristic];
-[CAFWirelessChargerStatus vehicleLayoutKeyCharacteristic];
```
