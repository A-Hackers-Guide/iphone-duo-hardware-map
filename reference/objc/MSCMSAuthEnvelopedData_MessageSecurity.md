# `MSCMSAuthEnvelopedData`

- Image: [`/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`](../userland/System__Library__PrivateFrameworks__MessageSecurity.framework__MessageSecurity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MSCMSMessage`
- 10 instance variables, 9 properties, 30 instance methods, 1 class methods

## Instance variables

```
@"MSOID" type;
? dataContent;
? recipients;
@"MSOID" encryptionAlgorithm;
? protectedAttributes;
? unprotectedAttributes;
? originatorCertificates;
@"MSOID" contentType;
@"<MSCMSMessage>" embeddedContent;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 encryptedContent;
```

## Properties

```
@property (T@"MSOID",N,&,Vtype) type;
@property (T@"NSData",N,C) dataContent;
@property (T@"NSArray",N,C) recipients;
@property (T@"MSOID",N,&,VencryptionAlgorithm) encryptionAlgorithm;
@property (T@"NSArray",N,C) protectedAttributes;
@property (T@"NSArray",N,C) unprotectedAttributes;
@property (T@"NSArray",N,C) originatorCertificates;
@property (T@"MSOID",N,&,VcontentType) contentType;
@property (T@"<MSCMSMessage>",N,&,VembeddedContent) embeddedContent;
```

## Class methods

```
+[MSCMSAuthEnvelopedData decodeMessageSecurityObject:options:error:];
```

## Instance methods

```
-[MSCMSAuthEnvelopedData setContentType:];
-[MSCMSAuthEnvelopedData encodeMessageSecurityObject:];
-[MSCMSAuthEnvelopedData init];
-[MSCMSAuthEnvelopedData addRecipient:];
-[MSCMSAuthEnvelopedData contentType];
-[MSCMSAuthEnvelopedData embeddedContent];
-[MSCMSAuthEnvelopedData setType:];
-[MSCMSAuthEnvelopedData type];
-[MSCMSAuthEnvelopedData setProtectedAttributes:];
-[MSCMSAuthEnvelopedData unprotectedAttributes];
-[MSCMSAuthEnvelopedData setEmbeddedContent:];
-[MSCMSAuthEnvelopedData setRecipients:];
-[MSCMSAuthEnvelopedData setUnprotectedAttributes:];
-[MSCMSAuthEnvelopedData dataContent];
-[MSCMSAuthEnvelopedData recipients];
-[MSCMSAuthEnvelopedData addProtectedAttribute:];
-[MSCMSAuthEnvelopedData setDataContent:];
-[MSCMSAuthEnvelopedData protectedAttributes];
-[MSCMSAuthEnvelopedData encryptionAlgorithm];
-[MSCMSAuthEnvelopedData setEncryptionAlgorithm:];
-[MSCMSAuthEnvelopedData initWithDataContent:recipient:];
-[MSCMSAuthEnvelopedData addUnprotectedAttribute:];
-[MSCMSAuthEnvelopedData getAttributesWithOID:];
-[MSCMSAuthEnvelopedData initWithDataContent:recipient:encryptionAlgorithm:];
-[MSCMSAuthEnvelopedData initWithEmbeddedContent:recipient:];
-[MSCMSAuthEnvelopedData initWithEmbeddedContent:recipient:encryptionAlgorithm:];
-[MSCMSAuthEnvelopedData initWithEncryptionAlgorithm:];
-[MSCMSAuthEnvelopedData originatorCertificates];
-[MSCMSAuthEnvelopedData setContentTypeWithType:];
-[MSCMSAuthEnvelopedData setOriginatorCertificates:];
```
