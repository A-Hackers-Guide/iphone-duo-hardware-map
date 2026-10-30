# `CSDMessagingVoucher`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 4 instance variables, 9 properties, 22 instance methods, 1 class methods

## Instance variables

```
@"NSData" _encryptedData;
@"CSDMessagingHandle" _handle;
@"NSString" _tokenPrefixedURI;
@"NSData" _unsafeData;
```

## Properties

```
@property (T@"TUVoucher",R,N) tuVoucher;
@property (TB,R,N) hasHandle;
@property (T@"CSDMessagingHandle",&,N,V_handle) handle;
@property (TB,R,N) hasTokenPrefixedURI;
@property (T@"NSString",&,N,V_tokenPrefixedURI) tokenPrefixedURI;
@property (TB,R,N) hasUnsafeData;
@property (T@"NSData",&,N,V_unsafeData) unsafeData;
@property (TB,R,N) hasEncryptedData;
@property (T@"NSData",&,N,V_encryptedData) encryptedData;
```

## Class methods

```
+[CSDMessagingVoucher voucherWithTUVoucher:];
```

## Instance methods

```
-[CSDMessagingVoucher writeTo:];
-[CSDMessagingVoucher mergeFrom:];
-[CSDMessagingVoucher handle];
-[CSDMessagingVoucher hasHandle];
-[CSDMessagingVoucher hash];
-[CSDMessagingVoucher copyTo:];
-[CSDMessagingVoucher description];
-[CSDMessagingVoucher setHandle:];
-[CSDMessagingVoucher readFrom:];
-[CSDMessagingVoucher copyWithZone:];
-[CSDMessagingVoucher isEqual:];
-[CSDMessagingVoucher dictionaryRepresentation];
-[CSDMessagingVoucher encryptedData];
-[CSDMessagingVoucher setEncryptedData:];
-[CSDMessagingVoucher hasEncryptedData];
-[CSDMessagingVoucher hasTokenPrefixedURI];
-[CSDMessagingVoucher hasUnsafeData];
-[CSDMessagingVoucher setTokenPrefixedURI:];
-[CSDMessagingVoucher setUnsafeData:];
-[CSDMessagingVoucher tokenPrefixedURI];
-[CSDMessagingVoucher tuVoucher];
-[CSDMessagingVoucher unsafeData];
```
