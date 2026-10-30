# `MSCMSMultipleSignaturesAttribute`

- Image: [`/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`](../userland/System__Library__PrivateFrameworks__MessageSecurity.framework__MessageSecurity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MSCMSAttributeCoder`
- 5 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"MSCMSSignerInfo" _containingSignerInfo;
@"MSAlgorithmIdentifier" _bodyHashAlgorithm;
@"MSAlgorithmIdentifier" _signatureAlgorithm;
@"MSAlgorithmIdentifier" _signedAttrsHashAlgorithm;
@"NSData" _signedAttrsHash;
```

## Properties

```
@property (T@"MSCMSSignerInfo",W,N,V_containingSignerInfo) containingSignerInfo;
@property (T@"MSAlgorithmIdentifier",&,N,V_bodyHashAlgorithm) bodyHashAlgorithm;
@property (T@"MSAlgorithmIdentifier",&,N,V_signatureAlgorithm) signatureAlgorithm;
@property (T@"MSAlgorithmIdentifier",&,N,V_signedAttrsHashAlgorithm) signedAttrsHashAlgorithm;
@property (T@"NSData",W,N,V_signedAttrsHash) signedAttrsHash;
@property (T@"MSOID",R,&) attributeType;
```

## Instance methods

```
-[MSCMSMultipleSignaturesAttribute init];
-[MSCMSMultipleSignaturesAttribute attributeType];
-[MSCMSMultipleSignaturesAttribute containingSignerInfo];
-[MSCMSMultipleSignaturesAttribute setSignatureAlgorithm:];
-[MSCMSMultipleSignaturesAttribute setContainingSignerInfo:];
-[MSCMSMultipleSignaturesAttribute signatureAlgorithm];
-[MSCMSMultipleSignaturesAttribute initWithAttribute:error:];
-[MSCMSMultipleSignaturesAttribute signedAttrsHash];
-[MSCMSMultipleSignaturesAttribute bodyHashAlgorithm];
-[MSCMSMultipleSignaturesAttribute encodeAttributeWithError:];
-[MSCMSMultipleSignaturesAttribute setBodyHashAlgorithm:];
-[MSCMSMultipleSignaturesAttribute setSignedAttrsHash:];
-[MSCMSMultipleSignaturesAttribute setSignedAttrsHashAlgorithm:];
-[MSCMSMultipleSignaturesAttribute signedAttrsHashAlgorithm];
```
