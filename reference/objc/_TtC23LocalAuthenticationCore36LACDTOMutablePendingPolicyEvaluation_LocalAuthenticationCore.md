# `_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTOPendingPolicyEvaluationMutable`
- 7 instance variables, 9 properties, 25 instance methods, 0 class methods

## Instance variables

```
_$sSS identifier;
Swift.Bool isInvalidated;
_$sSSSg callbackReason;
Foundation.URL ? callbackURL;
Foundation.Date ? notificationScheduledAt;
Foundation.Date ? coolOffStarted;
_$sSSSg ratchetUUID;
```

## Properties

```
@property (T@"NSString",N,R) description;
@property (T@"NSString",N,R) identifier;
@property (TB,N,VisInvalidated) isInvalidated;
@property (T@"NSString",N,C) callbackReason;
@property (T@"NSURL",N,C) callbackURL;
@property (T@"NSDate",N,C) notificationScheduledAt;
@property (T@"NSDate",N,C) coolOffStarted;
@property (T@"NSString",N,C) ratchetUUID;
@property (TB,N,R) hasNotifiedUserAboutCompletion;
```

## Instance methods

```
-[_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation identifier];
-[_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation init];
-[_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation isInvalidated];
-[_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation description];
-[_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation isEqual:];
-[_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation setIsInvalidated:];
-[_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation initWithIdentifier:];
-[_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation setCallbackURL:];
-[_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation callbackURL];
-[_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation setRatchetUUID:];
-[_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation isNotificationScheduledForDate:];
-[_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation callbackReason];
-[_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation coolOffStarted];
-[_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation hasNotifiedUserAboutCompletion];
-[_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation notificationScheduledAt];
-[_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation ratchetUUID];
-[_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation setCallbackReason:];
-[_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation setCoolOffStarted:];
-[_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation setNotificationScheduledAt:];
-[_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation updateCallbackReason:];
-[_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation updateCallbackURL:];
-[_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation updateCoolOffStarted:];
-[_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation updateIsInvalidated:];
-[_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation updateNotificationScheduledAt:];
-[_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation updateRatchetUUID:];
```
