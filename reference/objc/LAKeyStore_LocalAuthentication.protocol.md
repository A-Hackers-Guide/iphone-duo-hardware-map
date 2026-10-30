# `LAKeyStore` (protocol)

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 12 instance methods, 0 class methods

## Instance methods

```
-[LAKeyStore fetchKeysWithDomain:completion:];
-[LAKeyStore fetchGenericPasswordWithIdentifier:domain:completion:];
-[LAKeyStore fetchGenericPasswordsWithDomain:completion:];
-[LAKeyStore fetchItemsWithDomain:completion:];
-[LAKeyStore fetchKeyWithIdentifier:domain:completion:];
-[LAKeyStore fetchKeyWithPublicKeyHash:completion:];
-[LAKeyStore removeGenericPasswordsWithDomain:completion:];
-[LAKeyStore removeItemsWithCompletion:];
-[LAKeyStore removeItemsWithDomain:completion:];
-[LAKeyStore removeKeysWithDomain:completion:];
-[LAKeyStore storeGenericPassword:identifier:domain:protectedBy:completion:];
-[LAKeyStore storeKeyWithIdentifier:domain:protectedBy:completion:];
```
