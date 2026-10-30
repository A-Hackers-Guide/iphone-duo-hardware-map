# `CTXPCSendDeviceActionRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCSubscriptionContextRequest`
- 0 instance variables, 3 properties, 7 instance methods, 1 class methods

## Properties

```
@property (T@"CTLazuliDestination",R,N) destination;
@property (T@"CTLazuliMessageID",R,N) messageID;
@property (T@"CTLazuliSuggestedActionDevice",R,N) action;
```

## Class methods

```
+[CTXPCSendDeviceActionRequest allowedClassesForArguments];
```

## Instance methods

```
-[CTXPCSendDeviceActionRequest destination];
-[CTXPCSendDeviceActionRequest requiredEntitlement];
-[CTXPCSendDeviceActionRequest messageID];
-[CTXPCSendDeviceActionRequest ct_shortName];
-[CTXPCSendDeviceActionRequest action];
-[CTXPCSendDeviceActionRequest performRequestWithHandler:completionHandler:];
-[CTXPCSendDeviceActionRequest initWithContext:destination:messageID:action:];
```
