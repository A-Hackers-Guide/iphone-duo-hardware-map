# `WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats`

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
+[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats packetsType];
+[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats enableStateType];
+[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats txLatencyBEType];
+[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats txLatencyVIType];
+[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats txLatencyBKType];
+[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats txLatencyVOType];
+[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats bytesType];
+[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats npeersType];
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats txLatencyVIAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats clearBytes];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats clearPackets];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats addTxLatencyVI:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats packetsAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats txLatencyVIs];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats bytesCount];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats txLatencyVOs];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats addPackets:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats packets];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats txLatencyVOsCount];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats txLatencyBKsCount];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats packetsCount];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats addTxLatencyBE:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats addBytes:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats hasPeerCount];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats txLatencyBEs];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats bytesAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats setBytes:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats setTxLatencyBKs:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats txLatencyBEAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats txLatencyVIsCount];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats addTxLatencyVO:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats addTxLatencyBK:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats setTxLatencyBEs:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats clearTxLatencyBEs];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats clearTxLatencyBKs];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats txLatencyBKAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats clearTxLatencyVOs];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats clearTxLatencyVIs];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats setPackets:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats txLatencyBEsCount];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats setTxLatencyVIs:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats addNpeers:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats peersAdded];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats npeers];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats writeTo:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats setHasPeerCount:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats enabled];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats setEnableStates:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats setPeersRemoved:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats mergeFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats hasRole];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats setHasPeersAdded:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats setPeerCount:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats txLatencyBKs];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats hasEnabled];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats enableStateAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats clearNpeers];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats addEnableState:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats setPeersAdded:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats enableStatesCount];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats hasPeersAdded];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats peerCount];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats setNpeers:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats setEnabled:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats peersRemoved];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats setHasPeersRemoved:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats npeersAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats role];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats hash];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats clearEnableStates];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats setRole:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats copyTo:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats enableStates];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats description];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats npeersCount];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats readFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats txLatencyVOAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats setHasEnabled:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats copyWithZone:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats setTxLatencyVOs:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats isEqual:];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats bytes];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats hasPeersRemoved];
-[WiFiAnalyticsAWDWiFiNWActivityNANInterfaceStats dictionaryRepresentation];
```
