# `WiFiAwarePairingConfiguration`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 3 instance variables, 3 properties, 13 instance methods, 1 class methods

## Instance variables

```
B _pairingCachingEnabled;
@"NSArray" _supportedPairSetupMethods;
q _pairingSetupMode;
```

## Properties

```
@property (T@"NSArray",C,N,V_supportedPairSetupMethods) supportedPairSetupMethods;
@property (TB,N,V_pairingCachingEnabled) pairingCachingEnabled;
@property (Tq,N,V_pairingSetupMode) pairingSetupMode;
```

## Class methods

```
+[WiFiAwarePairingConfiguration supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwarePairingConfiguration encodeWithCoder:];
-[WiFiAwarePairingConfiguration description];
-[WiFiAwarePairingConfiguration initWithCoder:];
-[WiFiAwarePairingConfiguration copyWithZone:];
-[WiFiAwarePairingConfiguration isEqual:];
-[WiFiAwarePairingConfiguration initWithSupportedPairSetupMethods:pairingCachingEnabled:];
-[WiFiAwarePairingConfiguration setPairingCachingEnabled:];
-[WiFiAwarePairingConfiguration supportedPairSetupMethods];
-[WiFiAwarePairingConfiguration setPairingSetupMode:];
-[WiFiAwarePairingConfiguration initWithSupportedPairSetupMethods:pairingCachingEnabled:pairingSetupMode:];
-[WiFiAwarePairingConfiguration pairingCachingEnabled];
-[WiFiAwarePairingConfiguration pairingSetupMode];
-[WiFiAwarePairingConfiguration setSupportedPairSetupMethods:];
```
