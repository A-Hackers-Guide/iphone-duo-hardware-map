# `WiFiAnalyticsAWDWiFiDPSSnapshot`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 10 instance variables, 20 properties, 39 instance methods, 0 class methods

## Instance variables

```
@"WiFiAnalyticsAWDWiFiDPSAWDLSnapshot" _awdlSnapshot;
@"WiFiAnalyticsAWDWiFiDPSBTSnapshot" _btSnapshot;
@"WiFiAnalyticsAWDWiFiUsageSnapshot" _lteSnapshot;
@"WiFiAnalyticsAWDWiFiDPSNANSnapshot" _nanSnapshot;
@"WiFiAnalyticsAWDWiFiUsageSnapshot" _rc1Snapshot;
@"WiFiAnalyticsAWDWiFiUsageSnapshot" _rc2Snapshot;
@"WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot" _txCompletionSnapshotBE;
@"WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot" _txCompletionSnapshotBK;
@"WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot" _txCompletionSnapshotVI;
@"WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot" _txCompletionSnapshotVO;
```

## Properties

```
@property (TB,R,N) hasTxCompletionSnapshotBE;
@property (T@"WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot",&,N,V_txCompletionSnapshotBE) txCompletionSnapshotBE;
@property (TB,R,N) hasTxCompletionSnapshotBK;
@property (T@"WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot",&,N,V_txCompletionSnapshotBK) txCompletionSnapshotBK;
@property (TB,R,N) hasTxCompletionSnapshotVO;
@property (T@"WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot",&,N,V_txCompletionSnapshotVO) txCompletionSnapshotVO;
@property (TB,R,N) hasTxCompletionSnapshotVI;
@property (T@"WiFiAnalyticsAWDWiFiDPSPerACTxCompletionSnapshot",&,N,V_txCompletionSnapshotVI) txCompletionSnapshotVI;
@property (TB,R,N) hasBtSnapshot;
@property (T@"WiFiAnalyticsAWDWiFiDPSBTSnapshot",&,N,V_btSnapshot) btSnapshot;
@property (TB,R,N) hasAwdlSnapshot;
@property (T@"WiFiAnalyticsAWDWiFiDPSAWDLSnapshot",&,N,V_awdlSnapshot) awdlSnapshot;
@property (TB,R,N) hasRc1Snapshot;
@property (T@"WiFiAnalyticsAWDWiFiUsageSnapshot",&,N,V_rc1Snapshot) rc1Snapshot;
@property (TB,R,N) hasRc2Snapshot;
@property (T@"WiFiAnalyticsAWDWiFiUsageSnapshot",&,N,V_rc2Snapshot) rc2Snapshot;
@property (TB,R,N) hasLteSnapshot;
@property (T@"WiFiAnalyticsAWDWiFiUsageSnapshot",&,N,V_lteSnapshot) lteSnapshot;
@property (TB,R,N) hasNanSnapshot;
@property (T@"WiFiAnalyticsAWDWiFiDPSNANSnapshot",&,N,V_nanSnapshot) nanSnapshot;
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiDPSSnapshot writeTo:];
-[WiFiAnalyticsAWDWiFiDPSSnapshot mergeFrom:];
-[WiFiAnalyticsAWDWiFiDPSSnapshot hash];
-[WiFiAnalyticsAWDWiFiDPSSnapshot copyTo:];
-[WiFiAnalyticsAWDWiFiDPSSnapshot description];
-[WiFiAnalyticsAWDWiFiDPSSnapshot readFrom:];
-[WiFiAnalyticsAWDWiFiDPSSnapshot copyWithZone:];
-[WiFiAnalyticsAWDWiFiDPSSnapshot isEqual:];
-[WiFiAnalyticsAWDWiFiDPSSnapshot dictionaryRepresentation];
-[WiFiAnalyticsAWDWiFiDPSSnapshot hasAwdlSnapshot];
-[WiFiAnalyticsAWDWiFiDPSSnapshot setLteSnapshot:];
-[WiFiAnalyticsAWDWiFiDPSSnapshot setRc1Snapshot:];
-[WiFiAnalyticsAWDWiFiDPSSnapshot setNanSnapshot:];
-[WiFiAnalyticsAWDWiFiDPSSnapshot setRc2Snapshot:];
-[WiFiAnalyticsAWDWiFiDPSSnapshot awdlSnapshot];
-[WiFiAnalyticsAWDWiFiDPSSnapshot btSnapshot];
-[WiFiAnalyticsAWDWiFiDPSSnapshot hasBtSnapshot];
-[WiFiAnalyticsAWDWiFiDPSSnapshot hasLteSnapshot];
-[WiFiAnalyticsAWDWiFiDPSSnapshot hasNanSnapshot];
-[WiFiAnalyticsAWDWiFiDPSSnapshot hasRc1Snapshot];
-[WiFiAnalyticsAWDWiFiDPSSnapshot hasRc2Snapshot];
-[WiFiAnalyticsAWDWiFiDPSSnapshot hasTxCompletionSnapshotBE];
-[WiFiAnalyticsAWDWiFiDPSSnapshot hasTxCompletionSnapshotBK];
-[WiFiAnalyticsAWDWiFiDPSSnapshot hasTxCompletionSnapshotVI];
-[WiFiAnalyticsAWDWiFiDPSSnapshot hasTxCompletionSnapshotVO];
-[WiFiAnalyticsAWDWiFiDPSSnapshot lteSnapshot];
-[WiFiAnalyticsAWDWiFiDPSSnapshot nanSnapshot];
-[WiFiAnalyticsAWDWiFiDPSSnapshot rc1Snapshot];
-[WiFiAnalyticsAWDWiFiDPSSnapshot rc2Snapshot];
-[WiFiAnalyticsAWDWiFiDPSSnapshot setAwdlSnapshot:];
-[WiFiAnalyticsAWDWiFiDPSSnapshot setBtSnapshot:];
-[WiFiAnalyticsAWDWiFiDPSSnapshot setTxCompletionSnapshotBE:];
-[WiFiAnalyticsAWDWiFiDPSSnapshot setTxCompletionSnapshotBK:];
-[WiFiAnalyticsAWDWiFiDPSSnapshot setTxCompletionSnapshotVI:];
-[WiFiAnalyticsAWDWiFiDPSSnapshot setTxCompletionSnapshotVO:];
-[WiFiAnalyticsAWDWiFiDPSSnapshot txCompletionSnapshotBE];
-[WiFiAnalyticsAWDWiFiDPSSnapshot txCompletionSnapshotBK];
-[WiFiAnalyticsAWDWiFiDPSSnapshot txCompletionSnapshotVI];
-[WiFiAnalyticsAWDWiFiDPSSnapshot txCompletionSnapshotVO];
```
