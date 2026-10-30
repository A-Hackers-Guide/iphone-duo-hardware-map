# `CTXPCSendDispositionNotificationMessageRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCSubscriptionContextRequest`
- 0 instance variables, 5 properties, 11 instance methods, 1 class methods

## Properties

```
@property (T@"CTLazuliMessageID",R,N) messageID;
@property (Tq,R,N) notificationType;
@property (T@"CTLazuliMessageID",R,N) notificationMessageID;
@property (T@"CTLazuliDestination",R,N) destination;
@property (T@"CTLazuliGroupChatUri",R,N) groupChatURI;
```

## Class methods

```
+[CTXPCSendDispositionNotificationMessageRequest allowedClassesForArguments];
```

## Instance methods

```
-[CTXPCSendDispositionNotificationMessageRequest destination];
-[CTXPCSendDispositionNotificationMessageRequest notificationType];
-[CTXPCSendDispositionNotificationMessageRequest requiredEntitlement];
-[CTXPCSendDispositionNotificationMessageRequest messageID];
-[CTXPCSendDispositionNotificationMessageRequest ct_shortName];
-[CTXPCSendDispositionNotificationMessageRequest security];
-[CTXPCSendDispositionNotificationMessageRequest performRequestWithHandler:completionHandler:];
-[CTXPCSendDispositionNotificationMessageRequest groupChatURI];
-[CTXPCSendDispositionNotificationMessageRequest initWithContext:destination:messageID:notificationType:notificationMessageID:security:];
-[CTXPCSendDispositionNotificationMessageRequest initWithContext:groupChatURI:destination:messageID:notificationType:notificationMessageID:security:];
-[CTXPCSendDispositionNotificationMessageRequest notificationMessageID];
```
