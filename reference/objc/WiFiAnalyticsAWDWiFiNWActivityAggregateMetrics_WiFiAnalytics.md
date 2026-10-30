# `WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 25 instance variables, 48 properties, 105 instance methods, 0 class methods

## Instance variables

```
Q _kCtlTxCTS;
Q _kCtlTxRTS;
Q _kMACRxDataFrameMatchingRA;
Q _kMACRxDataFrameOtherRA;
Q _kMACRxUnicastCTStoMAC;
Q _kMACRxUnicastCTStoOther;
Q _kMACRxUnicastRTStoMAC;
Q _kMACRxUnicastRTStoOther;
Q _kRxBadFCS;
Q _kRxBadOther;
Q _kRxBadPLCP;
Q _kRxCRCGlitch;
Q _kRxDataErrors;
Q _kRxFrames;
Q _kRxGoodPLCP;
Q _kRxRetryBitSet;
Q _kTxFrames;
Q _kTxRetransmission;
Q _kdot11MultipleRetryCount;
Q _kdot11RTSFailureCount;
Q _kdot11RTSSuccessCount;
Q _kdot11RetryCount;
I _kMACRxControlFrameMatchingRA;
I _kMACRxControlFrameOtherRA;
{?="kCtlTxCTS"b1"kCtlTxRTS"b1"kMACRxDataFrameMatchingRA"b1"kMACRxDataFrameOtherRA"b1"kMACRxUnicastCTStoMAC"b1"kMACRxUnicastCTStoOther"b1"kMACRxUnicastRTStoMAC"b1"kMACRxUnicastRTStoOther"b1"kRxBadFCS"b1"kRxBadOther"b1"kRxBadPLCP"b1"kRxCRCGlitch"b1"kRxDataErrors"b1"kRxFrames"b1"kRxGoodPLCP"b1"kRxRetryBitSet"b1"kTxFrames"b1"kTxRetransmission"b1"kdot11MultipleRetryCount"b1"kdot11RTSFailureCount"b1"kdot11RTSSuccessCount"b1"kdot11RetryCount"b1"kMACRxControlFrameMatchingRA"b1"kMACRxControlFrameOtherRA"b1} _has;
```

## Properties

