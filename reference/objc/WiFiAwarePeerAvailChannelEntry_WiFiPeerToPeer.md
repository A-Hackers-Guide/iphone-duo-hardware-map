# `WiFiAwarePeerAvailChannelEntry`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 10 instance variables, 10 properties, 15 instance methods, 1 class methods

## Instance variables

```
C _mapId;
C _usagePreference;
C _rxNSS;
C _utilization;
I _channel;
I _bandwidth;
I _band;
I _period;
I _offset;
@"NSData" _timeBitmap;
```

## Properties

```
@property (TC,R,N,V_mapId) mapId;
@property (TI,R,N,V_channel) channel;
@property (TI,R,N,V_bandwidth) bandwidth;
@property (TI,R,N,V_band) band;
@property (TI,R,N,V_period) period;
@property (TI,R,N,V_offset) offset;
@property (T@"NSData",R,N,V_timeBitmap) timeBitmap;
@property (TC,R,N,V_usagePreference) usagePreference;
@property (TC,R,N,V_rxNSS) rxNSS;
@property (TC,R,N,V_utilization) utilization;
```

## Class methods

```
+[WiFiAwarePeerAvailChannelEntry supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwarePeerAvailChannelEntry period];
-[WiFiAwarePeerAvailChannelEntry channel];
-[WiFiAwarePeerAvailChannelEntry band];
-[WiFiAwarePeerAvailChannelEntry encodeWithCoder:];
-[WiFiAwarePeerAvailChannelEntry description];
-[WiFiAwarePeerAvailChannelEntry initWithCoder:];
-[WiFiAwarePeerAvailChannelEntry bandwidth];
-[WiFiAwarePeerAvailChannelEntry copyWithZone:];
-[WiFiAwarePeerAvailChannelEntry offset];
-[WiFiAwarePeerAvailChannelEntry usagePreference];
-[WiFiAwarePeerAvailChannelEntry initWithMapId:channel:bandwidth:band:period:offset:timeBitmap:usagePreference:rxNSS:utilization:];
-[WiFiAwarePeerAvailChannelEntry mapId];
-[WiFiAwarePeerAvailChannelEntry rxNSS];
-[WiFiAwarePeerAvailChannelEntry timeBitmap];
-[WiFiAwarePeerAvailChannelEntry utilization];
```
