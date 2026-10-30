# `ASAccessory`

- Image: [`/System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit`](../userland/System__Library__Frameworks__AccessorySetupKit.framework__AccessorySetupKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUXPCCodable`, `NSSecureCoding`, `NSCopying`
- 9 instance variables, 9 properties, 28 instance methods, 1 class methods

## Instance variables

```
q _state;
@"NSUUID" _bluetoothIdentifier;
@"NSData" _bluetoothTransportBridgingIdentifier;
@"NSString" _displayName;
@"NSString" _SSID;
Q _wifiAwarePairedDeviceID;
@"ASDiscoveryDescriptor" _descriptor;
@"NSString" _identifier;
Q _wifiAwarePairingID;
```

## Properties

```
@property (T@"NSString",C,N,V_identifier) identifier;
@property (Tq,N,V_state) state;
@property (T@"NSData",C,N,V_bluetoothTransportBridgingIdentifier) bluetoothTransportBridgingIdentifier;
@property (T@"NSUUID",C,N,V_bluetoothIdentifier) bluetoothIdentifier;
@property (T@"NSString",C,N,V_displayName) displayName;
@property (T@"NSString",C,N,V_SSID) SSID;
@property (T@"ASDiscoveryDescriptor",C,N,V_descriptor) descriptor;
@property (TQ,N,V_wifiAwarePairingID) wifiAwarePairingID;
@property (TQ,N,V_wifiAwarePairedDeviceID) wifiAwarePairedDeviceID;
```

## Class methods

```
+[ASAccessory supportsSecureCoding];
```

## Instance methods

```
-[ASAccessory encodeWithXPCObject:];
-[ASAccessory setDescriptor:];
-[ASAccessory setSSID:];
-[ASAccessory SSID];
-[ASAccessory initWithXPCObject:error:];
-[ASAccessory setState:];
-[ASAccessory descriptor];
-[ASAccessory descriptionWithLevel:];
-[ASAccessory identifier];
-[ASAccessory displayName];
-[ASAccessory setDisplayName:];
-[ASAccessory bluetoothIdentifier];
-[ASAccessory setIdentifier:];
-[ASAccessory encodeWithCoder:];
-[ASAccessory hash];
-[ASAccessory description];
-[ASAccessory initWithCoder:];
-[ASAccessory copyWithZone:];
-[ASAccessory isEqual:];
-[ASAccessory state];
-[ASAccessory setBluetoothIdentifier:];
-[ASAccessory bluetoothTransportBridgingIdentifier];
-[ASAccessory initWithDADevice:bundleID:];
-[ASAccessory setBluetoothTransportBridgingIdentifier:];
-[ASAccessory setWifiAwarePairedDeviceID:];
-[ASAccessory setWifiAwarePairingID:];
-[ASAccessory wifiAwarePairedDeviceID];
-[ASAccessory wifiAwarePairingID];
```
