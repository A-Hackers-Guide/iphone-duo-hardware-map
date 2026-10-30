# `CTXPCSendComposingIndicatorRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCSubscriptionContextRequest`
- 0 instance variables, 4 properties, 10 instance methods, 1 class methods

## Properties

```
@property (T@"CTLazuliMessageID",R,N) messageID;
@property (T@"CTLazuliMessageComposingIndicator",R,N) indication;
@property (T@"CTLazuliDestination",R,N) destination;
@property (T@"CTLazuliGroupChatUri",R,N) groupChatURI;
```

## Class methods

```
+[CTXPCSendComposingIndicatorRequest allowedClassesForArguments];
```

## Instance methods

```
-[CTXPCSendComposingIndicatorRequest destination];
-[CTXPCSendComposingIndicatorRequest requiredEntitlement];
-[CTXPCSendComposingIndicatorRequest messageID];
-[CTXPCSendComposingIndicatorRequest ct_shortName];
-[CTXPCSendComposingIndicatorRequest security];
-[CTXPCSendComposingIndicatorRequest performRequestWithHandler:completionHandler:];
-[CTXPCSendComposingIndicatorRequest groupChatURI];
-[CTXPCSendComposingIndicatorRequest indication];
-[CTXPCSendComposingIndicatorRequest initWithContext:destination:messageID:indication:security:];
-[CTXPCSendComposingIndicatorRequest initWithContext:groupChatURI:messageID:indication:security:];
```
