# `WiFiAwarePeerInfo`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 5 instance variables, 5 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"WiFiMACAddress" _peerAddress;
@"NSArray" _committedEntries;
@"NSArray" _potentialChannelEntries;
@"NSArray" _potentialBandEntries;
@"NSArray" _conditionalEntries;
```

## Properties

```
@property (T@"WiFiMACAddress",R,N,V_peerAddress) peerAddress;
@property (T@"NSArray",R,N,V_committedEntries) committedEntries;
@property (T@"NSArray",R,N,V_potentialChannelEntries) potentialChannelEntries;
@property (T@"NSArray",R,N,V_potentialBandEntries) potentialBandEntries;
@property (T@"NSArray",R,N,V_conditionalEntries) conditionalEntries;
```

## Class methods

```
+[WiFiAwarePeerInfo supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwarePeerInfo peerAddress];
-[WiFiAwarePeerInfo encodeWithCoder:];
-[WiFiAwarePeerInfo description];
-[WiFiAwarePeerInfo initWithCoder:];
-[WiFiAwarePeerInfo copyWithZone:];
-[WiFiAwarePeerInfo committedEntries];
-[WiFiAwarePeerInfo conditionalEntries];
-[WiFiAwarePeerInfo initWithPeerAddress:committedEntries:potentialChannelEntries:potentialBandEntries:conditionalEntries:];
-[WiFiAwarePeerInfo potentialBandEntries];
-[WiFiAwarePeerInfo potentialChannelEntries];
```
