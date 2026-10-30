# `CTLazuliMessageID`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"NSString" _uuid;
@"CTLazuliSecureGroupVersion" _secureGroupVersion;
@"CTLazuliOriginalMessageID" _originalId;
```

## Properties

```
@property (T@"NSString",C,N,V_uuid) uuid;
@property (T@"CTLazuliSecureGroupVersion",C,N,V_secureGroupVersion) secureGroupVersion;
@property (T@"CTLazuliOriginalMessageID",C,N,V_originalId) originalId;
```

## Class methods

```
+[CTLazuliMessageID supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliMessageID uuid];
-[CTLazuliMessageID setUuid:];
-[CTLazuliMessageID encodeWithCoder:];
-[CTLazuliMessageID description];
-[CTLazuliMessageID initWithCoder:];
-[CTLazuliMessageID copyWithZone:];
-[CTLazuliMessageID isEqual:];
-[CTLazuliMessageID extractRawMessageID];
-[CTLazuliMessageID initWithReflection:];
-[CTLazuliMessageID isEqualToCTLazuliMessageID:];
-[CTLazuliMessageID originalId];
-[CTLazuliMessageID secureGroupVersion];
-[CTLazuliMessageID setOriginalId:];
-[CTLazuliMessageID setSecureGroupVersion:];
```
