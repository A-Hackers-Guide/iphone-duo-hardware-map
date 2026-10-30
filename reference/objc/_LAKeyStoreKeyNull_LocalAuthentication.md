# `_LAKeyStoreKeyNull`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LAKeyStoreKey`
- 3 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSString" _identifier;
@"NSData" _acl;
@"NSString" _publicKeyHash;
```

## Properties

```
@property (T@"NSString",R,N) identifier;
@property (T@"NSData",R,N) acl;
@property (T@"NSData",R,N) publicKeyHash;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_LAKeyStoreKeyNull acl];
-[_LAKeyStoreKeyNull identifier];
-[_LAKeyStoreKeyNull init];
-[_LAKeyStoreKeyNull publicKeyHash];
-[_LAKeyStoreKeyNull canDecryptUsingSecKeyAlgorithm:];
-[_LAKeyStoreKeyNull canEncryptUsingSecKeyAlgorithm:];
-[_LAKeyStoreKeyNull canExchangeKeysUsingSecKeyAlgorithm:];
-[_LAKeyStoreKeyNull canSignUsingSecKeyAlgorithm:];
-[_LAKeyStoreKeyNull canVerifyUsingSecKeyAlgorithm:];
-[_LAKeyStoreKeyNull decryptData:secKeyAlgorithm:context:completion:];
-[_LAKeyStoreKeyNull encryptData:secKeyAlgorithm:completion:];
-[_LAKeyStoreKeyNull exchangeKeysWithPublicKey:secKeyAlgorithm:secKeyParameters:context:completion:];
-[_LAKeyStoreKeyNull exportBytesWithCompletion:];
-[_LAKeyStoreKeyNull signData:secKeyAlgorithm:context:completion:];
-[_LAKeyStoreKeyNull verifyData:signature:secKeyAlgorithm:completion:];
```
