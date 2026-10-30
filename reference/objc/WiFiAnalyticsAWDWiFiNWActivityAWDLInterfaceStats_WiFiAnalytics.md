# `WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 18 instance variables, 24 properties, 96 instance methods, 10 class methods

## Instance variables

```
I _afCount;
@"NSMutableArray" _awdlStates;
@"NSMutableArray" _bytes;
@"NSMutableArray" _enableStates;
I _enabled;
@"NSMutableArray" _npeers;
@"NSMutableArray" _nrtpeers;
@"NSMutableArray" _packets;
I _peerCount;
I _peersAdded;
I _peersRemoved;
@"NSString" _role;
I _rtPeerCount;
@"NSMutableArray" _txLatencyBEs;
@"NSMutableArray" _txLatencyBKs;
@"NSMutableArray" _txLatencyVIs;
@"NSMutableArray" _txLatencyVOs;
{?="afCount"b1"enabled"b1"peerCount"b1"peersAdded"b1"peersRemoved"b1"rtPeerCount"b1} _has;
```

## Properties

```
@property (TB,R,N) hasRole;
@property (T@"NSString",&,N,V_role) role;
@property (T@"NSMutableArray",&,N,V_packets) packets;
@property (T@"NSMutableArray",&,N,V_bytes) bytes;
@property (T@"NSMutableArray",&,N,V_npeers) npeers;
@property (T@"NSMutableArray",&,N,V_nrtpeers) nrtpeers;
@property (T@"NSMutableArray",&,N,V_awdlStates) awdlStates;
@property (TB,N) hasRtPeerCount;
@property (TI,N,V_rtPeerCount) rtPeerCount;
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
@property (TB,N) hasAfCount;
@property (TI,N,V_afCount) afCount;
```

## Class methods

```
+[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats packetsType];
+[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats enableStateType];
+[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats txLatencyBEType];
+[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats txLatencyVIType];
+[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats txLatencyBKType];
+[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats txLatencyVOType];
+[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats awdlStateType];
+[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats bytesType];
+[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats npeersType];
+[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats nrtpeersType];
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats txLatencyVIAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats clearBytes];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats clearPackets];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats addTxLatencyVI:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats packetsAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats txLatencyVIs];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats bytesCount];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats txLatencyVOs];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats addPackets:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats packets];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats txLatencyVOsCount];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats txLatencyBKsCount];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats packetsCount];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats addTxLatencyBE:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats addBytes:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats hasPeerCount];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats txLatencyBEs];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats bytesAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats setBytes:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats setTxLatencyBKs:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats txLatencyBEAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats txLatencyVIsCount];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats addTxLatencyVO:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats addTxLatencyBK:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats setTxLatencyBEs:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats clearTxLatencyBEs];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats clearTxLatencyBKs];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats txLatencyBKAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats clearTxLatencyVOs];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats clearTxLatencyVIs];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats setPackets:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats txLatencyBEsCount];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats setTxLatencyVIs:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats addNpeers:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats peersAdded];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats nrtpeersAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats npeers];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats writeTo:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats setHasPeerCount:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats enabled];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats rtPeerCount];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats setEnableStates:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats setPeersRemoved:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats mergeFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats hasRole];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats hasRtPeerCount];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats setAfCount:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats setHasPeersAdded:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats setPeerCount:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats txLatencyBKs];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats addNrtpeers:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats nrtpeersCount];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats hasEnabled];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats nrtpeers];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats enableStateAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats awdlStates];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats clearNpeers];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats addEnableState:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats setHasAfCount:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats addAwdlState:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats setPeersAdded:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats enableStatesCount];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats setNrtpeers:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats hasPeersAdded];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats awdlStatesCount];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats clearNrtpeers];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats peerCount];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats setNpeers:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats setEnabled:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats peersRemoved];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats setHasPeersRemoved:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats npeersAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats role];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats hasAfCount];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats hash];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats clearEnableStates];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats setRole:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats copyTo:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats enableStates];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats description];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats npeersCount];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats setHasRtPeerCount:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats readFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats txLatencyVOAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats setHasEnabled:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats copyWithZone:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats awdlStateAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats setTxLatencyVOs:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats isEqual:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats bytes];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats hasPeersRemoved];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats clearAwdlStates];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats setRtPeerCount:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats setAwdlStates:];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats dictionaryRepresentation];
-[WiFiAnalyticsAWDWiFiNWActivityAWDLInterfaceStats afCount];
```
