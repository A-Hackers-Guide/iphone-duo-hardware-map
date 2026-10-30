# `LACDTOMutablePolicyEvaluationResult`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTOPolicyEvaluationResult`
- 3 instance variables, 8 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSError" _error;
@"NSDictionary" _result;
@"NSString" _identifier;
```

## Properties

```
@property (T@"NSString",&,N,V_identifier) identifier;
@property (T@"NSError",&,N,V_error) error;
@property (T@"NSDictionary",&,N,V_result) result;
@property (TB,R,N) isSuccess;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACDTOMutablePolicyEvaluationResult isSuccess];
-[LACDTOMutablePolicyEvaluationResult setError:];
-[LACDTOMutablePolicyEvaluationResult setResult:];
-[LACDTOMutablePolicyEvaluationResult identifier];
-[LACDTOMutablePolicyEvaluationResult error];
-[LACDTOMutablePolicyEvaluationResult setIdentifier:];
-[LACDTOMutablePolicyEvaluationResult result];
-[LACDTOMutablePolicyEvaluationResult description];
-[LACDTOMutablePolicyEvaluationResult isEqual:];
-[LACDTOMutablePolicyEvaluationResult initWithIdentifier:];
```
