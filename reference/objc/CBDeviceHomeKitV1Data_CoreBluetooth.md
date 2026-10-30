# `CBDeviceHomeKitV1Data`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBDeviceDataComponent`, `CUXPCCodable`, `NSSecureCoding`, `NSCopying`
- 7 instance variables, 11 properties, 26 instance methods, 1 class methods

## Instance variables

```
C _homeKitV1CompatibleVersion;
C _homeKitV1ConfigurationNumber;
C _homeKitV1Flags;
S _homeKitV1Category;
S _homeKitV1StateNumber;
I _homeKitV1SetupHash;
@"NSData" _homeKitV1DeviceIDData;
```

## Properties

```
@property (TS,N,V_homeKitV1Category) homeKitV1Category;
@property (TC,N,V_homeKitV1CompatibleVersion) homeKitV1CompatibleVersion;
@property (TC,N,V_homeKitV1ConfigurationNumber) homeKitV1ConfigurationNumber;
@property (T@"NSData",C,N,V_homeKitV1DeviceIDData) homeKitV1DeviceIDData;
@property (TC,N,V_homeKitV1Flags) homeKitV1Flags;
@property (TS,N,V_homeKitV1StateNumber) homeKitV1StateNumber;
@property (TI,N,V_homeKitV1SetupHash) homeKitV1SetupHash;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBDeviceHomeKitV1Data supportsSecureCoding];
```

## Instance methods

```
-[CBDeviceHomeKitV1Data memoryFootprint];
-[CBDeviceHomeKitV1Data encodeWithXPCObject:];
-[CBDeviceHomeKitV1Data initWithDictionary:error:];
-[CBDeviceHomeKitV1Data clear];
-[CBDeviceHomeKitV1Data initWithXPCObject:error:];
-[CBDeviceHomeKitV1Data descriptionWithLevel:];
-[CBDeviceHomeKitV1Data encodeWithCoder:];
-[CBDeviceHomeKitV1Data description];
-[CBDeviceHomeKitV1Data initWithCoder:];
-[CBDeviceHomeKitV1Data hasAnyData];
-[CBDeviceHomeKitV1Data copyWithZone:];
-[CBDeviceHomeKitV1Data dictionaryRepresentation];
-[CBDeviceHomeKitV1Data homeKitV1Category];
-[CBDeviceHomeKitV1Data homeKitV1CompatibleVersion];
-[CBDeviceHomeKitV1Data homeKitV1ConfigurationNumber];
-[CBDeviceHomeKitV1Data homeKitV1DeviceIDData];
-[CBDeviceHomeKitV1Data homeKitV1Flags];
-[CBDeviceHomeKitV1Data homeKitV1SetupHash];
-[CBDeviceHomeKitV1Data homeKitV1StateNumber];
-[CBDeviceHomeKitV1Data setHomeKitV1Category:];
-[CBDeviceHomeKitV1Data setHomeKitV1CompatibleVersion:];
-[CBDeviceHomeKitV1Data setHomeKitV1ConfigurationNumber:];
-[CBDeviceHomeKitV1Data setHomeKitV1DeviceIDData:];
-[CBDeviceHomeKitV1Data setHomeKitV1Flags:];
-[CBDeviceHomeKitV1Data setHomeKitV1SetupHash:];
-[CBDeviceHomeKitV1Data setHomeKitV1StateNumber:];
```
