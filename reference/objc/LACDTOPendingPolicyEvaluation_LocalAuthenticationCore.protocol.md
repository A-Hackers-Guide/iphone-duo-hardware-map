# `LACDTOPendingPolicyEvaluation` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `LACDTOPolicyEvaluation`
- 0 instance variables, 7 properties, 8 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,N) callbackReason;
@property (T@"NSURL",R,N) callbackURL;
@property (TB,R,N) hasNotifiedUserAboutCompletion;
@property (TB,R,N) isInvalidated;
@property (T@"NSDate",R,N) notificationScheduledAt;
@property (T@"NSDate",R,N) coolOffStarted;
@property (T@"NSString",R,N) ratchetUUID;
```

## Instance methods

```
-[LACDTOPendingPolicyEvaluation isInvalidated];
-[LACDTOPendingPolicyEvaluation callbackURL];
-[LACDTOPendingPolicyEvaluation isNotificationScheduledForDate:];
-[LACDTOPendingPolicyEvaluation callbackReason];
-[LACDTOPendingPolicyEvaluation coolOffStarted];
-[LACDTOPendingPolicyEvaluation hasNotifiedUserAboutCompletion];
-[LACDTOPendingPolicyEvaluation notificationScheduledAt];
-[LACDTOPendingPolicyEvaluation ratchetUUID];
```
