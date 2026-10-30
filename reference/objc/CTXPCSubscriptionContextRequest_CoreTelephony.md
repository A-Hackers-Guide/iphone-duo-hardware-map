# `CTXPCSubscriptionContextRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCRequestMessage`
- 0 instance variables, 2 properties, 6 instance methods, 1 class methods

## Properties

```
@property (T@"CTXPCServiceSubscriptionContext",R,N) context;
@property (T@"CTServiceDescriptor",R,N) descriptor;
```

## Class methods

```
+[CTXPCSubscriptionContextRequest allowedClassesForArguments];
```

## Instance methods

```
-[CTXPCSubscriptionContextRequest initWithContext:];
-[CTXPCSubscriptionContextRequest descriptor];
-[CTXPCSubscriptionContextRequest initWithDescriptor:];
-[CTXPCSubscriptionContextRequest context];
-[CTXPCSubscriptionContextRequest initWithContext:namedArguments:];
-[CTXPCSubscriptionContextRequest initWithDescriptor:namedArguments:];
```
