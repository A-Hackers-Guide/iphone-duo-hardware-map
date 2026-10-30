# `CTLazuliFileDispositionInformation`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 8 instance variables, 9 properties, 26 instance methods, 1 class methods

## Instance variables

```
@"NSNumber" _fileSizeInBytes;
@"NSString" _originalFileName;
@"NSString" _untrustedContentType;
@"NSURL" _dataUrl;
@"NSString" _validUntil;
q _disposition;
@"NSNumber" _playingLengthInSeconds;
@"CTLazuliFileCryptoMaterial" _cryptoMaterial;
```

## Properties

```
@property (T@"NSString",&,N) contentType;
@property (T@"NSNumber",&,N,V_fileSizeInBytes) fileSizeInBytes;
@property (T@"NSString",&,N,V_originalFileName) originalFileName;
@property (T@"NSString",&,N,V_untrustedContentType) untrustedContentType;
@property (T@"NSURL",&,N,V_dataUrl) dataUrl;
@property (T@"NSString",&,N,V_validUntil) validUntil;
@property (Tq,N,V_disposition) disposition;
@property (T@"NSNumber",&,N,V_playingLengthInSeconds) playingLengthInSeconds;
@property (T@"CTLazuliFileCryptoMaterial",&,N,V_cryptoMaterial) cryptoMaterial;
```

## Class methods

```
+[CTLazuliFileDispositionInformation supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliFileDispositionInformation disposition];
-[CTLazuliFileDispositionInformation setContentType:];
-[CTLazuliFileDispositionInformation validUntil];
-[CTLazuliFileDispositionInformation init];
-[CTLazuliFileDispositionInformation contentType];
-[CTLazuliFileDispositionInformation setDisposition:];
-[CTLazuliFileDispositionInformation encodeWithCoder:];
-[CTLazuliFileDispositionInformation description];
-[CTLazuliFileDispositionInformation initWithCoder:];
-[CTLazuliFileDispositionInformation copyWithZone:];
-[CTLazuliFileDispositionInformation isEqual:];
-[CTLazuliFileDispositionInformation originalFileName];
-[CTLazuliFileDispositionInformation setOriginalFileName:];
-[CTLazuliFileDispositionInformation dataUrl];
-[CTLazuliFileDispositionInformation fileSizeInBytes];
-[CTLazuliFileDispositionInformation cryptoMaterial];
-[CTLazuliFileDispositionInformation initWithReflection:];
-[CTLazuliFileDispositionInformation isEqualToCTLazuliFileDispositionInformation:];
-[CTLazuliFileDispositionInformation playingLengthInSeconds];
-[CTLazuliFileDispositionInformation setCryptoMaterial:];
-[CTLazuliFileDispositionInformation setDataUrl:];
-[CTLazuliFileDispositionInformation setFileSizeInBytes:];
-[CTLazuliFileDispositionInformation setPlayingLengthInSeconds:];
-[CTLazuliFileDispositionInformation setUntrustedContentType:];
-[CTLazuliFileDispositionInformation setValidUntil:];
-[CTLazuliFileDispositionInformation untrustedContentType];
```
