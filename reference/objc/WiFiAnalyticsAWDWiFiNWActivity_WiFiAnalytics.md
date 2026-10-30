# `WiFiAnalyticsAWDWiFiNWActivity`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 15 instance variables, 23 properties, 67 instance methods, 5 class methods

## Instance variables

```
Q _timestamp;
@"NSMutableArray" _activities;
@"WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats" _apIfStats;
@"NSString" _apProfile;
@"WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats" _awdlIfStats;
@"NSMutableArray" _btleConnections;
@"WiFiAnalyticsAWDWiFiNWActivityControllerStats" _controllerStats;
@"NSMutableArray" _interfaceStats;
@"WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats" _irIfStats;
@"WiFiAnalyticsAWDLinkQualityMeasurements" _linkQualSample;
@"WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats" _nanIfStats;
@"NSString" _oui;
@"NSMutableArray" _peerStats;
@"NSMutableArray" _scores;
{?="timestamp"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (T@"NSMutableArray",&,N,V_activities) activities;
@property (T@"NSMutableArray",&,N,V_interfaceStats) interfaceStats;
@property (T@"NSMutableArray",&,N,V_peerStats) peerStats;
@property (TB,R,N) hasControllerStats;
@property (T@"WiFiAnalyticsAWDWiFiNWActivityControllerStats",&,N,V_controllerStats) controllerStats;
@property (TB,R,N) hasLinkQualSample;
@property (T@"WiFiAnalyticsAWDLinkQualityMeasurements",&,N,V_linkQualSample) linkQualSample;
@property (T@"NSMutableArray",&,N,V_scores) scores;
@property (T@"NSMutableArray",&,N,V_btleConnections) btleConnections;
@property (TB,R,N) hasApProfile;
@property (T@"NSString",&,N,V_apProfile) apProfile;
@property (TB,R,N) hasAwdlIfStats;
@property (T@"WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats",&,N,V_awdlIfStats) awdlIfStats;
@property (TB,R,N) hasApIfStats;
@property (T@"WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats",&,N,V_apIfStats) apIfStats;
@property (TB,R,N) hasNanIfStats;
@property (T@"WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats",&,N,V_nanIfStats) nanIfStats;
@property (TB,R,N) hasIrIfStats;
@property (T@"WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats",&,N,V_irIfStats) irIfStats;
@property (TB,R,N) hasOui;
@property (T@"NSString",&,N,V_oui) oui;
```

## Class methods

