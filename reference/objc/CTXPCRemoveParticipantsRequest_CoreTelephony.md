# `CTXPCRemoveParticipantsRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCSubscriptionContextRequest`
- 0 instance variables, 3 properties, 8 instance methods, 1 class methods

## Properties

```
@property (T@"CTLazuliGroupChatUri",R,N) groupChatURI;
@property (T@"CTLazuliGroupChatParticipantList",R,N) participants;
@property (T@"CTLazuliOperationID",R,N) operationID;
```

## Class methods

```
+[CTXPCRemoveParticipantsRequest allowedClassesForArguments];
```

## Instance methods

```
-[CTXPCRemoveParticipantsRequest operationID];
-[CTXPCRemoveParticipantsRequest requiredEntitlement];
-[CTXPCRemoveParticipantsRequest ct_shortName];
-[CTXPCRemoveParticipantsRequest security];
-[CTXPCRemoveParticipantsRequest performRequestWithHandler:completionHandler:];
-[CTXPCRemoveParticipantsRequest participants];
-[CTXPCRemoveParticipantsRequest initWithContext:groupChatURI:participants:operationID:security:];
-[CTXPCRemoveParticipantsRequest groupChatURI];
```
