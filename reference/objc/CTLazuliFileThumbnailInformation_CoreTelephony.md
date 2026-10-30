# `CTLazuliFileThumbnailInformation`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 5 instance variables, 6 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"NSNumber" _fileSizeInBytes;
@"NSString" _untrustedContentType;
@"NSURL" _dataUrl;
@"NSString" _validUntil;
@"CTLazuliFileCryptoMaterial" _cryptoMaterial;
```

## Properties

```
@property (T@"NSString",&,N) contentType;
@property (T@"NSNumber",&,N,V_fileSizeInBytes) fileSizeInBytes;
@property (T@"NSString",&,N,V_untrustedContentType) untrustedContentType;
@property (T@"NSURL",&,N,V_dataUrl) dataUrl;
@property (T@"NSString",&,N,V_validUntil) validUntil;
@property (T@"CTLazuliFileCryptoMaterial",&,N,V_cryptoMaterial) cryptoMaterial;
```

## Class methods

```
+[CTLazuliFileThumbnailInformation supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliFileThumbnailInformation setContentType:];
-[CTLazuliFileThumbnailInformation validUntil];
-[CTLazuliFileThumbnailInformation contentType];
-[CTLazuliFileThumbnailInformation encodeWithCoder:];
-[CTLazuliFileThumbnailInformation description];
-[CTLazuliFileThumbnailInformation initWithCoder:];
-[CTLazuliFileThumbnailInformation copyWithZone:];
-[CTLazuliFileThumbnailInformation isEqual:];
-[CTLazuliFileThumbnailInformation dataUrl];
-[CTLazuliFileThumbnailInformation fileSizeInBytes];
-[CTLazuliFileThumbnailInformation cryptoMaterial];
-[CTLazuliFileThumbnailInformation initWithReflection:];
-[CTLazuliFileThumbnailInformation isEqualToCTLazuliFileThumbnailInformation:];
-[CTLazuliFileThumbnailInformation setCryptoMaterial:];
-[CTLazuliFileThumbnailInformation setDataUrl:];
-[CTLazuliFileThumbnailInformation setFileSizeInBytes:];
-[CTLazuliFileThumbnailInformation setUntrustedContentType:];
-[CTLazuliFileThumbnailInformation setValidUntil:];
-[CTLazuliFileThumbnailInformation untrustedContentType];
```
