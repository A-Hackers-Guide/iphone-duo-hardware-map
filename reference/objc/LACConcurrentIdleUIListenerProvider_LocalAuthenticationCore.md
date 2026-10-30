# `LACConcurrentIdleUIListenerProvider`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACConcurrentIdleUIListenerProviding`, `NSXPCListenerDelegate`
- 2 instance variables, 2 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"<LACConcurrentIdleUIXPCHandling><LACConcurrentIdleUIHandling>" _handler;
@"NSObject<OS_dispatch_queue>" _replyQueue;
```

## Properties

```
@property (T@"<LACConcurrentIdleUIXPCHandling><LACConcurrentIdleUIHandling>",R,W,N,V_handler) handler;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_replyQueue) replyQueue;
```

## Instance methods

```
-[LACConcurrentIdleUIListenerProvider listener:shouldAcceptNewConnection:];
-[LACConcurrentIdleUIListenerProvider handler];
-[LACConcurrentIdleUIListenerProvider replyQueue];
-[LACConcurrentIdleUIListenerProvider anonymousListenerWithIdentifier:];
-[LACConcurrentIdleUIListenerProvider initWithHandler:replyQueue:];
```
