# `CTXPCSendResponseForSuggestedActionRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCSubscriptionContextRequest`
- 0 instance variables, 3 properties, 7 instance methods, 1 class methods

## Properties

```
@property (T@"CTLazuliDestination",R,N) destination;
@property (T@"CTLazuliMessageID",R,N) messageID;
@property (T@"CTLazuliChatBotResponseForSuggestedAction",R,N) response;
```

## Class methods

```
+[CTXPCSendResponseForSuggestedActionRequest allowedClassesForArguments];
```

## Instance methods

```
-[CTXPCSendResponseForSuggestedActionRequest destination];
-[CTXPCSendResponseForSuggestedActionRequest requiredEntitlement];
-[CTXPCSendResponseForSuggestedActionRequest messageID];
-[CTXPCSendResponseForSuggestedActionRequest ct_shortName];
-[CTXPCSendResponseForSuggestedActionRequest performRequestWithHandler:completionHandler:];
-[CTXPCSendResponseForSuggestedActionRequest response];
-[CTXPCSendResponseForSuggestedActionRequest initWithContext:destination:messageID:response:];
```
