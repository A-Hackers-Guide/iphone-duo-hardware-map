# `WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 14 instance variables, 18 properties, 76 instance methods, 8 class methods

## Instance variables

```
@"NSMutableArray" _bytes;
@"NSMutableArray" _enableStates;
I _enabled;
@"NSMutableArray" _npeers;
@"NSMutableArray" _packets;
I _peerCount;
I _peersAdded;
I _peersRemoved;
@"NSString" _role;
@"NSMutableArray" _txLatencyBEs;
@"NSMutableArray" _txLatencyBKs;
@"NSMutableArray" _txLatencyVIs;
@"NSMutableArray" _txLatencyVOs;
{?="enabled"b1"peerCount"b1"peersAdded"b1"peersRemoved"b1} _has;
```

## Properties

```
@property (TB,R,N) hasRole;
@property (T@"NSString",&,N,V_role) role;
@property (T@"NSMutableArray",&,N,V_packets) packets;
@property (T@"NSMutableArray",&,N,V_bytes) bytes;
@property (T@"NSMutableArray",&,N,V_npeers) npeers;
@property (TB,N) hasPeerCount;
@property (TI,N,V_peerCount) peerCount;
@property (TB,N) hasPeersAdded;
@property (TI,N,V_peersAdded) peersAdded;
@property (TB,N) hasPeersRemoved;
@property (TI,N,V_peersRemoved) peersRemoved;
@property (TB,N) hasEnabled;
@property (TI,N,V_enabled) enabled;
@property (T@"NSMutableArray",&,N,V_enableStates) enableStates;
@property (T@"NSMutableArray",&,N,V_txLatencyBKs) txLatencyBKs;
@property (T@"NSMutableArray",&,N,V_txLatencyBEs) txLatencyBEs;
@property (T@"NSMutableArray",&,N,V_txLatencyVOs) txLatencyVOs;
@property (T@"NSMutableArray",&,N,V_txLatencyVIs) txLatencyVIs;
```

## Class methods

```
+[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats packetsType];
+[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats enableStateType];
+[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats txLatencyBEType];
+[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats txLatencyVIType];
+[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats txLatencyBKType];
+[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats txLatencyVOType];
+[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats bytesType];
+[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats npeersType];
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats txLatencyVIAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats clearBytes];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats clearPackets];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats addTxLatencyVI:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats packetsAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats txLatencyVIs];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats bytesCount];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats txLatencyVOs];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats addPackets:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats packets];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats txLatencyVOsCount];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats txLatencyBKsCount];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats packetsCount];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats addTxLatencyBE:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats addBytes:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats hasPeerCount];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats txLatencyBEs];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats bytesAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats setBytes:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats setTxLatencyBKs:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats txLatencyBEAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats txLatencyVIsCount];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats addTxLatencyVO:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats addTxLatencyBK:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats setTxLatencyBEs:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats clearTxLatencyBEs];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats clearTxLatencyBKs];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats txLatencyBKAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats clearTxLatencyVOs];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats clearTxLatencyVIs];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats setPackets:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats txLatencyBEsCount];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats setTxLatencyVIs:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats addNpeers:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats peersAdded];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats npeers];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats writeTo:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats setHasPeerCount:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats enabled];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats setEnableStates:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats setPeersRemoved:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats mergeFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats hasRole];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats setHasPeersAdded:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats setPeerCount:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats txLatencyBKs];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats hasEnabled];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats enableStateAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats clearNpeers];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats addEnableState:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats setPeersAdded:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats enableStatesCount];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats hasPeersAdded];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats peerCount];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats setNpeers:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats setEnabled:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats peersRemoved];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats setHasPeersRemoved:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats npeersAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats role];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats hash];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats clearEnableStates];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats setRole:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats copyTo:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats enableStates];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats description];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats npeersCount];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats readFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats txLatencyVOAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats setHasEnabled:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats copyWithZone:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats setTxLatencyVOs:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats isEqual:];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats bytes];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats hasPeersRemoved];
-[WiFiAnalyticsAWDWiFiNWActivityAPInterfaceStats dictionaryRepresentation];
```
