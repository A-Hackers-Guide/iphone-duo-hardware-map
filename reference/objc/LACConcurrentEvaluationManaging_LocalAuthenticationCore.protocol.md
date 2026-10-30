# `LACConcurrentEvaluationManaging` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `LACConcurrentIdleUIHandling`, `LACConcurrentIdleUIXPCHandling`
- 0 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance methods

```
-[LACConcurrentEvaluationManaging hasStashedRequestsForContextID:];
-[LACConcurrentEvaluationManaging addObserver:forRequest:];
-[LACConcurrentEvaluationManaging cancelRequestsForContextID:];
-[LACConcurrentEvaluationManaging registerRequest:];
-[LACConcurrentEvaluationManaging removeObserver:forRequest:];
-[LACConcurrentEvaluationManaging restartRequestsForContextID:unpauseEvents:];
-[LACConcurrentEvaluationManaging stashRequest:acceptsIdleUI:];
-[LACConcurrentEvaluationManaging unregisterRequest:];
```
