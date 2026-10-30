# `CTXPCChangePINRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCSubscriptionContextRequest`
- 0 instance variables, 2 properties, 6 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,N) currentPin;
@property (T@"NSString",R,N) updatedPin;
```

## Instance methods

```
-[CTXPCChangePINRequest requiredEntitlement];
-[CTXPCChangePINRequest ct_shortName];
-[CTXPCChangePINRequest performRequestWithHandler:completionHandler:];
-[CTXPCChangePINRequest currentPin];
-[CTXPCChangePINRequest initWithContext:currentPin:updatedPin:];
-[CTXPCChangePINRequest updatedPin];
```
