# `FudPersonalizationObjectInfo`

- Image: [`/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/MobileAccessoryUpdater`](../userland/System__Library__PrivateFrameworks__MobileAccessoryUpdater.framework__MobileAccessoryUpdater.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 8 instance variables, 5 properties, 16 instance methods, 1 class methods

## Instance variables

```
B _esecSet;
B _eproSet;
B _trustedSet;
B _trusted;
B _effectiveProductionMode;
B _effectiveSecurityMode;
@"NSString" _objectTag;
@"NSData" _digest;
```

## Properties

```
@property (T@"NSString",R,C,N,V_objectTag) objectTag;
@property (T@"NSData",&,N,V_digest) digest;
@property (TB,N,V_trusted) trusted;
@property (TB,N,V_effectiveProductionMode) effectiveProductionMode;
@property (TB,N,V_effectiveSecurityMode) effectiveSecurityMode;
```

## Class methods

```
+[FudPersonalizationObjectInfo supportsSecureCoding];
```

## Instance methods

```
-[FudPersonalizationObjectInfo digest];
-[FudPersonalizationObjectInfo trusted];
-[FudPersonalizationObjectInfo dealloc];
-[FudPersonalizationObjectInfo encodeWithCoder:];
-[FudPersonalizationObjectInfo initWithTag:];
-[FudPersonalizationObjectInfo initWithCoder:];
-[FudPersonalizationObjectInfo setDigest:];
-[FudPersonalizationObjectInfo setTrusted:];
-[FudPersonalizationObjectInfo effectiveProductionMode];
-[FudPersonalizationObjectInfo effectiveSecurityMode];
-[FudPersonalizationObjectInfo setEffectiveProductionMode:];
-[FudPersonalizationObjectInfo setEffectiveSecurityMode:];
-[FudPersonalizationObjectInfo isEffectiveProductionModeSet];
-[FudPersonalizationObjectInfo isEffectiveSecurityModeSet];
-[FudPersonalizationObjectInfo isTrustedSet];
-[FudPersonalizationObjectInfo objectTag];
```
