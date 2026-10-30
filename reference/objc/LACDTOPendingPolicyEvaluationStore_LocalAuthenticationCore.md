# `LACDTOPendingPolicyEvaluationStore`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTOPendingPolicyEvaluationStore`
- 4 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"<LACPersistentStore>" store;
@"OS_dispatch_queue" workQueue;
taskGroup;
? pendingEvaluationsDict;
```

## Properties

```
@property (T@"<LACPersistentStore>",N,R,Vstore) store;
@property (T@"OS_dispatch_queue",N,R,VworkQueue) workQueue;
@property (T@"NSDictionary",N,C) pendingEvaluationsDict;
@property (T@"NSArray",N,R) pendingEvaluationValues;
@property (T@"NSArray",N,R) pendingEvaluations;
```

## Instance methods

```
-[LACDTOPendingPolicyEvaluationStore store];
-[LACDTOPendingPolicyEvaluationStore init];
-[LACDTOPendingPolicyEvaluationStore workQueue];
-[LACDTOPendingPolicyEvaluationStore addPendingEvaluation:];
-[LACDTOPendingPolicyEvaluationStore initWithPersistentStore:workQueue:];
-[LACDTOPendingPolicyEvaluationStore loadPersistedEvaluationsWithCompletion:];
-[LACDTOPendingPolicyEvaluationStore pendingEvaluationValues];
-[LACDTOPendingPolicyEvaluationStore pendingEvaluationWithIdentifier:];
-[LACDTOPendingPolicyEvaluationStore pendingEvaluations];
-[LACDTOPendingPolicyEvaluationStore pendingEvaluationsDict];
-[LACDTOPendingPolicyEvaluationStore persistEvaluations];
-[LACDTOPendingPolicyEvaluationStore removePendingEvaluationWithIdentifier:];
-[LACDTOPendingPolicyEvaluationStore setPendingEvaluationsDict:];
```
