# `WiFiAnalyticsAWDWiFiDPSAWDLSnapshot`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 8 properties, 25 instance methods, 0 class methods

## Instance variables

```
Q _ts;
I _duration;
I _sdb;
I _use;
{?="ts"b1"duration"b1"sdb"b1"use"b1} _has;
```

## Properties

```
@property (TB,N) hasTs;
@property (TQ,N,V_ts) ts;
@property (TB,N) hasDuration;
@property (TI,N,V_duration) duration;
@property (TB,N) hasUse;
@property (TI,N,V_use) use;
@property (TB,N) hasSdb;
@property (TI,N,V_sdb) sdb;
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiDPSAWDLSnapshot writeTo:];
-[WiFiAnalyticsAWDWiFiDPSAWDLSnapshot mergeFrom:];
-[WiFiAnalyticsAWDWiFiDPSAWDLSnapshot hasDuration];
-[WiFiAnalyticsAWDWiFiDPSAWDLSnapshot duration];
-[WiFiAnalyticsAWDWiFiDPSAWDLSnapshot setHasDuration:];
-[WiFiAnalyticsAWDWiFiDPSAWDLSnapshot hash];
-[WiFiAnalyticsAWDWiFiDPSAWDLSnapshot copyTo:];
-[WiFiAnalyticsAWDWiFiDPSAWDLSnapshot description];
-[WiFiAnalyticsAWDWiFiDPSAWDLSnapshot setDuration:];
-[WiFiAnalyticsAWDWiFiDPSAWDLSnapshot readFrom:];
-[WiFiAnalyticsAWDWiFiDPSAWDLSnapshot copyWithZone:];
-[WiFiAnalyticsAWDWiFiDPSAWDLSnapshot isEqual:];
-[WiFiAnalyticsAWDWiFiDPSAWDLSnapshot dictionaryRepresentation];
-[WiFiAnalyticsAWDWiFiDPSAWDLSnapshot use];
-[WiFiAnalyticsAWDWiFiDPSAWDLSnapshot setUse:];
-[WiFiAnalyticsAWDWiFiDPSAWDLSnapshot setSdb:];
-[WiFiAnalyticsAWDWiFiDPSAWDLSnapshot sdb];
-[WiFiAnalyticsAWDWiFiDPSAWDLSnapshot hasSdb];
-[WiFiAnalyticsAWDWiFiDPSAWDLSnapshot hasTs];
-[WiFiAnalyticsAWDWiFiDPSAWDLSnapshot hasUse];
-[WiFiAnalyticsAWDWiFiDPSAWDLSnapshot setHasSdb:];
-[WiFiAnalyticsAWDWiFiDPSAWDLSnapshot setHasTs:];
-[WiFiAnalyticsAWDWiFiDPSAWDLSnapshot setHasUse:];
-[WiFiAnalyticsAWDWiFiDPSAWDLSnapshot setTs:];
-[WiFiAnalyticsAWDWiFiDPSAWDLSnapshot ts];
```
