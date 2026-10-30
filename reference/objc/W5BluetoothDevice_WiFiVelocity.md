# `W5BluetoothDevice`

- Image: [`/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity`](../userland/System__Library__PrivateFrameworks__WiFiVelocity.framework__WiFiVelocity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 17 instance variables, 17 properties, 43 instance methods, 1 class methods

## Instance variables

```
B _isPaired;
B _isCloudPaired;
B _isConnected;
B _isAppleDevice;
B _isLowEnergy;
@"NSString" _name;
@"NSString" _address;
Q _majorClass;
Q _minorClass;
q _rssi;
@"NSString" _afhMap;
q _connectionMode;
Q _connectionModeInterval;
q _manufacturer;
Q _lmpVersion;
Q _lmpSubversion;
q _role;
```

## Properties

```
@property (T@"NSString",C,N,V_name) name;
@property (T@"NSString",C,N,V_address) address;
@property (TB,N,V_isPaired) isPaired;
@property (TB,N,V_isCloudPaired) isCloudPaired;
@property (TB,N,V_isConnected) isConnected;
@property (TB,N,V_isAppleDevice) isAppleDevice;
@property (TB,N,V_isLowEnergy) isLowEnergy;
@property (TQ,N,V_majorClass) majorClass;
@property (TQ,N,V_minorClass) minorClass;
@property (Tq,N,V_rssi) rssi;
@property (T@"NSString",C,N,V_afhMap) afhMap;
@property (Tq,N,V_connectionMode) connectionMode;
@property (TQ,N,V_connectionModeInterval) connectionModeInterval;
@property (Tq,N,V_manufacturer) manufacturer;
@property (TQ,N,V_lmpVersion) lmpVersion;
@property (TQ,N,V_lmpSubversion) lmpSubversion;
@property (Tq,N,V_role) role;
```

## Class methods

```
+[W5BluetoothDevice supportsSecureCoding];
```

## Instance methods

```
-[W5BluetoothDevice rssi];
-[W5BluetoothDevice isPaired];
-[W5BluetoothDevice isConnected];
-[W5BluetoothDevice address];
-[W5BluetoothDevice setAddress:];
-[W5BluetoothDevice setLmpVersion:];
-[W5BluetoothDevice dealloc];
-[W5BluetoothDevice setRssi:];
-[W5BluetoothDevice manufacturer];
-[W5BluetoothDevice lmpVersion];
-[W5BluetoothDevice encodeWithCoder:];
-[W5BluetoothDevice role];
-[W5BluetoothDevice conformsToProtocol:];
-[W5BluetoothDevice hash];
-[W5BluetoothDevice setRole:];
-[W5BluetoothDevice description];
-[W5BluetoothDevice setName:];
-[W5BluetoothDevice setConnectionMode:];
-[W5BluetoothDevice initWithCoder:];
-[W5BluetoothDevice copyWithZone:];
-[W5BluetoothDevice setIsConnected:];
-[W5BluetoothDevice isEqual:];
-[W5BluetoothDevice connectionMode];
-[W5BluetoothDevice name];
-[W5BluetoothDevice majorClass];
-[W5BluetoothDevice minorClass];
-[W5BluetoothDevice setManufacturer:];
-[W5BluetoothDevice isAppleDevice];
-[W5BluetoothDevice setIsPaired:];
-[W5BluetoothDevice isCloudPaired];
-[W5BluetoothDevice setIsLowEnergy:];
-[W5BluetoothDevice afhMap];
-[W5BluetoothDevice connectionModeInterval];
-[W5BluetoothDevice isEqualToBluetoothDevice:];
-[W5BluetoothDevice isLowEnergy];
-[W5BluetoothDevice lmpSubversion];
-[W5BluetoothDevice setAfhMap:];
-[W5BluetoothDevice setConnectionModeInterval:];
-[W5BluetoothDevice setIsAppleDevice:];
-[W5BluetoothDevice setIsCloudPaired:];
-[W5BluetoothDevice setLmpSubversion:];
-[W5BluetoothDevice setMajorClass:];
-[W5BluetoothDevice setMinorClass:];
```
