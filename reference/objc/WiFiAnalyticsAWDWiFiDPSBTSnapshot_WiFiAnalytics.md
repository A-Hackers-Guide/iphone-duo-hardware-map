# `WiFiAnalyticsAWDWiFiDPSBTSnapshot`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 4 instance variables, 6 properties, 21 instance methods, 0 class methods

## Instance variables

```
Q _ts;
I _duration;
I _use;
{?="ts"b1"duration"b1"use"b1} _has;
```

## Properties

```
@property (TB,N) hasTs;
@property (TQ,N,V_ts) ts;
@property (TB,N) hasDuration;
@property (TI,N,V_duration) duration;
@property (TB,N) hasUse;
@property (TI,N,V_use) use;
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiDPSBTSnapshot writeTo:];
-[WiFiAnalyticsAWDWiFiDPSBTSnapshot mergeFrom:];
-[WiFiAnalyticsAWDWiFiDPSBTSnapshot hasDuration];
-[WiFiAnalyticsAWDWiFiDPSBTSnapshot duration];
-[WiFiAnalyticsAWDWiFiDPSBTSnapshot setHasDuration:];
-[WiFiAnalyticsAWDWiFiDPSBTSnapshot hash];
-[WiFiAnalyticsAWDWiFiDPSBTSnapshot copyTo:];
-[WiFiAnalyticsAWDWiFiDPSBTSnapshot description];
-[WiFiAnalyticsAWDWiFiDPSBTSnapshot setDuration:];
-[WiFiAnalyticsAWDWiFiDPSBTSnapshot readFrom:];
-[WiFiAnalyticsAWDWiFiDPSBTSnapshot copyWithZone:];
-[WiFiAnalyticsAWDWiFiDPSBTSnapshot isEqual:];
-[WiFiAnalyticsAWDWiFiDPSBTSnapshot dictionaryRepresentation];
-[WiFiAnalyticsAWDWiFiDPSBTSnapshot use];
-[WiFiAnalyticsAWDWiFiDPSBTSnapshot setUse:];
-[WiFiAnalyticsAWDWiFiDPSBTSnapshot hasTs];
-[WiFiAnalyticsAWDWiFiDPSBTSnapshot hasUse];
-[WiFiAnalyticsAWDWiFiDPSBTSnapshot setHasTs:];
-[WiFiAnalyticsAWDWiFiDPSBTSnapshot setHasUse:];
-[WiFiAnalyticsAWDWiFiDPSBTSnapshot setTs:];
-[WiFiAnalyticsAWDWiFiDPSBTSnapshot ts];
```
