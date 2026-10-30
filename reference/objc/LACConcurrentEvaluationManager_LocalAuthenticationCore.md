# `LACConcurrentEvaluationManager`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACConcurrentEvaluationManaging`, `LACConcurrentIdleUIHandling`, `LACConcurrentIdleUIXPCHandling`
- 7 instance variables, 5 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"LACConcurrentEvaluationHelper" helper;
@"OS_dispatch_queue" replyQueue;
@ observers;
@ specializedObservers;
@ connectedUIInstances;
activeRequests;
stashedRequests;
```

## Properties

```
@property (T@"LACConcurrentEvaluationHelper",N,R,Vhelper) helper;
@property (T@"OS_dispatch_queue",N,R,VreplyQueue) replyQueue;
@property (T@,N,&,Vobservers) observers;
@property (T@,N,&,VspecializedObservers) specializedObservers;
@property (T@,N,&,VconnectedUIInstances) connectedUIInstances;
```

## Instance methods

```
-[LACConcurrentEvaluationManager helper];
-[LACConcurrentEvaluationManager init];
-[LACConcurrentEvaluationManager setObservers:];
-[LACConcurrentEvaluationManager replyQueue];
-[LACConcurrentEvaluationManager observers];
-[LACConcurrentEvaluationManager hasStashedRequestsForContextID:];
-[LACConcurrentEvaluationManager addObserver:forRequest:];
-[LACConcurrentEvaluationManager cancelRequestsForContextID:];
-[LACConcurrentEvaluationManager connectIdleUI:identifier:completion:];
-[LACConcurrentEvaluationManager connectedUIInstances];
-[LACConcurrentEvaluationManager connectionInvalidatedForIdentifier:];
-[LACConcurrentEvaluationManager idleUIGotFocus:identifier:completion:];
-[LACConcurrentEvaluationManager initWithHelper:replyQueue:];
-[LACConcurrentEvaluationManager registerRequest:];
-[LACConcurrentEvaluationManager removeObserver:forRequest:];
-[LACConcurrentEvaluationManager restartRequestsForContextID:unpauseEvents:];
-[LACConcurrentEvaluationManager setConnectedUIInstances:];
-[LACConcurrentEvaluationManager setSpecializedObservers:];
-[LACConcurrentEvaluationManager specializedObservers];
-[LACConcurrentEvaluationManager stashRequest:acceptsIdleUI:];
-[LACConcurrentEvaluationManager unregisterRequest:];
```
