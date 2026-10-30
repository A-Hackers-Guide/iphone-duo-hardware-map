# `CKKSPCSIdentityQuery`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSNumber" _serviceNumber;
@"NSString" _accessGroup;
@"NSString" _publicKey;
@"NSString" _zoneID;
```

## Properties

```
@property (T@"NSNumber",&,V_serviceNumber) serviceNumber;
@property (T@"NSString",&,V_accessGroup) accessGroup;
@property (T@"NSString",&,V_publicKey) publicKey;
@property (T@"NSString",&,V_zoneID) zoneID;
```

## Class methods

```
+[CKKSPCSIdentityQuery supportsSecureCoding];
```

## Instance methods

```
-[CKKSPCSIdentityQuery publicKey];
-[CKKSPCSIdentityQuery setZoneID:];
-[CKKSPCSIdentityQuery setPublicKey:];
-[CKKSPCSIdentityQuery setAccessGroup:];
-[CKKSPCSIdentityQuery accessGroup];
-[CKKSPCSIdentityQuery zoneID];
-[CKKSPCSIdentityQuery encodeWithCoder:];
-[CKKSPCSIdentityQuery description];
-[CKKSPCSIdentityQuery initWithCoder:];
-[CKKSPCSIdentityQuery initWithServiceNumber:accessGroup:publicKey:zoneID:];
-[CKKSPCSIdentityQuery serviceNumber];
-[CKKSPCSIdentityQuery setServiceNumber:];
```
