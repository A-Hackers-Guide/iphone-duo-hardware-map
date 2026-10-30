# `LAPublicKey`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"LARight" _right;
@"<LAKeyStoreKey>" _key;
@"NSObject<OS_dispatch_queue>" _workQueue;
Q _instanceID;
```

## Instance methods

```
-[LAPublicKey identifier];
-[LAPublicKey dealloc];
-[LAPublicKey setRight:];
-[LAPublicKey description];
-[LAPublicKey initWithKey:];
-[LAPublicKey right];
-[LAPublicKey canEncryptUsingSecKeyAlgorithm:];
-[LAPublicKey canVerifyUsingSecKeyAlgorithm:];
-[LAPublicKey encryptData:secKeyAlgorithm:completion:];
-[LAPublicKey exportBytesWithCompletion:];
-[LAPublicKey verifyData:signature:secKeyAlgorithm:completion:];
```
