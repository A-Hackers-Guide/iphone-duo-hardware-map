# `WiFiAnalyticsAWDWiFiNWActivityInterfaceStats`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 15 instance variables, 20 properties, 78 instance methods, 8 class methods

## Instance variables

```
@"WiFiAnalyticsAWDWiFiNWActivityAssoc" _assoc;
@"NSMutableArray" _awdlModes;
@"NSMutableArray" _bands;
@"NSMutableArray" _bytes;
I _consecutivedps;
I _dps;
@"NSMutableArray" _enableStates;
I _enabled;
@"NSMutableArray" _nss;
@"NSMutableArray" _packets;
@"NSMutableArray" _peers;
@"NSMutableArray" _phymodes;
@"NSString" _role;
@"WiFiAnalyticsAWDWiFiRxDataStallStats" _rxStall;
{?="consecutivedps"b1"dps"b1"enabled"b1} _has;
```

## Properties

```
@property (TB,R,N) hasRole;
@property (T@"NSString",&,N,V_role) role;
@property (T@"NSMutableArray",&,N,V_packets) packets;
@property (T@"NSMutableArray",&,N,V_bytes) bytes;
@property (T@"NSMutableArray",&,N,V_peers) peers;
@property (TB,N) hasDps;
@property (TI,N,V_dps) dps;
@property (TB,N) hasConsecutivedps;
@property (TI,N,V_consecutivedps) consecutivedps;
@property (TB,R,N) hasAssoc;
@property (T@"WiFiAnalyticsAWDWiFiNWActivityAssoc",&,N,V_assoc) assoc;
@property (T@"NSMutableArray",&,N,V_awdlModes) awdlModes;
@property (TB,N) hasEnabled;
@property (TI,N,V_enabled) enabled;
@property (T@"NSMutableArray",&,N,V_enableStates) enableStates;
@property (T@"NSMutableArray",&,N,V_nss) nss;
@property (T@"NSMutableArray",&,N,V_phymodes) phymodes;
@property (TB,R,N) hasRxStall;
@property (T@"WiFiAnalyticsAWDWiFiRxDataStallStats",&,N,V_rxStall) rxStall;
@property (T@"NSMutableArray",&,N,V_bands) bands;
```

## Class methods

```
+[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats peerType];
+[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats packetsType];
+[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats enableStateType];
+[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats nssType];
+[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats awdlModeType];
+[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats bandType];
+[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats bytesType];
+[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats phymodeType];
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats clearBytes];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats clearPackets];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats packetsAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats bytesCount];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats addPackets:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats packets];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats packetsCount];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats peers];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats addBytes:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats bytesAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats nss];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats setBytes:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats setPeers:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats setPackets:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats clearPhymodes];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats hasRxStall];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats addPeer:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats writeTo:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats awdlModeAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats setHasDps:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats clearPeers];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats enabled];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats awdlModes];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats setPhymodes:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats setEnableStates:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats bands];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats setConsecutivedps:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats mergeFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats addBand:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats hasRole];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats setAwdlModes:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats rxStall];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats nssAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats peerAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats hasDps];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats hasEnabled];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats clearBands];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats enableStateAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats awdlModesCount];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats addEnableState:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats nssCount];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats peersCount];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats phymodeAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats enableStatesCount];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats hasConsecutivedps];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats setEnabled:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats consecutivedps];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats hasAssoc];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats assoc];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats clearNss];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats role];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats bandsCount];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats clearAwdlModes];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats hash];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats clearEnableStates];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats setRole:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats copyTo:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats enableStates];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats description];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats phymodesCount];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats dps];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats setAssoc:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats setDps:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats addPhymode:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats readFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats addAwdlMode:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats addNss:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats setHasEnabled:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats copyWithZone:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats setNss:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats isEqual:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats bytes];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats setBands:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats setRxStall:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats setHasConsecutivedps:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats bandAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats phymodes];
-[WiFiAnalyticsAWDWiFiNWActivityInterfaceStats dictionaryRepresentation];
```
