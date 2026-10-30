# `CTXPCSendFileTransferMessageRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCSubscriptionContextRequest`
- 0 instance variables, 4 properties, 10 instance methods, 2 class methods

## Properties

```
@property (T@"CTLazuliMessageID",R,N) messageID;
@property (T@"CTLazuliFileTransferDescriptor",R,N) lazuliDescriptor;
@property (T@"CTLazuliDestination",R,N) destination;
@property (T@"CTLazuliGroupChatUri",R,N) groupChatURI;
```

## Class methods

```
+[CTXPCSendFileTransferMessageRequest allowedClassesForArguments];
+[CTXPCSendFileTransferMessageRequest isSensitiveMessage];
```

## Instance methods

```
-[CTXPCSendFileTransferMessageRequest destination];
-[CTXPCSendFileTransferMessageRequest requiredEntitlement];
-[CTXPCSendFileTransferMessageRequest messageID];
-[CTXPCSendFileTransferMessageRequest ct_shortName];
-[CTXPCSendFileTransferMessageRequest security];
-[CTXPCSendFileTransferMessageRequest performRequestWithHandler:completionHandler:];
-[CTXPCSendFileTransferMessageRequest groupChatURI];
-[CTXPCSendFileTransferMessageRequest initWithContext:destination:messageID:descriptor:security:];
-[CTXPCSendFileTransferMessageRequest initWithContext:groupChatURI:messageID:descriptor:security:];
-[CTXPCSendFileTransferMessageRequest lazuliDescriptor];
```
