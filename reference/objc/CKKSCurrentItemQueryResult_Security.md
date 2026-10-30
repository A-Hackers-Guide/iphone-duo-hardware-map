# `CKKSCurrentItemQueryResult`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSString" _identifier;
@"NSString" _accessGroup;
@"NSString" _zoneID;
@"NSDictionary" _decryptedRecord;
```

## Properties

```
@property (T@"NSString",&,V_identifier) identifier;
@property (T@"NSString",&,V_accessGroup) accessGroup;
@property (T@"NSString",&,V_zoneID) zoneID;
@property (T@"NSDictionary",&,V_decryptedRecord) decryptedRecord;
```

## Class methods

```
+[CKKSCurrentItemQueryResult supportsSecureCoding];
```

## Instance methods

```
-[CKKSCurrentItemQueryResult setZoneID:];
-[CKKSCurrentItemQueryResult setAccessGroup:];
-[CKKSCurrentItemQueryResult identifier];
-[CKKSCurrentItemQueryResult accessGroup];
-[CKKSCurrentItemQueryResult zoneID];
-[CKKSCurrentItemQueryResult setIdentifier:];
-[CKKSCurrentItemQueryResult encodeWithCoder:];
-[CKKSCurrentItemQueryResult description];
-[CKKSCurrentItemQueryResult initWithCoder:];
-[CKKSCurrentItemQueryResult decryptedRecord];
-[CKKSCurrentItemQueryResult initWithIdentifier:accessGroup:zoneID:decryptedRecord:];
-[CKKSCurrentItemQueryResult setDecryptedRecord:];
```
