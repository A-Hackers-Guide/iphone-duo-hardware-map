# `WiFiAvailabilityMatch`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WiFiRecommendation`
- 6 instance variables, 6 properties, 15 instance methods, 1 class methods

## Instance variables

```
B _unwantedNetworkName;
q _priority;
@"<WiFiCandidateNetwork>" _network;
@"NSString" _SSID;
@"<WiFiScannedNetwork>" _scannedNetwork;
@"NSDate" _matchedAt;
```

## Properties

```
@property (T@"<WiFiScannedNetwork>",&,N,V_scannedNetwork) scannedNetwork;
@property (T@"NSDate",&,N,V_matchedAt) matchedAt;
@property (TB,N,V_unwantedNetworkName) unwantedNetworkName;
@property (T@"NSString",R,C,N,V_SSID) SSID;
@property (T@"<WiFiCandidateNetwork>",R,N,V_network) network;
@property (Tq,R,N,V_priority) priority;
```

## Class methods

```
+[WiFiAvailabilityMatch matchWithNetwork:scannedNetwork:];
```

## Instance methods

```
-[WiFiAvailabilityMatch priority];
-[WiFiAvailabilityMatch SSID];
-[WiFiAvailabilityMatch unwantedNetworkName];
-[WiFiAvailabilityMatch network];
-[WiFiAvailabilityMatch isEqualToScannedNetwork:];
-[WiFiAvailabilityMatch hash];
-[WiFiAvailabilityMatch setMatchedAt:];
-[WiFiAvailabilityMatch initWithNetwork:scannedNetwork:];
-[WiFiAvailabilityMatch description];
-[WiFiAvailabilityMatch setUnwantedNetworkName:];
-[WiFiAvailabilityMatch matchedAt];
-[WiFiAvailabilityMatch scannedNetwork];
-[WiFiAvailabilityMatch isEqual:];
-[WiFiAvailabilityMatch setScannedNetwork:];
-[WiFiAvailabilityMatch isEqualToAvailabilityMatch:];
```
