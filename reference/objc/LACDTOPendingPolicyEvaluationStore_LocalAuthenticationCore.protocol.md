# `LACDTOPendingPolicyEvaluationStore` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 1 properties, 6 instance methods, 0 class methods

## Properties

```
@property (T@"NSArray",R,N) pendingEvaluations;
```

## Instance methods

```
-[LACDTOPendingPolicyEvaluationStore addPendingEvaluation:];
-[LACDTOPendingPolicyEvaluationStore loadPersistedEvaluationsWithCompletion:];
-[LACDTOPendingPolicyEvaluationStore pendingEvaluationWithIdentifier:];
-[LACDTOPendingPolicyEvaluationStore pendingEvaluations];
-[LACDTOPendingPolicyEvaluationStore persistEvaluations];
-[LACDTOPendingPolicyEvaluationStore removePendingEvaluationWithIdentifier:];
```
