# `CWFAutoJoinStatus`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CWFJSONEncodable`, `NSCopying`, `NSSecureCoding`
- 8 instance variables, 13 properties, 27 instance methods, 1 class methods

## Instance variables

```
B _result;
@"NSUUID" _UUID;
@"NSString" _interfaceName;
@"NSDate" _startedAt;
@"NSDate" _endedAt;
@"NSArray" _joinAttempts;
q _trigger;
q _state;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSUUID",C,N,V_UUID) UUID;
@property (T@"NSString",C,N,V_interfaceName) interfaceName;
@property (T@"NSDate",C,N,V_startedAt) startedAt;
@property (T@"NSDate",C,N,V_endedAt) endedAt;
@property (Td,R) duration;
@property (T@"NSArray",C,N,V_joinAttempts) joinAttempts;
@property (Tq,N,V_trigger) trigger;
@property (Tq,N,V_state) state;
@property (TB,N,V_result) result;
```

## Class methods

```
+[CWFAutoJoinStatus supportsSecureCoding];
```

## Instance methods

```
-[CWFAutoJoinStatus trigger];
-[CWFAutoJoinStatus setResult:];
-[CWFAutoJoinStatus JSONCompatibleKeyValueMap];
-[CWFAutoJoinStatus setState:];
-[CWFAutoJoinStatus init];
-[CWFAutoJoinStatus setUUID:];
-[CWFAutoJoinStatus UUID];
-[CWFAutoJoinStatus setInterfaceName:];
-[CWFAutoJoinStatus interfaceName];
-[CWFAutoJoinStatus duration];
-[CWFAutoJoinStatus endedAt];
-[CWFAutoJoinStatus setEndedAt:];
-[CWFAutoJoinStatus result];
-[CWFAutoJoinStatus setStartedAt:];
-[CWFAutoJoinStatus encodeWithCoder:];
-[CWFAutoJoinStatus hash];
-[CWFAutoJoinStatus deepCopy];
-[CWFAutoJoinStatus description];
-[CWFAutoJoinStatus initWithCoder:];
-[CWFAutoJoinStatus copyWithZone:];
-[CWFAutoJoinStatus startedAt];
-[CWFAutoJoinStatus isEqual:];
-[CWFAutoJoinStatus setTrigger:];
-[CWFAutoJoinStatus state];
-[CWFAutoJoinStatus joinAttempts];
-[CWFAutoJoinStatus isEqualToAutoJoinStatus:];
-[CWFAutoJoinStatus setJoinAttempts:];
```