```
@property (TB,N) hasKRxDataErrors;
@property (TQ,N,V_kRxDataErrors) kRxDataErrors;
@property (TB,N) hasKRxFrames;
@property (TQ,N,V_kRxFrames) kRxFrames;
@property (TB,N) hasKRxRetryBitSet;
@property (TQ,N,V_kRxRetryBitSet) kRxRetryBitSet;
@property (TB,N) hasKMACRxDataFrameMatchingRA;
@property (TQ,N,V_kMACRxDataFrameMatchingRA) kMACRxDataFrameMatchingRA;
@property (TB,N) hasKMACRxDataFrameOtherRA;
@property (TQ,N,V_kMACRxDataFrameOtherRA) kMACRxDataFrameOtherRA;
@property (TB,N) hasKMACRxControlFrameMatchingRA;
@property (TI,N,V_kMACRxControlFrameMatchingRA) kMACRxControlFrameMatchingRA;
@property (TB,N) hasKMACRxControlFrameOtherRA;
@property (TI,N,V_kMACRxControlFrameOtherRA) kMACRxControlFrameOtherRA;
@property (TB,N) hasKRxGoodPLCP;
@property (TQ,N,V_kRxGoodPLCP) kRxGoodPLCP;
@property (TB,N) hasKRxBadPLCP;
@property (TQ,N,V_kRxBadPLCP) kRxBadPLCP;
@property (TB,N) hasKRxBadFCS;
@property (TQ,N,V_kRxBadFCS) kRxBadFCS;
@property (TB,N) hasKTxFrames;
@property (TQ,N,V_kTxFrames) kTxFrames;
@property (TB,N) hasKTxRetransmission;
@property (TQ,N,V_kTxRetransmission) kTxRetransmission;
@property (TB,N) hasKdot11RetryCount;
@property (TQ,N,V_kdot11RetryCount) kdot11RetryCount;
@property (TB,N) hasKdot11MultipleRetryCount;
@property (TQ,N,V_kdot11MultipleRetryCount) kdot11MultipleRetryCount;
@property (TB,N) hasKdot11RTSSuccessCount;
@property (TQ,N,V_kdot11RTSSuccessCount) kdot11RTSSuccessCount;
@property (TB,N) hasKdot11RTSFailureCount;
@property (TQ,N,V_kdot11RTSFailureCount) kdot11RTSFailureCount;
@property (TB,N) hasKCtlTxRTS;
@property (TQ,N,V_kCtlTxRTS) kCtlTxRTS;
@property (TB,N) hasKRxCRCGlitch;
@property (TQ,N,V_kRxCRCGlitch) kRxCRCGlitch;
@property (TB,N) hasKMACRxUnicastCTStoMAC;
@property (TQ,N,V_kMACRxUnicastCTStoMAC) kMACRxUnicastCTStoMAC;
@property (TB,N) hasKMACRxUnicastCTStoOther;
@property (TQ,N,V_kMACRxUnicastCTStoOther) kMACRxUnicastCTStoOther;
@property (TB,N) hasKMACRxUnicastRTStoMAC;
@property (TQ,N,V_kMACRxUnicastRTStoMAC) kMACRxUnicastRTStoMAC;
@property (TB,N) hasKMACRxUnicastRTStoOther;
@property (TQ,N,V_kMACRxUnicastRTStoOther) kMACRxUnicastRTStoOther;
@property (TB,N) hasKCtlTxCTS;
@property (TQ,N,V_kCtlTxCTS) kCtlTxCTS;
@property (TB,N) hasKRxBadOther;
@property (TQ,N,V_kRxBadOther) kRxBadOther;
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics kdot11MultipleRetryCount];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setKRxDataErrors:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setKRxFrames:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setHasKCtlTxCTS:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setHasKMACRxUnicastRTStoOther:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setKMACRxDataFrameOtherRA:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics writeTo:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setHasKdot11RTSSuccessCount:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics hasKMACRxUnicastCTStoMAC];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setKMACRxUnicastCTStoMAC:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setKCtlTxCTS:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics kMACRxUnicastRTStoOther];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics kdot11RTSSuccessCount];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics hasKMACRxUnicastCTStoOther];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics kRxCRCGlitch];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setKdot11RTSFailureCount:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics kTxRetransmission];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setHasKCtlTxRTS:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics mergeFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setHasKRxRetryBitSet:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setHasKTxRetransmission:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setHasKMACRxControlFrameMatchingRA:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics hasKCtlTxCTS];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics kMACRxDataFrameMatchingRA];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setHasKRxBadFCS:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setHasKMACRxUnicastRTStoMAC:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setKdot11MultipleRetryCount:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setKTxRetransmission:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setKMACRxControlFrameMatchingRA:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setHasKdot11RetryCount:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics kMACRxDataFrameOtherRA];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setKMACRxUnicastCTStoOther:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setKMACRxUnicastRTStoMAC:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics hasKMACRxControlFrameMatchingRA];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics kRxDataErrors];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setHasKRxDataErrors:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics hasKdot11RTSSuccessCount];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics hasKMACRxControlFrameOtherRA];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics kdot11RetryCount];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics hasKCtlTxRTS];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics hasKdot11RTSFailureCount];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics hasKMACRxDataFrameMatchingRA];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setHasKdot11RTSFailureCount:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setHasKMACRxDataFrameOtherRA:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics kRxBadFCS];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics kRxGoodPLCP];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics kMACRxControlFrameMatchingRA];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics kCtlTxCTS];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics hasKRxFrames];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setHasKRxBadOther:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics hasKRxRetryBitSet];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setKRxBadPLCP:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setHasKRxFrames:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setKRxRetryBitSet:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setHasKMACRxDataFrameMatchingRA:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setKRxBadOther:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics hasKMACRxDataFrameOtherRA];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setKMACRxUnicastRTStoOther:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics hash];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setKMACRxDataFrameMatchingRA:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics hasKRxCRCGlitch];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics hasKRxBadOther];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics copyTo:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics hasKMACRxUnicastRTStoOther];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics description];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setKCtlTxRTS:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics kTxFrames];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics kMACRxUnicastCTStoOther];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics kRxBadOther];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setKTxFrames:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setHasKRxBadPLCP:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics hasKTxFrames];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics kMACRxUnicastCTStoMAC];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setHasKMACRxControlFrameOtherRA:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setKRxBadFCS:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setHasKRxCRCGlitch:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics kMACRxControlFrameOtherRA];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics kRxBadPLCP];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics readFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setKdot11RTSSuccessCount:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics hasKRxBadPLCP];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setHasKdot11MultipleRetryCount:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics kRxRetryBitSet];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics hasKMACRxUnicastRTStoMAC];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics kMACRxUnicastRTStoMAC];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics copyWithZone:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics hasKTxRetransmission];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics kCtlTxRTS];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setKRxGoodPLCP:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics hasKRxBadFCS];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics isEqual:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setHasKMACRxUnicastCTStoOther:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics hasKdot11MultipleRetryCount];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setKRxCRCGlitch:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics hasKRxDataErrors];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics hasKRxGoodPLCP];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setKdot11RetryCount:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics hasKdot11RetryCount];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics kdot11RTSFailureCount];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setKMACRxControlFrameOtherRA:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setHasKMACRxUnicastCTStoMAC:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setHasKTxFrames:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics setHasKRxGoodPLCP:];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics kRxFrames];
-[WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics dictionaryRepresentation];
```
