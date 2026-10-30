# `CBDeviceObjectDiscoveryData`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBDeviceDataComponent`, `CUXPCCodable`, `NSSecureCoding`, `NSCopying`
- 5 instance variables, 9 properties, 22 instance methods, 1 class methods

## Instance variables

```
C _objectDiscoveryBatteryState;
C _objectDiscoveryMode;
I _objectDiscoveryProductID;
@"NSData" _objectDiscoveryNearOwnerID;
@"NSData" _objectDiscoveryPublicKeyData;
```

## Properties

```
@property (TC,N,V_objectDiscoveryBatteryState) objectDiscoveryBatteryState;
@property (TC,N,V_objectDiscoveryMode) objectDiscoveryMode;
@property (T@"NSData",C,N,V_objectDiscoveryNearOwnerID) objectDiscoveryNearOwnerID;
@property (TI,N,V_objectDiscoveryProductID) objectDiscoveryProductID;
@property (T@"NSData",C,N,V_objectDiscoveryPublicKeyData) objectDiscoveryPublicKeyData;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBDeviceObjectDiscoveryData supportsSecureCoding];
```

## Instance methods

```
-[CBDeviceObjectDiscoveryData memoryFootprint];
-[CBDeviceObjectDiscoveryData encodeWithXPCObject:];
-[CBDeviceObjectDiscoveryData initWithDictionary:error:];
-[CBDeviceObjectDiscoveryData clear];
-[CBDeviceObjectDiscoveryData initWithXPCObject:error:];
-[CBDeviceObjectDiscoveryData descriptionWithLevel:];
-[CBDeviceObjectDiscoveryData encodeWithCoder:];
-[CBDeviceObjectDiscoveryData description];
-[CBDeviceObjectDiscoveryData initWithCoder:];
-[CBDeviceObjectDiscoveryData hasAnyData];
-[CBDeviceObjectDiscoveryData copyWithZone:];
-[CBDeviceObjectDiscoveryData dictionaryRepresentation];
-[CBDeviceObjectDiscoveryData objectDiscoveryBatteryState];
-[CBDeviceObjectDiscoveryData objectDiscoveryMode];
-[CBDeviceObjectDiscoveryData objectDiscoveryNearOwnerID];
-[CBDeviceObjectDiscoveryData objectDiscoveryProductID];
-[CBDeviceObjectDiscoveryData objectDiscoveryPublicKeyData];
-[CBDeviceObjectDiscoveryData setObjectDiscoveryBatteryState:];
-[CBDeviceObjectDiscoveryData setObjectDiscoveryMode:];
-[CBDeviceObjectDiscoveryData setObjectDiscoveryNearOwnerID:];
-[CBDeviceObjectDiscoveryData setObjectDiscoveryProductID:];
-[CBDeviceObjectDiscoveryData setObjectDiscoveryPublicKeyData:];
```
