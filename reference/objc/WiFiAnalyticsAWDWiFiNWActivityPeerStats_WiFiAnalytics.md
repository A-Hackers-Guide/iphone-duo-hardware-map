# `WiFiAnalyticsAWDWiFiNWActivityPeerStats`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 26 instance variables, 40 properties, 129 instance methods, 10 class methods

## Instance variables

```
@"NSMutableArray" _acCompletions;
@"NSMutableArray" _bytes;
I _ccaValue;
@"NSMutableArray" _ccas;
@"WiFiAnalyticsAWDWiFiNWActivityTxCompletions" _completions;
@"NSString" _hashID;
I _ibssCCA;
I _interferenceCCA;
i _nfValue;
I _obssCCA;
I _ofdmDesense;
@"NSMutableArray" _packets;
I _qbssCCA;
I _qbssSTACount;
i _role;
i _rssiValue;
i _rssiValue0;
i _rssiValue1;
@"NSMutableArray" _rssis;
i _snrValue;
@"NSMutableArray" _snrs;
@"NSMutableArray" _txLatencyBEs;
@"NSMutableArray" _txLatencyBKs;
@"NSMutableArray" _txLatencyVIs;
@"NSMutableArray" _txLatencyVOs;
{?="ccaValue"b1"ibssCCA"b1"interferenceCCA"b1"nfValue"b1"obssCCA"b1"ofdmDesense"b1"qbssCCA"b1"qbssSTACount"b1"role"b1"rssiValue"b1"rssiValue0"b1"rssiValue1"b1"snrValue"b1} _has;
```

## Properties

```
@property (TB,N) hasRole;
@property (Ti,N,V_role) role;
@property (TB,R,N) hasHashID;
@property (T@"NSString",&,N,V_hashID) hashID;
@property (T@"NSMutableArray",&,N,V_rssis) rssis;
@property (T@"NSMutableArray",&,N,V_ccas) ccas;
@property (T@"NSMutableArray",&,N,V_snrs) snrs;
@property (T@"NSMutableArray",&,N,V_packets) packets;
@property (T@"NSMutableArray",&,N,V_bytes) bytes;
@property (T@"NSMutableArray",&,N,V_txLatencyBKs) txLatencyBKs;
@property (T@"NSMutableArray",&,N,V_txLatencyBEs) txLatencyBEs;
@property (T@"NSMutableArray",&,N,V_txLatencyVOs) txLatencyVOs;
@property (T@"NSMutableArray",&,N,V_txLatencyVIs) txLatencyVIs;
@property (TB,R,N) hasCompletions;
@property (T@"WiFiAnalyticsAWDWiFiNWActivityTxCompletions",&,N,V_completions) completions;
@property (T@"NSMutableArray",&,N,V_acCompletions) acCompletions;
@property (TB,N) hasRssiValue;
@property (Ti,N,V_rssiValue) rssiValue;
@property (TB,N) hasSnrValue;
@property (Ti,N,V_snrValue) snrValue;
@property (TB,N) hasCcaValue;
@property (TI,N,V_ccaValue) ccaValue;
@property (TB,N) hasNfValue;
@property (Ti,N,V_nfValue) nfValue;
@property (TB,N) hasOfdmDesense;
@property (TI,N,V_ofdmDesense) ofdmDesense;
@property (TB,N) hasIbssCCA;
@property (TI,N,V_ibssCCA) ibssCCA;
@property (TB,N) hasObssCCA;
@property (TI,N,V_obssCCA) obssCCA;
@property (TB,N) hasInterferenceCCA;
@property (TI,N,V_interferenceCCA) interferenceCCA;
@property (TB,N) hasQbssCCA;
@property (TI,N,V_qbssCCA) qbssCCA;
@property (TB,N) hasQbssSTACount;
@property (TI,N,V_qbssSTACount) qbssSTACount;
@property (TB,N) hasRssiValue0;
@property (Ti,N,V_rssiValue0) rssiValue0;
@property (TB,N) hasRssiValue1;
@property (Ti,N,V_rssiValue1) rssiValue1;
```

## Class methods