```
+[WiFiAnalyticsAWDWiFiNWActivity scoreType];
+[WiFiAnalyticsAWDWiFiNWActivity activitiesType];
+[WiFiAnalyticsAWDWiFiNWActivity btleConnectionType];
+[WiFiAnalyticsAWDWiFiNWActivity interfaceStatsType];
+[WiFiAnalyticsAWDWiFiNWActivity peerStatsType];
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiNWActivity setPeerStats:];
-[WiFiAnalyticsAWDWiFiNWActivity activitiesCount];
-[WiFiAnalyticsAWDWiFiNWActivity hasTimestamp];
-[WiFiAnalyticsAWDWiFiNWActivity setHasTimestamp:];
-[WiFiAnalyticsAWDWiFiNWActivity peerStatsAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivity clearActivities];
-[WiFiAnalyticsAWDWiFiNWActivity activities];
-[WiFiAnalyticsAWDWiFiNWActivity setTimestamp:];
-[WiFiAnalyticsAWDWiFiNWActivity scoresCount];
-[WiFiAnalyticsAWDWiFiNWActivity addInterfaceStats:];
-[WiFiAnalyticsAWDWiFiNWActivity writeTo:];
-[WiFiAnalyticsAWDWiFiNWActivity btleConnectionsCount];
-[WiFiAnalyticsAWDWiFiNWActivity setIrIfStats:];
-[WiFiAnalyticsAWDWiFiNWActivity setApProfile:];
-[WiFiAnalyticsAWDWiFiNWActivity setLinkQualSample:];
-[WiFiAnalyticsAWDWiFiNWActivity linkQualSample];
-[WiFiAnalyticsAWDWiFiNWActivity scores];
-[WiFiAnalyticsAWDWiFiNWActivity mergeFrom:];
-[WiFiAnalyticsAWDWiFiNWActivity setControllerStats:];
-[WiFiAnalyticsAWDWiFiNWActivity apIfStats];
-[WiFiAnalyticsAWDWiFiNWActivity timestamp];
-[WiFiAnalyticsAWDWiFiNWActivity apProfile];
-[WiFiAnalyticsAWDWiFiNWActivity clearPeerStats];
-[WiFiAnalyticsAWDWiFiNWActivity nanIfStats];
-[WiFiAnalyticsAWDWiFiNWActivity setAwdlIfStats:];
-[WiFiAnalyticsAWDWiFiNWActivity hasAwdlIfStats];
-[WiFiAnalyticsAWDWiFiNWActivity setScores:];
-[WiFiAnalyticsAWDWiFiNWActivity hasApProfile];
-[WiFiAnalyticsAWDWiFiNWActivity addPeerStats:];
-[WiFiAnalyticsAWDWiFiNWActivity interfaceStatsCount];
-[WiFiAnalyticsAWDWiFiNWActivity interfaceStatsAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivity hasOui];
-[WiFiAnalyticsAWDWiFiNWActivity setOui:];
-[WiFiAnalyticsAWDWiFiNWActivity setBtleConnections:];
-[WiFiAnalyticsAWDWiFiNWActivity btleConnections];
-[WiFiAnalyticsAWDWiFiNWActivity activitiesAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivity addScore:];
-[WiFiAnalyticsAWDWiFiNWActivity btleConnectionAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivity hasApIfStats];
-[WiFiAnalyticsAWDWiFiNWActivity hash];
-[WiFiAnalyticsAWDWiFiNWActivity copyTo:];
-[WiFiAnalyticsAWDWiFiNWActivity setApIfStats:];
-[WiFiAnalyticsAWDWiFiNWActivity description];
-[WiFiAnalyticsAWDWiFiNWActivity controllerStats];
-[WiFiAnalyticsAWDWiFiNWActivity interfaceStats];
-[WiFiAnalyticsAWDWiFiNWActivity setActivities:];
-[WiFiAnalyticsAWDWiFiNWActivity hasNanIfStats];
-[WiFiAnalyticsAWDWiFiNWActivity hasIrIfStats];
-[WiFiAnalyticsAWDWiFiNWActivity setInterfaceStats:];
-[WiFiAnalyticsAWDWiFiNWActivity addBtleConnection:];
-[WiFiAnalyticsAWDWiFiNWActivity peerStatsCount];
-[WiFiAnalyticsAWDWiFiNWActivity readFrom:];
-[WiFiAnalyticsAWDWiFiNWActivity irIfStats];
-[WiFiAnalyticsAWDWiFiNWActivity copyWithZone:];
-[WiFiAnalyticsAWDWiFiNWActivity setNanIfStats:];
-[WiFiAnalyticsAWDWiFiNWActivity addActivities:];
-[WiFiAnalyticsAWDWiFiNWActivity scoreAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivity clearInterfaceStats];
-[WiFiAnalyticsAWDWiFiNWActivity isEqual:];
-[WiFiAnalyticsAWDWiFiNWActivity clearScores];
-[WiFiAnalyticsAWDWiFiNWActivity peerStats];
-[WiFiAnalyticsAWDWiFiNWActivity hasControllerStats];
-[WiFiAnalyticsAWDWiFiNWActivity awdlIfStats];
-[WiFiAnalyticsAWDWiFiNWActivity hasLinkQualSample];
-[WiFiAnalyticsAWDWiFiNWActivity oui];
-[WiFiAnalyticsAWDWiFiNWActivity clearBtleConnections];
-[WiFiAnalyticsAWDWiFiNWActivity dictionaryRepresentation];
```
