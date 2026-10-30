# `CTXPCMessageRevokeRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCSubscriptionContextRequest`
- 0 instance variables, 2 properties, 6 instance methods, 1 class methods

## Properties

```
@property (T@"CTLazuliMessageRevokeData",R,N) revokeData;
@property (T@"CTLazuliMessageID",R,N) messageID;
```

## Class methods

```
+[CTXPCMessageRevokeRequest allowedClassesForArguments];
```

## Instance methods

```
-[CTXPCMessageRevokeRequest requiredEntitlement];
-[CTXPCMessageRevokeRequest messageID];
-[CTXPCMessageRevokeRequest ct_shortName];
-[CTXPCMessageRevokeRequest performRequestWithHandler:completionHandler:];
-[CTXPCMessageRevokeRequest initWithContext:revokeData:messageID:];
-[CTXPCMessageRevokeRequest revokeData];
```
