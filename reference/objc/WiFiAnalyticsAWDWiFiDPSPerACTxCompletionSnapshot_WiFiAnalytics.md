# `WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 12 instance variables, 22 properties, 53 instance methods, 0 class methods

## Instance variables

```
I _chipModeError;
I _dropped;
I _expired;
I _firmwareFreePacket;
I _forceLifetimeExp;
I _maxRetries;
I _noAck;
I _noBuf;
I _noResources;
I _success;
I _txFailure;
{?="chipModeError"b1"dropped"b1"expired"b1"firmwareFreePacket"b1"forceLifetimeExp"b1"maxRetries"b1"noAck"b1"noBuf"b1"noResources"b1"success"b1"txFailure"b1} _has;
```

## Properties

```
@property (TB,N) hasSuccess;
@property (TI,N,V_success) success;
@property (TB,N) hasDropped;
@property (TI,N,V_dropped) dropped;
@property (TB,N) hasNoBuf;
@property (TI,N,V_noBuf) noBuf;
@property (TB,N) hasNoResources;
@property (TI,N,V_noResources) noResources;
@property (TB,N) hasNoAck;
@property (TI,N,V_noAck) noAck;
@property (TB,N) hasChipModeError;
@property (TI,N,V_chipModeError) chipModeError;
@property (TB,N) hasExpired;
@property (TI,N,V_expired) expired;
@property (TB,N) hasTxFailure;
@property (TI,N,V_txFailure) txFailure;
@property (TB,N) hasFirmwareFreePacket;
@property (TI,N,V_firmwareFreePacket) firmwareFreePacket;
@property (TB,N) hasMaxRetries;
@property (TI,N,V_maxRetries) maxRetries;
@property (TB,N) hasForceLifetimeExp;
@property (TI,N,V_forceLifetimeExp) forceLifetimeExp;
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot hasSuccess];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot writeTo:];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot setSuccess:];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot hasExpired];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot success];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot mergeFrom:];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot setHasSuccess:];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot expired];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot maxRetries];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot hash];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot copyTo:];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot description];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot setExpired:];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot readFrom:];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot copyWithZone:];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot isEqual:];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot setHasExpired:];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot dictionaryRepresentation];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot setMaxRetries:];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot dropped];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot setDropped:];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot setNoResources:];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot chipModeError];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot firmwareFreePacket];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot forceLifetimeExp];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot hasChipModeError];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot hasDropped];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot hasFirmwareFreePacket];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot hasForceLifetimeExp];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot hasMaxRetries];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot hasNoAck];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot hasNoBuf];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot hasNoResources];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot hasTxFailure];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot noAck];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot noBuf];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot noResources];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot setChipModeError:];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot setFirmwareFreePacket:];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot setForceLifetimeExp:];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot setHasChipModeError:];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot setHasDropped:];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot setHasFirmwareFreePacket:];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot setHasForceLifetimeExp:];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot setHasMaxRetries:];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot setHasNoAck:];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot setHasNoBuf:];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot setHasNoResources:];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot setHasTxFailure:];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot setNoAck:];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot setNoBuf:];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot setTxFailure:];
-[WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot txFailure];
```
