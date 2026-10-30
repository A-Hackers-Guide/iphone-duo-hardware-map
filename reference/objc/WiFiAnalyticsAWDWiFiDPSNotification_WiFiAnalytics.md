# `WiFiAnalyticsAWDWiFiDPSNotification`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 12 instance variables, 22 properties, 55 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
I _cca;
I _problemAC;
i _symptom;
I _txBETrId;
I _txBKTrId;
I _txVITrId;
I _txVOTrId;
B _activeRTGTraffic;
B _facetimeCallInProgress;
B _isNANEnabled;
{?="timestamp"b1"cca"b1"problemAC"b1"symptom"b1"txBETrId"b1"txBKTrId"b1"txVITrId"b1"txVOTrId"b1"activeRTGTraffic"b1"facetimeCallInProgress"b1"isNANEnabled"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasSymptom;
@property (Ti,N,V_symptom) symptom;
@property (TB,N) hasProblemAC;
@property (TI,N,V_problemAC) problemAC;
@property (TB,N) hasFacetimeCallInProgress;
@property (TB,N,V_facetimeCallInProgress) facetimeCallInProgress;
@property (TB,N) hasCca;
@property (TI,N,V_cca) cca;
@property (TB,N) hasTxBETrId;
@property (TI,N,V_txBETrId) txBETrId;
@property (TB,N) hasTxBKTrId;
@property (TI,N,V_txBKTrId) txBKTrId;
@property (TB,N) hasTxVITrId;
@property (TI,N,V_txVITrId) txVITrId;
@property (TB,N) hasTxVOTrId;
@property (TI,N,V_txVOTrId) txVOTrId;
@property (TB,N) hasIsNANEnabled;
@property (TB,N,V_isNANEnabled) isNANEnabled;
@property (TB,N) hasActiveRTGTraffic;
@property (TB,N,V_activeRTGTraffic) activeRTGTraffic;
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiDPSNotification cca];
-[WiFiAnalyticsAWDWiFiDPSNotification hasTimestamp];
-[WiFiAnalyticsAWDWiFiDPSNotification setHasTimestamp:];
-[WiFiAnalyticsAWDWiFiDPSNotification setTimestamp:];
-[WiFiAnalyticsAWDWiFiDPSNotification writeTo:];
-[WiFiAnalyticsAWDWiFiDPSNotification mergeFrom:];
-[WiFiAnalyticsAWDWiFiDPSNotification setCca:];
-[WiFiAnalyticsAWDWiFiDPSNotification timestamp];
-[WiFiAnalyticsAWDWiFiDPSNotification hash];
-[WiFiAnalyticsAWDWiFiDPSNotification copyTo:];
-[WiFiAnalyticsAWDWiFiDPSNotification description];
-[WiFiAnalyticsAWDWiFiDPSNotification readFrom:];
-[WiFiAnalyticsAWDWiFiDPSNotification copyWithZone:];
-[WiFiAnalyticsAWDWiFiDPSNotification isEqual:];
-[WiFiAnalyticsAWDWiFiDPSNotification dictionaryRepresentation];
-[WiFiAnalyticsAWDWiFiDPSNotification hasCca];
-[WiFiAnalyticsAWDWiFiDPSNotification setHasCca:];
-[WiFiAnalyticsAWDWiFiDPSNotification symptom];
-[WiFiAnalyticsAWDWiFiDPSNotification setSymptom:];
-[WiFiAnalyticsAWDWiFiDPSNotification hasIsNANEnabled];
-[WiFiAnalyticsAWDWiFiDPSNotification setHasTxBKTrId:];
-[WiFiAnalyticsAWDWiFiDPSNotification setHasTxVITrId:];
-[WiFiAnalyticsAWDWiFiDPSNotification StringAsSymptom:];
-[WiFiAnalyticsAWDWiFiDPSNotification setHasTxBETrId:];
-[WiFiAnalyticsAWDWiFiDPSNotification setHasTxVOTrId:];
-[WiFiAnalyticsAWDWiFiDPSNotification activeRTGTraffic];
-[WiFiAnalyticsAWDWiFiDPSNotification facetimeCallInProgress];
-[WiFiAnalyticsAWDWiFiDPSNotification hasActiveRTGTraffic];
-[WiFiAnalyticsAWDWiFiDPSNotification hasFacetimeCallInProgress];
-[WiFiAnalyticsAWDWiFiDPSNotification hasProblemAC];
-[WiFiAnalyticsAWDWiFiDPSNotification hasSymptom];
-[WiFiAnalyticsAWDWiFiDPSNotification hasTxBETrId];
-[WiFiAnalyticsAWDWiFiDPSNotification hasTxBKTrId];
-[WiFiAnalyticsAWDWiFiDPSNotification hasTxVITrId];
-[WiFiAnalyticsAWDWiFiDPSNotification hasTxVOTrId];
-[WiFiAnalyticsAWDWiFiDPSNotification isNANEnabled];
-[WiFiAnalyticsAWDWiFiDPSNotification problemAC];
-[WiFiAnalyticsAWDWiFiDPSNotification setActiveRTGTraffic:];
-[WiFiAnalyticsAWDWiFiDPSNotification setFacetimeCallInProgress:];
-[WiFiAnalyticsAWDWiFiDPSNotification setHasActiveRTGTraffic:];
-[WiFiAnalyticsAWDWiFiDPSNotification setHasFacetimeCallInProgress:];
-[WiFiAnalyticsAWDWiFiDPSNotification setHasIsNANEnabled:];
-[WiFiAnalyticsAWDWiFiDPSNotification setHasProblemAC:];
-[WiFiAnalyticsAWDWiFiDPSNotification setHasSymptom:];
-[WiFiAnalyticsAWDWiFiDPSNotification setIsNANEnabled:];
-[WiFiAnalyticsAWDWiFiDPSNotification setProblemAC:];
-[WiFiAnalyticsAWDWiFiDPSNotification setTxBETrId:];
-[WiFiAnalyticsAWDWiFiDPSNotification setTxBKTrId:];
-[WiFiAnalyticsAWDWiFiDPSNotification setTxVITrId:];
-[WiFiAnalyticsAWDWiFiDPSNotification setTxVOTrId:];
-[WiFiAnalyticsAWDWiFiDPSNotification symptomAsString:];
-[WiFiAnalyticsAWDWiFiDPSNotification txBETrId];
-[WiFiAnalyticsAWDWiFiDPSNotification txBKTrId];
-[WiFiAnalyticsAWDWiFiDPSNotification txVITrId];
-[WiFiAnalyticsAWDWiFiDPSNotification txVOTrId];
```
