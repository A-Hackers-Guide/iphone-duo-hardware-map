# `ASAccessorySettings`

- Image: [`/System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit`](../userland/System__Library__Frameworks__AccessorySetupKit.framework__AccessorySetupKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUXPCCodable`, `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 13 instance methods, 2 class methods

## Instance variables

```
@"NSString" _SSID;
@"NSData" _bluetoothTransportBridgingIdentifier;
@"NSString" _displayName;
```

## Properties

```
@property (T@"NSString",C,N,V_displayName) displayName;
@property (T@"NSString",C,N,V_SSID) SSID;
@property (T@"NSData",C,N,V_bluetoothTransportBridgingIdentifier) bluetoothTransportBridgingIdentifier;
```

## Class methods

```
+[ASAccessorySettings supportsSecureCoding];
+[ASAccessorySettings defaultSettings];
```

## Instance methods

```
-[ASAccessorySettings encodeWithXPCObject:];
-[ASAccessorySettings setSSID:];
-[ASAccessorySettings SSID];
-[ASAccessorySettings initWithXPCObject:error:];
-[ASAccessorySettings descriptionWithLevel:];
-[ASAccessorySettings displayName];
-[ASAccessorySettings setDisplayName:];
-[ASAccessorySettings encodeWithCoder:];
-[ASAccessorySettings description];
-[ASAccessorySettings initWithCoder:];
-[ASAccessorySettings copyWithZone:];
-[ASAccessorySettings bluetoothTransportBridgingIdentifier];
-[ASAccessorySettings setBluetoothTransportBridgingIdentifier:];
```
