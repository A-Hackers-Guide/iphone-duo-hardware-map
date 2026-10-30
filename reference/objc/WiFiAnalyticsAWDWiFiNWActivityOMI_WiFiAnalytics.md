# `WiFiAnalyticsAWDWiFiNWActivityOMI`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 17 instance variables, 32 properties, 73 instance methods, 0 class methods

## Instance variables

```
I _chBWAck;
I _chBWReq;
I _completionDelay;
I _dLResoundAck;
I _dLResoundReq;
I _eRSUAck;
I _eRSUReq;
I _retries;
I _rxNSSAck;
I _rxNSSReq;
I _scheduled;
I _success;
I _txNSTSAck;
I _txNSTSReq;
I _uLMUAck;
I _uLMUReq;
{?="chBWAck"b1"chBWReq"b1"completionDelay"b1"dLResoundAck"b1"dLResoundReq"b1"eRSUAck"b1"eRSUReq"b1"retries"b1"rxNSSAck"b1"rxNSSReq"b1"scheduled"b1"success"b1"txNSTSAck"b1"txNSTSReq"b1"uLMUAck"b1"uLMUReq"b1} _has;
```

## Properties

```
@property (TB,N) hasScheduled;
@property (TI,N,V_scheduled) scheduled;
@property (TB,N) hasSuccess;
@property (TI,N,V_success) success;
@property (TB,N) hasRetries;
@property (TI,N,V_retries) retries;
@property (TB,N) hasCompletionDelay;
@property (TI,N,V_completionDelay) completionDelay;
@property (TB,N) hasULMUReq;
@property (TI,N,V_uLMUReq) uLMUReq;
@property (TB,N) hasULMUAck;
@property (TI,N,V_uLMUAck) uLMUAck;
@property (TB,N) hasTxNSTSReq;
@property (TI,N,V_txNSTSReq) txNSTSReq;
@property (TB,N) hasTxNSTSAck;
@property (TI,N,V_txNSTSAck) txNSTSAck;
@property (TB,N) hasRxNSSReq;
@property (TI,N,V_rxNSSReq) rxNSSReq;
@property (TB,N) hasRxNSSAck;
@property (TI,N,V_rxNSSAck) rxNSSAck;
@property (TB,N) hasChBWReq;
@property (TI,N,V_chBWReq) chBWReq;
@property (TB,N) hasChBWAck;
@property (TI,N,V_chBWAck) chBWAck;
@property (TB,N) hasERSUReq;
@property (TI,N,V_eRSUReq) eRSUReq;
@property (TB,N) hasERSUAck;
@property (TI,N,V_eRSUAck) eRSUAck;
@property (TB,N) hasDLResoundReq;
@property (TI,N,V_dLResoundReq) dLResoundReq;
@property (TB,N) hasDLResoundAck;
@property (TI,N,V_dLResoundAck) dLResoundAck;
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiNWActivityOMI chBWReq];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setRetries:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI hasSuccess];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setScheduled:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setHasERSUReq:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI hasCompletionDelay];
-[WiFiAnalyticsAWDWiFiNWActivityOMI writeTo:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setSuccess:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setTxNSTSAck:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI hasULMUReq];
-[WiFiAnalyticsAWDWiFiNWActivityOMI chBWAck];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setULMUAck:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI success];
-[WiFiAnalyticsAWDWiFiNWActivityOMI hasERSUReq];
-[WiFiAnalyticsAWDWiFiNWActivityOMI hasDLResoundReq];
-[WiFiAnalyticsAWDWiFiNWActivityOMI hasRxNSSAck];
-[WiFiAnalyticsAWDWiFiNWActivityOMI uLMUAck];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setHasRxNSSAck:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI dLResoundAck];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setCompletionDelay:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI mergeFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI txNSTSReq];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setHasDLResoundAck:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI hasDLResoundAck];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setHasSuccess:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setULMUReq:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI uLMUReq];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setHasERSUAck:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI hasTxNSTSReq];
-[WiFiAnalyticsAWDWiFiNWActivityOMI scheduled];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setHasULMUAck:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI eRSUAck];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setHasRetries:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setChBWAck:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI hasRxNSSReq];
-[WiFiAnalyticsAWDWiFiNWActivityOMI hasULMUAck];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setHasTxNSTSAck:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setDLResoundReq:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setDLResoundAck:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setChBWReq:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI txNSTSAck];
-[WiFiAnalyticsAWDWiFiNWActivityOMI hasChBWAck];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setHasScheduled:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setTxNSTSReq:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI rxNSSAck];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setERSUAck:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI hash];
-[WiFiAnalyticsAWDWiFiNWActivityOMI copyTo:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI description];
-[WiFiAnalyticsAWDWiFiNWActivityOMI dLResoundReq];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setRxNSSReq:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setHasRxNSSReq:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setRxNSSAck:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI hasTxNSTSAck];
-[WiFiAnalyticsAWDWiFiNWActivityOMI readFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI hasERSUAck];
-[WiFiAnalyticsAWDWiFiNWActivityOMI rxNSSReq];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setERSUReq:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI eRSUReq];
-[WiFiAnalyticsAWDWiFiNWActivityOMI hasChBWReq];
-[WiFiAnalyticsAWDWiFiNWActivityOMI copyWithZone:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI hasScheduled];
-[WiFiAnalyticsAWDWiFiNWActivityOMI isEqual:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setHasChBWReq:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setHasTxNSTSReq:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setHasChBWAck:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setHasDLResoundReq:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI hasRetries];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setHasCompletionDelay:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI dictionaryRepresentation];
-[WiFiAnalyticsAWDWiFiNWActivityOMI completionDelay];
-[WiFiAnalyticsAWDWiFiNWActivityOMI setHasULMUReq:];
-[WiFiAnalyticsAWDWiFiNWActivityOMI retries];
```
