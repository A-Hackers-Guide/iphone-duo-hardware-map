# `CTXPCSendOneToManyFileTransferRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCSubscriptionContextRequest`
- 0 instance variables, 3 properties, 7 instance methods, 2 class methods

## Properties

```
@property (T@"CTLazuliDestinationList",R,N) destinationList;
@property (T@"CTLazuliMessageID",R,N) messageID;
@property (T@"CTLazuliFileTransferDescriptor",R,N) fileTransferDescriptor;
```

## Class methods

```
+[CTXPCSendOneToManyFileTransferRequest allowedClassesForArguments];
+[CTXPCSendOneToManyFileTransferRequest isSensitiveMessage];
```

## Instance methods

```
-[CTXPCSendOneToManyFileTransferRequest requiredEntitlement];
-[CTXPCSendOneToManyFileTransferRequest messageID];
-[CTXPCSendOneToManyFileTransferRequest ct_shortName];
-[CTXPCSendOneToManyFileTransferRequest performRequestWithHandler:completionHandler:];
-[CTXPCSendOneToManyFileTransferRequest destinationList];
-[CTXPCSendOneToManyFileTransferRequest fileTransferDescriptor];
-[CTXPCSendOneToManyFileTransferRequest initWithContext:to:withMessageID:withDescriptor:];
```
