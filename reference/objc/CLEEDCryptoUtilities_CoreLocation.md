# `CLEEDCryptoUtilities`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 0 instance methods, 17 class methods

## Class methods

```
+[CLEEDCryptoUtilities getRandomBytes:];
+[CLEEDCryptoUtilities copyAdrPublicKeyData:];
+[CLEEDCryptoUtilities copyCertFromBase64String:];
+[CLEEDCryptoUtilities copyPublicKeyFromPrivateKey:];
+[CLEEDCryptoUtilities createKeyExternalRepresentation:];
+[CLEEDCryptoUtilities createKeyFromExternalRepresentationData:keyClass:];
+[CLEEDCryptoUtilities createKeyFromExternalRepresentationString:keyClass:];
+[CLEEDCryptoUtilities createRandomP256PrivateKey];
+[CLEEDCryptoUtilities getAESGCMDecryptedData:key:iv:authTag:];
+[CLEEDCryptoUtilities getDerivedKeyWithLength:secretData:additionalInfo:];
+[CLEEDCryptoUtilities getECIESDecryptedData:key:sharedInfo:];
+[CLEEDCryptoUtilities getECIESEncryptedData:key:sharedInfo:prependKeyFingerprint:];
+[CLEEDCryptoUtilities getGMACWithAuthData:key:iv:];
+[CLEEDCryptoUtilities getKeyExternalRepresentation:];
+[CLEEDCryptoUtilities getKeyFingerprint:];
+[CLEEDCryptoUtilities getKeyFingerprintWithKeyData:];
+[CLEEDCryptoUtilities getSessionIDWithPhoneNumber:sessionStartTime:];
```
