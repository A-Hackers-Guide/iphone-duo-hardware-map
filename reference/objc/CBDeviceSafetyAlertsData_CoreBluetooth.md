# `CBDeviceSafetyAlertsData`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBDeviceDataComponent`, `CUXPCCodable`, `NSSecureCoding`, `NSCopying`
- 9 instance variables, 13 properties, 30 instance methods, 1 class methods

## Instance variables

```
C _safetyAlertsVersion;
C _safetyAlertsSegmentSegmentNumber;
C _safetyAlertsSegmentSegmentsTotal;
@"NSData" _safetyAlertsAlertData;
@"NSData" _safetyAlertsAlertID;
@"NSData" _safetyAlertsSignature;
@"NSData" _safetyAlertsSegmentAlertData;
@"NSData" _safetyAlertsSegmentServiceData;
@"NSData" _safetyAlertsSegmentSignature;
```

## Properties

```
@property (T@"NSData",C,N,V_safetyAlertsAlertData) safetyAlertsAlertData;
@property (T@"NSData",C,N,V_safetyAlertsAlertID) safetyAlertsAlertID;
@property (T@"NSData",C,N,V_safetyAlertsSignature) safetyAlertsSignature;
@property (TC,N,V_safetyAlertsVersion) safetyAlertsVersion;
@property (T@"NSData",C,N,V_safetyAlertsSegmentAlertData) safetyAlertsSegmentAlertData;
@property (TC,N,V_safetyAlertsSegmentSegmentNumber) safetyAlertsSegmentSegmentNumber;
@property (TC,N,V_safetyAlertsSegmentSegmentsTotal) safetyAlertsSegmentSegmentsTotal;
@property (T@"NSData",C,N,V_safetyAlertsSegmentServiceData) safetyAlertsSegmentServiceData;
@property (T@"NSData",C,N,V_safetyAlertsSegmentSignature) safetyAlertsSegmentSignature;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBDeviceSafetyAlertsData supportsSecureCoding];
```

## Instance methods

```
-[CBDeviceSafetyAlertsData memoryFootprint];
-[CBDeviceSafetyAlertsData encodeWithXPCObject:];
-[CBDeviceSafetyAlertsData initWithDictionary:error:];
-[CBDeviceSafetyAlertsData clear];
-[CBDeviceSafetyAlertsData initWithXPCObject:error:];
-[CBDeviceSafetyAlertsData setSafetyAlertsAlertID:];
-[CBDeviceSafetyAlertsData setSafetyAlertsAlertData:];
-[CBDeviceSafetyAlertsData descriptionWithLevel:];
-[CBDeviceSafetyAlertsData safetyAlertsAlertData];
-[CBDeviceSafetyAlertsData safetyAlertsVersion];
-[CBDeviceSafetyAlertsData safetyAlertsSignature];
-[CBDeviceSafetyAlertsData encodeWithCoder:];
-[CBDeviceSafetyAlertsData description];
-[CBDeviceSafetyAlertsData initWithCoder:];
-[CBDeviceSafetyAlertsData hasAnyData];
-[CBDeviceSafetyAlertsData setSafetyAlertsSignature:];
-[CBDeviceSafetyAlertsData safetyAlertsAlertID];
-[CBDeviceSafetyAlertsData copyWithZone:];
-[CBDeviceSafetyAlertsData setSafetyAlertsVersion:];
-[CBDeviceSafetyAlertsData dictionaryRepresentation];
-[CBDeviceSafetyAlertsData safetyAlertsSegmentAlertData];
-[CBDeviceSafetyAlertsData safetyAlertsSegmentSegmentNumber];
-[CBDeviceSafetyAlertsData safetyAlertsSegmentSegmentsTotal];
-[CBDeviceSafetyAlertsData safetyAlertsSegmentServiceData];
-[CBDeviceSafetyAlertsData safetyAlertsSegmentSignature];
-[CBDeviceSafetyAlertsData setSafetyAlertsSegmentAlertData:];
-[CBDeviceSafetyAlertsData setSafetyAlertsSegmentSegmentNumber:];
-[CBDeviceSafetyAlertsData setSafetyAlertsSegmentSegmentsTotal:];
-[CBDeviceSafetyAlertsData setSafetyAlertsSegmentServiceData:];
-[CBDeviceSafetyAlertsData setSafetyAlertsSegmentSignature:];
```
