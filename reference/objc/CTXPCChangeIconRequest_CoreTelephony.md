# `CTXPCChangeIconRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCSubscriptionContextRequest`
- 0 instance variables, 3 properties, 8 instance methods, 1 class methods

## Properties

```
@property (T@"CTLazuliGroupChatUri",R,N) groupChatURI;
@property (T@"CTLazuliGroupChatIcon",R,N) icon;
@property (T@"CTLazuliOperationID",R,N) operationID;
```

## Class methods

```
+[CTXPCChangeIconRequest allowedClassesForArguments];
```

## Instance methods

```
-[CTXPCChangeIconRequest operationID];
-[CTXPCChangeIconRequest requiredEntitlement];
-[CTXPCChangeIconRequest ct_shortName];
-[CTXPCChangeIconRequest security];
-[CTXPCChangeIconRequest performRequestWithHandler:completionHandler:];
-[CTXPCChangeIconRequest icon];
-[CTXPCChangeIconRequest groupChatURI];
-[CTXPCChangeIconRequest initWithContext:groupChatURI:icon:operationID:security:];
```
