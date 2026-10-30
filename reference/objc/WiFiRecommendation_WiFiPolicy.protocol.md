# `WiFiRecommendation` (protocol)

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 5 properties, 5 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,C,N) SSID;
@property (T@"<WiFiCandidateNetwork>",R,N) network;
@property (Tq,R,N) priority;
@property (T@"<WiFiScannedNetwork>",R,N) scannedNetwork;
@property (TB,R,N) unwantedNetworkName;
```

## Instance methods

```
-[WiFiRecommendation priority];
-[WiFiRecommendation SSID];
-[WiFiRecommendation unwantedNetworkName];
-[WiFiRecommendation network];
-[WiFiRecommendation scannedNetwork];
```
