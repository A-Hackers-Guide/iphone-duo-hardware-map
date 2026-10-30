# `WiFiAnalyticsAWDWiFiDPSNANSnapshot`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 10 properties, 29 instance methods, 0 class methods

## Instance variables

```
Q _ts;
I _duration;
I _nanInfraImpact;
I _sdb;
I _use;
{?="ts"b1"duration"b1"nanInfraImpact"b1"sdb"b1"use"b1} _has;
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
@property (TB,N) hasNanInfraImpact;
@property (TI,N,V_nanInfraImpact) nanInfraImpact;
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiDPSNANSnapshot writeTo:];
-[WiFiAnalyticsAWDWiFiDPSNANSnapshot mergeFrom:];
-[WiFiAnalyticsAWDWiFiDPSNANSnapshot hasDuration];
-[WiFiAnalyticsAWDWiFiDPSNANSnapshot duration];
-[WiFiAnalyticsAWDWiFiDPSNANSnapshot setHasDuration:];
-[WiFiAnalyticsAWDWiFiDPSNANSnapshot hash];
-[WiFiAnalyticsAWDWiFiDPSNANSnapshot copyTo:];
-[WiFiAnalyticsAWDWiFiDPSNANSnapshot description];
-[WiFiAnalyticsAWDWiFiDPSNANSnapshot setDuration:];
-[WiFiAnalyticsAWDWiFiDPSNANSnapshot readFrom:];
-[WiFiAnalyticsAWDWiFiDPSNANSnapshot copyWithZone:];
-[WiFiAnalyticsAWDWiFiDPSNANSnapshot isEqual:];
-[WiFiAnalyticsAWDWiFiDPSNANSnapshot dictionaryRepresentation];
-[WiFiAnalyticsAWDWiFiDPSNANSnapshot use];
-[WiFiAnalyticsAWDWiFiDPSNANSnapshot setUse:];
-[WiFiAnalyticsAWDWiFiDPSNANSnapshot setSdb:];
-[WiFiAnalyticsAWDWiFiDPSNANSnapshot sdb];
-[WiFiAnalyticsAWDWiFiDPSNANSnapshot hasNanInfraImpact];
-[WiFiAnalyticsAWDWiFiDPSNANSnapshot hasSdb];
-[WiFiAnalyticsAWDWiFiDPSNANSnapshot hasTs];
-[WiFiAnalyticsAWDWiFiDPSNANSnapshot hasUse];
-[WiFiAnalyticsAWDWiFiDPSNANSnapshot nanInfraImpact];
-[WiFiAnalyticsAWDWiFiDPSNANSnapshot setHasNanInfraImpact:];
-[WiFiAnalyticsAWDWiFiDPSNANSnapshot setHasSdb:];
-[WiFiAnalyticsAWDWiFiDPSNANSnapshot setHasTs:];
-[WiFiAnalyticsAWDWiFiDPSNANSnapshot setHasUse:];
-[WiFiAnalyticsAWDWiFiDPSNANSnapshot setNanInfraImpact:];
-[WiFiAnalyticsAWDWiFiDPSNANSnapshot setTs:];
-[WiFiAnalyticsAWDWiFiDPSNANSnapshot ts];
```
