# `WiFiAwareSrvSessionInfo`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 6 instance variables, 6 properties, 11 instance methods, 1 class methods

## Instance variables

```
C _srvId;
I _numofPeers;
Q _srvType;
@"NSString" _srvName;
@"NSData" _srvHash;
@"NSArray" _ndiInfos;
```

## Properties

```
@property (TC,R,N,V_srvId) srvId;
@property (TQ,R,N,V_srvType) srvType;
@property (T@"NSString",R,N,V_srvName) srvName;
@property (T@"NSData",R,N,V_srvHash) srvHash;
@property (T@"NSArray",R,N,V_ndiInfos) ndiInfos;
@property (TI,R,N,V_numofPeers) numofPeers;
```

## Class methods

```
+[WiFiAwareSrvSessionInfo supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwareSrvSessionInfo encodeWithCoder:];
-[WiFiAwareSrvSessionInfo description];
-[WiFiAwareSrvSessionInfo initWithCoder:];
-[WiFiAwareSrvSessionInfo copyWithZone:];
-[WiFiAwareSrvSessionInfo srvHash];
-[WiFiAwareSrvSessionInfo srvType];
-[WiFiAwareSrvSessionInfo srvName];
-[WiFiAwareSrvSessionInfo initWithSrvId:srvType:srvName:srvHash:ndiInfos:numofPeers:];
-[WiFiAwareSrvSessionInfo ndiInfos];
-[WiFiAwareSrvSessionInfo numofPeers];
-[WiFiAwareSrvSessionInfo srvId];
```
