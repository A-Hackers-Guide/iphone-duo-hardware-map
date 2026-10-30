# `WiFiAwareChannelSchedule`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 5 instance variables, 5 properties, 10 instance methods, 1 class methods

## Instance variables

```
I _channel;
I _bandwidth;
I _band;
I _period;
@"NSData" _timeBitmap;
```

## Properties

```
@property (TI,R,N,V_channel) channel;
@property (TI,R,N,V_bandwidth) bandwidth;
@property (TI,R,N,V_band) band;
@property (TI,R,N,V_period) period;
@property (T@"NSData",R,N,V_timeBitmap) timeBitmap;
```

## Class methods

```
+[WiFiAwareChannelSchedule supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwareChannelSchedule period];
-[WiFiAwareChannelSchedule channel];
-[WiFiAwareChannelSchedule band];
-[WiFiAwareChannelSchedule encodeWithCoder:];
-[WiFiAwareChannelSchedule description];
-[WiFiAwareChannelSchedule initWithCoder:];
-[WiFiAwareChannelSchedule bandwidth];
-[WiFiAwareChannelSchedule copyWithZone:];
-[WiFiAwareChannelSchedule initWithChannel:bandwidth:band:period:timeBitmap:];
-[WiFiAwareChannelSchedule timeBitmap];
```
