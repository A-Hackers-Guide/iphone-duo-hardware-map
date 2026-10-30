# `CWFEvent`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 6 instance variables, 7 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"NSDate" _timestamp;
@"NSDictionary" _info;
@"NSUUID" _UUID;
@"CWFEventID" _eventID;
Q _acknowledgementTimeout;
@? _acknowledge;
```

## Properties

```
@property (T@"NSUUID",C,N,V_UUID) UUID;
@property (T@"CWFEventID",C,N,V_eventID) eventID;
@property (TQ,N,V_acknowledgementTimeout) acknowledgementTimeout;
@property (T@?,C,N,V_acknowledge) acknowledge;
@property (Tq,D,N) type;
@property (T@"NSDate",C,N,V_timestamp) timestamp;
@property (T@"NSDictionary",C,N,V_info) info;
```

## Instance methods

```
-[CWFEvent setTimestamp:];
-[CWFEvent JSONCompatibleKeyValueMap];
-[CWFEvent eventID];
-[CWFEvent info];
-[CWFEvent init];
-[CWFEvent setInfo:];
-[CWFEvent setUUID:];
-[CWFEvent UUID];
-[CWFEvent isEqualToEvent:];
-[CWFEvent timestamp];
-[CWFEvent acknowledgementTimeout];
-[CWFEvent setType:];
-[CWFEvent type];
-[CWFEvent hash];
-[CWFEvent description];
-[CWFEvent setAcknowledgementTimeout:];
-[CWFEvent setAcknowledge:];
-[CWFEvent setEventID:];
-[CWFEvent copyWithZone:];
-[CWFEvent isEqual:];
-[CWFEvent acknowledge];
```
