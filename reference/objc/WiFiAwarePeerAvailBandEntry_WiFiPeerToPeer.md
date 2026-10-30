# `WiFiAwarePeerAvailBandEntry`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 5 instance variables, 5 properties, 10 instance methods, 1 class methods

## Instance variables

```
C _mapId;
C _usagePreference;
C _rxNSS;
C _utilization;
@"NSArray" _bands;
```

## Properties

```
@property (TC,R,N,V_mapId) mapId;
@property (T@"NSArray",R,N,V_bands) bands;
@property (TC,R,N,V_usagePreference) usagePreference;
@property (TC,R,N,V_rxNSS) rxNSS;
@property (TC,R,N,V_utilization) utilization;
```

## Class methods

```
+[WiFiAwarePeerAvailBandEntry supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwarePeerAvailBandEntry bands];
-[WiFiAwarePeerAvailBandEntry encodeWithCoder:];
-[WiFiAwarePeerAvailBandEntry description];
-[WiFiAwarePeerAvailBandEntry initWithCoder:];
-[WiFiAwarePeerAvailBandEntry copyWithZone:];
-[WiFiAwarePeerAvailBandEntry usagePreference];
-[WiFiAwarePeerAvailBandEntry initWithMapId:bands:usagePreference:rxNSS:utilization:];
-[WiFiAwarePeerAvailBandEntry mapId];
-[WiFiAwarePeerAvailBandEntry rxNSS];
-[WiFiAwarePeerAvailBandEntry utilization];
```
