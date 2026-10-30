# `WiFiAnalyticsAWDWiFiQualityScore`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 10 properties, 29 instance methods, 0 class methods

## Instance variables

```
I _channelQuality;
I _rxLatency;
I _rxLoss;
I _txLatency;
I _txLoss;
{?="channelQuality"b1"rxLatency"b1"rxLoss"b1"txLatency"b1"txLoss"b1} _has;
```

## Properties

```
@property (TB,N) hasChannelQuality;
@property (TI,N,V_channelQuality) channelQuality;
@property (TB,N) hasTxLoss;
@property (TI,N,V_txLoss) txLoss;
@property (TB,N) hasRxLoss;
@property (TI,N,V_rxLoss) rxLoss;
@property (TB,N) hasTxLatency;
@property (TI,N,V_txLatency) txLatency;
@property (TB,N) hasRxLatency;
@property (TI,N,V_rxLatency) rxLatency;
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiQualityScore writeTo:];
-[WiFiAnalyticsAWDWiFiQualityScore mergeFrom:];
-[WiFiAnalyticsAWDWiFiQualityScore hash];
-[WiFiAnalyticsAWDWiFiQualityScore copyTo:];
-[WiFiAnalyticsAWDWiFiQualityScore description];
-[WiFiAnalyticsAWDWiFiQualityScore readFrom:];
-[WiFiAnalyticsAWDWiFiQualityScore copyWithZone:];
-[WiFiAnalyticsAWDWiFiQualityScore isEqual:];
-[WiFiAnalyticsAWDWiFiQualityScore dictionaryRepresentation];
-[WiFiAnalyticsAWDWiFiQualityScore txLatency];
-[WiFiAnalyticsAWDWiFiQualityScore channelQuality];
-[WiFiAnalyticsAWDWiFiQualityScore hasChannelQuality];
-[WiFiAnalyticsAWDWiFiQualityScore hasRxLatency];
-[WiFiAnalyticsAWDWiFiQualityScore hasRxLoss];
-[WiFiAnalyticsAWDWiFiQualityScore hasTxLatency];
-[WiFiAnalyticsAWDWiFiQualityScore hasTxLoss];
-[WiFiAnalyticsAWDWiFiQualityScore rxLatency];
-[WiFiAnalyticsAWDWiFiQualityScore rxLoss];
-[WiFiAnalyticsAWDWiFiQualityScore setChannelQuality:];
-[WiFiAnalyticsAWDWiFiQualityScore setHasChannelQuality:];
-[WiFiAnalyticsAWDWiFiQualityScore setHasRxLatency:];
-[WiFiAnalyticsAWDWiFiQualityScore setHasRxLoss:];
-[WiFiAnalyticsAWDWiFiQualityScore setHasTxLatency:];
-[WiFiAnalyticsAWDWiFiQualityScore setHasTxLoss:];
-[WiFiAnalyticsAWDWiFiQualityScore setRxLatency:];
-[WiFiAnalyticsAWDWiFiQualityScore setRxLoss:];
-[WiFiAnalyticsAWDWiFiQualityScore setTxLatency:];
-[WiFiAnalyticsAWDWiFiQualityScore setTxLoss:];
-[WiFiAnalyticsAWDWiFiQualityScore txLoss];
```
