# `CTXPCEnablePINRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCSubscriptionContextRequest`
- 0 instance variables, 2 properties, 6 instance methods, 1 class methods

## Properties

```
@property (TB,R,N) enable;
@property (T@"NSString",R,N) pin;
```

## Class methods

```
+[CTXPCEnablePINRequest allowedClassesForArguments];
```

## Instance methods

```
-[CTXPCEnablePINRequest enable];
-[CTXPCEnablePINRequest requiredEntitlement];
-[CTXPCEnablePINRequest ct_shortName];
-[CTXPCEnablePINRequest performRequestWithHandler:completionHandler:];
-[CTXPCEnablePINRequest pin];
-[CTXPCEnablePINRequest initWithContext:enable:pin:];
```
