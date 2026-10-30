# `BTMagicPairingSettings`

- Image: [`/System/Library/PrivateFrameworks/BluetoothServices.framework/BluetoothServices`](../userland/System__Library__PrivateFrameworks__BluetoothServices.framework__BluetoothServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 25 instance variables, 25 properties, 54 instance methods, 2 class methods

## Instance variables

```
@"NSString" _bluetoothAddress;
@"NSData" _masterKey;
@"NSData" _masterHint;
@"NSData" _accessoryKey;
@"NSData" _accessoryHint;
@"NSData" _encryptionKey;
@"NSData" _irk;
@"NSData" _crownRotationDirection;
@"NSString" _name;
@"NSString" _productID;
@"NSString" _vendorID;
@"NSString" _buttonModes;
@"NSString" _color;
@"NSString" _deviceIDFeatureBitsV1;
@"NSString" _deviceIDFeatureBitsV2;
@"NSString" _listeningServices;
@"NSString" _listeningServicesV2;
@"NSString" _spatialAudio;
@"NSString" _optimizedBatteryCharging;
@"NSString" _optimizedBatteryFullChargeDeadline;
@"NSString" _ratchet;
@"NSString" _reserved;
@"NSString" _settingsMask;
@"NSString" _supportedServices;
@"NSString" _version;
```

## Properties

```
@property (T@"NSString",&,N,V_bluetoothAddress) bluetoothAddress;
@property (T@"NSData",&,N,V_masterKey) masterKey;
@property (T@"NSData",&,N,V_masterHint) masterHint;
@property (T@"NSData",&,N,V_accessoryKey) accessoryKey;
@property (T@"NSData",&,N,V_accessoryHint) accessoryHint;
@property (T@"NSData",&,N,V_encryptionKey) encryptionKey;
@property (T@"NSData",&,N,V_irk) irk;
@property (T@"NSData",&,N,V_crownRotationDirection) crownRotationDirection;
@property (T@"NSString",&,N,V_name) name;
@property (T@"NSString",&,N,V_productID) productID;
@property (T@"NSString",&,N,V_vendorID) vendorID;
@property (T@"NSString",&,N,V_buttonModes) buttonModes;
@property (T@"NSString",&,N,V_color) color;
@property (T@"NSString",&,N,V_deviceIDFeatureBitsV1) deviceIDFeatureBitsV1;
@property (T@"NSString",&,N,V_deviceIDFeatureBitsV2) deviceIDFeatureBitsV2;
@property (T@"NSString",&,N,V_listeningServices) listeningServices;
@property (T@"NSString",&,N,V_listeningServicesV2) listeningServicesV2;
@property (T@"NSString",&,N,V_spatialAudio) spatialAudio;
@property (T@"NSString",&,N,V_optimizedBatteryCharging) optimizedBatteryCharging;
@property (T@"NSString",&,N,V_optimizedBatteryFullChargeDeadline) optimizedBatteryFullChargeDeadline;
@property (T@"NSString",&,N,V_ratchet) ratchet;
@property (T@"NSString",&,N,V_reserved) reserved;
@property (T@"NSString",&,N,V_settingsMask) settingsMask;
@property (T@"NSString",&,N,V_supportedServices) supportedServices;
@property (T@"NSString",&,N,V_version) version;
```

## Class methods

```
+[BTMagicPairingSettings supportsSecureCoding];
+[BTMagicPairingSettings magicSettingsWithBluetoothAddress:];
```

## Instance methods

```
-[BTMagicPairingSettings vendorID];
-[BTMagicPairingSettings setProductID:];
-[BTMagicPairingSettings productID];
-[BTMagicPairingSettings setColor:];
-[BTMagicPairingSettings setBluetoothAddress:];
-[BTMagicPairingSettings reserved];
-[BTMagicPairingSettings setVendorID:];
-[BTMagicPairingSettings version];
-[BTMagicPairingSettings color];
-[BTMagicPairingSettings bluetoothAddress];
-[BTMagicPairingSettings supportedServices];
-[BTMagicPairingSettings encodeWithCoder:];
-[BTMagicPairingSettings description];
-[BTMagicPairingSettings setName:];
-[BTMagicPairingSettings initWithCoder:];
-[BTMagicPairingSettings setVersion:];
-[BTMagicPairingSettings setSupportedServices:];
-[BTMagicPairingSettings setReserved:];
-[BTMagicPairingSettings name];
-[BTMagicPairingSettings encryptionKey];
-[BTMagicPairingSettings setEncryptionKey:];
-[BTMagicPairingSettings masterKey];
-[BTMagicPairingSettings crownRotationDirection];
-[BTMagicPairingSettings setCrownRotationDirection:];
-[BTMagicPairingSettings ratchet];
-[BTMagicPairingSettings setRatchet:];
-[BTMagicPairingSettings setMasterKey:];
-[BTMagicPairingSettings setAccessoryKey:];
-[BTMagicPairingSettings irk];
-[BTMagicPairingSettings setButtonModes:];
-[BTMagicPairingSettings setIrk:];
-[BTMagicPairingSettings accessoryHint];
-[BTMagicPairingSettings accessoryKey];
-[BTMagicPairingSettings buttonModes];
-[BTMagicPairingSettings deviceIDFeatureBitsV1];
-[BTMagicPairingSettings deviceIDFeatureBitsV2];
-[BTMagicPairingSettings initWithBluetoothAddress:];
-[BTMagicPairingSettings listeningServices];
-[BTMagicPairingSettings listeningServicesV2];
-[BTMagicPairingSettings masterHint];
-[BTMagicPairingSettings optimizedBatteryCharging];
-[BTMagicPairingSettings optimizedBatteryFullChargeDeadline];
-[BTMagicPairingSettings setAccessoryHint:];
-[BTMagicPairingSettings setDeviceIDFeatureBitsV1:];
-[BTMagicPairingSettings setDeviceIDFeatureBitsV2:];
-[BTMagicPairingSettings setListeningServices:];
-[BTMagicPairingSettings setListeningServicesV2:];
-[BTMagicPairingSettings setMasterHint:];
-[BTMagicPairingSettings setOptimizedBatteryCharging:];
-[BTMagicPairingSettings setOptimizedBatteryFullChargeDeadline:];
-[BTMagicPairingSettings setSettingsMask:];
-[BTMagicPairingSettings setSpatialAudio:];
-[BTMagicPairingSettings settingsMask];
-[BTMagicPairingSettings spatialAudio];
```
