# `MSDecodeOptions`

- Image: [`/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`](../userland/System__Library__PrivateFrameworks__MessageSecurity.framework__MessageSecurity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 24 instance methods, 0 class methods

## Instance variables

```
B _verifySignatures;
B _verifySigners;
B _verifyTimestamps;
@"NSArray" _signerPolicies;
@"NSDate" _verifyTime;
^{__SecIdentity=} _identity;
@"NSData" _key;
@"NSData" _LAContext;
@"NSArray" _additionalCertificates;
@"NSArray" _anchorCertificates;
```

## Properties

```
@property (TB,V_verifySignatures) verifySignatures;
@property (TB,V_verifySigners) verifySigners;
@property (TB,V_verifyTimestamps) verifyTimestamps;
@property (T@"NSArray",&,V_signerPolicies) signerPolicies;
@property (T@"NSDate",&,V_verifyTime) verifyTime;
@property (T^{__SecIdentity=},V_identity) identity;
@property (T@"NSData",&,V_key) key;
@property (T@"NSData",&,V_LAContext) LAContext;
@property (T@"NSArray",&,V_additionalCertificates) additionalCertificates;
@property (T@"NSArray",&,V_anchorCertificates) anchorCertificates;
```

## Instance methods

```
-[MSDecodeOptions init];
-[MSDecodeOptions dealloc];
-[MSDecodeOptions LAContext];
-[MSDecodeOptions setIdentity:];
-[MSDecodeOptions setKey:];
-[MSDecodeOptions identity];
-[MSDecodeOptions setLAContext:];
-[MSDecodeOptions key];
-[MSDecodeOptions setAdditionalCertificates:];
-[MSDecodeOptions additionalCertificates];
-[MSDecodeOptions anchorCertificates];
-[MSDecodeOptions initWithDecryptionIdentity:];
-[MSDecodeOptions initWithDecryptionKey:];
-[MSDecodeOptions setAnchorCertificates:];
-[MSDecodeOptions setSignerPolicies:];
-[MSDecodeOptions setVerifySignatures:];
-[MSDecodeOptions setVerifySigners:];
-[MSDecodeOptions setVerifyTime:];
-[MSDecodeOptions setVerifyTimestamps:];
-[MSDecodeOptions signerPolicies];
-[MSDecodeOptions verifySignatures];
-[MSDecodeOptions verifySigners];
-[MSDecodeOptions verifyTime];
-[MSDecodeOptions verifyTimestamps];
```
