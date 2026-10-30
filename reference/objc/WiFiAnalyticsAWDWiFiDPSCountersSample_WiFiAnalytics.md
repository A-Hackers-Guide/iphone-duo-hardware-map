# `WiFiAnalyticsAWDWiFiDPSCountersSample`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 4 instance variables, 6 properties, 19 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
@"WiFiAnalyticsAWDWiFiNWActivityControllerStats" _controllerStats;
@"WiFiAnalyticsAWDWiFiNWActivityPeerStats" _peerStats;
{?="timestamp"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,R,N) hasControllerStats;
@property (T@"WiFiAnalyticsAWDWiFiNWActivityControllerStats",&,N,V_controllerStats) controllerStats;
@property (TB,R,N) hasPeerStats;
@property (T@"WiFiAnalyticsAWDWiFiNWActivityPeerStats",&,N,V_peerStats) peerStats;
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiDPSCountersSample setPeerStats:];
-[WiFiAnalyticsAWDWiFiDPSCountersSample hasTimestamp];
-[WiFiAnalyticsAWDWiFiDPSCountersSample setHasTimestamp:];
-[WiFiAnalyticsAWDWiFiDPSCountersSample setTimestamp:];
-[WiFiAnalyticsAWDWiFiDPSCountersSample writeTo:];
-[WiFiAnalyticsAWDWiFiDPSCountersSample mergeFrom:];
-[WiFiAnalyticsAWDWiFiDPSCountersSample setControllerStats:];
-[WiFiAnalyticsAWDWiFiDPSCountersSample timestamp];
-[WiFiAnalyticsAWDWiFiDPSCountersSample hash];
-[WiFiAnalyticsAWDWiFiDPSCountersSample copyTo:];
-[WiFiAnalyticsAWDWiFiDPSCountersSample description];
-[WiFiAnalyticsAWDWiFiDPSCountersSample controllerStats];
-[WiFiAnalyticsAWDWiFiDPSCountersSample readFrom:];
-[WiFiAnalyticsAWDWiFiDPSCountersSample copyWithZone:];
-[WiFiAnalyticsAWDWiFiDPSCountersSample isEqual:];
-[WiFiAnalyticsAWDWiFiDPSCountersSample peerStats];
-[WiFiAnalyticsAWDWiFiDPSCountersSample hasControllerStats];
-[WiFiAnalyticsAWDWiFiDPSCountersSample dictionaryRepresentation];
-[WiFiAnalyticsAWDWiFiDPSCountersSample hasPeerStats];
```
