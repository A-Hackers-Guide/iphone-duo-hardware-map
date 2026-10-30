# `ModelKeyServerAPIFetchKeyResult`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 7 instance variables, 12 properties, 31 instance methods, 0 class methods

## Instance variables

```
i _key;
@"NSString" _keyId;
@"NSString" _modelName;
@"ModelKeyServerAPIRawKey" _rawKey;
@"ModelKeyServerAPISignedKey" _signedKey;
@"NSString" _teamId;
{?="key"b1} _has;
```

## Properties

```
@property (TB,R,N) hasKeyId;
@property (T@"NSString",&,N,V_keyId) keyId;
@property (TB,R,N) hasModelName;
@property (T@"NSString",&,N,V_modelName) modelName;
@property (TB,R,N) hasTeamId;
@property (T@"NSString",&,N,V_teamId) teamId;
@property (TB,R,N) hasSignedKey;
@property (T@"ModelKeyServerAPISignedKey",&,N,V_signedKey) signedKey;
@property (TB,R,N) hasRawKey;
@property (T@"ModelKeyServerAPIRawKey",&,N,V_rawKey) rawKey;
@property (TB,N) hasKey;
@property (Ti,N,V_key) key;
```

## Instance methods

```
-[ModelKeyServerAPIFetchKeyResult writeTo:];
-[ModelKeyServerAPIFetchKeyResult mergeFrom:];
-[ModelKeyServerAPIFetchKeyResult setKey:];
-[ModelKeyServerAPIFetchKeyResult setModelName:];
-[ModelKeyServerAPIFetchKeyResult setHasKey:];
-[ModelKeyServerAPIFetchKeyResult hash];
-[ModelKeyServerAPIFetchKeyResult copyTo:];
-[ModelKeyServerAPIFetchKeyResult description];
-[ModelKeyServerAPIFetchKeyResult readFrom:];
-[ModelKeyServerAPIFetchKeyResult copyWithZone:];
-[ModelKeyServerAPIFetchKeyResult isEqual:];
-[ModelKeyServerAPIFetchKeyResult hasKey];
-[ModelKeyServerAPIFetchKeyResult key];
-[ModelKeyServerAPIFetchKeyResult modelName];
-[ModelKeyServerAPIFetchKeyResult dictionaryRepresentation];
-[ModelKeyServerAPIFetchKeyResult StringAsKey:];
-[ModelKeyServerAPIFetchKeyResult hasKeyId];
-[ModelKeyServerAPIFetchKeyResult hasModelName];
-[ModelKeyServerAPIFetchKeyResult keyAsString:];
-[ModelKeyServerAPIFetchKeyResult keyId];
-[ModelKeyServerAPIFetchKeyResult setKeyId:];
-[ModelKeyServerAPIFetchKeyResult clearOneofValuesForKey];
-[ModelKeyServerAPIFetchKeyResult hasRawKey];
-[ModelKeyServerAPIFetchKeyResult hasSignedKey];
-[ModelKeyServerAPIFetchKeyResult hasTeamId];
-[ModelKeyServerAPIFetchKeyResult rawKey];
-[ModelKeyServerAPIFetchKeyResult setRawKey:];
-[ModelKeyServerAPIFetchKeyResult setSignedKey:];
-[ModelKeyServerAPIFetchKeyResult setTeamId:];
-[ModelKeyServerAPIFetchKeyResult signedKey];
-[ModelKeyServerAPIFetchKeyResult teamId];
```
