# `_LAKeyStore`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_LAKeyStoreGenericPasswordCryptor`, `LAKeyStore`
- 2 instance variables, 4 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"<LAKeyStoreBackend>" _backend;
@"LAKeyStoreSecretCoder" _coder;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_LAKeyStore init];
-[_LAKeyStore fetchKeysWithDomain:completion:];
-[_LAKeyStore decryptData:publicKeyHash:context:completion:];
-[_LAKeyStore encryptData:publicKeyHash:completion:];
-[_LAKeyStore fetchGenericPasswordWithIdentifier:domain:completion:];
-[_LAKeyStore fetchGenericPasswordsWithDomain:completion:];
-[_LAKeyStore fetchItemsWithDomain:completion:];
-[_LAKeyStore fetchKeyWithIdentifier:domain:completion:];
-[_LAKeyStore fetchKeyWithPublicKeyHash:completion:];
-[_LAKeyStore removeGenericPasswordsWithDomain:completion:];
-[_LAKeyStore removeItemsWithCompletion:];
-[_LAKeyStore removeItemsWithDomain:completion:];
-[_LAKeyStore removeKeysWithDomain:completion:];
-[_LAKeyStore storeGenericPassword:identifier:domain:protectedBy:completion:];
-[_LAKeyStore storeKeyWithIdentifier:domain:protectedBy:completion:];
```
