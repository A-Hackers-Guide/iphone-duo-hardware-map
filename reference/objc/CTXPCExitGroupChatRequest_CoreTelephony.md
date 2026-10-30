# `CTXPCExitGroupChatRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCSubscriptionContextRequest`
- 0 instance variables, 2 properties, 6 instance methods, 1 class methods

## Properties

```
@property (T@"CTLazuliGroupChatUri",R,N) groupChatURI;
@property (T@"CTLazuliOperationID",R,N) operationID;
```

## Class methods

```
+[CTXPCExitGroupChatRequest allowedClassesForArguments];
```

## Instance methods

```
-[CTXPCExitGroupChatRequest operationID];
-[CTXPCExitGroupChatRequest requiredEntitlement];
-[CTXPCExitGroupChatRequest ct_shortName];
-[CTXPCExitGroupChatRequest performRequestWithHandler:completionHandler:];
-[CTXPCExitGroupChatRequest groupChatURI];
-[CTXPCExitGroupChatRequest initWithContext:groupChatURI:operationID:];
```
