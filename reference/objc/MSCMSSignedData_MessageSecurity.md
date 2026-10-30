# `MSCMSSignedData`

- Image: [`/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`](../userland/System__Library__PrivateFrameworks__MessageSecurity.framework__MessageSecurity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MSCMSMessage`
- 10 instance variables, 15 properties, 46 instance methods, 2 class methods

## Instance variables

```
B _detached;
B _contentChanged;
@"NSData" _dataContent;
@"<MSCMSMessage>" _embeddedContent;
@"MSOID" _contentType;
@"NSArray" _signers;
@"NSSet" _digestAlgorithms;
@"NSMutableSet" _certificates;
@"NSNumber" _version;
@"MSDecodeOptions" _options;
```

## Properties

```
@property (T@"NSNumber",&,V_version) version;
@property (T@"NSArray",&,V_signers) signers;
@property (T@"NSSet",&,V_digestAlgorithms) digestAlgorithms;
@property (T@"MSDecodeOptions",&,V_options) options;
@property (TB,V_contentChanged) contentChanged;
@property (TB,V_detached) detached;
@property (T@"NSMutableSet",&,V_certificates) certificates;
@property (T@"MSOID",R) type;
@property (T@"NSData",&,N,V_dataContent) dataContent;
@property (T@"<MSCMSMessage>",&,V_embeddedContent) embeddedContent;
@property (T@"MSOID",&,V_contentType) contentType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MSCMSSignedData decodeMessageSecurityObject:options:error:];
+[MSCMSSignedData isImplementedInObjectiveC];
```

## Instance methods

```
-[MSCMSSignedData certificates];
-[MSCMSSignedData setContentType:];
-[MSCMSSignedData addCounterSignerCertificates:mode:error:];
-[MSCMSSignedData encodeMessageSecurityObject:];
-[MSCMSSignedData initWithDataContent:isDetached:signer:error:];
-[MSCMSSignedData initWithEmbeddedContent:signer:additionalCertificates:error:];
-[MSCMSSignedData setOptions:];
-[MSCMSSignedData removeSignersWithIdentity:error:];
-[MSCMSSignedData removeSignerCertificatesWithIndexes:];
-[MSCMSSignedData signers];
-[MSCMSSignedData setCertificates:];
-[MSCMSSignedData removeSignersWithIndexes:error:];
-[MSCMSSignedData contentType];
-[MSCMSSignedData addCertificatesForSigner:mode:error:];
-[MSCMSSignedData setContentChanged:];
-[MSCMSSignedData addDigestAlgorithmFromSigner:];
-[MSCMSSignedData initCertsOnlyWithCertificates:error:];
-[MSCMSSignedData embeddedContent];
-[MSCMSSignedData addSigner:];
-[MSCMSSignedData version];
-[MSCMSSignedData setDetached:];
-[MSCMSSignedData verifySignaturesAndSignersWithPolicies:verifyTime:error:];
-[MSCMSSignedData initWithDataContent:isDetached:signer:additionalCertificates:error:];
-[MSCMSSignedData removeSignersWithEmailAddress:error:];
-[MSCMSSignedData digestAlgorithms];
-[MSCMSSignedData removeSignersWithCertificate:error:];
-[MSCMSSignedData type];
-[MSCMSSignedData initWithDataContent:isDetached:signer:signerChainMode:error:];
-[MSCMSSignedData initWithEmbeddedContent:signer:signerChainMode:error:];
-[MSCMSSignedData calculateContentDigestWithAlgorithm:error:];
-[MSCMSSignedData verifySignatures:];
-[MSCMSSignedData detached];
-[MSCMSSignedData addSigner:withChainMode:error:];
-[MSCMSSignedData setEmbeddedContent:];
-[MSCMSSignedData getSignerCertificate:error:];
-[MSCMSSignedData setVersion:];
-[MSCMSSignedData options];
-[MSCMSSignedData addSigner:withCertificates:];
-[MSCMSSignedData contentChanged];
-[MSCMSSignedData checkSignedPerRFC5652:];
-[MSCMSSignedData initWithEmbeddedContent:signer:error:];
-[MSCMSSignedData dataContent];
-[MSCMSSignedData setDigestAlgorithms:];
-[MSCMSSignedData setDataContent:];
-[MSCMSSignedData setSigners:];
-[MSCMSSignedData verifySignaturesAndSignersWithPolicies:verifyTime:anchorCertificates:error:];
```
