# `SADevice`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OSLogCoding`, `TAEventProtocol`
- 13 instance variables, 18 properties, 30 instance methods, 1 class methods

## Instance variables

```
B _notifyEnabled;
B _isAppleAudioAccessory;
@"NSUUID" _identifier;
@"NSUUID" _groupIdentifier;
@"NSString" _macAddress;
q _partIdentifier;
@"NSString" _name;
@"NSString" _model;
@"NSString" _systemVersion;
q _vendorId;
q _productId;
Q _deviceType;
@"NSDate" _date;
```

## Properties

```
@property (T@"NSUUID",R,C,N,V_identifier) identifier;
@property (T@"NSUUID",R,C,N,V_groupIdentifier) groupIdentifier;
@property (T@"NSString",&,N,V_macAddress) macAddress;
@property (Tq,R,N,V_partIdentifier) partIdentifier;
@property (T@"NSString",R,C,N,V_name) name;
@property (T@"NSString",R,C,N,V_model) model;
@property (T@"NSString",R,C,N,V_systemVersion) systemVersion;
@property (Tq,R,N,V_vendorId) vendorId;
@property (Tq,R,N,V_productId) productId;
@property (TQ,R,N,V_deviceType) deviceType;
@property (TB,R,N,V_notifyEnabled) notifyEnabled;
@property (T@"NSDate",R,C,N,V_date) date;
@property (TB,R,N,V_isAppleAudioAccessory) isAppleAudioAccessory;
@property (T@"NSString",R,C,N) descriptiveName;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SADevice supportsSecureCoding];
```

## Instance methods

```
-[SADevice model];
-[SADevice productId];
-[SADevice vendorId];
-[SADevice systemVersion];
-[SADevice groupIdentifier];
-[SADevice macAddress];
-[SADevice identifier];
-[SADevice deviceType];
-[SADevice setMacAddress:];
-[SADevice date];
-[SADevice getDate];
-[SADevice descriptionDictionary];
-[SADevice encodeWithCoder:];
-[SADevice description];
-[SADevice initWithCoder:];
-[SADevice copyWithZone:];
-[SADevice isEqual:];
-[SADevice name];
-[SADevice encodeWithOSLogCoder:options:maxLength:];
-[SADevice isAppleAudioAccessory];
-[SADevice partIdentifier];
-[SADevice notifyEnabled];
-[SADevice descriptiveName];
-[SADevice initWithDeviceUUID:groupIdentifier:macAddress:name:model:systemVersion:vendorId:productId:deviceType:notifyEnabled:isAppleAudioAccessory:date:];
-[SADevice initWithDeviceUUID:groupIdentifier:macAddress:partIdentifier:name:model:systemVersion:vendorId:productId:deviceType:notifyEnabled:isAppleAudioAccessory:date:];
-[SADevice initWithDeviceUUID:name:model:systemVersion:vendorId:productId:deviceType:notifyEnabled:isAppleAudioAccessory:date:];
-[SADevice isAirPodsCase];
-[SADevice isBudForAirPodsBLECase];
-[SADevice isReallyEqual:];
-[SADevice isValidPartID];
```
