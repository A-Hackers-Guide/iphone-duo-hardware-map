# `MSCMSSignerInfo`

- Image: [`/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`](../userland/System__Library__PrivateFrameworks__MessageSecurity.framework__MessageSecurity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 17 instance variables, 18 properties, 70 instance methods, 1 class methods

## Instance variables

```
B _useIssuerAndSerialNumber;
B _contentChanged;
B _signatureCalculated;
@"MSAlgorithmIdentifier" _signatureAlgorithm;
^{__SecCertificate=} _signerCertificate;
@"MSCMSMutableAttributeArray" _protectedAttributes;
@"NSData" _signature;
@"MSCMSMutableAttributeArray" _unprotectedAttributes;
@"NSData" _LAContext;
^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v} _signerPrivKey;
^{SignerInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}^{heim_base_data}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}^{heim_base_data}} _encodedSignerInfo;
@"NSData" _signedAttrsData;
@"NSData" _unsignedAttrsData;
@"NSData" _identifierData;
@"NSNumber" _version;
@"MSCMSSignedData" _containingSignedData;
@"MSAlgorithmIdentifier" _digestAlgorithm;
```

## Properties

```
@property (T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},V_signerPrivKey) signerPrivKey;
@property (T^{SignerInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}^{heim_base_data}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}^{heim_base_data}},V_encodedSignerInfo) encodedSignerInfo;
@property (T^{__SecCertificate=},V_signerCertificate) signerCertificate;
@property (TB,V_useIssuerAndSerialNumber) useIssuerAndSerialNumber;
@property (T@"MSAlgorithmIdentifier",&,V_signatureAlgorithm) signatureAlgorithm;
@property (T@"NSData",&,V_signedAttrsData) signedAttrsData;
@property (T@"NSData",&,V_unsignedAttrsData) unsignedAttrsData;
@property (T@"NSData",&,V_identifierData) identifierData;
@property (T@"NSNumber",&,V_version) version;
@property (T@"MSCMSSignedData",W,V_containingSignedData) containingSignedData;
@property (T@"MSAlgorithmIdentifier",&,V_digestAlgorithm) digestAlgorithm;
@property (T@"NSArray",R) certificates;
@property (TB,V_contentChanged) contentChanged;
@property (TB,R,V_signatureCalculated) signatureCalculated;
@property (T@"MSCMSMutableAttributeArray",&,V_protectedAttributes) protectedAttributes;
@property (T@"NSData",&,N,V_signature) signature;
@property (T@"MSCMSMutableAttributeArray",&,V_unprotectedAttributes) unprotectedAttributes;
@property (T@"NSData",&,V_LAContext) LAContext;
```

## Class methods

```
+[MSCMSSignerInfo decodeSignerInfo:certificates:LAContext:error:];
```

## Instance methods

```
-[MSCMSSignerInfo certificates];
-[MSCMSSignerInfo initWithIdentity:error:];
-[MSCMSSignerInfo setSignature:];
-[MSCMSSignerInfo calculateSignerInfoDigest:];
-[MSCMSSignerInfo signerCertificate];
-[MSCMSSignerInfo encodedSignerInfo];
-[MSCMSSignerInfo setIdentifierData:];
-[MSCMSSignerInfo calculateSignedAttributesDigest:];
-[MSCMSSignerInfo initWithIdentity:signatureAlgorithm:useIssuerAndSerialNumber:error:];
-[MSCMSSignerInfo initWithEmail:signatureAlgorithm:LAContext:error:];
-[MSCMSSignerInfo useIssuerAndSerialNumber];
-[MSCMSSignerInfo initWithCertificate:recipientsAlgorithmCapabilities:error:];
-[MSCMSSignerInfo initWithCertificate:signatureAlgorithm:useIssuerAndSerialNumber:error:];
-[MSCMSSignerInfo sign:];
-[MSCMSSignerInfo dealloc];
-[MSCMSSignerInfo setContentChanged:];
-[MSCMSSignerInfo unsignedAttrsData];
-[MSCMSSignerInfo setDigestAlgorithm:];
-[MSCMSSignerInfo LAContext];
-[MSCMSSignerInfo initWithIdentity:recipientsAlgorithmCapabilities:error:];
-[MSCMSSignerInfo signature];
-[MSCMSSignerInfo digestAlgorithm];
-[MSCMSSignerInfo createTrustObjectWithPolicies:verifyTime:anchorCertificates:error:];
-[MSCMSSignerInfo verifyCountersignaturesAndCountersignersWithPolicies:verifyTime:anchorCertificates:error:];
-[MSCMSSignerInfo encodeSignerInfo:error:];
-[MSCMSSignerInfo initWithCertificate:error:];
-[MSCMSSignerInfo initWithEmail:recipientsAlgorithmCapabilities:LAContext:error:];
-[MSCMSSignerInfo version];
-[MSCMSSignerInfo verifyTime:];
-[MSCMSSignerInfo verifyMessageDigestAttribute:error:];
-[MSCMSSignerInfo verifySignature:];
-[MSCMSSignerInfo identifierData];
-[MSCMSSignerInfo addMultipleSignaturesAttribute];
-[MSCMSSignerInfo signerPrivKey];
-[MSCMSSignerInfo initWithEmail:LAContext:error:];
-[MSCMSSignerInfo setContainingSignedData:];
-[MSCMSSignerInfo setProtectedAttributes:];
-[MSCMSSignerInfo unprotectedAttributes];
-[MSCMSSignerInfo addCounterSignerAttribute:];
-[MSCMSSignerInfo setUseIssuerAndSerialNumber:];
-[MSCMSSignerInfo verifyTimestamps:error:];
-[MSCMSSignerInfo signatureCalculated];
-[MSCMSSignerInfo containingSignedData];
-[MSCMSSignerInfo getAttributesWithType:protectedAttributes:];
-[MSCMSSignerInfo setVersion:];
-[MSCMSSignerInfo setSignerPrivKey:];
-[MSCMSSignerInfo signedAttrsData];
-[MSCMSSignerInfo setUnsignedAttrsData:];
-[MSCMSSignerInfo initWithCertificate:signatureAlgorithm:error:];
-[MSCMSSignerInfo setUnprotectedAttributes:];
-[MSCMSSignerInfo setLAContext:];
-[MSCMSSignerInfo verifyContentTypeAttribute:];
-[MSCMSSignerInfo setSignerCertificate:];
-[MSCMSSignerInfo contentChanged];
-[MSCMSSignerInfo createRequiredAttributes:];
-[MSCMSSignerInfo verifyTimestamps:];
-[MSCMSSignerInfo setSignatureAlgorithm:];
-[MSCMSSignerInfo verifyCountersignatures:];
-[MSCMSSignerInfo initWithIdentity:signatureAlgorithm:error:];
-[MSCMSSignerInfo setSignedAttrsData:];
-[MSCMSSignerInfo addProtectedAttribute:];
-[MSCMSSignerInfo setEncodedSignerInfo:];
-[MSCMSSignerInfo protectedAttributes];
-[MSCMSSignerInfo addSMIMEEncryptionKeyPreferenceAttribute:];
-[MSCMSSignerInfo createTrustObjectWithPolicies:error:];
-[MSCMSSignerInfo verifySignatureAndSignerWithPolicies:verifyTime:anchorCertificates:error:];
-[MSCMSSignerInfo calculateSignatureDigestWithAlgorithm:error:];
-[MSCMSSignerInfo signatureAlgorithm];
-[MSCMSSignerInfo addSMIMECapabilitiesAttribute:];
-[MSCMSSignerInfo getAttributesWithType:];
```
