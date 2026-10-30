# `SSRAESKeyManager`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 0 instance methods, 8 class methods

## Class methods

```
+[SSRAESKeyManager deleteAESKeyWithApplicationTag:keyLabel:];
+[SSRAESKeyManager generateAESKeyWithKeySizeInBits:];
+[SSRAESKeyManager generateIfNecessaryAESKeyWithKeySizeInBits:applicationTag:keyLabel:shouldGenerateIfNecessary:];
+[SSRAESKeyManager generateIfNecessaryVoiceTriggerProfilesAESKey];
+[SSRAESKeyManager getAESKeyFromKeychainWithApplicationTag:keyLabel:];
+[SSRAESKeyManager getKeychainAttributesForAESKeyWithApplicationTag:keyLabel:];
+[SSRAESKeyManager getVoiceTriggerProfilesAESKey];
+[SSRAESKeyManager storeAESKeyInKeychain:applicationTag:keyLabel:];
```
