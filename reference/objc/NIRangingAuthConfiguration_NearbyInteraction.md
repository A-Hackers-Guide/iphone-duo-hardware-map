# `NIRangingAuthConfiguration`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NIConfiguration`
- 5 instance variables, 5 properties, 14 instance methods, 1 class methods

## Instance variables

```
B _isResponder;
@"NIDiscoveryToken" _peerToken;
@"NSData" _macAddress;
@"NSData" _secureKey;
@"NIRangingAuthUWBInfo" _peerUWBRangingAuthInfo;
```

## Properties

```
@property (TB,R,N,V_isResponder) isResponder;
@property (T@"NIDiscoveryToken",R,C,N,V_peerToken) peerToken;
@property (T@"NSData",R,C,N,V_macAddress) macAddress;
@property (T@"NSData",R,C,N,V_secureKey) secureKey;
@property (T@"NIRangingAuthUWBInfo",R,C,N,V_peerUWBRangingAuthInfo) peerUWBRangingAuthInfo;
```

## Class methods

```
+[NIRangingAuthConfiguration supportsSecureCoding];
```

## Instance methods

```
-[NIRangingAuthConfiguration macAddress];
-[NIRangingAuthConfiguration descriptionInternal];
-[NIRangingAuthConfiguration encodeWithCoder:];
-[NIRangingAuthConfiguration hash];
-[NIRangingAuthConfiguration description];
-[NIRangingAuthConfiguration initWithCoder:];
-[NIRangingAuthConfiguration copyWithZone:];
-[NIRangingAuthConfiguration isEqual:];
-[NIRangingAuthConfiguration initAsResponder:macAddress:key:];
-[NIRangingAuthConfiguration initAsResponder:macAddress:key:peerUWBRangingAuthInfo:];
-[NIRangingAuthConfiguration isResponder];
-[NIRangingAuthConfiguration peerToken];
-[NIRangingAuthConfiguration peerUWBRangingAuthInfo];
-[NIRangingAuthConfiguration secureKey];
```
