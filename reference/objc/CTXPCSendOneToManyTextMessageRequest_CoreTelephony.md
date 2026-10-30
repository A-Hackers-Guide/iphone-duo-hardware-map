# `CTXPCSendOneToManyTextMessageRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCSubscriptionContextRequest`
- 0 instance variables, 3 properties, 7 instance methods, 2 class methods

## Properties

```
@property (T@"CTLazuliDestinationList",R,N) destinationList;
@property (T@"CTLazuliMessageID",R,N) messageID;
@property (T@"CTLazuliMessageText",R,N) message;
```

## Class methods

```
+[CTXPCSendOneToManyTextMessageRequest allowedClassesForArguments];
+[CTXPCSendOneToManyTextMessageRequest isSensitiveMessage];
```

## Instance methods

```
-[CTXPCSendOneToManyTextMessageRequest requiredEntitlement];
-[CTXPCSendOneToManyTextMessageRequest messageID];
-[CTXPCSendOneToManyTextMessageRequest message];
-[CTXPCSendOneToManyTextMessageRequest ct_shortName];
-[CTXPCSendOneToManyTextMessageRequest performRequestWithHandler:completionHandler:];
-[CTXPCSendOneToManyTextMessageRequest destinationList];
-[CTXPCSendOneToManyTextMessageRequest initWithContext:to:withMessageID:withMessage:];
```
