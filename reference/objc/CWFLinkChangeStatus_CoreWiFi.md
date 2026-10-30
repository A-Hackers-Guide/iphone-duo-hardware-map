# `CWFLinkChangeStatus`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 10 instance variables, 10 properties, 27 instance methods, 1 class methods

## Instance variables

```
B _linkDown;
B _linkDownDebounceInProgress;
B _involuntaryLinkDown;
i _reason;
@"NSDate" _timestamp;
@"NSString" _interfaceName;
q _subreason;
q _RSSI;
q _noise;
Q _CCA;
```

## Properties

```
@property (T@"NSDate",C,N,V_timestamp) timestamp;
@property (T@"NSString",C,N,V_interfaceName) interfaceName;
@property (TB,N,GisLinkDown,V_linkDown) linkDown;
@property (TB,N,GisLinkDownDebounceInProgress,V_linkDownDebounceInProgress) linkDownDebounceInProgress;
@property (TB,N,GisInvoluntaryLinkDown,V_involuntaryLinkDown) involuntaryLinkDown;
@property (Ti,N,V_reason) reason;
@property (Tq,N,V_subreason) subreason;
@property (Tq,N,V_RSSI) RSSI;
@property (Tq,N,V_noise) noise;
@property (TQ,N,V_CCA) CCA;
```

## Class methods

```
+[CWFLinkChangeStatus supportsSecureCoding];
```

## Instance methods

```
-[CWFLinkChangeStatus setNoise:];
-[CWFLinkChangeStatus setCCA:];
-[CWFLinkChangeStatus setTimestamp:];
-[CWFLinkChangeStatus CCA];
-[CWFLinkChangeStatus noise];
-[CWFLinkChangeStatus setRSSI:];
-[CWFLinkChangeStatus RSSI];
-[CWFLinkChangeStatus setInterfaceName:];
-[CWFLinkChangeStatus timestamp];
-[CWFLinkChangeStatus interfaceName];
-[CWFLinkChangeStatus setReason:];
-[CWFLinkChangeStatus isInvoluntaryLinkDown];
-[CWFLinkChangeStatus setLinkDownDebounceInProgress:];
-[CWFLinkChangeStatus setInvoluntaryLinkDown:];
-[CWFLinkChangeStatus setLinkDown:];
-[CWFLinkChangeStatus isLinkDown];
-[CWFLinkChangeStatus encodeWithCoder:];
-[CWFLinkChangeStatus hash];
-[CWFLinkChangeStatus description];
-[CWFLinkChangeStatus initWithCoder:];
-[CWFLinkChangeStatus reason];
-[CWFLinkChangeStatus copyWithZone:];
-[CWFLinkChangeStatus isEqual:];
-[CWFLinkChangeStatus isEqualToLinkChangeStatus:];
-[CWFLinkChangeStatus isLinkDownDebounceInProgress];
-[CWFLinkChangeStatus setSubreason:];
-[CWFLinkChangeStatus subreason];
```
