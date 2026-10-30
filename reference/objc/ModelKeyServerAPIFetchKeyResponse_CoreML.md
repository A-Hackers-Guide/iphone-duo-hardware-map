# `ModelKeyServerAPIFetchKeyResponse`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 4 instance variables, 6 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"ModelKeyServerAPIResultError" _error;
i _result;
@"ModelKeyServerAPIFetchKeyResult" _success;
{?="result"b1} _has;
```

## Properties

```
@property (TB,R,N) hasSuccess;
@property (T@"ModelKeyServerAPIFetchKeyResult",&,N,V_success) success;
@property (TB,R,N) hasError;
@property (T@"ModelKeyServerAPIResultError",&,N,V_error) error;
@property (TB,N) hasResult;
@property (Ti,N,V_result) result;
```

## Instance methods

```
-[ModelKeyServerAPIFetchKeyResponse hasResult];
-[ModelKeyServerAPIFetchKeyResponse hasSuccess];
-[ModelKeyServerAPIFetchKeyResponse setError:];
-[ModelKeyServerAPIFetchKeyResponse setResult:];
-[ModelKeyServerAPIFetchKeyResponse writeTo:];
-[ModelKeyServerAPIFetchKeyResponse setSuccess:];
-[ModelKeyServerAPIFetchKeyResponse success];
-[ModelKeyServerAPIFetchKeyResponse mergeFrom:];
-[ModelKeyServerAPIFetchKeyResponse error];
-[ModelKeyServerAPIFetchKeyResponse result];
-[ModelKeyServerAPIFetchKeyResponse hash];
-[ModelKeyServerAPIFetchKeyResponse copyTo:];
-[ModelKeyServerAPIFetchKeyResponse description];
-[ModelKeyServerAPIFetchKeyResponse readFrom:];
-[ModelKeyServerAPIFetchKeyResponse copyWithZone:];
-[ModelKeyServerAPIFetchKeyResponse isEqual:];
-[ModelKeyServerAPIFetchKeyResponse hasError];
-[ModelKeyServerAPIFetchKeyResponse dictionaryRepresentation];
-[ModelKeyServerAPIFetchKeyResponse setHasResult:];
-[ModelKeyServerAPIFetchKeyResponse resultAsString:];
-[ModelKeyServerAPIFetchKeyResponse StringAsResult:];
-[ModelKeyServerAPIFetchKeyResponse clearOneofValuesForResult];
```
