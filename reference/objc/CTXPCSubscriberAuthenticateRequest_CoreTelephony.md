# `CTXPCSubscriberAuthenticateRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCSubscriptionContextRequest`
- 0 instance variables, 1 properties, 5 instance methods, 1 class methods

## Properties

```
@property (T@"CTSubscriberAuthDataHolder",R,N) authInfo;
```

## Class methods

```
+[CTXPCSubscriberAuthenticateRequest allowedClassesForArguments];
```

## Instance methods

```
-[CTXPCSubscriberAuthenticateRequest requiredEntitlement];
-[CTXPCSubscriberAuthenticateRequest ct_shortName];
-[CTXPCSubscriberAuthenticateRequest authInfo];
-[CTXPCSubscriberAuthenticateRequest performRequestWithHandler:completionHandler:];
-[CTXPCSubscriberAuthenticateRequest initWithContext:authInfo:];
```
