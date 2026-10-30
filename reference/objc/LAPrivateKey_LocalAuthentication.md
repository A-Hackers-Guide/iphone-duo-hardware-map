# `LAPrivateKey`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"LARight" _right;
@"<LAKeyStoreKey>" _key;
@"NSObject<OS_dispatch_queue>" _workQueue;
Q _instanceID;
```

## Properties

```
@property (T@"LAPublicKey",R,N) publicKey;
```

## Instance methods

```
-[LAPrivateKey publicKey];
-[LAPrivateKey identifier];
-[LAPrivateKey dealloc];
-[LAPrivateKey setRight:];
-[LAPrivateKey description];
-[LAPrivateKey initWithKey:];
-[LAPrivateKey right];
-[LAPrivateKey canDecryptUsingSecKeyAlgorithm:];
-[LAPrivateKey canExchangeKeysUsingSecKeyAlgorithm:];
-[LAPrivateKey canSignUsingSecKeyAlgorithm:];
-[LAPrivateKey decryptData:secKeyAlgorithm:completion:];
-[LAPrivateKey exchangeKeysWithPublicKey:secKeyAlgorithm:secKeyParameters:completion:];
-[LAPrivateKey signData:secKeyAlgorithm:completion:];
```
