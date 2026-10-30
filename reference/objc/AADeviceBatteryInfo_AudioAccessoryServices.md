# `AADeviceBatteryInfo`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 16 instance variables, 29 properties, 71 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _batteryMap;
C _color;
C _dynamicEndOfChargeCapability;
B _isConnected;
B _isNearby;
C _optimizedBatteryChargingCapability;
C _caseVersion;
C _caseLedColor;
C _caseLedStatus;
I _productID;
@"NSString" _bluetoothAddress;
@"NSString" _identifier;
@"NSString" _model;
@"NSString" _name;
@"NSString" _findMyGroupIdentifier;
@"NSString" _caseIdentifier;
```

## Properties

```
@property (T@"NSMutableDictionary",C,N) batteryMap;
@property (T@"NSString",C,N,V_bluetoothAddress) bluetoothAddress;
@property (TC,N,V_dynamicEndOfChargeCapability) dynamicEndOfChargeCapability;
@property (TC,V_color) color;
@property (T@"NSString",C,N,V_model) model;
@property (T@"NSString",C,N,V_name) name;
@property (TC,N,V_optimizedBatteryChargingCapability) optimizedBatteryChargingCapability;
@property (TI,V_productID) productID;
@property (TB,V_isConnected) isConnected;
@property (TB,V_isNearby) isNearby;
@property (T@"NSString",C,N,V_findMyGroupIdentifier) findMyGroupIdentifier;
@property (T@"NSString",C,N,V_caseIdentifier) caseIdentifier;
@property (TC,V_caseVersion) caseVersion;
@property (TC,V_caseLedColor) caseLedColor;
@property (TC,V_caseLedStatus) caseLedStatus;
@property (TB,R,N) areAnyBatteriesAvailable;
@property (T@"NSArray",R,N) batteries;
@property (T@"AABattery",R,N) batteryCase;
@property (T@"AABattery",R,N) batteryLeft;
@property (T@"AABattery",R,N) batteryMain;
@property (T@"AABattery",R,N) batteryRight;
@property (T@"AABattery",R,N) batteryCombinedLeftRight;
@property (T@"NSString",R,N,V_identifier) identifier;
@property (TB,R,N) reportLowBatteryFromMain;
@property (T@"AABattery",R,N) visibleBatteryCase;
@property (T@"AABattery",R,N) visibleBatteryLeft;
@property (T@"AABattery",R,N) visibleBatteryMain;
@property (T@"AABattery",R,N) visibleBatteryRight;
@property (T@"AABattery",R,N) visibleBatteryCombinedLeftRight;
```

## Class methods

```
+[AADeviceBatteryInfo supportsSecureCoding];
```

## Instance methods

```
-[AADeviceBatteryInfo setProductID:];
-[AADeviceBatteryInfo productID];
-[AADeviceBatteryInfo model];
-[AADeviceBatteryInfo isConnected];
-[AADeviceBatteryInfo setColor:];
-[AADeviceBatteryInfo setModel:];
-[AADeviceBatteryInfo descriptionWithLevel:];
-[AADeviceBatteryInfo identifier];
-[AADeviceBatteryInfo setBluetoothAddress:];
-[AADeviceBatteryInfo color];
-[AADeviceBatteryInfo bluetoothAddress];
-[AADeviceBatteryInfo encodeWithCoder:];
-[AADeviceBatteryInfo description];
-[AADeviceBatteryInfo setName:];
-[AADeviceBatteryInfo initWithCoder:];
-[AADeviceBatteryInfo copyWithZone:];
-[AADeviceBatteryInfo setIsConnected:];
-[AADeviceBatteryInfo name];
-[AADeviceBatteryInfo initWithIdentifier:];
-[AADeviceBatteryInfo isNearby];
-[AADeviceBatteryInfo caseIdentifier];
-[AADeviceBatteryInfo setIsNearby:];
-[AADeviceBatteryInfo visibleBatteryCombinedLeftRight];
-[AADeviceBatteryInfo batteryCase];
-[AADeviceBatteryInfo batteryLeft];
-[AADeviceBatteryInfo batteryMain];
-[AADeviceBatteryInfo batteryRight];
-[AADeviceBatteryInfo dynamicEndOfChargeCapability];
-[AADeviceBatteryInfo optimizedBatteryChargingCapability];
-[AADeviceBatteryInfo visibleBatteryCase];
-[AADeviceBatteryInfo visibleBatteryLeft];
-[AADeviceBatteryInfo visibleBatteryMain];
-[AADeviceBatteryInfo visibleBatteryRight];
-[AADeviceBatteryInfo setCaseVersion:];
-[AADeviceBatteryInfo caseVersion];
-[AADeviceBatteryInfo findMyGroupIdentifier];
-[AADeviceBatteryInfo setFindMyGroupIdentifier:];
-[AADeviceBatteryInfo batteryForType:];
-[AADeviceBatteryInfo _batteryStateFromCharging:chargingOBC:chargingDEOC:];
-[AADeviceBatteryInfo _clearCombinedBattery];
-[AADeviceBatteryInfo _updateBatteriesFromTetheredAdvertisement:];
-[AADeviceBatteryInfo _updateBatteriesFromUntetheredAdvertisement:];
-[AADeviceBatteryInfo _updateCaseInfo:];
-[AADeviceBatteryInfo _updateChargingOBCTimeUntilCharged:];
-[AADeviceBatteryInfo _updateCombinedBatteryWithChanges:];
-[AADeviceBatteryInfo _updateWithAACPBatteryInfo:];
-[AADeviceBatteryInfo _updateWithNearbyBattery:forType:withSource:];
-[AADeviceBatteryInfo _updateWithProximityPairingPayload:];
-[AADeviceBatteryInfo applyOverrideFromStr:forBatteryType:];
-[AADeviceBatteryInfo areAnyBatteriesAvailable];
-[AADeviceBatteryInfo batteries];
-[AADeviceBatteryInfo batteryCombinedLeftRight];
-[AADeviceBatteryInfo batteryMap];
-[AADeviceBatteryInfo caseLedColor];
-[AADeviceBatteryInfo caseLedStatus];
-[AADeviceBatteryInfo clearExpiredBatteries];
-[AADeviceBatteryInfo removeBatteryInMap:];
-[AADeviceBatteryInfo reportLowBatteryFromMain];
-[AADeviceBatteryInfo setBatteryInMap:];
-[AADeviceBatteryInfo setBatteryMap:];
-[AADeviceBatteryInfo setCaseIdentifier:];
-[AADeviceBatteryInfo setCaseLedColor:];
-[AADeviceBatteryInfo setCaseLedStatus:];
-[AADeviceBatteryInfo setDynamicEndOfChargeCapability:];
-[AADeviceBatteryInfo setOptimizedBatteryChargingCapability:];
-[AADeviceBatteryInfo updateWithAACPBatteryInfoData:];
-[AADeviceBatteryInfo updateWithAANearbyDevice:];
-[AADeviceBatteryInfo updateWithConnectedDevice:];
-[AADeviceBatteryInfo updateWithDisconnectedDevice:];
-[AADeviceBatteryInfo updateWithLostAANearbyDevice:];
-[AADeviceBatteryInfo updateWithPairedDevice:];
```
