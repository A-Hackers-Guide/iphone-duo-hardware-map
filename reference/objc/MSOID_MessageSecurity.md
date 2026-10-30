# `MSOID`

- Image: [`/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`](../userland/System__Library__PrivateFrameworks__MessageSecurity.framework__MessageSecurity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 5 properties, 18 instance methods, 8 class methods

## Instance variables

```
@"NSData" _OIDBytes;
@"NSString" _OIDString;
{heim_oid="length"Q"components"^I} _Asn1OID;
```

## Properties

```
@property (T{heim_oid=Q^I},R,V_Asn1OID) Asn1OID;
@property (Tr^{ccdigest_info=QQQQ*^v^?^?i^?},R) ccdigest;
@property (T@"NSData",R,V_OIDBytes) OIDBytes;
@property (T@"NSString",R,V_OIDString) OIDString;
@property (T^{__CFString=},R) secKeyAlgorithm;
```

## Class methods

```
+[MSOID OIDWithString:error:];
+[MSOID ECSignatureOIDWithDigestAlgorithm:error:];
+[MSOID OIDWithAsn1OID:error:];
+[MSOID HybridSignatureOIDWithDigestAlgorithm:error:];
+[MSOID OIDWithData:error:];
+[MSOID RSASignatureOIDWithDigestAlgorithm:error:];
+[MSOID digestOIDWithSignatureAlgorithm:error:];
+[MSOID signatureAlgorithmOIDWithSecKeyAlgorithm:error:];
```

## Instance methods

```
-[MSOID OIDString];
-[MSOID initSignatureOIDWithSecKeyAlgorithm:error:];
-[MSOID dealloc];
-[MSOID initRSASignatureOIDWithDigestAlgorithm:error:];
-[MSOID initWithData:error:];
-[MSOID ccdigest];
-[MSOID isEqualToString:];
-[MSOID initDigestOIDWithSignatureAlgorithm:error:];
-[MSOID Asn1OID];
-[MSOID OIDBytes];
-[MSOID hash];
-[MSOID initHybridSignatureOIDWithDigestAlgorithm:error:];
-[MSOID setAsn1OidFromOIDString:error:];
-[MSOID initWithAsn1OID:error:];
-[MSOID initWithString:error:];
-[MSOID isEqual:];
-[MSOID secKeyAlgorithm];
-[MSOID initECSignatureOIDWithDigestAlgorithm:error:];
```
