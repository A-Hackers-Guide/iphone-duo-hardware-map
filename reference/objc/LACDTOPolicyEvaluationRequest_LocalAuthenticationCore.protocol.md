# `LACDTOPolicyEvaluationRequest` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `LACDTOPolicyEvaluation`
- 0 instance variables, 5 properties, 6 instance methods, 0 class methods

## Properties

```
@property (Tq,R,N) policy;
@property (T@"NSDictionary",R,N) options;
@property (T@"<LACDTOEnvironment>",R,N) environment;
@property (TB,R,N) isInteractiveRatchetEvaluation;
@property (T@"NSDictionary",R,N) payload;
```

## Instance methods

```
-[LACDTOPolicyEvaluationRequest payload];
-[LACDTOPolicyEvaluationRequest options];
-[LACDTOPolicyEvaluationRequest environment];
-[LACDTOPolicyEvaluationRequest updatePayload:];
-[LACDTOPolicyEvaluationRequest policy];
-[LACDTOPolicyEvaluationRequest isInteractiveRatchetEvaluation];
```
