# `LACDTONotificationManager`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACUNManagerDelegate`
- 3 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _replyQueue;
@"<LACDTONotificationFactory>" _notificationFactory;
@"<LACDTONotificationManagerDelegate>" _delegate;
```

## Properties

```
@property (T@"<LACDTONotificationManagerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACDTONotificationManager setDelegate:];
-[LACDTONotificationManager delegate];
-[LACDTONotificationManager initWithReplyQueue:];
-[LACDTONotificationManager _securityDelayManager];
-[LACDTONotificationManager cancelPreviousNewSecurityDelayRequiredNotificationWithCompletion:];
-[LACDTONotificationManager cancelPreviousSecurityDelayFinishedNotificationForPendingEvaluation:scheduledOnly:completion:];
-[LACDTONotificationManager initWithReplyQueue:notificationFactory:];
-[LACDTONotificationManager notificationManager:didRespondToNotification:fromCategory:withAction:completionHandler:];
-[LACDTONotificationManager postNewSecurityDelayRequiredNotificationWithCompletion:];
-[LACDTONotificationManager scheduleSecurityDelayFinishedNotificationForPendingEvaluation:after:validity:completion:];
```
