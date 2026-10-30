# `CBOOBKeyInfo`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUXPCCodable`
- 6 instance variables, 6 properties, 18 instance methods, 0 class methods

## Instance variables

```
C _btAddressType;
C _addressType;
C _keyType;
S _version;
@"NSData" _btAddressData;
@"NSData" _irkData;
```

## Properties

```
@property (T@"NSData",C,N,V_btAddressData) btAddressData;
@property (TC,N,V_btAddressType) btAddressType;
@property (TC,N,V_addressType) addressType;
@property (T@"NSData",C,N,V_irkData) irkData;
@property (TC,N,V_keyType) keyType;
@property (TS,N,V_version) version;
```

## Instance methods

```
-[CBOOBKeyInfo encodeWithXPCObject:];
-[CBOOBKeyInfo initWithXPCObject:error:];
-[CBOOBKeyInfo version];
-[CBOOBKeyInfo hash];
-[CBOOBKeyInfo description];
-[CBOOBKeyInfo setVersion:];
-[CBOOBKeyInfo isEqual:];
-[CBOOBKeyInfo keyType];
-[CBOOBKeyInfo btAddressData];
-[CBOOBKeyInfo irkData];
-[CBOOBKeyInfo setIrkData:];
-[CBOOBKeyInfo addressType];
-[CBOOBKeyInfo setAddressType:];
-[CBOOBKeyInfo setKeyType:];
-[CBOOBKeyInfo setBtAddressData:];
-[CBOOBKeyInfo btAddressType];
-[CBOOBKeyInfo proxyHash];
-[CBOOBKeyInfo setBtAddressType:];
```
