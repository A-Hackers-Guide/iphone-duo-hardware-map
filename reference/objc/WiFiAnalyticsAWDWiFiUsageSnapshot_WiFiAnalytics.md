# `WiFiAnalyticsAWDWiFiUsageSnapshot`

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
-[WiFiAnalyticsAWDWiFiUsageSnapshot writeTo:];
-[WiFiAnalyticsAWDWiFiUsageSnapshot mergeFrom:];
-[WiFiAnalyticsAWDWiFiUsageSnapshot hasDuration];
-[WiFiAnalyticsAWDWiFiUsageSnapshot duration];
-[WiFiAnalyticsAWDWiFiUsageSnapshot setHasDuration:];
-[WiFiAnalyticsAWDWiFiUsageSnapshot hash];
-[WiFiAnalyticsAWDWiFiUsageSnapshot copyTo:];
-[WiFiAnalyticsAWDWiFiUsageSnapshot description];
-[WiFiAnalyticsAWDWiFiUsageSnapshot setDuration:];
-[WiFiAnalyticsAWDWiFiUsageSnapshot readFrom:];
-[WiFiAnalyticsAWDWiFiUsageSnapshot copyWithZone:];
-[WiFiAnalyticsAWDWiFiUsageSnapshot isEqual:];
-[WiFiAnalyticsAWDWiFiUsageSnapshot dictionaryRepresentation];
-[WiFiAnalyticsAWDWiFiUsageSnapshot use];
-[WiFiAnalyticsAWDWiFiUsageSnapshot setUse:];
-[WiFiAnalyticsAWDWiFiUsageSnapshot hasTs];
-[WiFiAnalyticsAWDWiFiUsageSnapshot hasUse];
-[WiFiAnalyticsAWDWiFiUsageSnapshot setHasTs:];
-[WiFiAnalyticsAWDWiFiUsageSnapshot setHasUse:];
-[WiFiAnalyticsAWDWiFiUsageSnapshot setTs:];
-[WiFiAnalyticsAWDWiFiUsageSnapshot ts];
```
