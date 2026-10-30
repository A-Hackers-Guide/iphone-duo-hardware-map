# `CBServiceUUIDParamInfo`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUXPCCodable`
- 3 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSData" _serviceUUID;
@"NSData" _blobData;
@"NSData" _maskData;
```

## Properties

```
@property (T@"NSData",C,N,V_serviceUUID) serviceUUID;
@property (T@"NSData",C,N,V_blobData) blobData;
@property (T@"NSData",C,N,V_maskData) maskData;
```

## Instance methods

```
-[CBServiceUUIDParamInfo encodeWithXPCObject:];
-[CBServiceUUIDParamInfo initWithXPCObject:error:];
-[CBServiceUUIDParamInfo serviceUUID];
-[CBServiceUUIDParamInfo setServiceUUID:];
-[CBServiceUUIDParamInfo hash];
-[CBServiceUUIDParamInfo description];
-[CBServiceUUIDParamInfo isEqual:];
-[CBServiceUUIDParamInfo blobData];
-[CBServiceUUIDParamInfo maskData];
-[CBServiceUUIDParamInfo setBlobData:];
-[CBServiceUUIDParamInfo setMaskData:];
```
