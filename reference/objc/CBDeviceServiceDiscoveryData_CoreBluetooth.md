# `CBDeviceServiceDiscoveryData`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBDeviceDataComponent`, `CUXPCCodable`, `NSSecureCoding`, `NSCopying`
- 4 instance variables, 8 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"NSData" _serviceDiscoveryEncryptedData;
@"NSData" _serviceDiscoveryGenerationCount;
@"NSData" _serviceDiscoveryIntegrityTagData;
@"NSData" _serviceDiscoveryRowIndex;
```

## Properties

```
@property (T@"NSData",C,N,V_serviceDiscoveryEncryptedData) serviceDiscoveryEncryptedData;
@property (T@"NSData",C,N,V_serviceDiscoveryGenerationCount) serviceDiscoveryGenerationCount;
@property (T@"NSData",C,N,V_serviceDiscoveryIntegrityTagData) serviceDiscoveryIntegrityTagData;
@property (T@"NSData",C,N,V_serviceDiscoveryRowIndex) serviceDiscoveryRowIndex;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBDeviceServiceDiscoveryData supportsSecureCoding];
```

## Instance methods

```
-[CBDeviceServiceDiscoveryData memoryFootprint];
-[CBDeviceServiceDiscoveryData encodeWithXPCObject:];
-[CBDeviceServiceDiscoveryData initWithDictionary:error:];
-[CBDeviceServiceDiscoveryData clear];
-[CBDeviceServiceDiscoveryData initWithXPCObject:error:];
-[CBDeviceServiceDiscoveryData descriptionWithLevel:];
-[CBDeviceServiceDiscoveryData serviceDiscoveryGenerationCount];
-[CBDeviceServiceDiscoveryData serviceDiscoveryRowIndex];
-[CBDeviceServiceDiscoveryData setServiceDiscoveryGenerationCount:];
-[CBDeviceServiceDiscoveryData encodeWithCoder:];
-[CBDeviceServiceDiscoveryData setServiceDiscoveryRowIndex:];
-[CBDeviceServiceDiscoveryData description];
-[CBDeviceServiceDiscoveryData initWithCoder:];
-[CBDeviceServiceDiscoveryData hasAnyData];
-[CBDeviceServiceDiscoveryData copyWithZone:];
-[CBDeviceServiceDiscoveryData dictionaryRepresentation];
-[CBDeviceServiceDiscoveryData serviceDiscoveryEncryptedData];
-[CBDeviceServiceDiscoveryData serviceDiscoveryIntegrityTagData];
-[CBDeviceServiceDiscoveryData setServiceDiscoveryEncryptedData:];
-[CBDeviceServiceDiscoveryData setServiceDiscoveryIntegrityTagData:];
```
