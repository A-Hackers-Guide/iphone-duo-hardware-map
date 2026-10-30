# `CBDeviceIdentity`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUXPCCodable`
- 9 instance variables, 9 properties, 23 instance methods, 0 class methods

## Instance variables

```
i _type;
@"NSString" _accountID;
@"NSUUID" _bluetoothIdentifier;
@"NSString" _contactID;
@"NSString" _identifier;
@"NSString" _idsDeviceID;
@"NSData" _irkData;
@"NSString" _model;
@"NSString" _name;
```

## Properties

```
@property (T@"NSString",C,N,V_accountID) accountID;
@property (T@"NSUUID",C,N,V_bluetoothIdentifier) bluetoothIdentifier;
@property (T@"NSString",C,N,V_contactID) contactID;
@property (T@"NSString",C,N,V_identifier) identifier;
@property (T@"NSString",C,N,V_idsDeviceID) idsDeviceID;
@property (T@"NSData",C,N,V_irkData) irkData;
@property (T@"NSString",C,N,V_model) model;
@property (T@"NSString",C,N,V_name) name;
@property (Ti,N,V_type) type;
```

## Instance methods

```
-[CBDeviceIdentity encodeWithXPCObject:];
-[CBDeviceIdentity model];
-[CBDeviceIdentity setAccountID:];
-[CBDeviceIdentity setModel:];
-[CBDeviceIdentity initWithXPCObject:error:];
-[CBDeviceIdentity descriptionWithLevel:];
-[CBDeviceIdentity identifier];
-[CBDeviceIdentity setIdsDeviceID:];
-[CBDeviceIdentity accountID];
-[CBDeviceIdentity bluetoothIdentifier];
-[CBDeviceIdentity setIdentifier:];
-[CBDeviceIdentity setType:];
-[CBDeviceIdentity type];
-[CBDeviceIdentity setContactID:];
-[CBDeviceIdentity description];
-[CBDeviceIdentity idsDeviceID];
-[CBDeviceIdentity setName:];
-[CBDeviceIdentity isEqual:];
-[CBDeviceIdentity name];
-[CBDeviceIdentity contactID];
-[CBDeviceIdentity irkData];
-[CBDeviceIdentity setIrkData:];
-[CBDeviceIdentity setBluetoothIdentifier:];
```
