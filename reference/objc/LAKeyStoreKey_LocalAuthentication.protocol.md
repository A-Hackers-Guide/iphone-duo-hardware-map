# `LAKeyStoreKey` (protocol)

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 14 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,N) identifier;
@property (T@"NSData",R,N) acl;
@property (T@"NSData",R,N) publicKeyHash;
```

## Instance methods

```
-[LAKeyStoreKey acl];
-[LAKeyStoreKey identifier];
-[LAKeyStoreKey publicKeyHash];
-[LAKeyStoreKey canDecryptUsingSecKeyAlgorithm:];
-[LAKeyStoreKey canEncryptUsingSecKeyAlgorithm:];
-[LAKeyStoreKey canExchangeKeysUsingSecKeyAlgorithm:];
-[LAKeyStoreKey canSignUsingSecKeyAlgorithm:];
-[LAKeyStoreKey canVerifyUsingSecKeyAlgorithm:];
-[LAKeyStoreKey decryptData:secKeyAlgorithm:context:completion:];
-[LAKeyStoreKey encryptData:secKeyAlgorithm:completion:];
-[LAKeyStoreKey exchangeKeysWithPublicKey:secKeyAlgorithm:secKeyParameters:context:completion:];
-[LAKeyStoreKey exportBytesWithCompletion:];
-[LAKeyStoreKey signData:secKeyAlgorithm:context:completion:];
-[LAKeyStoreKey verifyData:signature:secKeyAlgorithm:completion:];
```
