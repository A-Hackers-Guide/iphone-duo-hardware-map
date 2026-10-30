# `CBDeviceHomeKitV2Data`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBDeviceDataComponent`, `CUXPCCodable`, `NSSecureCoding`, `NSCopying`
- 5 instance variables, 9 properties, 22 instance methods, 1 class methods

## Instance variables

```
S _homeKitV2InstanceID;
S _homeKitV2StateNumber;
@"NSData" _homeKitV2AccessoryIDData;
@"NSData" _homeKitV2AuthTagData;
Q _homeKitV2Value;
```

## Properties

```
@property (T@"NSData",C,N,V_homeKitV2AccessoryIDData) homeKitV2AccessoryIDData;
@property (T@"NSData",C,N,V_homeKitV2AuthTagData) homeKitV2AuthTagData;
@property (TS,N,V_homeKitV2InstanceID) homeKitV2InstanceID;
@property (TS,N,V_homeKitV2StateNumber) homeKitV2StateNumber;
@property (TQ,N,V_homeKitV2Value) homeKitV2Value;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBDeviceHomeKitV2Data supportsSecureCoding];
```

## Instance methods

```
-[CBDeviceHomeKitV2Data memoryFootprint];
-[CBDeviceHomeKitV2Data encodeWithXPCObject:];
-[CBDeviceHomeKitV2Data initWithDictionary:error:];
-[CBDeviceHomeKitV2Data clear];
-[CBDeviceHomeKitV2Data initWithXPCObject:error:];
-[CBDeviceHomeKitV2Data descriptionWithLevel:];
-[CBDeviceHomeKitV2Data encodeWithCoder:];
-[CBDeviceHomeKitV2Data description];
-[CBDeviceHomeKitV2Data initWithCoder:];
-[CBDeviceHomeKitV2Data hasAnyData];
-[CBDeviceHomeKitV2Data copyWithZone:];
-[CBDeviceHomeKitV2Data dictionaryRepresentation];
-[CBDeviceHomeKitV2Data homeKitV2AccessoryIDData];
-[CBDeviceHomeKitV2Data homeKitV2AuthTagData];
-[CBDeviceHomeKitV2Data homeKitV2InstanceID];
-[CBDeviceHomeKitV2Data homeKitV2StateNumber];
-[CBDeviceHomeKitV2Data homeKitV2Value];
-[CBDeviceHomeKitV2Data setHomeKitV2AccessoryIDData:];
-[CBDeviceHomeKitV2Data setHomeKitV2AuthTagData:];
-[CBDeviceHomeKitV2Data setHomeKitV2InstanceID:];
-[CBDeviceHomeKitV2Data setHomeKitV2StateNumber:];
-[CBDeviceHomeKitV2Data setHomeKitV2Value:];
```
