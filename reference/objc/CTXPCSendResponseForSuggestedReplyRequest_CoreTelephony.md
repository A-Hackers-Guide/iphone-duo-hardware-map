# `CTXPCSendResponseForSuggestedReplyRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCSubscriptionContextRequest`
- 0 instance variables, 3 properties, 7 instance methods, 1 class methods

## Properties

```
@property (T@"CTLazuliDestination",R,N) destination;
@property (T@"CTLazuliMessageID",R,N) messageID;
@property (T@"CTLazuliChatBotResponseForSuggestedReply",R,N) response;
```

## Class methods

```
+[CTXPCSendResponseForSuggestedReplyRequest allowedClassesForArguments];
```

## Instance methods

```
-[CTXPCSendResponseForSuggestedReplyRequest destination];
-[CTXPCSendResponseForSuggestedReplyRequest requiredEntitlement];
-[CTXPCSendResponseForSuggestedReplyRequest messageID];
-[CTXPCSendResponseForSuggestedReplyRequest ct_shortName];
-[CTXPCSendResponseForSuggestedReplyRequest performRequestWithHandler:completionHandler:];
-[CTXPCSendResponseForSuggestedReplyRequest response];
-[CTXPCSendResponseForSuggestedReplyRequest initWithContext:destination:messageID:response:];
```
