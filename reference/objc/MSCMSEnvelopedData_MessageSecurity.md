# `MSCMSEnvelopedData`

- Image: [`/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`](../userland/System__Library__PrivateFrameworks__MessageSecurity.framework__MessageSecurity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MSCMSMessage`
- 13 instance variables, 17 properties, 43 instance methods, 2 class methods

## Instance variables

```
B _legacyASN1Encoding;
B _contentChanged;
@"MSOID" _type;
@"NSData" _dataContent;
@"<MSCMSMessage>" _embeddedContent;
@"MSOID" _contentType;
@"NSArray" _recipients;
@"MSAlgorithmIdentifier" _encryptionAlgorithm;
@"NSData" _encryptionKey;
@"NSMutableArray" _unprotectedAttributes;
@"NSMutableArray" _originatorCertificates;
@"NSData" _encryptedContent;
@"NSNumber" _version;
```

## Properties

```
@property (T@"NSArray",&,V_recipients) recipients;
@property (T@"NSData",&,V_encryptedContent) encryptedContent;
@property (TB,V_contentChanged) contentChanged;
@property (T@"NSNumber",R,V_version) version;
@property (T@"MSAlgorithmIdentifier",&,V_encryptionAlgorithm) encryptionAlgorithm;
@property (T@"NSData",&,V_encryptionKey) encryptionKey;
@property (T@"NSMutableArray",&,V_unprotectedAttributes) unprotectedAttributes;
@property (T@"NSMutableArray",&,V_originatorCertificates) originatorCertificates;
@property (TB,V_legacyASN1Encoding) legacyASN1Encoding;
@property (T@"MSOID",R,V_type) type;
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
+[MSCMSEnvelopedData decodeMessageSecurityObject:options:error:];
+[MSCMSEnvelopedData encodeOriginatorInfoCertificates:error:];
```

## Instance methods

```
-[MSCMSEnvelopedData setContentType:];
-[MSCMSEnvelopedData encodeMessageSecurityObject:];
-[MSCMSEnvelopedData addRecipient:];
-[MSCMSEnvelopedData contentType];
-[MSCMSEnvelopedData setContentChanged:];
-[MSCMSEnvelopedData embeddedContent];
-[MSCMSEnvelopedData version];
-[MSCMSEnvelopedData type];
-[MSCMSEnvelopedData unprotectedAttributes];
-[MSCMSEnvelopedData setEmbeddedContent:];
-[MSCMSEnvelopedData setVersion:];
-[MSCMSEnvelopedData setRecipients:];
-[MSCMSEnvelopedData setUnprotectedAttributes:];
-[MSCMSEnvelopedData contentChanged];
-[MSCMSEnvelopedData dataContent];
-[MSCMSEnvelopedData recipients];
-[MSCMSEnvelopedData setDataContent:];
-[MSCMSEnvelopedData encryptionKey];
-[MSCMSEnvelopedData setEncryptionKey:];
-[MSCMSEnvelopedData encryptionAlgorithm];
-[MSCMSEnvelopedData setEncryptionAlgorithm:];
-[MSCMSEnvelopedData initWithDataContent:recipient:];
-[MSCMSEnvelopedData encryptContent:];
-[MSCMSEnvelopedData addRecipient:error:];
-[MSCMSEnvelopedData bulkEncryptDecrypt:algorithm:mode:key:iv:error:];
-[MSCMSEnvelopedData checkDecryptionResult:];
-[MSCMSEnvelopedData decryptContent:error:];
-[MSCMSEnvelopedData encodeEncryptionParameters:];
-[MSCMSEnvelopedData encryptDecryptContent:ccOperation:error:];
-[MSCMSEnvelopedData encryptedContent];
-[MSCMSEnvelopedData findBestEncryptionAlgorithmForNewRecipient:];
-[MSCMSEnvelopedData generateEncryptionKey:];
-[MSCMSEnvelopedData getRecipients];
-[MSCMSEnvelopedData initWithDataContent:recipient:encryptionAlgorithm:];
-[MSCMSEnvelopedData initWithEmbeddedContent:recipient:];
-[MSCMSEnvelopedData initWithEmbeddedContent:recipient:encryptionAlgorithm:];
-[MSCMSEnvelopedData legacyASN1Encoding];
-[MSCMSEnvelopedData originatorCertificates];
-[MSCMSEnvelopedData removeRecipientWithCertificate:error:];
-[MSCMSEnvelopedData removeRecipientWithEmailAddress:error:];
-[MSCMSEnvelopedData setEncryptedContent:];
-[MSCMSEnvelopedData setLegacyASN1Encoding:];
-[MSCMSEnvelopedData setOriginatorCertificates:];
```
