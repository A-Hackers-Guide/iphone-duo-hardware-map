# `WiFiAwareFastDiscoveryConfiguration`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 2 instance variables, 2 properties, 10 instance methods, 1 class methods

## Instance variables

```
C _peerBandInformation;
@"NSNumber" _instantCommunicationChannel;
```

## Properties

```
@property (T@"NSNumber",C,N,V_instantCommunicationChannel) instantCommunicationChannel;
@property (TC,N,V_peerBandInformation) peerBandInformation;
```

## Class methods

```
+[WiFiAwareFastDiscoveryConfiguration supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwareFastDiscoveryConfiguration init];
-[WiFiAwareFastDiscoveryConfiguration encodeWithCoder:];
-[WiFiAwareFastDiscoveryConfiguration description];
-[WiFiAwareFastDiscoveryConfiguration initWithCoder:];
-[WiFiAwareFastDiscoveryConfiguration copyWithZone:];
-[WiFiAwareFastDiscoveryConfiguration isEqual:];
-[WiFiAwareFastDiscoveryConfiguration setInstantCommunicationChannel:];
-[WiFiAwareFastDiscoveryConfiguration instantCommunicationChannel];
-[WiFiAwareFastDiscoveryConfiguration peerBandInformation];
-[WiFiAwareFastDiscoveryConfiguration setPeerBandInformation:];
```
