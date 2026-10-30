# `MSCMSRecipientInfo`

- Image: [`/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`](../userland/System__Library__PrivateFrameworks__MessageSecurity.framework__MessageSecurity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 42 instance methods, 3 class methods

## Instance variables

```
@"NSArray" _algorithmCapabilities;
@"MSAlgorithmIdentifier" _keyEncryptionAlgorithm;
^{__SecCertificate=} _recipientCertificate;
@"NSArray" _recipientCertificates;
^{__SecCertificate=} _originator;
^{__SecIdentity=} _originatorIdentity;
@"NSData" _originatorPubKey;
@"NSNumber" _version;
@"NSArray" _encryptedKeys;
@"NSData" _userKeyingMaterial;
```

## Properties

```
@property (T@"NSNumber",&,V_version) version;
@property (T@"NSArray",&,V_encryptedKeys) encryptedKeys;
@property (T@"NSData",&,V_userKeyingMaterial) userKeyingMaterial;
@property (T@"NSArray",&,V_algorithmCapabilities) algorithmCapabilities;
@property (T@"MSAlgorithmIdentifier",&,V_keyEncryptionAlgorithm) keyEncryptionAlgorithm;
@property (T^{__SecCertificate=},N,V_recipientCertificate) recipientCertificate;
@property (T@"NSArray",&,V_recipientCertificates) recipientCertificates;
@property (T^{__SecCertificate=},N,V_originator) originator;
@property (T^{__SecIdentity=},N,V_originatorIdentity) originatorIdentity;
@property (T@"NSData",&,V_originatorPubKey) originatorPubKey;
```

## Class methods

```
+[MSCMSRecipientInfo decodeKeyAgreeRecipientInfo:certificates:LAContext:error:];
+[MSCMSRecipientInfo decodeKeyTransRecipientInfo:certificates:LAContext:error:];
+[MSCMSRecipientInfo decodeRecipientInfo:certificates:LAContext:error:];
```

## Instance methods

```
-[MSCMSRecipientInfo originatorIdentity];
-[MSCMSRecipientInfo dealloc];
-[MSCMSRecipientInfo setOriginator:];
-[MSCMSRecipientInfo version];
-[MSCMSRecipientInfo setVersion:];
-[MSCMSRecipientInfo originator];
-[MSCMSRecipientInfo initWithCertificate:];
-[MSCMSRecipientInfo key];
-[MSCMSRecipientInfo recipientCertificate];
-[MSCMSRecipientInfo initWithEmail:];
-[MSCMSRecipientInfo initWithCertificate:algorithmCapabilities:];
-[MSCMSRecipientInfo key:];
-[MSCMSRecipientInfo encryptBulkKey:];
-[MSCMSRecipientInfo algorithmCapabilities];
-[MSCMSRecipientInfo createSecCMSSharedInfo:];
-[MSCMSRecipientInfo createSharedInfo:];
-[MSCMSRecipientInfo decryptWrappedKey:kek:iv:];
-[MSCMSRecipientInfo encodeKeyAgreeRecipientInfo:recipientInfo:error:];
-[MSCMSRecipientInfo encodeKeyTransRecipientInfo:recipientInfo:error:];
-[MSCMSRecipientInfo encodeRecipientInfo:recipientInfo:error:];
-[MSCMSRecipientInfo encryptedKeys];
-[MSCMSRecipientInfo freeKeyTransRecipientInfo:];
-[MSCMSRecipientInfo freeRecipientInfo:];
-[MSCMSRecipientInfo initWithCertificate:algorithmCapabilities:originator:];
-[MSCMSRecipientInfo initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:];
-[MSCMSRecipientInfo initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:originator:];
-[MSCMSRecipientInfo initWithCertificate:legacyKeyWrapAlgorithm:];
-[MSCMSRecipientInfo initWithEmail:algorithmCapabilities:];
-[MSCMSRecipientInfo initWithEmail:keyEncryptionAlgorithm:];
-[MSCMSRecipientInfo keyEncryptionAlgorithm];
-[MSCMSRecipientInfo keyEncryptionKey:forEncryption:secCMSCompatibility:];
-[MSCMSRecipientInfo originatorPubKey];
-[MSCMSRecipientInfo recipientCertificates];
-[MSCMSRecipientInfo setAlgorithmCapabilities:];
-[MSCMSRecipientInfo setEncryptedKeys:];
-[MSCMSRecipientInfo setKeyEncryptionAlgorithm:];
-[MSCMSRecipientInfo setOriginatorIdentity:];
-[MSCMSRecipientInfo setOriginatorPubKey:];
-[MSCMSRecipientInfo setRecipientCertificate:];
-[MSCMSRecipientInfo setRecipientCertificates:];
-[MSCMSRecipientInfo setUserKeyingMaterial:];
-[MSCMSRecipientInfo userKeyingMaterial];
```
