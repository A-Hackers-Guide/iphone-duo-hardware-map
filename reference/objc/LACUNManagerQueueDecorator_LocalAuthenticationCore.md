# `LACUNManagerQueueDecorator`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACUNManagerDelegate`, `LACUNManager`
- 4 instance variables, 5 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"<LACUNManagerDelegate>" _delegate;
@"<LACUNManager>" _manager;
@"NSObject<OS_dispatch_queue>" _workQueue;
@"NSObject<OS_dispatch_queue>" _replyQueue;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<LACUNManagerDelegate>",W,N) delegate;
```

## Instance methods

```
-[LACUNManagerQueueDecorator setDelegate:];
-[LACUNManagerQueueDecorator delegate];
-[LACUNManagerQueueDecorator cancelAllNotificationsWithCompletion:];
-[LACUNManagerQueueDecorator cancelNotificationsWithIdentifiers:scheduledOnly:completion:];
-[LACUNManagerQueueDecorator initWithManager:replyQueue:];
-[LACUNManagerQueueDecorator initWithManager:workQueue:replyQueue:];
-[LACUNManagerQueueDecorator notificationManager:didRespondToNotification:fromCategory:withAction:completionHandler:];
-[LACUNManagerQueueDecorator postNotification:completion:];
```
