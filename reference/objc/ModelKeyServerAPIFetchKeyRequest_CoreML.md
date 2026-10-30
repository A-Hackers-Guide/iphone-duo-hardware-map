# `ModelKeyServerAPIFetchKeyRequest`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBRequest`
- Protocols: `NSCopying`
- 5 instance variables, 8 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"NSString" _keyId;
@"NSData" _signedKeyRequest;
@"NSString" _teamId;
B _rawRequest;
{?="rawRequest"b1} _has;
```

## Properties

```
@property (TB,R,N) hasKeyId;
@property (T@"NSString",&,N,V_keyId) keyId;
@property (TB,R,N) hasTeamId;
@property (T@"NSString",&,N,V_teamId) teamId;
@property (TB,R,N) hasSignedKeyRequest;
@property (T@"NSData",&,N,V_signedKeyRequest) signedKeyRequest;
@property (TB,N) hasRawRequest;
@property (TB,N,V_rawRequest) rawRequest;
```

## Instance methods

```
-[ModelKeyServerAPIFetchKeyRequest writeTo:];
-[ModelKeyServerAPIFetchKeyRequest mergeFrom:];
-[ModelKeyServerAPIFetchKeyRequest hash];
-[ModelKeyServerAPIFetchKeyRequest copyTo:];
-[ModelKeyServerAPIFetchKeyRequest description];
-[ModelKeyServerAPIFetchKeyRequest readFrom:];
-[ModelKeyServerAPIFetchKeyRequest copyWithZone:];
-[ModelKeyServerAPIFetchKeyRequest isEqual:];
-[ModelKeyServerAPIFetchKeyRequest dictionaryRepresentation];
-[ModelKeyServerAPIFetchKeyRequest hasKeyId];
-[ModelKeyServerAPIFetchKeyRequest keyId];
-[ModelKeyServerAPIFetchKeyRequest setKeyId:];
-[ModelKeyServerAPIFetchKeyRequest hasRawRequest];
-[ModelKeyServerAPIFetchKeyRequest hasSignedKeyRequest];
-[ModelKeyServerAPIFetchKeyRequest hasTeamId];
-[ModelKeyServerAPIFetchKeyRequest rawRequest];
-[ModelKeyServerAPIFetchKeyRequest setHasRawRequest:];
-[ModelKeyServerAPIFetchKeyRequest setRawRequest:];
-[ModelKeyServerAPIFetchKeyRequest setSignedKeyRequest:];
-[ModelKeyServerAPIFetchKeyRequest setTeamId:];
-[ModelKeyServerAPIFetchKeyRequest signedKeyRequest];
-[ModelKeyServerAPIFetchKeyRequest teamId];
```
