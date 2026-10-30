# `CTXPCAddParticipantsRequest`

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
+[CTXPCAddParticipantsRequest allowedClassesForArguments];
```

## Instance methods

```
-[CTXPCAddParticipantsRequest operationID];
-[CTXPCAddParticipantsRequest requiredEntitlement];
-[CTXPCAddParticipantsRequest ct_shortName];
-[CTXPCAddParticipantsRequest security];
-[CTXPCAddParticipantsRequest performRequestWithHandler:completionHandler:];
-[CTXPCAddParticipantsRequest participants];
-[CTXPCAddParticipantsRequest initWithContext:groupChatURI:participants:operationID:security:];
-[CTXPCAddParticipantsRequest groupChatURI];
```
