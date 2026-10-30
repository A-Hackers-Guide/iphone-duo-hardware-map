# `WiFiAnalyticsAWDWiFiRxDataStallStats`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 15 instance variables, 28 properties, 65 instance methods, 0 class methods

## Instance variables

```
Q _healthcheckFaults;
Q _healthcheckFaultsRtscts;
Q _rxMuPpdu;
Q _rxMuRts;
Q _rxTotalPpdu;
Q _srMuRtsNoUcast;
Q _srRtsCtsNoUcast;
Q _srStallInProgress;
Q _srTimNoUcast;
Q _srTxBlanking;
Q _stallAge;
Q _stallElapsedDur;
Q _txCtsNoUcast;
Q _txCtsRxUcast;
{?="healthcheckFaults"b1"healthcheckFaultsRtscts"b1"rxMuPpdu"b1"rxMuRts"b1"rxTotalPpdu"b1"srMuRtsNoUcast"b1"srRtsCtsNoUcast"b1"srStallInProgress"b1"srTimNoUcast"b1"srTxBlanking"b1"stallAge"b1"stallElapsedDur"b1"txCtsNoUcast"b1"txCtsRxUcast"b1} _has;
```

## Properties

```
@property (TB,N) hasHealthcheckFaults;
@property (TQ,N,V_healthcheckFaults) healthcheckFaults;
@property (TB,N) hasHealthcheckFaultsRtscts;
@property (TQ,N,V_healthcheckFaultsRtscts) healthcheckFaultsRtscts;
@property (TB,N) hasTxCtsNoUcast;
@property (TQ,N,V_txCtsNoUcast) txCtsNoUcast;
@property (TB,N) hasTxCtsRxUcast;
@property (TQ,N,V_txCtsRxUcast) txCtsRxUcast;
@property (TB,N) hasRxMuRts;
@property (TQ,N,V_rxMuRts) rxMuRts;
@property (TB,N) hasRxTotalPpdu;
@property (TQ,N,V_rxTotalPpdu) rxTotalPpdu;
@property (TB,N) hasRxMuPpdu;
@property (TQ,N,V_rxMuPpdu) rxMuPpdu;
@property (TB,N) hasStallAge;
@property (TQ,N,V_stallAge) stallAge;
@property (TB,N) hasStallElapsedDur;
@property (TQ,N,V_stallElapsedDur) stallElapsedDur;
@property (TB,N) hasSrStallInProgress;
@property (TQ,N,V_srStallInProgress) srStallInProgress;
@property (TB,N) hasSrTimNoUcast;
@property (TQ,N,V_srTimNoUcast) srTimNoUcast;
@property (TB,N) hasSrRtsCtsNoUcast;
@property (TQ,N,V_srRtsCtsNoUcast) srRtsCtsNoUcast;
@property (TB,N) hasSrMuRtsNoUcast;
@property (TQ,N,V_srMuRtsNoUcast) srMuRtsNoUcast;
@property (TB,N) hasSrTxBlanking;
@property (TQ,N,V_srTxBlanking) srTxBlanking;
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiRxDataStallStats setHasStallElapsedDur:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats setHasHealthcheckFaults:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats setSrTxBlanking:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats setHasSrMuRtsNoUcast:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats writeTo:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats hasRxMuPpdu];
-[WiFiAnalyticsAWDWiFiRxDataStallStats hasHealthcheckFaultsRtscts];
-[WiFiAnalyticsAWDWiFiRxDataStallStats setSrStallInProgress:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats stallElapsedDur];
-[WiFiAnalyticsAWDWiFiRxDataStallStats hasStallAge];
-[WiFiAnalyticsAWDWiFiRxDataStallStats setHasSrStallInProgress:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats setHasRxMuPpdu:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats mergeFrom:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats hasTxCtsRxUcast];
-[WiFiAnalyticsAWDWiFiRxDataStallStats hasSrTimNoUcast];
-[WiFiAnalyticsAWDWiFiRxDataStallStats hasSrMuRtsNoUcast];
-[WiFiAnalyticsAWDWiFiRxDataStallStats setHasSrTxBlanking:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats hasStallElapsedDur];
-[WiFiAnalyticsAWDWiFiRxDataStallStats hasSrTxBlanking];
-[WiFiAnalyticsAWDWiFiRxDataStallStats setSrTimNoUcast:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats setStallElapsedDur:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats setTxCtsNoUcast:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats srStallInProgress];
-[WiFiAnalyticsAWDWiFiRxDataStallStats setHasTxCtsNoUcast:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats hasRxMuRts];
-[WiFiAnalyticsAWDWiFiRxDataStallStats setHasRxMuRts:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats setRxMuRts:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats setHasSrTimNoUcast:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats setHasTxCtsRxUcast:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats setHealthcheckFaultsRtscts:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats hasRxTotalPpdu];
-[WiFiAnalyticsAWDWiFiRxDataStallStats setHasStallAge:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats setHealthcheckFaults:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats healthcheckFaults];
-[WiFiAnalyticsAWDWiFiRxDataStallStats setRxTotalPpdu:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats setSrRtsCtsNoUcast:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats rxMuPpdu];
-[WiFiAnalyticsAWDWiFiRxDataStallStats hash];
-[WiFiAnalyticsAWDWiFiRxDataStallStats setHasSrRtsCtsNoUcast:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats copyTo:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats srMuRtsNoUcast];
-[WiFiAnalyticsAWDWiFiRxDataStallStats txCtsNoUcast];
-[WiFiAnalyticsAWDWiFiRxDataStallStats description];
-[WiFiAnalyticsAWDWiFiRxDataStallStats setHasHealthcheckFaultsRtscts:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats healthcheckFaultsRtscts];
-[WiFiAnalyticsAWDWiFiRxDataStallStats setTxCtsRxUcast:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats hasHealthcheckFaults];
-[WiFiAnalyticsAWDWiFiRxDataStallStats readFrom:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats hasSrRtsCtsNoUcast];
-[WiFiAnalyticsAWDWiFiRxDataStallStats txCtsRxUcast];
-[WiFiAnalyticsAWDWiFiRxDataStallStats copyWithZone:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats rxMuRts];
-[WiFiAnalyticsAWDWiFiRxDataStallStats isEqual:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats hasTxCtsNoUcast];
-[WiFiAnalyticsAWDWiFiRxDataStallStats srRtsCtsNoUcast];
-[WiFiAnalyticsAWDWiFiRxDataStallStats rxTotalPpdu];
-[WiFiAnalyticsAWDWiFiRxDataStallStats setHasRxTotalPpdu:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats srTimNoUcast];
-[WiFiAnalyticsAWDWiFiRxDataStallStats srTxBlanking];
-[WiFiAnalyticsAWDWiFiRxDataStallStats stallAge];
-[WiFiAnalyticsAWDWiFiRxDataStallStats setSrMuRtsNoUcast:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats setRxMuPpdu:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats dictionaryRepresentation];
-[WiFiAnalyticsAWDWiFiRxDataStallStats setStallAge:];
-[WiFiAnalyticsAWDWiFiRxDataStallStats hasSrStallInProgress];
```
