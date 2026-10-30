# `NIBluetoothSample`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 10 instance variables, 10 properties, 24 instance methods, 1 class methods

## Instance variables

```
i _channel;
d _rssi;
@"NSString" _identifier;
@"NSString" _model;
d _machContinuousTimeSeconds;
@"NSString" _partIdentifier;
@"NSString" _name;
@"NSData" _presenceConfigData;
q _devicePlacement;
@"NSNumber" _isLidClosed;
```

## Properties

```
@property (T@"NSString",R,V_partIdentifier) partIdentifier;
@property (T@"NSString",C,N,V_name) name;
@property (T@"NSData",C,N,V_presenceConfigData) presenceConfigData;
@property (Tq,V_devicePlacement) devicePlacement;
@property (T@"NSNumber",&,N,V_isLidClosed) isLidClosed;
@property (Td,R,V_rssi) rssi;
@property (T@"NSString",R,V_identifier) identifier;
@property (T@"NSString",R,V_model) model;
@property (Ti,R,V_channel) channel;
@property (Td,R,V_machContinuousTimeSeconds) machContinuousTimeSeconds;
```

## Class methods

```
+[NIBluetoothSample supportsSecureCoding];
```

## Instance methods

```
-[NIBluetoothSample rssi];
-[NIBluetoothSample model];
-[NIBluetoothSample channel];
-[NIBluetoothSample identifier];
-[NIBluetoothSample descriptionInternal];
-[NIBluetoothSample encodeWithCoder:];
-[NIBluetoothSample hash];
-[NIBluetoothSample description];
-[NIBluetoothSample setName:];
-[NIBluetoothSample initWithCoder:];
-[NIBluetoothSample copyWithZone:];
-[NIBluetoothSample isEqual:];
-[NIBluetoothSample name];
-[NIBluetoothSample machContinuousTimeSeconds];
-[NIBluetoothSample partIdentifier];
-[NIBluetoothSample presenceConfigData];
-[NIBluetoothSample setPresenceConfigData:];
-[NIBluetoothSample devicePlacement];
-[NIBluetoothSample setIsLidClosed:];
-[NIBluetoothSample initWithBluetoothSample:];
-[NIBluetoothSample initWithRSSI:identifier:model:channel:machContinuousTimeSeconds:];
-[NIBluetoothSample initWithRSSI:identifier:model:channel:machContinuousTimeSeconds:partIdentifier:name:presenceConfigData:];
-[NIBluetoothSample isLidClosed];
-[NIBluetoothSample setDevicePlacement:];
```
