# `MLKeyManager`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 0 instance methods, 6 class methods

## Class methods

```
+[MLKeyManager syncQueue];
+[MLKeyManager createPersistentKeyBlobForKeyID:usesCodeSigningIdentityForEncryption:error:];
+[MLKeyManager decryptSessionForModelAtURL:error:];
+[MLKeyManager extractKeyIdentifierFromModelAtURL:usesCodeSigningIdentityForEncryption:error:];
+[MLKeyManager isModelEncrypted:];
+[MLKeyManager loadDecryptionKeyForModelAtURL:retUsesCodeSigningIdentityForEncryption:error:];
```
