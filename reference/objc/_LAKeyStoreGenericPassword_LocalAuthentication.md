# `_LAKeyStoreGenericPassword`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LAKeyStoreGenericPassword`
- 5 instance variables, 6 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"NSString" _identifier;
@"NSData" _wrappedData;
@"NSData" _publicKeyHash;
@"<LAKeyStoreKey>" _wrapperKey;
@"<_LAKeyStoreGenericPasswordCryptor>" _cryptor;
```

## Properties

```
@property (T@"<_LAKeyStoreGenericPasswordCryptor>",W,N,V_cryptor) cryptor;
@property (T@"NSString",R,N) identifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_LAKeyStoreGenericPassword buildWithDictionary:error:];
```

## Instance methods

```
-[_LAKeyStoreGenericPassword identifier];
-[_LAKeyStoreGenericPassword cryptor];
-[_LAKeyStoreGenericPassword fetchDataWithContext:completion:];
-[_LAKeyStoreGenericPassword setCryptor:];
```
