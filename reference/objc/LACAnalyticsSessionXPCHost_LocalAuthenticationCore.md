# `LACAnalyticsSessionXPCHost`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACAnalyticsSessionXPC`
- 4 instance variables, 2 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _workQueue;
B _connected;
@"NSUUID" _contextUUID;
@"LACAnalyticsSession" _session;
```

## Properties

```
@property (T@"NSUUID",R,N,V_contextUUID) contextUUID;
@property (T@"LACAnalyticsSession",R,N,V_session) session;
```

## Instance methods

```
-[LACAnalyticsSessionXPCHost session];
-[LACAnalyticsSessionXPCHost contextUUID];
-[LACAnalyticsSessionXPCHost _checkQueueAndSessionWithAction:replyOnFailure:];
-[LACAnalyticsSessionXPCHost authenticationAction:failing:reply:];
-[LACAnalyticsSessionXPCHost authenticationAttemptFailedForEvent:reply:];
-[LACAnalyticsSessionXPCHost authenticationStartedForEvent:reply:];
-[LACAnalyticsSessionXPCHost authenticationSuccessfulForEvent:reply:];
-[LACAnalyticsSessionXPCHost finishWithReply:];
-[LACAnalyticsSessionXPCHost initWithSession:contextUUID:connected:workQueue:];
-[LACAnalyticsSessionXPCHost updateContextUUID:reply:];
```
