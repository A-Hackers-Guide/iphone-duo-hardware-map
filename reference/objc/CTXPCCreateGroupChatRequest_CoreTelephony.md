# `CTXPCCreateGroupChatRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCSubscriptionContextRequest`
- 0 instance variables, 2 properties, 6 instance methods, 1 class methods

## Properties

```
@property (T@"CTLazuliGroupChatInformation",R,N) groupChatInfo;
@property (T@"CTLazuliOperationID",R,N) operationID;
```

## Class methods

```
+[CTXPCCreateGroupChatRequest allowedClassesForArguments];
```

## Instance methods

```
-[CTXPCCreateGroupChatRequest operationID];
-[CTXPCCreateGroupChatRequest requiredEntitlement];
-[CTXPCCreateGroupChatRequest ct_shortName];
-[CTXPCCreateGroupChatRequest performRequestWithHandler:completionHandler:];
-[CTXPCCreateGroupChatRequest groupChatInfo];
-[CTXPCCreateGroupChatRequest initWithContext:groupChatInfo:operationID:];
```
