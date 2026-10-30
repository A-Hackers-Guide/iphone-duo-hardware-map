# `LACConcurrentEvaluationController`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACConcurrentEvaluationManagerObserver`, `LACConcurrentEvaluationControlling`, `LACEvaluationRequestProcessor`
- 5 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"LACConcurrentEvaluationHelper" helper;
@"<LACConcurrentEvaluationManaging>" manager;
@"LACConcurrentIdleUIListenerProvider" idleUIListenerProvider;
@"OS_dispatch_queue" replyQueue;
stashedRequests;
```

## Properties

```
@property (T@"LACConcurrentEvaluationHelper",N,R,Vhelper) helper;
@property (T@"<LACConcurrentEvaluationManaging>",N,R,Vmanager) manager;
@property (T@"LACConcurrentIdleUIListenerProvider",N,R,VidleUIListenerProvider) idleUIListenerProvider;
@property (T@"OS_dispatch_queue",N,R,VreplyQueue) replyQueue;
```

## Instance methods

```
-[LACConcurrentEvaluationController helper];
-[LACConcurrentEvaluationController processRequest:configuration:completion:];
-[LACConcurrentEvaluationController init];
-[LACConcurrentEvaluationController manager];
-[LACConcurrentEvaluationController replyQueue];
-[LACConcurrentEvaluationController postProcessRequest:result:completion:];
-[LACConcurrentEvaluationController canProcessRequest:];
-[LACConcurrentEvaluationController systemDidCancelRequest:manager:];
-[LACConcurrentEvaluationController idleUIListenerProvider];
-[LACConcurrentEvaluationController initWithHelper:manager:replyQueue:];
-[LACConcurrentEvaluationController systemReadyForRequest:manager:];
```
