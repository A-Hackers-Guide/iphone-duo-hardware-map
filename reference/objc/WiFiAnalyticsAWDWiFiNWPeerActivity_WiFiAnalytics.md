# `WiFiAnalyticsAWDWiFiNWPeerActivity`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 3 instance variables, 3 properties, 19 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
@"NSMutableArray" _peerStats;
{?="timestamp"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (T@"NSMutableArray",&,N,V_peerStats) peerStats;
```

## Class methods

```
+[WiFiAnalyticsAWDWiFiNWPeerActivity peerStatsType];
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiNWPeerActivity setPeerStats:];
-[WiFiAnalyticsAWDWiFiNWPeerActivity hasTimestamp];
-[WiFiAnalyticsAWDWiFiNWPeerActivity setHasTimestamp:];
-[WiFiAnalyticsAWDWiFiNWPeerActivity peerStatsAtIndex:];
-[WiFiAnalyticsAWDWiFiNWPeerActivity setTimestamp:];
-[WiFiAnalyticsAWDWiFiNWPeerActivity writeTo:];
-[WiFiAnalyticsAWDWiFiNWPeerActivity mergeFrom:];
-[WiFiAnalyticsAWDWiFiNWPeerActivity timestamp];
-[WiFiAnalyticsAWDWiFiNWPeerActivity clearPeerStats];
-[WiFiAnalyticsAWDWiFiNWPeerActivity addPeerStats:];
-[WiFiAnalyticsAWDWiFiNWPeerActivity hash];
-[WiFiAnalyticsAWDWiFiNWPeerActivity copyTo:];
-[WiFiAnalyticsAWDWiFiNWPeerActivity description];
-[WiFiAnalyticsAWDWiFiNWPeerActivity peerStatsCount];
-[WiFiAnalyticsAWDWiFiNWPeerActivity readFrom:];
-[WiFiAnalyticsAWDWiFiNWPeerActivity copyWithZone:];
-[WiFiAnalyticsAWDWiFiNWPeerActivity isEqual:];
-[WiFiAnalyticsAWDWiFiNWPeerActivity peerStats];
-[WiFiAnalyticsAWDWiFiNWPeerActivity dictionaryRepresentation];
```
