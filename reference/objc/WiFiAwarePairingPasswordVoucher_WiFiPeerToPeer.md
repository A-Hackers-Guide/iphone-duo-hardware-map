# `WiFiAwarePairingPasswordVoucher`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 5 instance variables, 5 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _token;
q _pairingMode;
@"NSString" _password;
Q _usageCount;
@"NSDate" _expiration;
```

## Properties

```
@property (T@"NSUUID",C,N,V_token) token;
@property (Tq,N,V_pairingMode) pairingMode;
@property (T@"NSString",C,N,V_password) password;
@property (TQ,N,V_usageCount) usageCount;
@property (T@"NSDate",C,N,V_expiration) expiration;
```

## Class methods

```
+[WiFiAwarePairingPasswordVoucher supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwarePairingPasswordVoucher expiration];
-[WiFiAwarePairingPasswordVoucher setExpiration:];
-[WiFiAwarePairingPasswordVoucher encodeWithCoder:];
-[WiFiAwarePairingPasswordVoucher description];
-[WiFiAwarePairingPasswordVoucher initWithCoder:];
-[WiFiAwarePairingPasswordVoucher token];
-[WiFiAwarePairingPasswordVoucher setToken:];
-[WiFiAwarePairingPasswordVoucher setPassword:];
-[WiFiAwarePairingPasswordVoucher copyWithZone:];
-[WiFiAwarePairingPasswordVoucher password];
-[WiFiAwarePairingPasswordVoucher pairingMode];
-[WiFiAwarePairingPasswordVoucher usageCount];
-[WiFiAwarePairingPasswordVoucher setUsageCount:];
-[WiFiAwarePairingPasswordVoucher setPairingMode:];
-[WiFiAwarePairingPasswordVoucher initWithToken:pairingMode:password:usageCount:expiration:];
```
