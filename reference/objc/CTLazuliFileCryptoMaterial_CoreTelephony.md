# `CTLazuliFileCryptoMaterial`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 6 properties, 19 instance methods, 1 class methods

## Instance variables

```
q _algorithm;
@"NSData" _key;
@"NSData" _nonce;
@"NSData" _aad;
@"NSData" _authTag;
@"NSNumber" _originalFileSizeInBytes;
```

## Properties

```
@property (Tq,N,V_algorithm) algorithm;
@property (T@"NSData",&,N,V_key) key;
@property (T@"NSData",&,N,V_nonce) nonce;
@property (T@"NSData",&,N,V_aad) aad;
@property (T@"NSData",&,N,V_authTag) authTag;
@property (T@"NSNumber",&,N,V_originalFileSizeInBytes) originalFileSizeInBytes;
```

## Class methods

```
+[CTLazuliFileCryptoMaterial supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliFileCryptoMaterial nonce];
-[CTLazuliFileCryptoMaterial algorithm];
-[CTLazuliFileCryptoMaterial setKey:];
-[CTLazuliFileCryptoMaterial setAlgorithm:];
-[CTLazuliFileCryptoMaterial encodeWithCoder:];
-[CTLazuliFileCryptoMaterial description];
-[CTLazuliFileCryptoMaterial initWithCoder:];
-[CTLazuliFileCryptoMaterial copyWithZone:];
-[CTLazuliFileCryptoMaterial isEqual:];
-[CTLazuliFileCryptoMaterial key];
-[CTLazuliFileCryptoMaterial setNonce:];
-[CTLazuliFileCryptoMaterial authTag];
-[CTLazuliFileCryptoMaterial setAuthTag:];
-[CTLazuliFileCryptoMaterial setAad:];
-[CTLazuliFileCryptoMaterial aad];
-[CTLazuliFileCryptoMaterial initWithReflection:];
-[CTLazuliFileCryptoMaterial isEqualToCTLazuliFileCryptoMaterial:];
-[CTLazuliFileCryptoMaterial originalFileSizeInBytes];
-[CTLazuliFileCryptoMaterial setOriginalFileSizeInBytes:];
```
