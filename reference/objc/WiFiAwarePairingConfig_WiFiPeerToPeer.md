# `WiFiAwarePairingConfig`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 5 instance variables, 5 properties, 15 instance methods, 3 class methods

## Instance variables

```
I _userID;
q _pairingMode;
@"WiFiAwarePairingMetadata" _pairingMetadata;
q _pairingSetupMode;
@"NSUUID" _passwordVoucherToken;
```

## Properties

```
@property (Tq,N,V_pairingMode) pairingMode;
@property (T@"WiFiAwarePairingMetadata",&,N,V_pairingMetadata) pairingMetadata;
@property (Tq,N,V_pairingSetupMode) pairingSetupMode;
@property (TI,N,V_userID) userID;
@property (T@"NSUUID",C,N,V_passwordVoucherToken) passwordVoucherToken;
```

## Class methods

```
+[WiFiAwarePairingConfig supportsSecureCoding];
+[WiFiAwarePairingConfig stringForPairSetupMode:];
+[WiFiAwarePairingConfig stringForPairingMode:];
```

## Instance methods

```
-[WiFiAwarePairingConfig userID];
-[WiFiAwarePairingConfig setUserID:];
-[WiFiAwarePairingConfig encodeWithCoder:];
-[WiFiAwarePairingConfig description];
-[WiFiAwarePairingConfig initWithCoder:];
-[WiFiAwarePairingConfig copyWithZone:];
-[WiFiAwarePairingConfig pairingMetadata];
-[WiFiAwarePairingConfig initWithPairingMode:pairingMetadata:];
-[WiFiAwarePairingConfig setPairingMetadata:];
-[WiFiAwarePairingConfig pairingMode];
-[WiFiAwarePairingConfig setPasswordVoucherToken:];
-[WiFiAwarePairingConfig setPairingMode:];
-[WiFiAwarePairingConfig setPairingSetupMode:];
-[WiFiAwarePairingConfig pairingSetupMode];
-[WiFiAwarePairingConfig passwordVoucherToken];
```
