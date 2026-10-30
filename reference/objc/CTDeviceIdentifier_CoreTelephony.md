# `CTDeviceIdentifier`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 12 instance variables, 12 properties, 33 instance methods, 1 class methods

## Instance variables

```
@"NSString" _modelName;
@"NSString" _osVersion;
@"NSString" _deviceName;
Q _deviceType;
@"NSString" _EID;
@"NSString" _IMEI;
@"NSString" _IMEI1;
@"NSString" _IMEI2;
@"NSString" _NAL;
@"NSString" _idsDeviceId;
@"NSString" _bleDeviceId;
@"NSString" _serialNumber;
```

## Properties

```
@property (T@"NSString",&,N,V_deviceName) deviceName;
@property (TQ,N,V_deviceType) deviceType;
@property (T@"NSString",&,N,V_EID) EID;
@property (T@"NSString",&,N,V_IMEI) IMEI;
@property (T@"NSString",&,N,V_IMEI1) IMEI1;
@property (T@"NSString",&,N,V_IMEI2) IMEI2;
@property (T@"NSString",&,N,V_NAL) NAL;
@property (T@"NSString",&,N,V_idsDeviceId) idsDeviceId;
@property (T@"NSString",&,N,V_bleDeviceId) bleDeviceId;
@property (T@"NSString",&,N,V_serialNumber) serialNumber;
@property (T@"NSString",&,N,V_modelName) modelName;
@property (T@"NSString",&,N,V_osVersion) osVersion;
```

## Class methods

```
+[CTDeviceIdentifier supportsSecureCoding];
```

## Instance methods

```
-[CTDeviceIdentifier IMEI];
-[CTDeviceIdentifier setDeviceType:];
-[CTDeviceIdentifier setSerialNumber:];
-[CTDeviceIdentifier osVersion];
-[CTDeviceIdentifier setIMEI:];
-[CTDeviceIdentifier idsDeviceId];
-[CTDeviceIdentifier setOsVersion:];
-[CTDeviceIdentifier init];
-[CTDeviceIdentifier deviceType];
-[CTDeviceIdentifier serialNumber];
-[CTDeviceIdentifier setDeviceName:];
-[CTDeviceIdentifier setModelName:];
-[CTDeviceIdentifier encodeWithCoder:];
-[CTDeviceIdentifier description];
-[CTDeviceIdentifier initWithCoder:];
-[CTDeviceIdentifier isEqual:];
-[CTDeviceIdentifier deviceName];
-[CTDeviceIdentifier modelName];
-[CTDeviceIdentifier NAL];
-[CTDeviceIdentifier IMEI2];
-[CTDeviceIdentifier setBleDeviceId:];
-[CTDeviceIdentifier setIdsDeviceId:];
-[CTDeviceIdentifier EID];
-[CTDeviceIdentifier IMEI1];
-[CTDeviceIdentifier setEID:];
-[CTDeviceIdentifier setNAL:];
-[CTDeviceIdentifier bleDeviceId];
-[CTDeviceIdentifier initWithDeviceType:EID:IMEI:IMEI1:IMEI2:NAL:idsDeviceId:];
-[CTDeviceIdentifier initWithDeviceType:EID:IMEI:idsDeviceId:];
-[CTDeviceIdentifier isVinylCapable];
-[CTDeviceIdentifier setIMEI1:];
-[CTDeviceIdentifier setIMEI2:];
-[CTDeviceIdentifier toQRCodeString];
```
