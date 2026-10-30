# `LACMutableEvaluationEventValuePushButtonStatus`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACEvaluationEventValuePushButtonStatus`, `LACEvaluationEventValue`
- 4 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
? authorizingAccessoryId;
? accessoryAuthorizationError;
@"NSNumber" accessoryAuthorizationResult;
@"NSNumber" isCredentialPresent;
```

## Properties

```
@property (T@"NSData",N,C) authorizingAccessoryId;
@property (T@"NSError",N,C) accessoryAuthorizationError;
@property (T@"NSNumber",N,&,VaccessoryAuthorizationResult) accessoryAuthorizationResult;
@property (T@"NSNumber",N,&,VisCredentialPresent) isCredentialPresent;
@property (T@"NSString",N,R) description;
@property (Tq,N,R) hash;
```

## Instance methods

```
-[LACMutableEvaluationEventValuePushButtonStatus init];
-[LACMutableEvaluationEventValuePushButtonStatus hash];
-[LACMutableEvaluationEventValuePushButtonStatus description];
-[LACMutableEvaluationEventValuePushButtonStatus isEqual:];
-[LACMutableEvaluationEventValuePushButtonStatus setAccessoryAuthorizationError:];
-[LACMutableEvaluationEventValuePushButtonStatus accessoryAuthorizationError];
-[LACMutableEvaluationEventValuePushButtonStatus accessoryAuthorizationResult];
-[LACMutableEvaluationEventValuePushButtonStatus authorizingAccessoryId];
-[LACMutableEvaluationEventValuePushButtonStatus isCredentialPresent];
-[LACMutableEvaluationEventValuePushButtonStatus setAccessoryAuthorizationResult:];
-[LACMutableEvaluationEventValuePushButtonStatus setAuthorizingAccessoryId:];
-[LACMutableEvaluationEventValuePushButtonStatus setIsCredentialPresent:];
```
