# `WiFiAnalyticsAWDWiFiNWActivityNANPeerStats`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 13 instance variables, 16 properties, 73 instance methods, 8 class methods

## Instance variables

```
@"NSMutableArray" _acCompletions;
@"NSMutableArray" _bytes;
@"WiFiAnalyticsAWDWiFiNWActivityTxCompletions" _completions;
@"NSString" _hashID;
@"NSMutableArray" _packets;
i _role;
i _rssiValue;
@"NSMutableArray" _rssis;
@"NSMutableArray" _txLatencyBEs;
@"NSMutableArray" _txLatencyBKs;
@"NSMutableArray" _txLatencyVIs;
@"NSMutableArray" _txLatencyVOs;
{?="role"b1"rssiValue"b1} _has;
```

## Properties

```
@property (TB,N) hasRole;
@property (Ti,N,V_role) role;
@property (TB,R,N) hasHashID;
@property (T@"NSString",&,N,V_hashID) hashID;
@property (T@"NSMutableArray",&,N,V_rssis) rssis;
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
```

## Class methods

```
+[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats packetsType];
+[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats txLatencyBEType];
+[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats txLatencyVIType];
+[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats txLatencyBKType];
+[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats txLatencyVOType];
+[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats acCompletionsType];
+[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats bytesType];
+[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats rssiType];
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats txLatencyVIAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats clearBytes];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats clearPackets];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats addTxLatencyVI:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats packetsAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats txLatencyVIs];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats bytesCount];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats txLatencyVOs];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats addPackets:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats packets];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats txLatencyVOsCount];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats txLatencyBKsCount];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats packetsCount];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats addTxLatencyBE:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats addBytes:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats txLatencyBEs];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats bytesAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats setBytes:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats setTxLatencyBKs:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats txLatencyBEAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats txLatencyVIsCount];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats addTxLatencyVO:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats rssiAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats addTxLatencyBK:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats setTxLatencyBEs:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats clearTxLatencyBEs];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats clearTxLatencyBKs];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats txLatencyBKAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats hasRssiValue];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats clearTxLatencyVOs];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats clearTxLatencyVIs];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats setPackets:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats txLatencyBEsCount];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats setHasRole:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats setTxLatencyVIs:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats addRssi:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats writeTo:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats hashID];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats addAcCompletions:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats setHasRssiValue:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats roleAsString:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats setCompletions:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats mergeFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats hasRole];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats completions];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats txLatencyBKs];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats setRssis:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats setHashID:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats clearRssis];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats setRssiValue:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats rssis];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats acCompletionsCount];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats acCompletions];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats hasHashID];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats role];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats hash];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats setRole:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats copyTo:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats StringAsRole:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats description];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats setAcCompletions:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats readFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats txLatencyVOAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats copyWithZone:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats acCompletionsAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats hasCompletions];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats setTxLatencyVOs:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats isEqual:];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats bytes];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats clearAcCompletions];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats rssisCount];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats rssiValue];
-[WiFiAnalyticsAWDWiFiNWActivityNANPeerStats dictionaryRepresentation];
```
