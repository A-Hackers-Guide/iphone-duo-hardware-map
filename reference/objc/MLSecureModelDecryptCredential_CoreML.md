# `MLSecureModelDecryptCredential`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 1 instance variables, 1 properties, 4 instance methods, 1 class methods

## Instance variables

```
q _cryptoKey;
```

## Properties

```
@property (Tq,N,V_cryptoKey) cryptoKey;
```

## Class methods

```
+[MLSecureModelDecryptCredential supportsSecureCoding];
```

## Instance methods

```
-[MLSecureModelDecryptCredential encodeWithCoder:];
-[MLSecureModelDecryptCredential initWithCoder:];
-[MLSecureModelDecryptCredential cryptoKey];
-[MLSecureModelDecryptCredential setCryptoKey:];
```
