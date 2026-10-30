# `WiFiAnalyticsAWDWiFiTDMSlice`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 13 instance variables, 24 properties, 57 instance methods, 0 class methods

## Instance variables

```
Q _txDeferDuration;
Q _txPriDuration;
Q _txaDuration;
I _ackTxPowerBackoffCount;
I _txDeferredCount;
I _txMuteCount;
I _txPathEnableReqCount;
I _txPathMuteCount;
I _txPriorityCount;
I _txaONCount;
I _txaPORCount;
I _txaTimeoutCount;
{?="txDeferDuration"b1"txPriDuration"b1"txaDuration"b1"ackTxPowerBackoffCount"b1"txDeferredCount"b1"txMuteCount"b1"txPathEnableReqCount"b1"txPathMuteCount"b1"txPriorityCount"b1"txaONCount"b1"txaPORCount"b1"txaTimeoutCount"b1} _has;
```

## Properties

```
@property (TB,N) hasTxaONCount;
@property (TI,N,V_txaONCount) txaONCount;
@property (TB,N) hasTxaTimeoutCount;
@property (TI,N,V_txaTimeoutCount) txaTimeoutCount;
@property (TB,N) hasTxaPORCount;
@property (TI,N,V_txaPORCount) txaPORCount;
@property (TB,N) hasTxPathEnableReqCount;
@property (TI,N,V_txPathEnableReqCount) txPathEnableReqCount;
@property (TB,N) hasTxPathMuteCount;
@property (TI,N,V_txPathMuteCount) txPathMuteCount;
@property (TB,N) hasTxPriorityCount;
@property (TI,N,V_txPriorityCount) txPriorityCount;
@property (TB,N) hasTxDeferredCount;
@property (TI,N,V_txDeferredCount) txDeferredCount;
@property (TB,N) hasTxMuteCount;
@property (TI,N,V_txMuteCount) txMuteCount;
@property (TB,N) hasAckTxPowerBackoffCount;
@property (TI,N,V_ackTxPowerBackoffCount) ackTxPowerBackoffCount;
@property (TB,N) hasTxaDuration;
@property (TQ,N,V_txaDuration) txaDuration;
@property (TB,N) hasTxPriDuration;
@property (TQ,N,V_txPriDuration) txPriDuration;
@property (TB,N) hasTxDeferDuration;
@property (TQ,N,V_txDeferDuration) txDeferDuration;
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiTDMSlice writeTo:];
-[WiFiAnalyticsAWDWiFiTDMSlice mergeFrom:];
-[WiFiAnalyticsAWDWiFiTDMSlice hash];
-[WiFiAnalyticsAWDWiFiTDMSlice copyTo:];
-[WiFiAnalyticsAWDWiFiTDMSlice description];
-[WiFiAnalyticsAWDWiFiTDMSlice readFrom:];
-[WiFiAnalyticsAWDWiFiTDMSlice copyWithZone:];
-[WiFiAnalyticsAWDWiFiTDMSlice isEqual:];
-[WiFiAnalyticsAWDWiFiTDMSlice dictionaryRepresentation];
-[WiFiAnalyticsAWDWiFiTDMSlice setTxaDuration:];
-[WiFiAnalyticsAWDWiFiTDMSlice txDeferDuration];
-[WiFiAnalyticsAWDWiFiTDMSlice txPathMuteCount];
-[WiFiAnalyticsAWDWiFiTDMSlice setTxMuteCount:];
-[WiFiAnalyticsAWDWiFiTDMSlice setTxaPORCount:];
-[WiFiAnalyticsAWDWiFiTDMSlice txDeferredCount];
-[WiFiAnalyticsAWDWiFiTDMSlice txPriorityCount];
-[WiFiAnalyticsAWDWiFiTDMSlice txaTimeoutCount];
-[WiFiAnalyticsAWDWiFiTDMSlice ackTxPowerBackoffCount];
-[WiFiAnalyticsAWDWiFiTDMSlice hasAckTxPowerBackoffCount];
-[WiFiAnalyticsAWDWiFiTDMSlice hasTxDeferDuration];
-[WiFiAnalyticsAWDWiFiTDMSlice hasTxDeferredCount];
-[WiFiAnalyticsAWDWiFiTDMSlice hasTxMuteCount];
-[WiFiAnalyticsAWDWiFiTDMSlice hasTxPathEnableReqCount];
-[WiFiAnalyticsAWDWiFiTDMSlice hasTxPathMuteCount];
-[WiFiAnalyticsAWDWiFiTDMSlice hasTxPriDuration];
-[WiFiAnalyticsAWDWiFiTDMSlice hasTxPriorityCount];
-[WiFiAnalyticsAWDWiFiTDMSlice hasTxaDuration];
-[WiFiAnalyticsAWDWiFiTDMSlice hasTxaONCount];
-[WiFiAnalyticsAWDWiFiTDMSlice hasTxaPORCount];
-[WiFiAnalyticsAWDWiFiTDMSlice hasTxaTimeoutCount];
-[WiFiAnalyticsAWDWiFiTDMSlice setAckTxPowerBackoffCount:];
-[WiFiAnalyticsAWDWiFiTDMSlice setHasAckTxPowerBackoffCount:];
-[WiFiAnalyticsAWDWiFiTDMSlice setHasTxDeferDuration:];
-[WiFiAnalyticsAWDWiFiTDMSlice setHasTxDeferredCount:];
-[WiFiAnalyticsAWDWiFiTDMSlice setHasTxMuteCount:];
-[WiFiAnalyticsAWDWiFiTDMSlice setHasTxPathEnableReqCount:];
-[WiFiAnalyticsAWDWiFiTDMSlice setHasTxPathMuteCount:];
-[WiFiAnalyticsAWDWiFiTDMSlice setHasTxPriDuration:];
-[WiFiAnalyticsAWDWiFiTDMSlice setHasTxPriorityCount:];
-[WiFiAnalyticsAWDWiFiTDMSlice setHasTxaDuration:];
-[WiFiAnalyticsAWDWiFiTDMSlice setHasTxaONCount:];
-[WiFiAnalyticsAWDWiFiTDMSlice setHasTxaPORCount:];
-[WiFiAnalyticsAWDWiFiTDMSlice setHasTxaTimeoutCount:];
-[WiFiAnalyticsAWDWiFiTDMSlice setTxDeferDuration:];
-[WiFiAnalyticsAWDWiFiTDMSlice setTxDeferredCount:];
-[WiFiAnalyticsAWDWiFiTDMSlice setTxPathEnableReqCount:];
-[WiFiAnalyticsAWDWiFiTDMSlice setTxPathMuteCount:];
-[WiFiAnalyticsAWDWiFiTDMSlice setTxPriDuration:];
-[WiFiAnalyticsAWDWiFiTDMSlice setTxPriorityCount:];
-[WiFiAnalyticsAWDWiFiTDMSlice setTxaONCount:];
-[WiFiAnalyticsAWDWiFiTDMSlice setTxaTimeoutCount:];
-[WiFiAnalyticsAWDWiFiTDMSlice txMuteCount];
-[WiFiAnalyticsAWDWiFiTDMSlice txPathEnableReqCount];
-[WiFiAnalyticsAWDWiFiTDMSlice txPriDuration];
-[WiFiAnalyticsAWDWiFiTDMSlice txaDuration];
-[WiFiAnalyticsAWDWiFiTDMSlice txaONCount];
-[WiFiAnalyticsAWDWiFiTDMSlice txaPORCount];
```
