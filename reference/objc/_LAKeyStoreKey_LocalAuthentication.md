# `_LAKeyStoreKey`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LAKeyStoreKey`
- 5 instance variables, 7 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"NSString" _identifier;
@"NSData" _acl;
@"NSData" _publicKeyHash;
@ _keyRef;
@ _pubKeyRef;
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

## Class methods

```
+[_LAKeyStoreKey buildWithDictionary:error:];
```

## Instance methods

```
-[_LAKeyStoreKey acl];
-[_LAKeyStoreKey identifier];
-[_LAKeyStoreKey publicKeyHash];
-[_LAKeyStoreKey canDecryptUsingSecKeyAlgorithm:];
-[_LAKeyStoreKey canEncryptUsingSecKeyAlgorithm:];
-[_LAKeyStoreKey canExchangeKeysUsingSecKeyAlgorithm:];
-[_LAKeyStoreKey canSignUsingSecKeyAlgorithm:];
-[_LAKeyStoreKey canVerifyUsingSecKeyAlgorithm:];
-[_LAKeyStoreKey decryptData:secKeyAlgorithm:context:completion:];
-[_LAKeyStoreKey encryptData:secKeyAlgorithm:completion:];
-[_LAKeyStoreKey exchangeKeysWithPublicKey:secKeyAlgorithm:secKeyParameters:context:completion:];
-[_LAKeyStoreKey exportBytesWithCompletion:];
-[_LAKeyStoreKey signData:secKeyAlgorithm:context:completion:];
-[_LAKeyStoreKey verifyData:signature:secKeyAlgorithm:completion:];
```
