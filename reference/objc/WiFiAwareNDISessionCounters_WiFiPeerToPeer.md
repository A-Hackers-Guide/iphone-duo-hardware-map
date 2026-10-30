# `WiFiAwareNDISessionCounters`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
I _total;
I _established;
I _with24GOnlyPeer;
I _rtm;
I _rtmWith24GOnly;
I _rtmLowLatency;
```

## Properties

```
@property (TI,R,N,V_total) total;
@property (TI,R,N,V_established) established;
@property (TI,R,N,V_with24GOnlyPeer) with24GOnlyPeer;
@property (TI,R,N,V_rtm) rtm;
@property (TI,R,N,V_rtmWith24GOnly) rtmWith24GOnly;
@property (TI,R,N,V_rtmLowLatency) rtmLowLatency;
```

## Instance methods

```
-[WiFiAwareNDISessionCounters total];
-[WiFiAwareNDISessionCounters established];
-[WiFiAwareNDISessionCounters description];
-[WiFiAwareNDISessionCounters rtm];
-[WiFiAwareNDISessionCounters with24GOnlyPeer];
-[WiFiAwareNDISessionCounters initWithTotal:established:with24GOnlyPeer:rtm:rtmWith24GOnly:rtmLowLatency:];
-[WiFiAwareNDISessionCounters rtmLowLatency];
-[WiFiAwareNDISessionCounters rtmWith24GOnly];
```
