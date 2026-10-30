# `WiFiAwareDataPathSessionInfo`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 7 instance variables, 7 properties, 12 instance methods, 1 class methods

## Instance variables

```
C _dpId;
C _serviceId;
Q _dpRole;
@"WiFiMACAddress" _initiatorDataAddress;
@"WiFiMACAddress" _peerNmiMacAddress;
@"WiFiMACAddress" _peerDataAddress;
Q _sessionState;
```

## Properties

```
@property (TC,R,N,V_dpId) dpId;
@property (TQ,R,N,V_dpRole) dpRole;
@property (TC,R,N,V_serviceId) serviceId;
@property (T@"WiFiMACAddress",R,N,V_initiatorDataAddress) initiatorDataAddress;
@property (T@"WiFiMACAddress",R,N,V_peerNmiMacAddress) peerNmiMacAddress;
@property (T@"WiFiMACAddress",R,N,V_peerDataAddress) peerDataAddress;
@property (TQ,R,N,V_sessionState) sessionState;
```

## Class methods

```
+[WiFiAwareDataPathSessionInfo supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwareDataPathSessionInfo sessionState];
-[WiFiAwareDataPathSessionInfo init];
-[WiFiAwareDataPathSessionInfo serviceId];
-[WiFiAwareDataPathSessionInfo encodeWithCoder:];
-[WiFiAwareDataPathSessionInfo initWithCoder:];
-[WiFiAwareDataPathSessionInfo copyWithZone:];
-[WiFiAwareDataPathSessionInfo initiatorDataAddress];
-[WiFiAwareDataPathSessionInfo peerDataAddress];
-[WiFiAwareDataPathSessionInfo dpId];
-[WiFiAwareDataPathSessionInfo dpRole];
-[WiFiAwareDataPathSessionInfo initWithDpId:dpRole:serviceId:initiatorDataAddress:peerNmiMacAddress:peerDataAddress:sessionState:];
-[WiFiAwareDataPathSessionInfo peerNmiMacAddress];
```
