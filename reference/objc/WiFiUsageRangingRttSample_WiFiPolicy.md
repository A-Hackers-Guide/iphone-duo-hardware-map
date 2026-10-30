# `WiFiUsageRangingRttSample`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 12 properties, 24 instance methods, 0 class methods

## Instance variables

```
q _rssi;
q _rtt;
Q _flags;
Q _channel;
Q _selfSnr;
Q _selfCoreId;
Q _selfBitErrorRate;
Q _selfPhyError;
Q _peerSnr;
Q _peerCoreId;
Q _peerBitErrorRate;
Q _peerPhyError;
```

## Properties

```
@property (Tq,N,V_rssi) rssi;
@property (Tq,N,V_rtt) rtt;
@property (TQ,N,V_flags) flags;
@property (TQ,N,V_channel) channel;
@property (TQ,N,V_selfSnr) selfSnr;
@property (TQ,N,V_selfCoreId) selfCoreId;
@property (TQ,N,V_selfBitErrorRate) selfBitErrorRate;
@property (TQ,N,V_selfPhyError) selfPhyError;
@property (TQ,N,V_peerSnr) peerSnr;
@property (TQ,N,V_peerCoreId) peerCoreId;
@property (TQ,N,V_peerBitErrorRate) peerBitErrorRate;
@property (TQ,N,V_peerPhyError) peerPhyError;
```

## Instance methods

```
-[WiFiUsageRangingRttSample rssi];
-[WiFiUsageRangingRttSample setChannel:];
-[WiFiUsageRangingRttSample channel];
-[WiFiUsageRangingRttSample setFlags:];
-[WiFiUsageRangingRttSample flags];
-[WiFiUsageRangingRttSample setRssi:];
-[WiFiUsageRangingRttSample rtt];
-[WiFiUsageRangingRttSample peerSnr];
-[WiFiUsageRangingRttSample selfSnr];
-[WiFiUsageRangingRttSample setRtt:];
-[WiFiUsageRangingRttSample peerBitErrorRate];
-[WiFiUsageRangingRttSample peerCoreId];
-[WiFiUsageRangingRttSample peerPhyError];
-[WiFiUsageRangingRttSample selfBitErrorRate];
-[WiFiUsageRangingRttSample selfCoreId];
-[WiFiUsageRangingRttSample selfPhyError];
-[WiFiUsageRangingRttSample setPeerBitErrorRate:];
-[WiFiUsageRangingRttSample setPeerCoreId:];
-[WiFiUsageRangingRttSample setPeerPhyError:];
-[WiFiUsageRangingRttSample setPeerSnr:];
-[WiFiUsageRangingRttSample setSelfBitErrorRate:];
-[WiFiUsageRangingRttSample setSelfCoreId:];
-[WiFiUsageRangingRttSample setSelfPhyError:];
-[WiFiUsageRangingRttSample setSelfSnr:];
```
