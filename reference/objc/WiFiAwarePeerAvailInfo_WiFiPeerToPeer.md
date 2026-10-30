# `WiFiAwarePeerAvailInfo`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 2 instance variables, 2 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"WiFiAwareInterfaceInfo" _interfaceInfo;
@"NSArray" _peerInfos;
```

## Properties

```
@property (T@"WiFiAwareInterfaceInfo",R,C,N,V_interfaceInfo) interfaceInfo;
@property (T@"NSArray",R,N,V_peerInfos) peerInfos;
```

## Class methods

```
+[WiFiAwarePeerAvailInfo supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwarePeerAvailInfo init];
-[WiFiAwarePeerAvailInfo detailedDescription];
-[WiFiAwarePeerAvailInfo encodeWithCoder:];
-[WiFiAwarePeerAvailInfo description];
-[WiFiAwarePeerAvailInfo initWithCoder:];
-[WiFiAwarePeerAvailInfo copyWithZone:];
-[WiFiAwarePeerAvailInfo detailedDescriptionWithChangedOptions:previousPeerAvailInfo:forceAllChangedOptions:];
-[WiFiAwarePeerAvailInfo initWithInterfaceInfo:peerInfos:];
-[WiFiAwarePeerAvailInfo interfaceInfo];
-[WiFiAwarePeerAvailInfo peerInfos];
```
