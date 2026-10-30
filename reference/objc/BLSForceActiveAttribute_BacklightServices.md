# `BLSForceActiveAttribute`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BLSAttribute`
- Protocols: `BSXPCCoding`
- 1 instance variables, 5 properties, 11 instance methods, 3 class methods

## Instance variables

```
B _userInitiated;
```

## Properties

```
@property (TB,R,N,V_userInitiated) userInitiated;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSForceActiveAttribute supportsSecureCoding];
+[BLSForceActiveAttribute forceActive];
+[BLSForceActiveAttribute forceActiveUserInitiated:];
```

## Instance methods

```
-[BLSForceActiveAttribute userInitiated];
-[BLSForceActiveAttribute initWithXPCDictionary:];
-[BLSForceActiveAttribute encodeWithXPCDictionary:];
-[BLSForceActiveAttribute encodeWithCoder:];
-[BLSForceActiveAttribute hash];
-[BLSForceActiveAttribute description];
-[BLSForceActiveAttribute initWithCoder:];
-[BLSForceActiveAttribute copyWithZone:];
-[BLSForceActiveAttribute isEqual:];
-[BLSForceActiveAttribute checkEntitlementSourceForRequiredEntitlements:error:];
-[BLSForceActiveAttribute initWithUserInitiated:];
```
