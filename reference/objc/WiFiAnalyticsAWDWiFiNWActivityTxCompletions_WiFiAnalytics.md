# `WiFiAnalyticsAWDWiFiNWActivityTxCompletions`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 12 instance variables, 22 properties, 53 instance methods, 0 class methods

## Instance variables

```
I _chipmodeerror;
I _expired;
I _internalerror;
I _ioerror;
I _mbfree;
I _noack;
I _nobuf;
I _noremotepeer;
I _noresources;
I _success;
I _txfailure;
{?="chipmodeerror"b1"expired"b1"internalerror"b1"ioerror"b1"mbfree"b1"noack"b1"nobuf"b1"noremotepeer"b1"noresources"b1"success"b1"txfailure"b1} _has;
```

## Properties

```
@property (TB,N) hasSuccess;
@property (TI,N,V_success) success;
@property (TB,N) hasExpired;
@property (TI,N,V_expired) expired;
@property (TB,N) hasNobuf;
@property (TI,N,V_nobuf) nobuf;
@property (TB,N) hasNoack;
@property (TI,N,V_noack) noack;
@property (TB,N) hasTxfailure;
@property (TI,N,V_txfailure) txfailure;
@property (TB,N) hasNoresources;
@property (TI,N,V_noresources) noresources;
@property (TB,N) hasIoerror;
@property (TI,N,V_ioerror) ioerror;
@property (TB,N) hasMbfree;
@property (TI,N,V_mbfree) mbfree;
@property (TB,N) hasChipmodeerror;
@property (TI,N,V_chipmodeerror) chipmodeerror;
@property (TB,N) hasNoremotepeer;
@property (TI,N,V_noremotepeer) noremotepeer;
@property (TB,N) hasInternalerror;
@property (TI,N,V_internalerror) internalerror;
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions hasSuccess];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions setMbfree:];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions hasTxfailure];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions hasNoresources];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions writeTo:];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions setSuccess:];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions hasChipmodeerror];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions hasExpired];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions success];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions setHasNoresources:];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions mergeFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions hasNobuf];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions setNoresources:];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions setHasSuccess:];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions noresources];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions chipmodeerror];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions hasMbfree];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions expired];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions setChipmodeerror:];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions setHasMbfree:];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions hasIoerror];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions setIoerror:];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions mbfree];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions hasNoremotepeer];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions setNoremotepeer:];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions noack];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions setHasTxfailure:];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions setHasNoack:];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions txfailure];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions hasNoack];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions setHasNobuf:];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions noremotepeer];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions setHasChipmodeerror:];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions setInternalerror:];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions setHasIoerror:];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions hash];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions setHasNoremotepeer:];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions copyTo:];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions setTxfailure:];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions description];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions setExpired:];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions setNoack:];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions setHasInternalerror:];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions internalerror];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions hasInternalerror];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions ioerror];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions readFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions copyWithZone:];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions isEqual:];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions setNobuf:];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions nobuf];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions setHasExpired:];
-[WiFiAnalyticsAWDWiFiNWActivityTxCompletions dictionaryRepresentation];
```
