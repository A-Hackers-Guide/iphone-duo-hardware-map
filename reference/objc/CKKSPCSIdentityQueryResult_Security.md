# `CKKSPCSIdentityQueryResult`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSNumber" _serviceNumber;
@"NSString" _publicKey;
@"NSString" _zoneID;
@"NSDictionary" _decryptedRecord;
```

## Properties

```
@property (T@"NSNumber",&,V_serviceNumber) serviceNumber;
@property (T@"NSString",&,V_publicKey) publicKey;
@property (T@"NSString",&,V_zoneID) zoneID;
@property (T@"NSDictionary",&,V_decryptedRecord) decryptedRecord;
```

## Class methods

```
+[CKKSPCSIdentityQueryResult supportsSecureCoding];
```

## Instance methods

```
-[CKKSPCSIdentityQueryResult publicKey];
-[CKKSPCSIdentityQueryResult setZoneID:];
-[CKKSPCSIdentityQueryResult setPublicKey:];
-[CKKSPCSIdentityQueryResult zoneID];
-[CKKSPCSIdentityQueryResult encodeWithCoder:];
-[CKKSPCSIdentityQueryResult description];
-[CKKSPCSIdentityQueryResult initWithCoder:];
-[CKKSPCSIdentityQueryResult decryptedRecord];
-[CKKSPCSIdentityQueryResult initWithServiceNumber:publicKey:zoneID:decryptedRecord:];
-[CKKSPCSIdentityQueryResult serviceNumber];
-[CKKSPCSIdentityQueryResult setDecryptedRecord:];
-[CKKSPCSIdentityQueryResult setServiceNumber:];
```
