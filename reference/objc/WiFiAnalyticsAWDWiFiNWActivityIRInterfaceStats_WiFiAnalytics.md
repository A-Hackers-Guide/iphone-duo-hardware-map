# `WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats`

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
+[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats packetsType];
+[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats enableStateType];
+[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats txLatencyBEType];
+[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats txLatencyVIType];
+[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats txLatencyBKType];
+[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats txLatencyVOType];
+[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats bytesType];
+[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats npeersType];
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats txLatencyVIAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats clearBytes];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats clearPackets];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats addTxLatencyVI:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats packetsAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats txLatencyVIs];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats bytesCount];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats txLatencyVOs];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats addPackets:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats packets];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats txLatencyVOsCount];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats txLatencyBKsCount];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats packetsCount];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats addTxLatencyBE:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats addBytes:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats hasPeerCount];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats txLatencyBEs];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats bytesAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats setBytes:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats setTxLatencyBKs:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats txLatencyBEAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats txLatencyVIsCount];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats addTxLatencyVO:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats addTxLatencyBK:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats setTxLatencyBEs:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats clearTxLatencyBEs];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats clearTxLatencyBKs];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats txLatencyBKAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats clearTxLatencyVOs];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats clearTxLatencyVIs];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats setPackets:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats txLatencyBEsCount];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats setTxLatencyVIs:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats addNpeers:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats peersAdded];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats npeers];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats writeTo:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats setHasPeerCount:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats enabled];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats setEnableStates:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats setPeersRemoved:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats mergeFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats hasRole];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats setHasPeersAdded:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats setPeerCount:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats txLatencyBKs];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats hasEnabled];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats enableStateAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats clearNpeers];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats addEnableState:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats setPeersAdded:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats enableStatesCount];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats hasPeersAdded];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats peerCount];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats setNpeers:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats setEnabled:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats peersRemoved];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats setHasPeersRemoved:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats npeersAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats role];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats hash];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats clearEnableStates];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats setRole:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats copyTo:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats enableStates];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats description];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats npeersCount];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats readFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats txLatencyVOAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats setHasEnabled:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats copyWithZone:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats setTxLatencyVOs:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats isEqual:];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats bytes];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats hasPeersRemoved];
-[WiFiAnalyticsAWDWiFiNWActivityIRInterfaceStats dictionaryRepresentation];
```
