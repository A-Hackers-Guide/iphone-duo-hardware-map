# `LACDTOMutablePolicyEvaluationRequest`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTOPolicyEvaluationRequest`
- 5 instance variables, 10 properties, 16 instance methods, 0 class methods

## Instance variables

```
q _policy;
@"NSDictionary" _options;
@"<LACDTOEnvironment>" _environment;
@"NSDictionary" _payload;
@"NSString" _identifier;
```

## Properties

```
@property (T@"NSString",&,N,V_identifier) identifier;
@property (Tq,N,V_policy) policy;
@property (T@"NSDictionary",&,N,V_options) options;
@property (T@"<LACDTOEnvironment>",&,N,V_environment) environment;
@property (T@"NSDictionary",&,N,V_payload) payload;
@property (TB,R,N) isInteractiveRatchetEvaluation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACDTOMutablePolicyEvaluationRequest setEnvironment:];
-[LACDTOMutablePolicyEvaluationRequest setOptions:];
-[LACDTOMutablePolicyEvaluationRequest identifier];
-[LACDTOMutablePolicyEvaluationRequest payload];
-[LACDTOMutablePolicyEvaluationRequest setPayload:];
-[LACDTOMutablePolicyEvaluationRequest setIdentifier:];
-[LACDTOMutablePolicyEvaluationRequest hash];
-[LACDTOMutablePolicyEvaluationRequest description];
-[LACDTOMutablePolicyEvaluationRequest options];
-[LACDTOMutablePolicyEvaluationRequest isEqual:];
-[LACDTOMutablePolicyEvaluationRequest setPolicy:];
-[LACDTOMutablePolicyEvaluationRequest initWithIdentifier:];
-[LACDTOMutablePolicyEvaluationRequest environment];
-[LACDTOMutablePolicyEvaluationRequest updatePayload:];
-[LACDTOMutablePolicyEvaluationRequest policy];
-[LACDTOMutablePolicyEvaluationRequest isInteractiveRatchetEvaluation];
```