```
+[WiFiAnalyticsAWDWiFiNWActivityPeerStats snrType];
+[WiFiAnalyticsAWDWiFiNWActivityPeerStats packetsType];
+[WiFiAnalyticsAWDWiFiNWActivityPeerStats txLatencyBEType];
+[WiFiAnalyticsAWDWiFiNWActivityPeerStats txLatencyVIType];
+[WiFiAnalyticsAWDWiFiNWActivityPeerStats ccaType];
+[WiFiAnalyticsAWDWiFiNWActivityPeerStats txLatencyBKType];
+[WiFiAnalyticsAWDWiFiNWActivityPeerStats txLatencyVOType];
+[WiFiAnalyticsAWDWiFiNWActivityPeerStats acCompletionsType];
+[WiFiAnalyticsAWDWiFiNWActivityPeerStats bytesType];
+[WiFiAnalyticsAWDWiFiNWActivityPeerStats rssiType];
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats txLatencyVIAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats clearBytes];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats clearPackets];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats addTxLatencyVI:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats packetsAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats txLatencyVIs];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats bytesCount];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats txLatencyVOs];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats addPackets:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats packets];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats txLatencyVOsCount];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats txLatencyBKsCount];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats packetsCount];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats addTxLatencyBE:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats addBytes:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats txLatencyBEs];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats bytesAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setBytes:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setTxLatencyBKs:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats txLatencyBEAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats txLatencyVIsCount];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats addTxLatencyVO:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats rssiAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats addTxLatencyBK:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setTxLatencyBEs:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats clearTxLatencyBEs];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats clearTxLatencyBKs];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats txLatencyBKAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats hasRssiValue];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats clearTxLatencyVOs];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats clearTxLatencyVIs];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setPackets:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats txLatencyBEsCount];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats clearSnrs];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setHasRole:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setTxLatencyVIs:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setObssCCA:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats addRssi:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setHasRssiValue0:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setHasSnrValue:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats writeTo:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setHasCcaValue:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats ibssCCA];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats hashID];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats nfValue];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats addAcCompletions:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats snrsCount];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setHasRssiValue:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats roleAsString:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setCompletions:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setHasOfdmDesense:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats mergeFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats rssiValue1];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats hasIbssCCA];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats hasRole];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setHasInterferenceCCA:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats hasQbssSTACount];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats completions];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats hasQbssCCA];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats txLatencyBKs];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setQbssCCA:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setRssiValue1:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats qbssCCA];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats addCca:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats ccaAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setQbssSTACount:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setRssis:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats hasInterferenceCCA];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setOfdmDesense:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats hasRssiValue0];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setHashID:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setInterferenceCCA:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats qbssSTACount];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats clearRssis];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats obssCCA];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats ccaValue];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setSnrValue:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setHasQbssCCA:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setRssiValue:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setCcas:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats rssis];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats acCompletionsCount];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats acCompletions];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats snrAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats clearCcas];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats hasHashID];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats snrValue];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats interferenceCCA];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setCcaValue:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats role];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats hasRssiValue1];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats hasSnrValue];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setRssiValue0:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats hash];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setRole:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats copyTo:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats StringAsRole:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats hasNfValue];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats description];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats rssiValue0];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats addSnr:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setAcCompletions:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats ofdmDesense];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setNfValue:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setHasIbssCCA:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setHasNfValue:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setIbssCCA:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats readFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats txLatencyVOAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setHasObssCCA:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats hasObssCCA];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats copyWithZone:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats hasCcaValue];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats hasOfdmDesense];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats acCompletionsAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats hasCompletions];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setTxLatencyVOs:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats isEqual:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setSnrs:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setHasRssiValue1:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats bytes];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats clearAcCompletions];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats snrs];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats setHasQbssSTACount:];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats rssisCount];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats ccasCount];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats rssiValue];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats ccas];
-[WiFiAnalyticsAWDWiFiNWActivityPeerStats dictionaryRepresentation];
```
