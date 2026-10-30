# `WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 13 instance variables, 26 properties, 88 instance methods, 0 class methods

## Instance variables

```
{?="list"^Q"count"Q"size"Q} _ampduAGGs;
{?="list"^Q"count"Q"size"Q} _rxHESuccess;
{?="list"^Q"count"Q"size"Q} _rxMCSSuccess;
{?="list"^Q"count"Q"size"Q} _rxVHTSuccess;
{?="list"^Q"count"Q"size"Q} _rxampduMUMIMOs;
{?="list"^Q"count"Q"size"Q} _rxampduOFDMAs;
{?="list"^Q"count"Q"size"Q} _rxampduSUs;
{?="list"^Q"count"Q"size"Q} _txHESuccess;
{?="list"^Q"count"Q"size"Q} _txMCSSuccess;
{?="list"^Q"count"Q"size"Q} _txVHTSuccess;
{?="list"^Q"count"Q"size"Q} _txampduMUMIMOs;
{?="list"^Q"count"Q"size"Q} _txampduOFDMAs;
{?="list"^Q"count"Q"size"Q} _txampduSUs;
```

## Properties

```
@property (TQ,R,N) rxVHTSuccessCount;
@property (T^Q,R,N) rxVHTSuccess;
@property (TQ,R,N) txVHTSuccessCount;
@property (T^Q,R,N) txVHTSuccess;
@property (TQ,R,N) rxMCSSuccessCount;
@property (T^Q,R,N) rxMCSSuccess;
@property (TQ,R,N) txMCSSuccessCount;
@property (T^Q,R,N) txMCSSuccess;
@property (TQ,R,N) ampduAGGsCount;
@property (T^Q,R,N) ampduAGGs;
@property (TQ,R,N) rxHESuccessCount;
@property (T^Q,R,N) rxHESuccess;
@property (TQ,R,N) txHESuccessCount;
@property (T^Q,R,N) txHESuccess;
@property (TQ,R,N) rxampduSUsCount;
@property (T^Q,R,N) rxampduSUs;
@property (TQ,R,N) txampduSUsCount;
@property (T^Q,R,N) txampduSUs;
@property (TQ,R,N) rxampduOFDMAsCount;
@property (T^Q,R,N) rxampduOFDMAs;
@property (TQ,R,N) txampduOFDMAsCount;
@property (T^Q,R,N) txampduOFDMAs;
@property (TQ,R,N) rxampduMUMIMOsCount;
@property (T^Q,R,N) rxampduMUMIMOs;
@property (TQ,R,N) txampduMUMIMOsCount;
@property (T^Q,R,N) txampduMUMIMOs;
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation writeTo:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation mergeFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation dealloc];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation hash];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation copyTo:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation description];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation readFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation copyWithZone:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation isEqual:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation dictionaryRepresentation];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation addRxHESuccess:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation addTxHESuccess:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation clearTxampduSUs];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation rxampduSUsCount];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation txampduSUsCount];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation clearRxampduSUs];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation addAmpduAGG:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation addRxMCSSuccess:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation addRxVHTSuccess:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation addRxampduMUMIMO:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation addRxampduOFDMA:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation addRxampduSU:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation addTxMCSSuccess:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation addTxVHTSuccess:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation addTxampduMUMIMO:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation addTxampduOFDMA:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation addTxampduSU:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation ampduAGGAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation ampduAGGs];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation ampduAGGsCount];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation clearAmpduAGGs];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation clearRxHESuccess];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation clearRxMCSSuccess];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation clearRxVHTSuccess];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation clearRxampduMUMIMOs];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation clearRxampduOFDMAs];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation clearTxHESuccess];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation clearTxMCSSuccess];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation clearTxVHTSuccess];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation clearTxampduMUMIMOs];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation clearTxampduOFDMAs];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation rxHESuccess];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation rxHESuccessAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation rxHESuccessCount];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation rxMCSSuccess];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation rxMCSSuccessAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation rxMCSSuccessCount];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation rxVHTSuccess];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation rxVHTSuccessAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation rxVHTSuccessCount];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation rxampduMUMIMOAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation rxampduMUMIMOs];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation rxampduMUMIMOsCount];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation rxampduOFDMAAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation rxampduOFDMAs];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation rxampduOFDMAsCount];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation rxampduSUAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation rxampduSUs];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation setAmpduAGGs:count:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation setRxHESuccess:count:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation setRxMCSSuccess:count:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation setRxVHTSuccess:count:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation setRxampduMUMIMOs:count:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation setRxampduOFDMAs:count:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation setRxampduSUs:count:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation setTxHESuccess:count:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation setTxMCSSuccess:count:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation setTxVHTSuccess:count:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation setTxampduMUMIMOs:count:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation setTxampduOFDMAs:count:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation setTxampduSUs:count:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation txHESuccess];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation txHESuccessAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation txHESuccessCount];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation txMCSSuccess];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation txMCSSuccessAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation txMCSSuccessCount];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation txVHTSuccess];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation txVHTSuccessAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation txVHTSuccessCount];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation txampduMUMIMOAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation txampduMUMIMOs];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation txampduMUMIMOsCount];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation txampduOFDMAAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation txampduOFDMAs];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation txampduOFDMAsCount];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation txampduSUAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation txampduSUs];
```
