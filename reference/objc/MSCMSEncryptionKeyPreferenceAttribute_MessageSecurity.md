# `MSCMSEncryptionKeyPreferenceAttribute`

- Image: [`/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`](../userland/System__Library__PrivateFrameworks__MessageSecurity.framework__MessageSecurity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MSCMSAttributeCoder`
- 2 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _legacyASN1Encoding;
^{__SecCertificate=} _encryptionCertificate;
```

## Properties

```
@property (T^{__SecCertificate=},R,V_encryptionCertificate) encryptionCertificate;
@property (TB,V_legacyASN1Encoding) legacyASN1Encoding;
@property (T@"MSOID",R,&) attributeType;
```

## Instance methods

```
-[MSCMSEncryptionKeyPreferenceAttribute initWithEmailAddress:];
-[MSCMSEncryptionKeyPreferenceAttribute attributeType];
-[MSCMSEncryptionKeyPreferenceAttribute dealloc];
-[MSCMSEncryptionKeyPreferenceAttribute initWithIdentity:];
-[MSCMSEncryptionKeyPreferenceAttribute initWithCertificate:];
-[MSCMSEncryptionKeyPreferenceAttribute initWithAttribute:error:];
-[MSCMSEncryptionKeyPreferenceAttribute encryptionCertificate];
-[MSCMSEncryptionKeyPreferenceAttribute initWithAttribute:certificates:LAContext:error:];
-[MSCMSEncryptionKeyPreferenceAttribute encodeAttributeWithError:];
-[MSCMSEncryptionKeyPreferenceAttribute legacyASN1Encoding];
-[MSCMSEncryptionKeyPreferenceAttribute setLegacyASN1Encoding:];
```
