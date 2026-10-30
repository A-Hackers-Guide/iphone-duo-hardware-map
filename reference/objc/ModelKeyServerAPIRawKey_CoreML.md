# `ModelKeyServerAPIRawKey`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 2 instance variables, 4 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSData" _encryptionIv;
@"NSData" _encryptionKey;
```

## Properties

```
@property (TB,R,N) hasEncryptionKey;
@property (T@"NSData",&,N,V_encryptionKey) encryptionKey;
@property (TB,R,N) hasEncryptionIv;
@property (T@"NSData",&,N,V_encryptionIv) encryptionIv;
```

## Instance methods

```
-[ModelKeyServerAPIRawKey writeTo:];
-[ModelKeyServerAPIRawKey mergeFrom:];
-[ModelKeyServerAPIRawKey hash];
-[ModelKeyServerAPIRawKey copyTo:];
-[ModelKeyServerAPIRawKey description];
-[ModelKeyServerAPIRawKey readFrom:];
-[ModelKeyServerAPIRawKey copyWithZone:];
-[ModelKeyServerAPIRawKey isEqual:];
-[ModelKeyServerAPIRawKey dictionaryRepresentation];
-[ModelKeyServerAPIRawKey hasEncryptionIv];
-[ModelKeyServerAPIRawKey encryptionIv];
-[ModelKeyServerAPIRawKey encryptionKey];
-[ModelKeyServerAPIRawKey hasEncryptionKey];
-[ModelKeyServerAPIRawKey setEncryptionIv:];
-[ModelKeyServerAPIRawKey setEncryptionKey:];
```
