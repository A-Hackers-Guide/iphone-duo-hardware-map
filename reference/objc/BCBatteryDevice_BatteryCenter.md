# `BCBatteryDevice`

- Image: [`/System/Library/PrivateFrameworks/BatteryCenter.framework/BatteryCenter`](../userland/System__Library__PrivateFrameworks__BatteryCenter.framework__BatteryCenter.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 23 instance variables, 23 properties, 50 instance methods, 2 class methods

## Instance variables

```
@"NSString" _identifier;
@"NSString" _matchIdentifier;
q _percentCharge;
B _charging;
B _connected;
B _paused;
B _lowPowerModeActive;
B _lowBattery;
B _internal;
B _powerSource;
B _approximatesPercentCharge;
B _wirelesslyCharging;
B _fake;
q _vendor;
q _powerSourceState;
q _productIdentifier;
@"NSString" _accessoryIdentifier;
@"NSString" _name;
@"NSString" _modelNumber;
Q _parts;
Q _accessoryCategory;
@"NSString" _groupName;
q _transportType;
```

## Properties

```
@property (T@"NSString",C,N,V_identifier) identifier;
@property (T@"NSString",C,N,V_name) name;
@property (Tq,N,V_percentCharge) percentCharge;
@property (TB,N,GisConnected,V_connected) connected;
@property (TB,N,GisCharging,V_charging) charging;
@property (TB,N,GisPaused,V_paused) paused;
@property (TB,N,GisInternal,V_internal) internal;
@property (TB,N,GisPowerSource,V_powerSource) powerSource;
@property (TB,N,V_approximatesPercentCharge) approximatesPercentCharge;
@property (TQ,N,V_parts) parts;
@property (TB,N,GisWirelesslyCharging,V_wirelesslyCharging) wirelesslyCharging;
@property (T@"NSString",C,N,V_groupName) groupName;
@property (T@"NSString",R,C,N,V_matchIdentifier) matchIdentifier;
@property (Tq,N,V_transportType) transportType;
@property (Tq,N,V_powerSourceState) powerSourceState;
@property (TB,N,GisFake,V_fake) fake;
@property (TB,N,GisLowPowerModeActive,V_lowPowerModeActive) lowPowerModeActive;
@property (TB,N,GisLowBattery,V_lowBattery) lowBattery;
@property (T@"NSString",C,N,V_accessoryIdentifier) accessoryIdentifier;
@property (TQ,N,V_accessoryCategory) accessoryCategory;
@property (T@"NSString",C,N,V_modelNumber) modelNumber;
@property (Tq,R,N,V_vendor) vendor;
@property (Tq,R,N,V_productIdentifier) productIdentifier;
```

## Class methods

```
+[BCBatteryDevice supportsSecureCoding];
+[BCBatteryDevice batteryDeviceWithIdentifier:vendor:productIdentifier:parts:matchIdentifier:];
```

## Instance methods

```
-[BCBatteryDevice isCharging];
-[BCBatteryDevice modelNumber];
-[BCBatteryDevice isInternal];
-[BCBatteryDevice setConnected:];
-[BCBatteryDevice isConnected];
-[BCBatteryDevice isPaused];
-[BCBatteryDevice setTransportType:];
-[BCBatteryDevice identifier];
-[BCBatteryDevice productIdentifier];
-[BCBatteryDevice isBatterySaverModeActive];
-[BCBatteryDevice setModelNumber:];
-[BCBatteryDevice setGroupName:];
-[BCBatteryDevice transportType];
-[BCBatteryDevice setPaused:];
-[BCBatteryDevice setAccessoryCategory:];
-[BCBatteryDevice setIdentifier:];
-[BCBatteryDevice setCharging:];
-[BCBatteryDevice encodeWithCoder:];
-[BCBatteryDevice groupName];
-[BCBatteryDevice accessoryCategory];
-[BCBatteryDevice description];
-[BCBatteryDevice setInternal:];
-[BCBatteryDevice setName:];
-[BCBatteryDevice initWithCoder:];
-[BCBatteryDevice setPercentCharge:];
-[BCBatteryDevice copyWithZone:];
-[BCBatteryDevice percentCharge];
-[BCBatteryDevice name];
-[BCBatteryDevice isLowBattery];
-[BCBatteryDevice parts];
-[BCBatteryDevice vendor];
-[BCBatteryDevice accessoryIdentifier];
-[BCBatteryDevice setAccessoryIdentifier:];
-[BCBatteryDevice setParts:];
-[BCBatteryDevice isLowPowerModeActive];
-[BCBatteryDevice isPowerSource];
-[BCBatteryDevice isWirelesslyCharging];
-[BCBatteryDevice powerSourceState];
-[BCBatteryDevice isFake];
-[BCBatteryDevice setLowBattery:];
-[BCBatteryDevice matchIdentifier];
-[BCBatteryDevice synthesizedRepresentativeDevice];
-[BCBatteryDevice setPowerSource:];
-[BCBatteryDevice approximatesPercentCharge];
-[BCBatteryDevice initWithIdentifier:vendor:productIdentifier:parts:matchIdentifier:];
-[BCBatteryDevice setApproximatesPercentCharge:];
-[BCBatteryDevice setFake:];
-[BCBatteryDevice setLowPowerModeActive:];
-[BCBatteryDevice setPowerSourceState:];
-[BCBatteryDevice setWirelesslyCharging:];
```
