# `CTXPCChangeSubjectRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCSubscriptionContextRequest`
- 0 instance variables, 3 properties, 8 instance methods, 1 class methods

## Properties

```
@property (T@"CTLazuliGroupChatUri",R,N) groupChatURI;
@property (T@"CTLazuliGroupChatSubject",R,N) subject;
@property (T@"CTLazuliOperationID",R,N) operationID;
```

## Class methods

```
+[CTXPCChangeSubjectRequest allowedClassesForArguments];
```

## Instance methods

```
-[CTXPCChangeSubjectRequest operationID];
-[CTXPCChangeSubjectRequest subject];
-[CTXPCChangeSubjectRequest requiredEntitlement];
-[CTXPCChangeSubjectRequest ct_shortName];
-[CTXPCChangeSubjectRequest security];
-[CTXPCChangeSubjectRequest performRequestWithHandler:completionHandler:];
-[CTXPCChangeSubjectRequest groupChatURI];
-[CTXPCChangeSubjectRequest initWithContext:groupChatURI:subject:operationID:security:];
```
