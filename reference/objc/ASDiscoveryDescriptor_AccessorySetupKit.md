# `ASDiscoveryDescriptor`

- Image: [`/System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit`](../userland/System__Library__Frameworks__AccessorySetupKit.framework__AccessorySetupKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUXPCCodable`, `NSSecureCoding`, `NSCopying`
- 19 instance variables, 19 properties, 48 instance methods, 1 class methods

## Instance variables

```
S _bluetoothCompanyIdentifier;
Q _supportedOptions;
@"NSData" _bluetoothManufacturerDataBlob;
@"NSData" _bluetoothManufacturerDataMask;
Q _bluetoothNameSubstringCompareOptions;
@"NSString" _bluetoothNameSubstring;
q _bluetoothRange;
@"NSData" _bluetoothServiceDataBlob;
@"NSData" _bluetoothServiceDataMask;
@"CBUUID" _bluetoothServiceUUID;
@"NSString" _SSID;
@"NSString" _SSIDPrefix;
@"NSString" _wifiAwareServiceName;
q _wifiAwareServiceRole;
@"ASPropertyCompareString" _wifiAwareModelNameMatch;
@"ASPropertyCompareString" _wifiAwareVendorNameMatch;
@"NSString" _bonjourServiceName;
@"NSString" _bonjourServiceType;
@"NSData" _bonjourTXTRecordData;
```

## Properties

```
@property (T@"NSString",C,N,V_bonjourServiceName) bonjourServiceName;
@property (T@"NSString",C,N,V_bonjourServiceType) bonjourServiceType;
@property (T@"NSData",C,N,V_bonjourTXTRecordData) bonjourTXTRecordData;
@property (TQ,N,V_supportedOptions) supportedOptions;
@property (TS,N,V_bluetoothCompanyIdentifier) bluetoothCompanyIdentifier;
@property (T@"NSData",C,N,V_bluetoothManufacturerDataBlob) bluetoothManufacturerDataBlob;
@property (T@"NSData",C,N,V_bluetoothManufacturerDataMask) bluetoothManufacturerDataMask;
@property (TQ,N,V_bluetoothNameSubstringCompareOptions) bluetoothNameSubstringCompareOptions;
@property (T@"NSString",C,N,V_bluetoothNameSubstring) bluetoothNameSubstring;
@property (Tq,N,V_bluetoothRange) bluetoothRange;
@property (T@"NSData",C,N,V_bluetoothServiceDataBlob) bluetoothServiceDataBlob;
@property (T@"NSData",C,N,V_bluetoothServiceDataMask) bluetoothServiceDataMask;
@property (T@"CBUUID",C,N,V_bluetoothServiceUUID) bluetoothServiceUUID;
@property (T@"NSString",C,N,V_SSID) SSID;
@property (T@"NSString",C,N,V_SSIDPrefix) SSIDPrefix;
@property (T@"NSString",C,N,V_wifiAwareServiceName) wifiAwareServiceName;
@property (Tq,N,V_wifiAwareServiceRole) wifiAwareServiceRole;
@property (T@"ASPropertyCompareString",C,N,V_wifiAwareModelNameMatch) wifiAwareModelNameMatch;
@property (T@"ASPropertyCompareString",C,N,V_wifiAwareVendorNameMatch) wifiAwareVendorNameMatch;
```

## Class methods

```
+[ASDiscoveryDescriptor supportsSecureCoding];
```

## Instance methods

```
-[ASDiscoveryDescriptor encodeWithXPCObject:];
-[ASDiscoveryDescriptor setSSID:];
-[ASDiscoveryDescriptor SSID];
-[ASDiscoveryDescriptor initWithXPCObject:error:];
-[ASDiscoveryDescriptor descriptionWithLevel:];
-[ASDiscoveryDescriptor supportedOptions];
-[ASDiscoveryDescriptor setBonjourServiceType:];
-[ASDiscoveryDescriptor setSupportedOptions:];
-[ASDiscoveryDescriptor encodeWithCoder:];
-[ASDiscoveryDescriptor hash];
-[ASDiscoveryDescriptor bonjourServiceType];
-[ASDiscoveryDescriptor description];
-[ASDiscoveryDescriptor initWithCoder:];
-[ASDiscoveryDescriptor copyWithZone:];
-[ASDiscoveryDescriptor isEqual:];
-[ASDiscoveryDescriptor bonjourServiceName];
-[ASDiscoveryDescriptor setWifiAwareServiceName:];
-[ASDiscoveryDescriptor setWifiAwareVendorNameMatch:];
-[ASDiscoveryDescriptor wifiAwareServiceName];
-[ASDiscoveryDescriptor wifiAwareVendorNameMatch];
-[ASDiscoveryDescriptor SSIDPrefix];
-[ASDiscoveryDescriptor initWithDiscoveryConfiguration:];
-[ASDiscoveryDescriptor bluetoothCompanyIdentifier];
-[ASDiscoveryDescriptor bluetoothManufacturerDataBlob];
-[ASDiscoveryDescriptor bluetoothManufacturerDataMask];
-[ASDiscoveryDescriptor bluetoothNameSubstring];
-[ASDiscoveryDescriptor bluetoothNameSubstringCompareOptions];
-[ASDiscoveryDescriptor bluetoothRange];
-[ASDiscoveryDescriptor bluetoothServiceDataBlob];
-[ASDiscoveryDescriptor bluetoothServiceDataMask];
-[ASDiscoveryDescriptor bluetoothServiceUUID];
-[ASDiscoveryDescriptor bonjourTXTRecordData];
-[ASDiscoveryDescriptor setBluetoothCompanyIdentifier:];
-[ASDiscoveryDescriptor setBluetoothManufacturerDataBlob:];
-[ASDiscoveryDescriptor setBluetoothManufacturerDataMask:];
-[ASDiscoveryDescriptor setBluetoothNameSubstring:];
-[ASDiscoveryDescriptor setBluetoothNameSubstringCompareOptions:];
-[ASDiscoveryDescriptor setBluetoothRange:];
-[ASDiscoveryDescriptor setBluetoothServiceDataBlob:];
-[ASDiscoveryDescriptor setBluetoothServiceDataMask:];
-[ASDiscoveryDescriptor setBluetoothServiceUUID:];
-[ASDiscoveryDescriptor setBonjourServiceName:];
-[ASDiscoveryDescriptor setBonjourTXTRecordData:];
-[ASDiscoveryDescriptor setSSIDPrefix:];
-[ASDiscoveryDescriptor setWifiAwareModelNameMatch:];
-[ASDiscoveryDescriptor setWifiAwareServiceRole:];
-[ASDiscoveryDescriptor wifiAwareModelNameMatch];
-[ASDiscoveryDescriptor wifiAwareServiceRole];
```
