# `CWFAutoJoinRequest`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 6 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _allowAutoHotspotFallback;
B _throttled;
@"NSUUID" _UUID;
@"CWFAutoJoinParameters" _parameters;
@"NSDate" _addedAt;
@? _reply;
```

## Properties

```
@property (T@"NSUUID",C,N,V_UUID) UUID;
@property (T@"CWFAutoJoinParameters",C,N,V_parameters) parameters;
@property (TB,N,V_allowAutoHotspotFallback) allowAutoHotspotFallback;
@property (T@"NSDate",C,N,V_addedAt) addedAt;
@property (TB,N,V_throttled) throttled;
@property (T@?,C,N,V_reply) reply;
```

## Instance methods

```
-[CWFAutoJoinRequest parameters];
-[CWFAutoJoinRequest setThrottled:];
-[CWFAutoJoinRequest reply];
-[CWFAutoJoinRequest setAllowAutoHotspotFallback:];
-[CWFAutoJoinRequest setParameters:];
-[CWFAutoJoinRequest setUUID:];
-[CWFAutoJoinRequest UUID];
-[CWFAutoJoinRequest throttled];
-[CWFAutoJoinRequest setReply:];
-[CWFAutoJoinRequest allowAutoHotspotFallback];
-[CWFAutoJoinRequest addedAt];
-[CWFAutoJoinRequest description];
-[CWFAutoJoinRequest copyWithZone:];
-[CWFAutoJoinRequest setAddedAt:];
```
