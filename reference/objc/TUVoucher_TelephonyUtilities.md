# `TUVoucher`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 5 properties, 15 instance methods, 2 class methods

## Instance variables

```
@"TUHandle" _handle;
@"NSString" _tokenPrefixedURI;
@"NSData" _encryptedData;
@"NSData" _unsafeData;
```

## Properties

```
@property (T@"NSData",R,C,N,V_encryptedData) encryptedData;
@property (T@"NSData",R,C,N,V_unsafeData) unsafeData;
@property (T@"NSData",R,C,N) data;
@property (T@"TUHandle",R,N,V_handle) handle;
@property (T@"NSString",R,C,N,V_tokenPrefixedURI) tokenPrefixedURI;
```

## Class methods

```
+[TUVoucher supportsSecureCoding];
+[TUVoucher voucherFromMessagingData:];
```

## Instance methods

```
-[TUVoucher data];
-[TUVoucher messagingData];
-[TUVoucher handle];
-[TUVoucher encodeWithCoder:];
-[TUVoucher hash];
-[TUVoucher description];
-[TUVoucher initWithCoder:];
-[TUVoucher copyWithZone:];
-[TUVoucher isEqual:];
-[TUVoucher encryptedData];
-[TUVoucher initWithHandle:tokenPrefixedURI:data:encryptedData:];
-[TUVoucher initWithVoucher:];
-[TUVoucher isEqualToVoucher:];
-[TUVoucher tokenPrefixedURI];
-[TUVoucher unsafeData];
```
