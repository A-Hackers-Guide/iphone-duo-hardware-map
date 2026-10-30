# `LACEvaluationEventValuePushButtonStatus` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `LACEvaluationEventValue`
- 0 instance variables, 4 properties, 4 instance methods, 0 class methods

## Properties

```
@property (T@"NSNumber",R,N) isCredentialPresent;
@property (T@"NSData",R,N) authorizingAccessoryId;
@property (T@"NSError",R,N) accessoryAuthorizationError;
@property (T@"NSNumber",R,N) accessoryAuthorizationResult;
```

## Instance methods

```
-[LACEvaluationEventValuePushButtonStatus accessoryAuthorizationError];
-[LACEvaluationEventValuePushButtonStatus accessoryAuthorizationResult];
-[LACEvaluationEventValuePushButtonStatus authorizingAccessoryId];
-[LACEvaluationEventValuePushButtonStatus isCredentialPresent];
```
