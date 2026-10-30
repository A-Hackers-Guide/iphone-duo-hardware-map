# `WiFiAnalyticsAWDWAPeerDiscoveryInfo`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 8 properties, 25 instance methods, 0 class methods

## Instance variables

```
I _iOSPeers;
I _macOSPeers;
I _numPeersDiscovered;
I _tvOSPeers;
{?="iOSPeers"b1"macOSPeers"b1"numPeersDiscovered"b1"tvOSPeers"b1} _has;
```

## Properties

```
@property (TB,N) hasNumPeersDiscovered;
@property (TI,N,V_numPeersDiscovered) numPeersDiscovered;
@property (TB,N) hasIOSPeers;
@property (TI,N,V_iOSPeers) iOSPeers;
@property (TB,N) hasTvOSPeers;
@property (TI,N,V_tvOSPeers) tvOSPeers;
@property (TB,N) hasMacOSPeers;
@property (TI,N,V_macOSPeers) macOSPeers;
```

## Instance methods

```
-[WiFiAnalyticsAWDWAPeerDiscoveryInfo writeTo:];
-[WiFiAnalyticsAWDWAPeerDiscoveryInfo mergeFrom:];
-[WiFiAnalyticsAWDWAPeerDiscoveryInfo hash];
-[WiFiAnalyticsAWDWAPeerDiscoveryInfo copyTo:];
-[WiFiAnalyticsAWDWAPeerDiscoveryInfo description];
-[WiFiAnalyticsAWDWAPeerDiscoveryInfo readFrom:];
-[WiFiAnalyticsAWDWAPeerDiscoveryInfo copyWithZone:];
-[WiFiAnalyticsAWDWAPeerDiscoveryInfo isEqual:];
-[WiFiAnalyticsAWDWAPeerDiscoveryInfo dictionaryRepresentation];
-[WiFiAnalyticsAWDWAPeerDiscoveryInfo setHasIOSPeers:];
-[WiFiAnalyticsAWDWAPeerDiscoveryInfo hasIOSPeers];
-[WiFiAnalyticsAWDWAPeerDiscoveryInfo hasMacOSPeers];
-[WiFiAnalyticsAWDWAPeerDiscoveryInfo hasNumPeersDiscovered];
-[WiFiAnalyticsAWDWAPeerDiscoveryInfo hasTvOSPeers];
-[WiFiAnalyticsAWDWAPeerDiscoveryInfo iOSPeers];
-[WiFiAnalyticsAWDWAPeerDiscoveryInfo macOSPeers];
-[WiFiAnalyticsAWDWAPeerDiscoveryInfo numPeersDiscovered];
-[WiFiAnalyticsAWDWAPeerDiscoveryInfo setHasMacOSPeers:];
-[WiFiAnalyticsAWDWAPeerDiscoveryInfo setHasNumPeersDiscovered:];
-[WiFiAnalyticsAWDWAPeerDiscoveryInfo setHasTvOSPeers:];
-[WiFiAnalyticsAWDWAPeerDiscoveryInfo setIOSPeers:];
-[WiFiAnalyticsAWDWAPeerDiscoveryInfo setMacOSPeers:];
-[WiFiAnalyticsAWDWAPeerDiscoveryInfo setNumPeersDiscovered:];
-[WiFiAnalyticsAWDWAPeerDiscoveryInfo setTvOSPeers:];
-[WiFiAnalyticsAWDWAPeerDiscoveryInfo tvOSPeers];
```
