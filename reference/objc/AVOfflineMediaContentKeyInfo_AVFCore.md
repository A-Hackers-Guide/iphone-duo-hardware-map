# `AVOfflineMediaContentKeyInfo`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSString" _keyIdentifier;
q _keySystem;
q _encryptionMethod;
@"NSData" _initializationVector;
```

## Properties

```
@property (T@"NSString",R,N,V_keyIdentifier) keyIdentifier;
@property (Tq,R,N,V_keySystem) keySystem;
@property (Tq,R,N,V_encryptionMethod) encryptionMethod;
@property (T@"NSData",R,N,V_initializationVector) initializationVector;
```

## Instance methods

```
-[AVOfflineMediaContentKeyInfo dealloc];
-[AVOfflineMediaContentKeyInfo initializationVector];
-[AVOfflineMediaContentKeyInfo keySystem];
-[AVOfflineMediaContentKeyInfo keyIdentifier];
-[AVOfflineMediaContentKeyInfo encryptionMethod];
-[AVOfflineMediaContentKeyInfo initWithKeyIdentifier:keySystem:encryptionMethod:initializationVector:];
```
