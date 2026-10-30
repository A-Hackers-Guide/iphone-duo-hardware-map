# `BLSAttribute`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCCoding`, `NSCopying`, `NSSecureCoding`
- 0 instance variables, 4 properties, 12 instance methods, 1 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSAttribute supportsSecureCoding];
```

## Instance methods

```
-[BLSAttribute init];
-[BLSAttribute initWithXPCDictionary:];
-[BLSAttribute encodeWithXPCDictionary:];
-[BLSAttribute encodeWithCoder:];
-[BLSAttribute hash];
-[BLSAttribute initWithCoder:];
-[BLSAttribute copyWithZone:];
-[BLSAttribute isEqual:];
-[BLSAttribute canBePaused];
-[BLSAttribute checkEntitlementSource:forSingleEntitlement:error:];
-[BLSAttribute checkEntitlementSourceForRequiredEntitlements:error:];
-[BLSAttribute errorForMissingEntitlement:inSource:];
```
