# `WiFiAwarePairingMetadata`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 6 instance variables, 6 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"NSString" _bundleID;
@"NSString" _selfPairingName;
@"NSString" _peerDeviceName;
q _storageClass;
d _lifetime;
q _pairingClient;
```

## Properties

```
@property (T@"NSString",C,N,V_bundleID) bundleID;
@property (T@"NSString",C,N,V_selfPairingName) selfPairingName;
@property (T@"NSString",C,N,V_peerDeviceName) peerDeviceName;
@property (Tq,N,V_storageClass) storageClass;
@property (Td,N,V_lifetime) lifetime;
@property (Tq,N,V_pairingClient) pairingClient;
```

## Class methods

```
+[WiFiAwarePairingMetadata supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwarePairingMetadata setBundleID:];
-[WiFiAwarePairingMetadata encodeWithCoder:];
-[WiFiAwarePairingMetadata description];
-[WiFiAwarePairingMetadata initWithCoder:];
-[WiFiAwarePairingMetadata bundleID];
-[WiFiAwarePairingMetadata lifetime];
-[WiFiAwarePairingMetadata copyWithZone:];
-[WiFiAwarePairingMetadata storageClass];
-[WiFiAwarePairingMetadata setLifetime:];
-[WiFiAwarePairingMetadata initWithBundleID:selfPairingName:peerDeviceName:storageClass:lifetime:pairingClient:];
-[WiFiAwarePairingMetadata pairingClient];
-[WiFiAwarePairingMetadata setPairingClient:];
-[WiFiAwarePairingMetadata selfPairingName];
-[WiFiAwarePairingMetadata peerDeviceName];
-[WiFiAwarePairingMetadata setPeerDeviceName:];
-[WiFiAwarePairingMetadata setSelfPairingName:];
-[WiFiAwarePairingMetadata setStorageClass:];
```
