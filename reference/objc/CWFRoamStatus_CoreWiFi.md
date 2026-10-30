# `CWFRoamStatus`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CWFJSONEncodable`, `NSCopying`, `NSSecureCoding`
- 17 instance variables, 23 properties, 45 instance methods, 1 class methods

## Instance variables

```
i _reason;
i _status;
@"NSUUID" _UUID;
@"NSString" _interfaceName;
Q _timeStarted;
Q _timeEnded;
@"NSDate" _startedAt;
@"NSDate" _endedAt;
@"NSData" _SSID;
@"NSString" _originOUI;
@"NSString" _targetOUI;
@"NSString" _fromBSSID;
@"NSString" _toBSSID;
Q _fromChannel;
Q _toChannel;
q _fromRSSI;
q _toRSSI;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSUUID",C,N,V_UUID) UUID;
@property (T@"NSString",C,N,V_interfaceName) interfaceName;
@property (TQ,N,V_timeStarted) timeStarted;
@property (TQ,N,V_timeEnded) timeEnded;
@property (T@"NSDate",C,N,V_startedAt) startedAt;
@property (T@"NSDate",C,N,V_endedAt) endedAt;
@property (Td,R) duration;
@property (T@"NSData",C,N,V_SSID) SSID;
@property (T@"NSString",R,C,D,N) networkName;
@property (T@"NSString",C,N,V_originOUI) originOUI;
@property (T@"NSString",C,N,V_targetOUI) targetOUI;
@property (T@"NSString",C,N,V_fromBSSID) fromBSSID;
@property (T@"NSString",C,N,V_toBSSID) toBSSID;
@property (TQ,N,V_fromChannel) fromChannel;
@property (TQ,N,V_toChannel) toChannel;
@property (Tq,N,V_fromRSSI) fromRSSI;
@property (Tq,N,V_toRSSI) toRSSI;
@property (Ti,N,V_reason) reason;
@property (Ti,N,V_status) status;
```

## Class methods

```
+[CWFRoamStatus supportsSecureCoding];
```

## Instance methods

```
-[CWFRoamStatus networkName];
-[CWFRoamStatus setSSID:];
-[CWFRoamStatus SSID];
-[CWFRoamStatus JSONCompatibleKeyValueMap];
-[CWFRoamStatus init];
-[CWFRoamStatus setUUID:];
-[CWFRoamStatus UUID];
-[CWFRoamStatus setInterfaceName:];
-[CWFRoamStatus status];
-[CWFRoamStatus interfaceName];
-[CWFRoamStatus setReason:];
-[CWFRoamStatus duration];
-[CWFRoamStatus endedAt];
-[CWFRoamStatus setEndedAt:];
-[CWFRoamStatus setStartedAt:];
-[CWFRoamStatus encodeWithCoder:];
-[CWFRoamStatus hash];
-[CWFRoamStatus description];
-[CWFRoamStatus initWithCoder:];
-[CWFRoamStatus reason];
-[CWFRoamStatus setStatus:];
-[CWFRoamStatus copyWithZone:];
-[CWFRoamStatus startedAt];
-[CWFRoamStatus isEqual:];
-[CWFRoamStatus setFromChannel:];
-[CWFRoamStatus setTimeStarted:];
-[CWFRoamStatus toBSSID];
-[CWFRoamStatus fromBSSID];
-[CWFRoamStatus fromChannel];
-[CWFRoamStatus fromRSSI];
-[CWFRoamStatus isEqualToRoamStatus:];
-[CWFRoamStatus originOUI];
-[CWFRoamStatus setFromBSSID:];
-[CWFRoamStatus setFromRSSI:];
-[CWFRoamStatus setOriginOUI:];
-[CWFRoamStatus setTargetOUI:];
-[CWFRoamStatus setTimeEnded:];
-[CWFRoamStatus setToBSSID:];
-[CWFRoamStatus setToChannel:];
-[CWFRoamStatus setToRSSI:];
-[CWFRoamStatus targetOUI];
-[CWFRoamStatus timeEnded];
-[CWFRoamStatus timeStarted];
-[CWFRoamStatus toChannel];
-[CWFRoamStatus toRSSI];
```
