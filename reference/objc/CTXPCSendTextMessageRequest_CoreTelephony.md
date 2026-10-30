# `CTXPCSendTextMessageRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCSubscriptionContextRequest`
- 0 instance variables, 5 properties, 10 instance methods, 2 class methods

## Properties

```
@property (T@"CTLazuliMessageID",R,N) messageID;
@property (T@"CTLazuliMessageText",R,N) message;
@property (T@"CTLazuliDestination",R,N) destination;
@property (T@"CTLazuliGroupChatUri",R,N) groupChatURI;
@property (T@"CTLazuliSecurity",R,N) security;
```

## Class methods

```
+[CTXPCSendTextMessageRequest allowedClassesForArguments];
+[CTXPCSendTextMessageRequest isSensitiveMessage];
```

## Instance methods

```
-[CTXPCSendTextMessageRequest destination];
-[CTXPCSendTextMessageRequest requiredEntitlement];
-[CTXPCSendTextMessageRequest messageID];
-[CTXPCSendTextMessageRequest message];
-[CTXPCSendTextMessageRequest ct_shortName];
-[CTXPCSendTextMessageRequest security];
-[CTXPCSendTextMessageRequest performRequestWithHandler:completionHandler:];
-[CTXPCSendTextMessageRequest groupChatURI];
-[CTXPCSendTextMessageRequest initWithContext:destination:messageID:message:security:];
-[CTXPCSendTextMessageRequest initWithContext:groupChatURI:messageID:message:security:];
```
