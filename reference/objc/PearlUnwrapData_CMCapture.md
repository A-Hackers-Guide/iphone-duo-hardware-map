# `PearlUnwrapData`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSData" _encryptionKey;
@"NSData" _encryptionKeyHmac;
@"NSData" _initializationVector;
@"NSData" _tag;
@"NSData" _signature;
```

## Properties

```
@property (T@"NSData",R,V_encryptionKey) encryptionKey;
@property (T@"NSData",R,V_encryptionKeyHmac) encryptionKeyHmac;
@property (T@"NSData",R,V_initializationVector) initializationVector;
@property (T@"NSData",R,V_tag) tag;
@property (T@"NSData",R,V_signature) signature;
```

## Instance methods

```
-[PearlUnwrapData signature];
-[PearlUnwrapData initializationVector];
-[PearlUnwrapData tag];
-[PearlUnwrapData encryptionKey];
-[PearlUnwrapData encryptionKeyHmac];
-[PearlUnwrapData initWithEncryptionKey:encryptionKeyHmac:initializationVector:tag:signature:];
```
